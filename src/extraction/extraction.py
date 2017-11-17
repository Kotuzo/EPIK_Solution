import pandas as pd
import config as conf
import ads as a
import searchQueries as s
import common as common


def main():
    searchQueries = s.extractSearchQueries()
    common.convertDataFrameToCSV(searchQueries, conf.columnsSearchQueries, 'search')
    ads = a.extractAds()
    print(ads.keys())

    #TODO: why it doesn't merge
    # final = pd.merge(ads, searchQueries, on=['sorting_date', 'category_id'], how='right')

    common.convertDataFrameToCSV(ads, conf.columnsAds, 'ads')
    # common.convertDataFrameToCSV(final, conf.finalColumns, 'final')

if __name__ == '__main__':
    main()
