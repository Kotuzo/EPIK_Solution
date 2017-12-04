import os
import pandas as pd
import config as conf

path = os.getcwd().replace('/src/extraction', '/all_data/') \
    .replace("\\src\\extraction", "\\all_data \\")

extractedPath = path + 'extracted'
categories = pd.DataFrame(pd.read_csv(
    path + os.sep + 'categories.csv')).rename(columns={'id': 'category_id'})


def findPathsByStartsWith(startsWith, defaultDir=path, transform=False):
    paths = []
    for subdir, dir, files in os.walk(defaultDir):
        for file in files:
            if transform or not subdir.startswith(extractedPath):
                filepath = subdir + os.sep + file
                if (file.startswith(startsWith)):
                    paths.append(filepath)
    return paths

def findDirsByStartsWith(startsWith, transform=False):
    dirs = []
    for subdir, dir, files in os.walk(path):
        if transform or not subdir.startswith(extractedPath):
            if (subdir.__contains__(startsWith)):
                dirs.append(subdir)
    return dirs


def findCharIndexesInString(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def convertDataFrameToCSV(df, columns, filename):
    if not os.path.exists(extractedPath):
        os.makedirs(extractedPath)
    the_path = extractedPath + os.sep + 'extracted_' + filename + '.csv'
    try:
        pd.DataFrame(df[columns]).to_csv(the_path, index=False)
    except KeyError:
        pd.DataFrame(df[conf.columnsAdsTest]).to_csv(the_path, index=False)