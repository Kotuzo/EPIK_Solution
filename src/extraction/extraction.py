import pandas as pd
import os
import config as conf

path = os.getcwd().replace('/src/extraction', '/all_data/').replace("\\src\\extraction", "\\all_data\\")
extractedPath = path + 'extracted'
categories = pd.DataFrame(pd.read_csv(path + os.sep + 'categories.csv')).rename(columns={'id': 'category_id'})


def searchPathsByStartsWith(startsWith: str):
    paths = []
    for subdir, dir, files in os.walk(path):
        for file in files:
            if not subdir.startswith(extractedPath):
                filepath = subdir + os.sep + file
                if file.startswith(startsWith):
                    paths.append(filepath)
    return paths


def repairFile(paths):
    for path in paths:
        tempString = ''
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                commaIndexes = findIndexes(line, ',')
                if len(commaIndexes) > 2:
                    for i in commaIndexes[:-2]:
                        temp = list(line)
                        temp[i] = '.'
                        line = "".join(temp)
                tempString += line
        with open(path[:-4] + 'oczko' + '.csv', 'w', encoding='utf-8') as f:
            f.write(tempString)


def findIndexes(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def searchQueriesFromCSV():
    paths = searchPathsByStartsWith('search')
    print('\n'.join(paths[1:2]))
    return pd.DataFrame(pd.concat(
        [pd.read_csv(p, names=conf.columnNamesSearchQueries) for p in paths[1:2]]))


def adsFromCSV():
    paths = searchPathsByStartsWith('ads')
    return pd.DataFrame(pd.concat(
        [pd.read_csv(p) for p in paths]))


def toCSV(df, columns, filename):
    if not os.path.exists(extractedPath):
        os.makedirs(extractedPath)
    pd.DataFrame(df[columns]).to_csv(extractedPath + os.sep + filename + '.csv')


def main():
    repairFile(searchPathsByStartsWith('search'))
    # print(searchQueriesFromCSV().iloc[122990])
    # toCSV(pd.merge(searchQueriesFromCSV(), categories, on='category_id'), conf.columnsSearchQueries, 'search')
    # toCSV(pd.merge(adsFromCSV(), categories, on='category_id'), conf.columnsAds, 'ads')


if __name__ == '__main__':
    main()
