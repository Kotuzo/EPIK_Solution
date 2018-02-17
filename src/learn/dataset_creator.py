from learn.features import (
    description_len,
    full_description_len,
    predict_sold_to_numbers,
    paid_ads,
    nb_photos,
    photos_surface
)


def pre_processing(data_frame):
    print('preprocessing started.')
    return data_frame


@description_len(False)
@full_description_len(False)
@predict_sold_to_numbers(False)
@paid_ads(True)
@nb_photos(False)
@photos_surface(True)
def data_processor(data_frame):
    '''
    This function should be decorated with processing steps
    '''
    return data_frame


def post_processing(data_frame):
    print('postprocessing started.')
    data_frame.drop(['used'], axis=1, inplace=True)
    data_frame.drop(['business'], axis=1, inplace=True)
    #very high correlation with price
    data_frame.drop(['arranged'], axis=1, inplace=True)
    return data_frame


def run(data_frame):
    #pre_processing(data_frame)
    return post_processing(data_processor(pre_processing(data_frame)))
