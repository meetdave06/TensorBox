'''
Author: Meet Dave 
Date: 09/18/2016
Description: Takes idl files and converts it into json format
E.g. :- python idl_to_json.py data/brainwash/brainwash_train.idl data/brainwash/brainwash_train.json

'''


import json
import sys
from utils.annolist import AnnotationLib as al


#get our files for processing

if len(sys.argv) < 3:
    print "Too few params, try something like:  python make_idl.py train640x480 train.idl"
    exit()
path = sys.argv[1]
outfile_name = sys.argv[2]


# Open idl file
true_annolist = al.parse(path)



final_json = []
for i in range(len(true_annolist)):
    # True_anno contains image name and list of rects
    true_anno = true_annolist[i]
    json_dict = {}
    json_dict['image_path'] = true_anno.imageName
    json_dict['rects'] = []

    for rect in true_anno.rects:
        rects = {}            
        rects['x1'] = rect.x1
        rects['x2'] = rect.x2
        rects['y1'] = rect.y1
        rects['y2'] = rect.y2
        json_dict['rects'].append(rects)

    final_json.append(json_dict)




# Write to a json

with open(outfile_name, 'w') as outfile:
    json.dump(final_json, outfile, sort_keys = True, indent=4)



