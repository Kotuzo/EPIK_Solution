from learn.features import (
    description_len
)


def pre_processing(data_frame):
    pass


@description_len(False)
def data_processor(data_frame):
    '''
    This function should be decorated with processing steps
    '''
    return data_frame


def post_processing(data_frame):
    pass


def run(data_frame):
    return data_processor(data_frame)
