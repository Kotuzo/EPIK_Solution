import os
import pandas as pd
import config as conf

path = os.getcwd().replace('/src/extraction', '/all_data/') \
    .replace("\\src\\extraction", "\\all_data\\")

extractedPath = path + 'extracted' + os.sep
categories = pd.DataFrame(pd.read_csv(
    path + os.sep + 'categories.csv')).rename(columns={'id': 'category_id'})


def find_files_in_directory_starts_with(startsWith, defaultDir=path):
    paths = []
    for subdir, dir, files in os.walk(defaultDir):
        for file in files:
            if not subdir.startswith(extractedPath):
                filepath = subdir + os.sep + file
                if file.startswith(startsWith):
                    paths.append(filepath)
    return paths


def find_directories_starts_with(starts_with):
    dirs = []
    for subdir, dir, files in os.walk(path):
        if not subdir.startswith(extractedPath):
            if subdir.__contains__(starts_with):
                dirs.append(subdir)
    return dirs


def findCharIndexesInString(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def save_data_frame(df, columns, filename, directory_name):
    create_directory_if_not_exists(extractedPath + directory_name)
    the_path = extractedPath + directory_name + os.sep + filename + '.csv'
    try:
        pd.DataFrame(df[columns]).to_csv(the_path, index=False)
    except KeyError:
        pd.DataFrame(df[conf.columnsAdsTest]).to_csv(the_path, index=False)

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)