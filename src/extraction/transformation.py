import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

import common as commn
import config as conf

dirStartsWith = 'extracted'
nameTransform = 'transformationSQ_'
nameAds = 'adsTransformSQ'
pathStartsWithSearch = dirStartsWith + '_search'
pathStartsWithAds = dirStartsWith + '_ads'
pathStartsWithTransform = dirStartsWith + '_' + nameTransform
X = sm.add_constant(np.arange(14))


def get_ts_for_cat(l_id, df):
    temp_df = df[df['category_id'] == l_id]
    return temp_df['sessions_count'].resample('D').sum()


def fix_nans_with_avg(vals):
    temp = []
    mean = np.nanmean(vals)
    for v in vals:
        if np.isnan(v):
            temp.append(mean)
        else:
            temp.append(v)
    return np.array(temp)


def get_derivative_of_ts(vals):
    vals = fix_nans_with_avg(vals)
    lm = LinearRegression()
    X = np.arange(len(vals))
    X = sm.add_constant(X)
    lm.fit(X, vals)
    return lm.coef_[1]


# Returns DataFrame with cat , derivative, min, max, mean for each category
def get_statistic_data(cat, df, stat_data):
    temp_ts = get_ts_for_cat(cat, df)
    Y = np.array(list(temp_ts))
    if not np.all(np.isnan(Y)):
        derivative = get_derivative_of_ts(Y)
        Y = fix_nans_with_avg(Y)
        stat_data.loc[-1] = [cat, derivative, Y.mean(), Y.min(), Y.max()]
        stat_data.index = stat_data.index + 1
        stat_data = stat_data.reset_index(drop=True)
    return stat_data


def transformation_search_queries():
    dirs = commn.findDirsByStartsWith(dirStartsWith, True)

    print('\ntransformation search queries')
    for d in dirs:
        paths = commn.findPathsByStartsWith(pathStartsWithSearch, d, True)
        for i, p in enumerate(paths, start=1):
            sys.stdout.write('\r %i/%i parts processed' % (i, len(paths)))
            df = pd.read_csv(p, parse_dates=['sorting_date'])
            df_cat = df['category_id'].drop_duplicates().dropna()
            df = df.set_index('sorting_date')
            stat_data = pd.DataFrame(columns=conf.columnsSQ)
            for cat in df_cat:
                stat_data = get_statistic_data(cat, df, stat_data)
            commn.convertDataFrameToCSV(stat_data, conf.columnsSQ, nameTransform + p[-11:-4])


def merge_with_ads():
    dirs = commn.findDirsByStartsWith(dirStartsWith, True)

    print('\nmerge transformation and ads')
    for d in dirs:
        pathsAds = commn.findPathsByStartsWith(pathStartsWithAds, d, True)
        for i, p in enumerate(pathsAds, start=1):
            sys.stdout.write('\r %i/%i parts processed' % (i, len(pathsAds)))
            startsWith = pathStartsWithTransform + p[-11:]
            transformPath = commn.findPathsByStartsWith(startsWith, d, True)
            dfTransform = pd.read_csv(transformPath[0])
            dfAds = pd.read_csv(p)
            dfAdsTransform = pd.merge(dfAds, dfTransform, on='category_id', how='left')
            commn.convertDataFrameToCSV(dfAdsTransform, conf.columnsAds + conf.columnsParams + conf.columnsSQ,
                                        nameAds + '_' + p[-11:-4])
