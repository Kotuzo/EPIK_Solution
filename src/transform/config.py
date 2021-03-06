columnsSQ = ['category_id', 'derivative', 'average', 'min', 'max']

finalTransformColumns = ['id', 'category_id', 'title', 'description', 'predict_sold', 'predict_replies',
                         'predict_views', 'priceValue', 'derivative', 'average', 'min', 'max', 'business', 'private',
                         'arranged', 'exchange', 'free', 'price', 'new', 'used', 'photo_sizes', 'paidads_id_index',
                         'paidads_valid_to']

columnsAds = ['id', 'region_id', 'category_id', 'subregion_id', 'district_id',
              'city_id', 'accurate_location', 'user_id', 'sorting_date',
              'created_at_first', 'valid_to', 'title', 'description',
              'full_description', 'has_phone', 'params', 'private_business',
              'has_person', 'photo_sizes', 'paidads_id_index', 'paidads_valid_to',
              'predict_sold', 'predict_replies', 'predict_views', 'reply_call',
              'reply_sms', 'reply_chat', 'reply_call_intent', 'reply_chat_intent',
              'parent_id', 'name_pl', 'full_description']

columnsParams = ['priceType', 'priceValue', 'state', 'type', 'mark', 'size']

columnsAdsTest = ['id', 'region_id', 'category_id', 'subregion_id', 'district_id',
                  'city_id', 'accurate_location', 'user_id', 'sorting_date',
                  'created_at_first', 'valid_to', 'title', 'description',
                  'full_description', 'has_phone', 'params', 'private_business',
                  'has_person', 'photo_sizes', 'paidads_id_index', 'paidads_valid_to',
                  'parent_id', 'name_pl', 'full_description']

columnsFinalTransformColumnsTest = ['id', 'category_id', 'title', 'description', 'priceValue', 'derivative', 'average',
                                    'min', 'max', 'business', 'private', 'arranged', 'exchange', 'free', 'price', 'new',
                                    'used', 'photo_sizes', 'paidads_id_index', 'paidads_valid_to']

numberOfTopOccurredWords = 100
columnsOfOccurredWords = ['category_id', 'phrase', 'sessions_count']
EXTRACTION_MODE = 'words_per_category'
