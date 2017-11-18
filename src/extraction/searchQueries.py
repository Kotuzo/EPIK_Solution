import pandas as pd
import common as common
import config as conf
import os

startsWith = 'search_queries'

def prepareCSV(paths):
    for path in paths:
        tempString = ''
        with open(path, 'r', encoding='utf-8') as f:
            date = "\"" + f.name[-14:-4] + "\","
            date = date.replace('_', '-')
            for line in f:
                commaIndexes = common.findCharIndexesInString(line, ',')
                if not line.startswith(date):
                    tempString += date
                    if len(commaIndexes) > 2:
                        for i in commaIndexes[:-2]:
                            temp = list(line)
                            temp[i] = '.'
                            line = "".join(temp)
                tempString += line
        with open(path, 'w', encoding='utf-8') as f:
            f.write(tempString)


def groupBy(df):
    return df.filter(['category_id', 'sorting_date', 'sessions_count', 'name_pl'], axis=1).groupby(
        ['category_id', 'sorting_date', 'name_pl']).mean().reset_index()


def extractSearchQueries():
    dirs = common.findDirsByStartsWith(startsWith)
    for d in dirs:
        paths = common.findPathsByStartsWith(startsWith, d)
        df = pd.DataFrame(pd.concat(
            [pd.read_csv(p, names=conf.namesOfSearchQueriesColumns) for p in paths]))
        searchQueriesCategories = pd.merge(df, common.categories, on='category_id')
        common.convertDataFrameToCSV(searchQueriesCategories, conf.columnsSearchQueries, d[-25:-3])
