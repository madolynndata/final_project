'''' 
________________________________clean Json file from None value_________________________________________
//
Step : 
>>
___________________________________________work in progress__________________________________________
>>ahk script to factorize
'''

import os
import json
import pandas as pd
import datetime
import time
import numpy
#path_folder = 'C:\Users\Lenovo\Documents\marine_trotters\DATA\in_progress_clean_up' #path for the folder where wold be sotcked file that are cleaned, waiting for the parsing

folder_data_clean_up = r'C:\Users\Lenovo\Documents\marine_trotters\DATA\in_progress_clean_up\stepB'


json_file = r'C:\Users\Lenovo\Documents\marine_trotters\DATA\in_progress_clean_up\stepA\file_stepAplanet_osm_line_19-11-25_18-24.json'

test_json_file_name = ((os.path.basename(json_file)).split('.'))[0]
long = (len(test_json_file_name))-15
json_file_name = test_json_file_name[10:long]



file = open(json_file,'r')
data = json.load(file)

list_tempo = []
for dt in data:
    list_pota = []

    for d in dt:
        for key,value in d.items():
            if key == 'tags':
                for clef,val in value.items():
                    value_dict = {}
                    value_dict[clef] = val
                    list_pota.append(value_dict)    

            elif value != None :

                list_pota.append(d)
    list_tempo.append(list_pota)

print(list_tempo) 

def convert(o):
    if isinstance(o, numpy.int64):return int(o)  
    raise TypeError

#file_out = '\C:\Users\Lenovo\Documents\marine_trotters\DATA\in_progress_clean_up\file_test_pop.json'
current_time = datetime.datetime.now().strftime("%y-%m-%d_%H-%M")
export_file_name = 'file_stepB_'+json_file_name+'_'+current_time  


with open(folder_data_clean_up +'\\'+ export_file_name +'.json','w') as exported_file:
    exported_file.write(json.dumps(list_tempo,default=convert,sort_keys=True,indent=2,separators=(',',':')))
    exported_file.close()