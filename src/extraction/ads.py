import common as common
import pandas as pd
import config as conf


def removeTimeFromDateTime(df, columnName):
    return pd.to_datetime(df[columnName]).dt.date


def extractAds():
    paths = common.findPathsByStartsWith('ads')
    for p in paths:
        df = pd.DataFrame(pd.concat(
            [pd.read_csv(p) for p in paths]))
        df['sorting_date'] = removeTimeFromDateTime(df, 'sorting_date')
        ads = pd.merge(df, common.categories, on='category_id')
        common.convertDataFrameToCSV(ads, conf.columnsAds, p[-14:-3])
