import pandas as pd
import os
import config as conf

path = os.getcwd().replace('/src/extraction', '/all_data/').replace("\\src\\extraction", "\\all_data\\")
extractedPath = path + os.sep + 'extracted'

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


def searchQueriesFromCSV():
    paths = searchPathsByStartsWith('search')
    return pd.DataFrame(pd.concat(
        [pd.read_csv(p, names=conf.columnsSearchQueries) for p in paths]))


def adsFromCSV():
    paths = searchPathsByStartsWith('ads')
    print(paths)
    return pd.DataFrame(pd.concat(
        [pd.read_csv(p) for p in paths]))


def toCSV(df, columns, filename):
    if not os.path.exists(extractedPath):
        os.makedirs(extractedPath)
    pd.DataFrame(df[columns]).to_csv(extractedPath + os.sep + filename + '.csv')


def main():
    toCSV(pd.merge(searchQueriesFromCSV(), categories, on='category_id'), conf.columnsSearchQueries, 'search')
    toCSV(pd.merge(adsFromCSV(), categories, on='category_id'), conf.columnsAds, 'ads')


if __name__ == '__main__':
    main()
