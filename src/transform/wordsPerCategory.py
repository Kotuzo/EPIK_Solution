import os
import pandas as pd
import config as conf
import common as commn
import numpy as np
from string import punctuation
import sys


def all_sq_to_df():
    paths = commn.find_search_queries_paths()
    for p in paths:
        print(p)
        result = pd.DataFrame([])
        result = pd.read_csv(p, usecols=['phrase', 'category_id', 'sessions_count'])
        result = occurrence_per_cat(result)
        commn.save_data_frame(result, conf.columnsOfOccurredWords,
                              'occurredWordsTop' + str(conf.numberOfTopOccurredWords) + "_" + p[-11:-4],
                              transform=False)


def replace_nan_by_empty(df):
    return df.replace(np.nan, 'nan', regex=True)


def concat_phrase_per_cat(df):
    result = pd.DataFrame([])
    result = df.groupby('category_id').phrase.apply(lambda p: ','.join(p)).reset_index()
    return result


def get_stop_words():
    stop_words = []
    with open('../learn/polish_stopwords.txt', 'r', encoding="utf-8") as f:
        stop_words = [line[:-1] for line in f]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    stop_words += numbers
    return stop_words


def occurrence_per_cat(df):
    stop_words = get_stop_words()
    words = {}
    categories = get_categories(df)
    df_top_words = pd.DataFrame(columns=['phrase', 'sessions_count', 'category_id'])
    for i, cat in enumerate(categories, start=1):
        sys.stdout.write('\r %i / %i processed' % (i, len(categories)))
        for _, row in df[(df['category_id'] == cat)][['phrase', 'sessions_count']].dropna().iterrows():
            for word in row['phrase'].split():
                word = word.strip(punctuation).lower()
                if word not in stop_words and len(word) > 3:
                    words[word] = words.get(word, 0) + row['sessions_count']
        top_words = sorted(words.items(), key=lambda x: x[1], reverse=True)[:conf.numberOfTopOccurredWords]
        top_word_cat = pd.DataFrame(list(dict(top_words).items()),
                                    columns=['phrase', 'sessions_count'])
        top_word_cat['category_id'] = cat
        df_top_words = pd.concat([df_top_words, top_word_cat], ignore_index=True)
    return df_top_words


def get_categories(df):
    return df['category_id'].unique()


def run():
    all_sq_to_df()
    # phrase_cat = replace_nan_by_empty(phrase_cat)
    # phrase_cat = concat_phrase_per_cat(phrase_cat)
