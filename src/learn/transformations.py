import json

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

def title_tranformation(title):
    pass

def description_transformation(description):
    pass
