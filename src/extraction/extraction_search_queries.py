import pandas as pd
import common as common
import config as conf
import sys
import time

startsWith = 'search_queries'


def replace_unhappy_commas_and_add_dates_to_csv(paths):
    for path in paths:
        tempString = ''
        with open(path, 'r', encoding='utf-8') as f:
            date = "\"" + f.name[-14:-4] + "\","
            date = date.replace('_', '-')
            start = time.clock()
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
            print(time.clock() - start)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(tempString)


def extract_search_queries():
    dirs = common.find_directories_starts_with(startsWith)
    print('\nextracting search queries')
    for i, d in enumerate(dirs, start=1):
        paths = common.find_files_in_directory_starts_with(startsWith, d)
        replace_unhappy_commas_and_add_dates_to_csv(paths)
        sys.stdout.write('\r %i/%i parts processed' % (i, len(dirs)))
        sys.stdout.flush()

        df = pd.DataFrame(pd.concat(
            [pd.read_csv(p, names=conf.namesOfSearchQueriesColumns)
             for p in paths]))

        searchQueriesCategories = pd.merge(df,
                                           common.categories,
                                           on='category_id')

        common.save_data_frame(searchQueriesCategories,
                               conf.columnsSearchQueries,
                               remove_path_and_csv_from(d),
                               startsWith)


def remove_path_and_csv_from(full_path):
    return full_path[-25:-3]
