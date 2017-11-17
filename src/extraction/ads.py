import common as common
import pandas as pd

def convertAdsCSVToDataFrame():
    paths = common.findPathsByStartsWith('ads')
    return pd.DataFrame(pd.concat(
        [pd.read_csv(p) for p in paths]))

def removeTimeFromDateTime(df, columnName):
    return pd.to_datetime(df[columnName]).dt.date

def extractAds():
    ads = convertAdsCSVToDataFrame()
    ads['sorting_date'] = removeTimeFromDateTime(ads, 'sorting_date')
    return ads