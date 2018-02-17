'''This script contains functions, which are used to create new features'''
import numpy as np
import json
from learn.transformations import *


def description_len(drop=False):
    def decorator(func):
        def inner(data_frame):
            # creation of new feature
            data_frame['description_len'] = data_frame['description'].apply(lambda d: len(d))
            if drop:
                # if u want to drop original column, then do this
                data_frame.drop(['description'], axis=1, inplace=True)
            # call next step / function
            return func(data_frame)
        return inner
    return decorator

def full_description_len(drop=False):
    def decorator(func):
        def inner(data_frame):
            # creation of new feature
            data_frame['full_description_len'] = data_frame['full_description'].apply(lambda d: len(d))
            if drop:
                # if u want to drop original column, then do this
                data_frame.drop(['full_description'], axis=1, inplace=True)
            # call next step / function
            return func(data_frame)
        return inner
    return decorator

def predict_sold_to_numbers(drop=False):
    def decorator(func):
        def inner(data_frame):
            data_frame['predict_sold'] = data_frame['predict_sold'].apply(lambda d: 0 if d == 'f' else 1)
            if drop:
                # if u want to drop original column, then do this
                #data_frame.drop(['predict_sold'], axis=1, inplace=True)
                pass
            # call next step / function
            return func(data_frame)
        return inner
    return decorator

def paid_ads(drop=False):
    def decorator(func):
        def inner(data_frame):
            data_frame['paid_ads'] = data_frame['paidads_id_index'].apply(lambda d: 0 if np.isnan(d) else 1)
            if drop:
                # if u want to drop original column, then do this
                data_frame.drop(['paidads_id_index', 'paidads_valid_to'], axis=1, inplace=True)
                pass
            # call next step / function
            return func(data_frame)
        return inner
    return decorator

def nb_photos(drop=False):
    def decorator(func):
        def inner(data_frame):
            data_frame['nb_photos'] = data_frame['photo_sizes'].apply(lambda d: transform_nb_photos(d))
            if drop:
                # if u want to drop original column, then do this
                data_frame.drop(['photo_sizes'], axis=1, inplace=True)
                pass
            # call next step / function
            return func(data_frame)
        return inner
    return decorator

def photos_surface(drop=False):
    def decorator(func):
        def inner(data_frame):
            data_frame['photos_surface'] = data_frame['photo_sizes'].apply(lambda d: transform_photos_surface(d))
            if drop:
                # if u want to drop original column, then do this
                data_frame.drop(['photo_sizes'], axis=1, inplace=True)
                pass
            # call next step / function
            return func(data_frame)
        return inner
    return decorator

#use only if there are nb_photos and photo_sizes features, dont use it now...
def avg_photos_surface(drop=False):
    def decorator(func):
        def inner(data_frame):
            data_frame['photos_surface'] = data_frame['photo_sizes'].apply(lambda d: transform_photos_surface(d))
            if drop:
                # if u want to drop original column, then do this
                data_frame.drop(['photo_sizes'], axis=1, inplace=True)
                pass
            # call next step / function
            return func(data_frame)
        return inner
    return decorator