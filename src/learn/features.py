'''This script contains functions, which are used to create new features'''


def description_len(drop=False):
    def decorator(func):
        def inner(data_frame):
            # creation of new feature
            data_frame['description_len'] = data_frame['description'].apply(lambda d: len(d))
            if drop:
                # if u want to drop original column, then do this
                data_frame.drop(['description'], axis=1, in_place=True)
            # call next step / function
            return func(data_frame)
        return inner
    return decorator
