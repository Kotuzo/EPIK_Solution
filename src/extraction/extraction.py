import ads as a
import searchQueries as s
import config as conf
import transformation as ts

# To Place:
# Ads files in all_data
# Categories.vsc in all_data
# SearchQueries in unziped in all_data, .gz removed
# Result in extracted f.g ads_YYYY_MM , search_queries_YYYY_MM
# Selecting extracted columns by config.py

def main():
    s.extractSearchQueries()
    a.extractAds()
    ts.transformation_search_queries()
    ts.merge_with_ads()


def extraction_mode(mode):
    modes = {
        'all': main,
        'only_ads': a.extractAds,
        'only_search_queries': s.extractSearchQueries,
        'only_transformation': ts.transformation_search_queries,
        'only_ads_transform': ts.merge_with_ads
    }
    return modes[mode]()


if __name__ == '__main__':
    extraction_mode(conf.EXTRACTION_MODE)
