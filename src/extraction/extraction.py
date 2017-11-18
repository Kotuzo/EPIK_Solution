import pandas as pd
import config as conf
import ads as a
import searchQueries as s
import common as common

# To Place:
# Ads files in all_data
# Categories.vsc in all_data
# SearchQueries in unziped in all_data, .gz removed
# Result in extracted f.g ads_YYYY_MM , search_queries_YYYY_MM
# Selecting extracted columns by config.py

def main():
    s.extractSearchQueries()
    a.extractAds()

if __name__ == '__main__':
    main()
