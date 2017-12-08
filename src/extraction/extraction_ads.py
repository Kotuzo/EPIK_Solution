import common as common
import pandas as pd
import config as conf
import sys

pd.options.display.max_colwidth = 100

startsWith = "ads"


def remove_time_from_sorting_date(df, columnName):
    return pd.to_datetime(df[columnName]).dt.date


def transform_params_column_into_records(df):
    s = df.str.replace('price<', 'priceType<', 1).str.replace('price<=', 'priceValue<=', 1).str.split('<br>')
    d = []
    for w in s:
        if str(w) != 'nan':
            d.append(dict(x.split('<=>', 1) for x in w))
        else:
            d.append(dict())

    # cols = list(set(val for dic in d for val in dic.keys())) # Returns more params than on their website 'builttype', 'price', 'motor_hours', 'petrol', 'breeding', 'organisation', 'rate_per_hour', 'floor_select', 'size', 'enginepower', 'country_origin', 'power', 'model', 'width', 'contract', 'priceType', 'enginesize', 'car_body', 'tiretype', 'remote_work', 'roomsize', 'publishyear', 'milage', 'year', 'color', 'state', 'rooms', 'lostfound', 'rims', 'm', 'axes', 'loadcapacity', 'requirements', 'condition', 'profile', 'type', 'mark', 'furniture', 'price_per_m', 'transmission'
    cols = list(conf.columnsParams)
    return pd.DataFrame.from_records(d, index=df.index, columns=cols)


def extract_ads():
    paths = common.find_files_in_directory_starts_with('ads')
    print('\nextracting ads')
    for i, p in enumerate(paths, start=1):
        print(p)
        sys.stdout.write('\r %i/%i files processed' % (i, len(paths)))
        sys.stdout.flush()
        df = pd.read_csv(p)
        params = transform_params_column_into_records(df['params'])
        df = pd.merge(df, params, left_index=True, right_index=True)
        df['sorting_date'] = remove_time_from_sorting_date(df, 'sorting_date')
        ads = pd.merge(df, common.categories, on='category_id')
        common.save_data_frame(ads, conf.columnsAds + conf.columnsParams, p[-14:-3], startsWith)
