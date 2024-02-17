# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:07:13 2023

@author: biknb
"""


import os, sys
import pandas as pd
import linecache

# # alat = 2.85 >> 3.0
# alat = '2.84'    
# #T = 300, 500, 700, 1000, 1300
# temp = '300K'   
sys = 'ord'
alat = [2.889]#, 2.890, 2.889, 2.892, 2.895] #you can input here a list or s aingle volume
temp = [700]#, 500, 700 ,1000, 1300] 


for x in alat:
    for y in temp:
        #read from SPOSCAR and multiply all cols by latt_param
        df = pd.read_csv('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\files\\SPOSCAR', sep=' ', skiprows=8, skipinitialspace=True, header=None, names = ["xx", "yy", "zz"])
        # df = pd.read_csv('C:\\Users\\biknb\\Downloads\\Cesar\\FeV\\FeV_'     '_'+temp+'\\SPOSCAR', sep=' ', skiprows=8, skipinitialspace=True, header=None, names = ["x", "y", "z"])
        
        # grab lattice constant from "atomic_position.data"
        # mult = linecache.getline('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\FeV_'+str(x)+'_'+str(y)+'\\atoms_positions.data', 7).split()[1]
        mult = next((line.split()[1] for i, line in enumerate(open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\LAMMPS\\FeV_'+str(x)+'_'+str(y)+'K\\atoms_positions.data')) if i == 6), None)

        
        df = df.multiply(float(mult))
        #add 1st col with new col name : "data" 
        data = {"data": list(range(1,2001,1)) }
        data = pd.DataFrame(data)
        
        #add 1st col with new col name : "type" 
        type_list = []
        type_list.extend([1 for i in range(1000)])
        type_list.extend([2 for i in range(1000)])
        type = pd.DataFrame(type_list)
        
        #combine 2 cols "data" and "type" as w
        w = data.join(type)
        
        ##combine "w" with "xx", "yy", "zz"
        z = w.join(df)
        
        ###############
        z.to_csv('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\LAMMPS\\FeV_'+str(x)+'_'+str(y)+'K\\sorted_atoms_positions.data', header=None, index=None, sep=' ')
        
        #copy header from "atoms_positions.data" to new file "atoms_header.data"
        N=12  
        with open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\LAMMPS\\FeV_'+str(x)+'_'+str(y)+'K\\atoms_header.data', "w") as file:     
            with open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\LAMMPS\\FeV_'+str(x)+'_'+str(y)+'K\\atoms_positions.data', 'r') as f:
                for i in range(N):
                    line = next(f).strip()
                    # print(line)
                    file.write(line+ '\n')
                
        #append "sorted_atoms_positions.data" and "atoms_header.data"
        def merge(atoms_header, sorted_atoms_positions, new_atoms_positions):
            file1 = open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\LAMMPS\\FeV_'+str(x)+'_'+str(y)+'K\\atoms_header.data')
            file2 = open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\LAMMPS\\FeV_'+str(x)+'_'+str(y)+'K\\sorted_atoms_positions.data')
            new_file = open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\LAMMPS\\FeV_'+str(x)+'_'+str(y)+'K\\atoms_positions.data', "w")
            
            file1_content = file1.read()
            file2_content = file2.read()
            
            new_file.write(file1_content)
            new_file.write(file2_content)
            
            file1.close()  
            file2.close()
            new_file.close()
        
        merge('atoms_header.data', 'sorted_atoms_positions', 'atoms_positions.data')
        
        # #remove unnnecessary files
        # out_path = 'C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\'+sys+'\\LAMMPS\\FeV_'+str(x)+'_'+str(y)+'K\\'
        # os.chdir(out_path)
        # command = "rm  atoms_header.data"
        # os.system(command)
        # command = "rm  sorted_atoms_positions.data"
        # os.system(command)
        
        
        # sys.exit()
