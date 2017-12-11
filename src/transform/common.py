import os
import pandas as pd
import config as conf

path = os.getcwd().replace('/src/transform', '/all_data/') \
    .replace("\\src\\transform", "\\all_data\\")

extractedPath = path + 'extracted'
searchQueriesDir = extractedPath + os.sep + "search_queries"
adsDir = extractedPath + os.sep + "ads"
transformationDir = extractedPath + os.sep + "transformed"
categories = pd.DataFrame(pd.read_csv(
    path + os.sep + 'categories.csv')).rename(columns={'id': 'category_id'})


def find_search_queries_paths():
    return find_files_in_directory_starts_with("search_queries", searchQueriesDir)


def find_ads_paths():
    return find_files_in_directory_starts_with("ads", adsDir)


def find_transformed_file_starts_with(startsWith):
    return find_files_in_directory_starts_with(startsWith, transformationDir)


def find_files_in_directory_starts_with(startsWith, dir):
    paths = []
    for subdir, dir, files in os.walk(dir):
        for file in files:
            filepath = subdir + os.sep + file
            if file.startswith(startsWith):
                paths.append(filepath)
    return paths


def find_extracted_dictionaries():
    dirs = []
    for subdir, dir, files in os.walk(path):
        if subdir.startswith(extractedPath):
            if subdir.__contains__(path + extractedPath):
                dirs.append(subdir)
    return dirs


def findCharIndexesInString(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def save_data_frame(df, columns, filename, transform=False):
    create_directory_if_not_exists(transformationDir)
    the_path = transformationDir + os.sep + filename + '.csv'
    print(df.keys())
    print(columns)
    try:
        pd.DataFrame(df[columns]).to_csv(the_path, index=False)
    except KeyError:
        print("\nTest Set " + the_path)
        if not transform:
            pd.DataFrame(df[conf.columnsAdsTest + conf.columnsParams + conf.columnsSQ]).to_csv(the_path, index=False)
        else:
            pd.DataFrame(df[conf.columnsFinalTransformColumnsTest]).to_csv(the_path, index=False)


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
