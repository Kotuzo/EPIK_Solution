import json
from learn.file_loader import load


_OCCURENCES_PATH = '/home/ubuntu/Notebooks/Project/EPIK_Solution/all_data/extracted/transformed/Occurrences/'
_OCCURENCES = load(_OCCURENCES_PATH)

def transform_nb_photos(j_son):
    if isinstance(j_son, str):
        temp = json.loads(j_son)
        num_photos = 0
        for k,v in temp.items():
            num_photos += int(k)
        return num_photos
    else:
        return 0
    
    
def transform_photos_surface(j_son):
    if isinstance(j_son, str):
        temp = json.loads(j_son)
        photos_surface = 0
        for k,v in temp.items():
            photos_surface += int(k) * (v['w'] * v['h'])
        return photos_surface
    else:
        return 0


def title_transformation(row):
    temp_cat = row['category_id']
    temp_period = row['period']
    temp_title = row['title']
    
    for occ in _OCCURENCES[(_OCCURENCES['period'] == temp_period) & 
                      (_OCCURENCES['category_id'] == temp_cat)]['phrase']:
        if occ in temp_title.lower():
            return 1
    return 0


def description_transformation(description):
    pass
