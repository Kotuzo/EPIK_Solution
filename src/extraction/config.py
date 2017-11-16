 # ['id', 'region_id', 'category_id', 'subregion_id', 'district_id',
 #       'city_id', 'accurate_location', 'user_id', 'sorting_date',
 #       'created_at_first', 'valid_to', 'title', 'description',
 #       'full_description', 'has_phone', 'params', 'private_business',
 #       'has_person', 'photo_sizes', 'paidads_id_index', 'paidads_valid_to',
 #       'predict_sold', 'predict_replies', 'predict_views', 'reply_call',
 #       'reply_sms', 'reply_chat', 'reply_call_intent', 'reply_chat_intent']
columnsAds = ['sorting_date', 'category_id', 'title']
# ['sorting_date', 'phrase', 'category_id', 'sessions_count', 'parent_id', 'name_pl']
columnsSearchQueries = ['sorting_date',  'category_id',  'name_pl', 'sessions_count']

finalColumns = ['sessions_count', 'title', 'name_pl', 'sorting_date', 'phrase']
staticColumnsSearchQueries= ['sorting_date', 'phrase', 'category_id', 'sessions_count']
