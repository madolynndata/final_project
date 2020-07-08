'''' 
____________________________________code to clean up tables from PostgreSQL__________________________
//
Step : 
>>import datas from postgresql 
>>transform datas to k,v structures
>>export datas as json files

!! code will raise a warning like "SAWarning: Did not recognize type 'geometry' of column 'way'
  "Did not recognize type '%s' of column '%s'" % (attype, name)"
  >> ignore the warning (will not affect the process)
___________________________________________work in progress__________________________________________
>> factorize the script
'''

#try to update datas from pg tables with python script

import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import json
import datetime
import time
import numpy
#from config import config

#local_path
folder_data_clean_up = r'C:\Users\Lenovo\Documents\marine_trotters\DATA\in_progress_clean_up\stepA'

#conn to pg db

host = 'localhost'
db_name = 'osm_test_1115'
user = 'postgres'
password= 'digifab'
port= 5433

alchemyEngine = create_engine('postgresql+psycopg2://postgres:DIGIFAB@localhost:5433/osm_test_1115', pool_recycle=3600) #here transform to connection using configuration dictionnary
#dialect+driver://username:password@host:port/database

dbConn = alchemyEngine.connect()

#df = pd.read_sql('SELECT * FROM planet_osm_line;', dbConn)
pd.set_option('display.expand_frame_repr', False) # from tutoriel online

table_temp_line = 'planet_osm_line' #to automatize

df = pd.read_sql_table(table_temp_line, con= dbConn)


"""loop to get all the data's on key, values structure"""
#code to put in function

list_df = []

for j in range (0,len(df)):
    value_list = []

    for col in df.columns:
        value_dict = {}

        if df[col].values[j] != None :
            value_dict[col] = df[col].values[j]
                    
        else:
            value_dict[col]= None

        value_list.append(value_dict)
    list_df.append(value_list)

current_time = datetime.datetime.now().strftime("%y-%m-%d_%H-%M")
export_file_name = 'file_stepA'+table_temp_line+'_'+current_time  

def convert(o):
    '''function to force json with Python 3 on json 
    objects with int(64) dtype'''

    if isinstance(o, numpy.int64): return int(o)  
    raise TypeError

with open(folder_data_clean_up +'\\'+ export_file_name +'.json','w') as exported_file:
    exported_file.write(json.dumps(list_df,default=convert,sort_keys=True,indent=2,separators=(',',':')))
    exported_file.close()
