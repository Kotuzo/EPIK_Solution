# 'id', 'region_id', 'category_id', 'subregion_id', 'district_id',
#        'city_id', 'accurate_location', 'user_id', 'sorting_date',
#        'created_at_first', 'valid_to', 'title', 'description',
#        'full_description', 'has_phone', 'params', 'private_business',
#        'has_person', 'photo_sizes', 'paidads_id_index', 'paidads_valid_to',
#        'predict_sold', 'predict_replies', 'predict_views', 'reply_call',
#        'reply_sms', 'reply_chat', 'reply_call_intent', 'reply_chat_intent',
#          'parent_id', 'name_pl'
EXTRACTION_MODE = 'all'  # all/only_ads/only_search_queries/only_ads_transform/only_transformation
columnsAds = ['id', 'region_id', 'category_id', 'subregion_id', 'district_id',
              'city_id', 'accurate_location', 'user_id', 'sorting_date',
              'created_at_first', 'valid_to', 'title', 'description',
              'full_description', 'has_phone', 'params', 'private_business',
              'has_person', 'photo_sizes', 'paidads_id_index', 'paidads_valid_to',
              'predict_sold', 'predict_replies', 'predict_views', 'reply_call',
              'reply_sms', 'reply_chat', 'reply_call_intent', 'reply_chat_intent',
              'parent_id', 'name_pl']

columnsParams = ['priceType', 'price', 'state', 'type', 'mark', 'size']

columnsAdsTest = ['id', 'region_id', 'category_id', 'subregion_id', 'district_id',
              	  'city_id', 'accurate_location', 'user_id', 'sorting_date',
	              'created_at_first', 'valid_to', 'title', 'description',
	              'full_description', 'has_phone', 'params', 'private_business',
	              'has_person', 'photo_sizes', 'paidads_id_index', 'paidads_valid_to',
	              'parent_id', 'name_pl']
# 'sorting_date', 'phrase', 'category_id', 'sessions_count', 'parent_id', 'name_pl'
columnsSearchQueries = ['sorting_date', 'phrase', 'category_id', 'sessions_count', 'parent_id', 'name_pl']
# ['id', 'region_id', 'category_id', 'subregion_id', 'district_id',
#        'city_id', 'accurate_location', 'user_id', 'sorting_date',
#        'created_at_first', 'valid_to', 'title', 'description',
#        'full_description', 'has_phone', 'params', 'private_business',
#        'has_person', 'photo_sizes', 'paidads_id_index', 'paidads_valid_to',
#        'predict_sold', 'predict_replies', 'predict_views', 'reply_call',
#        'reply_sms', 'reply_chat', 'reply_call_intent', 'reply_chat_intent',
#        'sessions_count']
finalColumns = ['title', 'category_id', 'sorting_date', 'sessions_count']

namesOfSearchQueriesColumns = ['sorting_date', 'phrase', 'category_id', 'sessions_count']

# config for transformation
columnsSQ = ['category_id', 'derivative', 'average', 'min', 'max']


