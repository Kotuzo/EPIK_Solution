EXTRACTION_MODE = 'words_per_category'

columnsSQ = ['category_id', 'derivative', 'average', 'min', 'max']

finalTransformColumns = ['id', 'predict_sold', 'predict_replies', 'predict_views', 'priceValue', 'derivative',
                         'average', 'min', 'max', 'business', 'private', 'arranged', 'exchange', 'free',
                         'price', 'new', 'used']

columnsAds = ['id', 'region_id', 'category_id', 'subregion_id', 'district_id',
              'city_id', 'accurate_location', 'user_id', 'sorting_date',
              'created_at_first', 'valid_to', 'title', 'description',
              'full_description', 'has_phone', 'params', 'private_business',
              'has_person', 'photo_sizes', 'paidads_id_index', 'paidads_valid_to',
              'predict_sold', 'predict_replies', 'predict_views', 'reply_call',
              'reply_sms', 'reply_chat', 'reply_call_intent', 'reply_chat_intent',
              'parent_id', 'name_pl']

columnsParams = ['priceType', 'priceValue', 'state', 'type', 'mark', 'size']

columnsAdsTest = ['id', 'region_id', 'category_id', 'subregion_id', 'district_id',
                  'city_id', 'accurate_location', 'user_id', 'sorting_date',
                  'created_at_first', 'valid_to', 'title', 'description',
                  'full_description', 'has_phone', 'params', 'private_business',
                  'has_person', 'photo_sizes', 'paidads_id_index', 'paidads_valid_to',
                  'parent_id', 'name_pl']
columnsFinalTransformColumnsTest = ['id', 'priceValue', 'derivative', 'average', 'min', 'max',
                                    'business', 'private', 'arranged', 'exchange', 'free', 'price', 'new',
                                    'used']

numberOfTopOccurredWords = 4

columnsOfOccurredWords = ['category_id', 'phrase']
