import pandas as pd
import common as common
import config as conf
import sys

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
    filter_cols = ['category_id', 'sorting_date', 'sessions_count', 'name_pl']
    groupby_cols = ['category_id', 'sorting_date', 'name_pl']
    return df.filter(filter_cols, axis=1).groupby(
        groupby_cols).mean().reset_index()


def extractSearchQueries():
    dirs = common.findDirsByStartsWith(startsWith)
    print('\nextracting search queries')

    for i, d in enumerate(dirs, start=1):
        paths = common.findPathsByStartsWith(startsWith, d)
        prepareCSV(paths)
        sys.stdout.write('\r %i/%i parts processed' % (i, len(dirs)))
        sys.stdout.flush()

        df = pd.DataFrame(pd.concat(
            [pd.read_csv(p, names=conf.namesOfSearchQueriesColumns)
             for p in paths]))

        searchQueriesCategories = pd.merge(df,
                                           common.categories,
                                           on='category_id')

        common.convertDataFrameToCSV(searchQueriesCategories,
                                     conf.columnsSearchQueries,
                                     d[-25:-3])
