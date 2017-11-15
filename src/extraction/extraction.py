import pandas as pd
import os
from IPython.display import display, HTML

path = os.getcwd().replace('/src/extraction', '/all_data/')

categories = pd.DataFrame(pd.read_csv(path + os.sep + 'categories.csv')).rename(columns={'id': 'category_id'})


def searchPathsByStartsWith(startsWith: str):
    paths = []
    for subdir, dir, files in os.walk(path):
        for file in files:
            filepath = subdir + os.sep + file
            if file.startswith(startsWith):
                paths.append(filepath)
    return paths


def concatSearchCSV():
    paths = searchPathsByStartsWith('search')
    return pd.DataFrame(pd.concat(
        [pd.read_csv(p, names=['phrase', 'category_id', 'sessions_count']) for p in paths[:10]]))


def concatAdsCSV():
    paths = searchPathsByStartsWith('ads')
    return pd.DataFrame(pd.concat(
        [pd.read_csv(p) for p in paths]))


def main():
    searchQueries = concatSearchCSV()
    # print(searchQueries)
    # print(searchQueries.keys())
    # print(categories.keys())
    test = searchQueries.merge(categories, on='category_id', how='inner', suffixes=('_sq', '_cat'))
    print(test.keys())
    print(test)
    # print(test[['category_id_sq', 'category_id_cat']])
    test.to_csv(
        path + os.sep + 'test.csv', index=False)


if __name__ == '__main__':
    main()
