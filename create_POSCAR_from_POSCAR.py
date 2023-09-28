# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 12:23:43 2023

@author: biknb
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:07:13 2023

@author: biknb
"""
 #after running this code run "./replace_POSCAR_1_1.sh" in terminal


import os, sys
import pandas as pd

sys = 'ord'
alat = [2.85, 2.86, 2.87, 2.88, 2.89, 2.90, 2.91, 2.92, 2.93, 2.94, 2.95, 2.96, 2.97, 2.98, 2.99, 3.00] #you can input here a list or s aingle volume
temp = [300, 500, 700 ,1000, 1300]    

for x in alat:
    for y in temp:
#read from SPOSCAR and multiply all cols by latt_param
        df = pd.read_csv('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\files\\POSCAR', sep=' ', skiprows=8, skipinitialspace=True, header=None)#, names = ["x", "y", "z"])
        
        ###############
        df.to_csv('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\Phonopy\\'+str(y)+'\\FeV_'+str(x)+'_'+str(y)+'K' +'\\sorted_poscar.data', header=None, index=None, sep=' ')
        
        #copy header from "poscar.data" to new file "atoms_header.data"
        N=8
        with open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\Phonopy\\'+str(y)+'\\FeV_'+str(x)+'_'+str(y)+'K' +'\\poscar_header.data', "w") as file:     
            with open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\Phonopy\\'+str(y)+'\\FeV_'+str(x)+'_'+str(y)+'K' +'\\POSCAR', 'r') as f:
                for i in range(N):
                    line = next(f).strip()
                    # print(line)
                    file.write(line+ '\n')
                
        #append "sorted_poscar.data" and "atoms_header.data"
        def merge(atoms_header, sorted_poscar, new_poscar):
            file1 = open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\Phonopy\\'+str(y)+'\\FeV_'+str(x)+'_'+str(y)+'K' +'\\poscar_header.data')
            file2 = open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\Phonopy\\'+str(y)+'\\FeV_'+str(x)+'_'+str(y)+'K' +'\\sorted_poscar.data')
            new_file = open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\Phonopy\\'+str(y)+'\\FeV_'+str(x)+'_'+str(y)+'K' +'\\POSCAR', "w")
            
            file1_content = file1.read()
            file2_content = file2.read()
            
            new_file.write(file1_content)
            new_file.write(file2_content)
            
            file1.close()  
            file2.close()
            new_file.close()
        
        merge('poscar_header.data', 'sorted_poscar', 'new_poscar')
        
        #remove unnnecessary files
        out_path = 'C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\Phonopy\\'+str(y)+'\\FeV_'+str(x)+'_'+str(y)+'K' +'\\'
        os.chdir(out_path)
        command = "rm  poscar_header.data"
        os.system(command)
        command = "rm  sorted_poscar.data"
        os.system(command)
        
        
        # sys.exit()
