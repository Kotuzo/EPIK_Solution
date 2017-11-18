import common as common
import pandas as pd
import config as conf
import sys


def removeTimeFromDateTime(df, columnName):
    return pd.to_datetime(df[columnName]).dt.date


def extractAds():
    paths = common.findPathsByStartsWith('ads')
    print('extracting ads')
    for i, p in enumerate(paths, start=1):
        sys.stdout.write('\r %i/%i files processed' % (i, len(paths)))
        sys.stdout.flush()
        # df = pd.DataFrame(pd.concat(
        #     [pd.read_csv(p) for p in paths]))  # we dont want to cancat it here
        df = pd.read_csv(p)
        df['sorting_date'] = removeTimeFromDateTime(df, 'sorting_date')
        ads = pd.merge(df, common.categories, on='category_id')
        common.convertDataFrameToCSV(ads, conf.columnsAds, p[-14:-3])
