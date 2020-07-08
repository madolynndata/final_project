'''' 
__________________code to separe datas before importation on two differents table in PGsql__________________________
//
Step : 
>>
___________________________________________work in progress__________________________________________
>> factorize
'''
#import libraries
import os
import json
import pandas as pd
import datetime
import time
import numpy

#implementation of the lists
list_port_datas = []   #   json file for green tables
list_utility_datas = [] #   json file for blue tables

#comparing list
list_amenity = ['atm' , 'bank' , 'bureau-de-change' , 'drinking water' , 'hospital' , 'internet_cafe' , 'post_office' , 'shower' , 'telephone' , 'toilet']

list_man_made = ['pier','water_top']

list_building = ['supermarket','toilets','commercial','kiosk']

#paths
folder_data_clean_up = r'C:\Users\Lenovo\Documents\marine_trotters\DATA\in_progress_clean_up\stepC'

json_file = r'C:\Users\Lenovo\Documents\marine_trotters\DATA\in_progress_clean_up\stepB\file_stepB_planet_osm_line_19-11-26_09-13.json'

test_json_file_name = ((os.path.basename(json_file)).split('.'))[0]
long = (len(test_json_file_name))-15
json_file_name = test_json_file_name[10:long]

'''with open(json_file,'r') as jfile :
    json.load(jfile)
'''
file = open(json_file,'r')
data = json.load(file)

#list_tempo = [] #not use
for dt in data:
   for d in dt:
        for key,value in d.items():
            if key == 'landuse' :
                if d['landuse'] == 'port':
                    list_port_datas.append(dt)
            if key == 'man_made':
                if d['man_made'] in list_man_made:
                    list_port_datas.append(dt)
            elif key == 'office' :
                if d['office'] == 'harbour master':
                    list_port_datas.append(dt)
            elif key == 'waterway':
                if d['waterway'] == 'dock' :
                    list_port_datas.append(dt)
            elif key == 'amenity' :
                if d['amenity'] in list_amenity :
                    list_utility_datas.append(dt)
            elif key == 'building' :
                if d['building'] in list_building :
                    list_utility_datas.append(dt)

def convert(o):
    if isinstance(o, numpy.int64):return int(o)  
    raise TypeError

#file_out = '\C:\Users\Lenovo\Documents\marine_trotters\DATA\in_progress_clean_up\file_test_pop.json'
current_time = datetime.datetime.now().strftime("%y-%m-%d_%H-%M")
export_file_name = 'file_stepC_'+json_file_name+'_'  

#write on folder for list_port_datas // blue tables
with open(folder_data_clean_up +'\\'+ export_file_name+'port_datas_'+current_time+'.json','w') as exported_file :
    exported_file.write(json.dumps(list_port_datas,default=convert,sort_keys=True,indent=2,separators=(',',':')))
    exported_file.close()

#write on folder for list_utility_datas // green tables
with open(folder_data_clean_up +'\\' + export_file_name+'port_utilities_' +current_time+'.json','w') as exported_file :
    exported_file.write(json.dumps(list_utility_datas,default=convert,sort_keys=True,indent=2,separators=(',',':')))
    exported_file.close()


print(list_port_datas)