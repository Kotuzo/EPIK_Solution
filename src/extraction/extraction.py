import pandas as pd
import os
from IPython.display import display, HTML

path = os.getcwd().replace('/src/extraction', '/all_data/').replace("\\src\\extraction", "\\all_data\\")

categories = pd.DataFrame(pd.read_csv(path + os.sep + 'categories.csv'))


# .rename(columns={'id': 'category_id'})


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
        [pd.read_csv(p, names=['phrase', 'category_id', 'sessions_count']) for p in paths]))


def concatAdsCSV():
    paths = searchPathsByStartsWith('ads')
    return pd.DataFrame(pd.concat(
        [pd.read_csv(p) for p in paths]))


def main():
    # searchQueries = concatSearchCSV()
    ads = concatAdsCSV()
    # test = searchQueries.merge(categories, left_on='category_id', right_on='parent_id', how='left', suffixes=('_sq', '_cat'))
    test1 = ads.merge(categories, left_on='category_id', right_on='id', how='inner', suffixes=('_ads', '_cat'))
    print(test1[['id_ads', 'id_cat']])


if __name__ == '__main__':
    main()
