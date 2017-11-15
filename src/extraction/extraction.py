import pandas as pd
import os
import glob

path = os.getcwd().replace('/src/extraction', '/all_data/')

categories = pd.DataFrame(pd.read_csv(path + os.sep + 'categories.csv', error_bad_lines=False))

def searchPathsByStartsWith(startsWith: str):
    paths = []
    for subdir, dir, files in os.walk(path):
        for file in files:
            filepath = subdir + os.sep + file
            if file.startswith(startsWith):
                paths.append(filepath)
    return paths


#TODO remove :5 from loop
def concatCSV(paths):
    return pd.concat([pd.read_csv(p, error_bad_lines=False) for p in paths[:5]])


def main():
    searchQueries = pd.DataFrame(concatCSV(searchPathsByStartsWith('search')))
    print(searchQueries.keys())

if __name__ == '__main__':
    main()
