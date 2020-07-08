'''' 
__________________code convert stepC's files to list of dictionnaries__________________________
//
Step : 
>>
___________________________________________work in progress__________________________________________
>> factorize
'''
import os
import json
import datetime
import time
import numpy

json_file = (r'C:\Users\Lenovo\Documents\marine_trotters\DATA\in_progress_clean_up\stepC\file_stepC__planet_osm_line_port_datas_19-11-26_13-40.json')

folder_data_clean_up = r'C:\Users\Lenovo\Documents\marine_trotters\DATA\in_progress_clean_up\stepD'


test_json_file_name = ((os.path.basename(json_file)).split('.'))[0]
long = (len(test_json_file_name))-15
json_file_name = test_json_file_name[12:long]


with open(json_file, 'r') as fichier:
    parsed = json.load(fichier)
    dico_end_recup = []
    for p in parsed:
       
        dicoRecup={}

        for truc in p:
            for key,value in truc.items():
                dicoRecup[key]=value
        dico_end_recup.append(dicoRecup)

def convert(o):
    if isinstance(o, numpy.int64):return int(o)  
    raise TypeError

#file_out = '\C:\Users\Lenovo\Documents\marine_trotters\DATA\in_progress_clean_up\file_test_pop.json'
current_time = datetime.datetime.now().strftime("%y-%m-%d_%H-%M")
export_file_name = 'file_stepD_'+json_file_name+'_'  

with open(folder_data_clean_up +'\\'+ export_file_name +current_time +'.json','w') as exported_file :
    exported_file.write(json.dumps(dico_end_recup,default=convert,sort_keys=True,indent=2,separators=(',',':')))
    exported_file.close()