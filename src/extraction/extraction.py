import pandas as pd
import os
import config as conf

path = os.getcwd().replace('/src/extraction', '/all_data/').replace("\\src\\extraction", "\\all_data\\")
extractedPath = path + 'extracted'
categories = pd.DataFrame(pd.read_csv(path + os.sep + 'categories.csv')).rename(columns={'id': 'category_id'})

def findPathsByStartsWith(startsWith):
    paths = []
    for subdir, dir, files in os.walk(path):
        for file in files:
            if not subdir.startswith(extractedPath):
                filepath = subdir + os.sep + file
                if (file.startswith(startsWith)):
                    paths.append(filepath)
    return paths


def findCharIndexesInString(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def convertSearchQueriesCSVToDataFrame():
    paths = findPathsByStartsWith('search')
    return pd.DataFrame(pd.concat(
        [pd.read_csv(p, names=conf.staticColumnsSearchQueries) for p in paths]))


def convertAdsCSVToDataFrame():
    paths = findPathsByStartsWith('ads')
    return pd.DataFrame(pd.concat(
        [pd.read_csv(p) for p in paths]))


def convertDataFrameToCSV(df, columns, filename):
    if not os.path.exists(extractedPath):
        os.makedirs(extractedPath)
    pd.DataFrame(df[columns]).to_csv(extractedPath + os.sep + filename + '.csv')


def prepareSearchQueriesCSV(paths):
    for path in paths:
        tempString = ''
        with open(path, 'r', encoding='utf-8') as f:
            date = "\"" + f.name[-14:-4] + "\","
            date = date.replace('_', '-')
            for line in f:
                commaIndexes = findCharIndexesInString(line, ',')
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


def removeTimeFromDateTime(df, columnName):
    return pd.to_datetime(df[columnName]).dt.date


def main():
    prepareSearchQueriesCSV(findPathsByStartsWith('search'))
    searchQueriesCategories = pd.merge(convertSearchQueriesCSVToDataFrame(), categories, on='category_id')
    ads = convertAdsCSVToDataFrame()
    ads['sorting_date'] = removeTimeFromDateTime(ads, 'sorting_date')

    convertDataFrameToCSV(searchQueriesCategories, conf.columnsSearchQueries, 'search')
    convertDataFrameToCSV(ads, conf.columnsAds, 'ads')

    # finalDataFrame = pd.merge(ads, searchQueriesCategories, on=['sorting_date', 'category_id'])
    # convertDataFrameToCSV(finalDataFrame, conf.finalColumns, 'final')


if __name__ == '__main__':
    main()
