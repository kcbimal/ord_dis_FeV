#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:36:22 2021

@author: biknb
"""

import os, shutil


#parent dir in UTEP
parent_dir = "C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\dis\\"
disp_agg_path = parent_dir + 'dispersion_aggregator.py'
disp_agg_anal = parent_dir + 'dispersion_aggregator_anal.py'

#Creates the heatmaps dir

heatmaps = os.mkdir(parent_dir + 'HeatMaps') #comment or uncomment to create or just copy files inside
heatmaps_dir = parent_dir + 'HeatMaps\\'
vols = [2.85, 2.86, 2.87, 2.88, 2.89, 2.90, 2.91, 2.92, 2.93, 2.94, 2.95, 2.96, 2.97, 2.98, 2.99, 3.00] #you can input here a list or s aingle volume
temp = [300, 500, 700 ,1000, 1300] 

with open(disp_agg_path,'r') as msg:
            data = msg.read()
for x in vols:
    for y in temp:
          dir_name =  heatmaps_dir  + 'FeV' + '_' + str(x) + '_' + str(y) + 'K'
          dirs = os.mkdir(dir_name)
          shutil.copy(disp_agg_path , dir_name)
          #shutil.copy(libmeam, dir_name)
          rename = data.replace("latt_par", str(x)).replace("tmp", str(y))
          with open(parent_dir +'disp_agg_FeV_' + str(x) + '_' + str(y) +'K.py','w') as out_msg:
              out_msg.write(rename)
          shutil.move(parent_dir +'disp_agg_FeV_' + str(x) + '_' + str(y) +'K.py', dir_name)

with open(disp_agg_anal,'r') as msg:
            data = msg.read()  
for x in vols:
    for y in temp:
        dir_name =  heatmaps_dir  + 'FeV' + '_' + str(x) + '_' + str(y) + 'K'
        shutil.copy(disp_agg_anal , dir_name)
        rename = data.replace("latt_par", str(x)).replace("tmp", str(y))
        with open(parent_dir +'disp_agg_anal_FeV_' + str(x) + '_' + str(y) +'K.py','w') as out_msg:
                out_msg.write(rename)
        shutil.move(parent_dir +'disp_agg_anal_FeV_' + str(x) + '_' + str(y) +'K.py', dir_name)