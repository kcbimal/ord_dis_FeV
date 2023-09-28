# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:07:13 2023

@author: biknb
"""
# do this only for ordered structure........!!!!!!!!!!!!!!!!!!!!!!!!!!
# the "atoms_positions" are created using  "lammps script ordered simulation.... .py"  ---
#                                   --- at their respective temperature and lattice parameter.
# this code is used to modify "atoms_Positions" file to calculate HELD ord_FeV structure
# this code arranges atom types in ascending order and replace first column with regular number
# when done: 
#         copy the values from "sorted_atoms_positions.data" &,
#         replace the values in "atoms_positions" file

import os, sys
import pandas as pd

# alat = 2.85 >> 3.0
alat = '2.99'    
#T = 300, 500, 700, 1000, 1300
temp = '1300K'   

df = pd.read_csv('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\LAMMPS\\FeV_'+alat+'_'+temp+'\\atoms_positions.data', sep=' ', skiprows=12, skipinitialspace=True, header=None)
y = df.sort_values(1)
z = y. iloc[:,1:]              #delete the first column  
data =list(range(1,2001,1))    #define col with values from 1-2000
x = z.insert(0, 5, data)       #add first col. with value range 0-2000
z.to_csv('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\LAMMPS\\FeV_'+alat+'_'+temp+'\\sorted_atoms_positions.data', header=None, index=None, sep=' ')

#copy header from "atoms_positions.data" to new file "atoms_header.data"
N=12  
with open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\LAMMPS\\FeV_'+alat+'_'+temp+'\\atoms_header.data', "w") as file:     
    with open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\LAMMPS\\FeV_'+alat+'_'+temp+'\\atoms_positions.data', 'r') as f:
        for i in range(N):
            line = next(f).strip()
            # print(line)
            file.write(line+ '\n')
        
#append "sorted_atoms_positions.data" and "atoms_header.data"
def merge(atoms_header, sorted_atoms_positions, new_atoms_positions):
    file1 = open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\LAMMPS\\FeV_'+alat+'_'+temp+'\\atoms_header.data')
    file2 = open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\LAMMPS\\FeV_'+alat+'_'+temp+'\\sorted_atoms_positions.data')
    new_file = open('C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\LAMMPS\\FeV_'+alat+'_'+temp+'\\atoms_positions.data', "w")
    
    file1_content = file1.read()
    file2_content = file2.read()
    
    new_file.write(file1_content)
    new_file.write(file2_content)
    
    file1.close()  
    file2.close()
    new_file.close()

merge('atoms_header.data', 'sorted_atoms_positions', 'new_atoms_positions')

#remove unnnecessary files
out_path = 'C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\LAMMPS\\FeV_'+alat+'_'+temp+'\\'
os.chdir(out_path)
command = "rm  atoms_header.data"
os.system(command)
command = "rm  sorted_atoms_positions.data"
os.system(command)


sys.exit()
