import os
import pandas as pd
import numpy as np
import sys

_TEST_FILENAME = 'transformed2017_10.csv'

def _get_files(data_path):
    temp = []
    for file in os.listdir(data_path):
        if ('transformed' in file) or ('occurred' in file):
            temp.append(file)
    return temp


def load(data_path):
    file_paths = _get_files(data_path)
    df = None
    first = True
    for file in file_paths:
        sys.stdout.write('\rprocessing %s' % file)
        if first and (file != _TEST_FILENAME):
            df = pd.read_csv(data_path+file)
            df['period'] = file[-11:-4]
            first = False
        elif file != _TEST_FILENAME:
            temp_df = pd.read_csv(data_path+file)
            temp_df['period'] = file[-11:-4]
            df = df.append(temp_df, 1)
    return df
