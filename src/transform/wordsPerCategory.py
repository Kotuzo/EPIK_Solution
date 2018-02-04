import os
import pandas as pd
import config as conf
import common as commn
import numpy as np


def all_sq_to_df():
    paths = commn.find_search_queries_paths()
    result = pd.DataFrame([])
    for p in paths[:1]:
        result = result.append(pd.read_csv(p, usecols=['phrase', 'category_id']))
    return result


def replace_nan_by_empty(df):
    return df.replace(np.nan, 'nan', regex=True)


def concat_phrase_per_cat(df):
    result = pd.DataFrame([])
    result = df.groupby('category_id').phrase.apply(lambda p: ','.join(p)).reset_index()
    return result


def occurrence_per_cat(df):
    df = df.set_index('category_id')
    for index, row in df.iterrows():
        print(index)
        words = row['phrase'].split(',')
        uniques = []
        for word in words:
            if word not in uniques:
                uniques.append(str(word))
        counts = []
        for unique in uniques:
            count = 0
            for word in words:
                if word == unique:
                    count += 1
            counts.append((count, str(unique)))

        counts.sort()
        counts.reverse()
        wordCountMap = {}
        for i in range(min(conf.numberOfTopOccurredWords, len(counts))):
            count, word = counts[i]
            wordCountMap[word] = count
        print(wordCountMap)
        df.at[index, 'phrase'] = wordCountMap
    return df.reset_index()


def categories_count(df):
    return (len(df['category_id'].unique()))


def run():
    phrase_cat = all_sq_to_df()
    categoriesCount = categories_count(phrase_cat)
    phrase_cat = replace_nan_by_empty(phrase_cat)
    phrase_cat = concat_phrase_per_cat(phrase_cat)
    commn.save_data_frame(occurrence_per_cat(phrase_cat), conf.columnsOfOccurredWords,
                          'occurredWordsTop_' + str(conf.numberOfTopOccurredWords), transform=False)
