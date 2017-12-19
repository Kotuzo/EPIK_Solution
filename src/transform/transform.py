import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

import common as commn
import config as conf

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
    print('\ntransformation search queries')
    paths = commn.find_search_queries_paths()
    for i, p in enumerate(paths, start=1):
        sys.stdout.write('\r %i/%i parts processed ' % (i, len(paths)))
        sys.stdout.flush()
        df = pd.read_csv(p, parse_dates=['sorting_date'])
        df_cat = df['category_id'].drop_duplicates().dropna()
        df = df.set_index('sorting_date')
        stat_data = pd.DataFrame(columns=conf.columnsSQ)
        print("\nStatistic data")
        for cat in df_cat:
            stat_data = get_statistic_data(cat, df, stat_data)
        commn.save_data_frame(stat_data, conf.columnsSQ, get_transformed_name_from_path(p))


def merge_transformed_with_ads():
    print('\nmerge transformation and ads')
    pathsAds = commn.find_ads_paths()
    for i, p in enumerate(pathsAds, start=1):
        sys.stdout.write('\r %i/%i parts processed' % (i, len(pathsAds)))
        sys.stdout.flush()
        startsWith = get_transformed_name_from_path(p)
        transformPath = commn.find_transformed_file_starts_with(startsWith)
        dfTransform = pd.read_csv(transformPath[0])
        dfAds = pd.read_csv(p)
        dfAdsTransform = pd.merge(dfAds, dfTransform, on='category_id', how='left')
        commn.save_data_frame(dfAdsTransform, conf.columnsAds + conf.columnsParams + conf.columnsSQ,
                              startsWith)


def get_transformed_name_from_path(path):
    return "transformed" + path[-11:-4]


def final_transformation():
    print('\nfinal transformation')
    paths = commn.find_transformed_file_starts_with("transformed")
    for i, p in enumerate(paths, start=1):
        sys.stdout.write('\r %i/%i parts processed' % (i, len(paths)))
        df = pd.read_csv(p)
        df = dropColumnsNotIn(df, ['id', 'has_phone','private_business', 'predict_sold', 'predict_replies',
                                   'predict_views', 'priceType', 'priceValue', 'state', 'derivative', 'average', 'min',
                                   'max'])
        df = replaceDummies(df, ['private_business', 'priceType', 'state'])
        df.dropna(inplace=True)
        commn.save_data_frame(df, conf.finalTransformColumns, get_transformed_name_from_path(p), True)


def replaceDummies(df, columns):
    for c in columns:
        df = pd.concat([df, pd.get_dummies(df[c])], axis=1)
        df.drop([c], axis=1, inplace=True)
    return df


def dropColumnsNotIn(df, columns):
    for c in df.keys():
        if c not in columns:
            df.drop([c], axis=1, inplace=True)
    return df


def main():
    transformation_search_queries()
    merge_transformed_with_ads()
    final_transformation()


if __name__ == '__main__':
    main()
