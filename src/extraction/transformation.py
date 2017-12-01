import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

import common as commn
import config as conf

dirStartsWith = 'extracted'
pathStartsWith = dirStartsWith + '_search'
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
    return temp


def get_derivative_of_ts(vals):
    vals = fix_nans_with_avg(vals)
    lm = LinearRegression()
    X = np.arange(len(vals))
    X = sm.add_constant(X)
    lm.fit(X, vals)
    return lm.coef_[1]


def transformation_search_queries():
    dirs = commn.findDirsByStartsWith(dirStartsWith, True)

    for d in dirs:
        paths = commn.findPathsByStartsWith(pathStartsWith, d, True)
        for i, p in enumerate(paths, start=1):
            sys.stdout.write('\r %i/%i parts processed' % (i, len(paths)))
            df = pd.read_csv(p, parse_dates=['sorting_date'])
            df_cat = df['category_id'].drop_duplicates().dropna()
            df = df.set_index('sorting_date')
            result = pd.DataFrame(columns=conf.transformationSQColumns)
            for cat in df_cat:
                temp_ts = get_ts_for_cat(cat, df)
                Y = np.array(list(temp_ts))
                if not np.all(np.isnan(Y)):
                    derivative = get_derivative_of_ts(Y)
                    result.loc[-1] = [cat, derivative, Y.mean(), Y.min(), Y.max()]
                    result.index = result.index + 1
                    result = result.reset_index(drop=True)
            commn.convertDataFrameToCSV(result, conf.transformationSQColumns, 'transformationSQ_' + p[-11:-4])


def main():
    transformation_search_queries()


if __name__ == '__main__':
    main()
