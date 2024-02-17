# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:07:13 2023

@author: biknb
"""


import os, sys
import pandas as pd

# syst = 'ord'
# alat = [2.889]#, 2.889, 2.89, 2.892,2.895 ] #you can input here a list or s aingle volume
# temp = [700]#, 500, 700 ,1000, 1300]   

syst = 'dis'
alat = [2.939]#, 2.919, 2.92, 2.924, 2.939 ] #you can input here a list or s aingle volume
temp = [1300]#, 500, 700 ,1000, 1300]   

for x in alat:
    for y in temp:
        df = pd.read_csv('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\equilibrium\\'+syst+'\\LAMMPS\\FeV_'+str(x)+'_'+str(y)+'K' +'\\ideal_FeV_B2_'+str(y)+'K' +'.txt', sep=' ', skiprows=9, skipinitialspace=True, header=None, nrows=2000)
        
        df.to_csv('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\equilibrium\\'+syst+'\\LAMMPS\\FeV_'+str(x)+'_'+str(y)+'K' +'\\ideal_FeV_B2_'+str(y)+'K' +'_unit.txt', header=None, index=None, sep=' ')#, float_format='%.4f')

