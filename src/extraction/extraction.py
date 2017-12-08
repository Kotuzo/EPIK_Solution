import extraction_ads as a
import extraction_search_queries as s
import config as conf

# To Place:
# Ads files in all_data
# Categories.vsc in all_data
# SearchQueries in unziped in all_data, .gz removed
# Result in extracted f.g ads_YYYY_MM , search_queries_YYYY_MM
# Selecting extracted columns by config.py

def main():
    s.extract_search_queries()
    a.extract_ads()

def extraction_mode(mode):
    modes = {
        'all': main,
        'only_ads': a.extract_ads,
        'only_search_queries': s.extract_search_queries,
    }
    return modes[mode]()


if __name__ == '__main__':
    extraction_mode(conf.EXTRACTION_MODE)
