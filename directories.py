#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:23:13 2021

@author: biknb
"""

import os, shutil



#This would be the location of the files. potential1/2 are the fe.meam and meam.library files
parent_dir = "C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\"
eam = parent_dir + 'FeV.meam'
libmeam = parent_dir + 'FeV.library.meam'
lammps_in_file = parent_dir + 'FeV.in'
position_footer = parent_dir + 'atoms_positions.txt'
position_header = parent_dir + 'atoms_header.txt'

#Create the LAMMPS directory with the V and T folders & input files
lammps_dir = os.mkdir(parent_dir + 'LAMMPS')
lammps_path = "C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\LAMMPS\\"

vols = [2.85, 2.86, 2.87, 2.88, 2.89, 2.90, 2.91, 2.92, 2.93, 2.94, 2.95, 2.96, 2.97, 2.98, 2.99, 3.00] #you can input here a list or s aingle volume
temp = [300, 500, 700 ,1000, 1300]  
 

with open(lammps_in_file,'r') as msg:
            data = msg.read()
for x in vols:
    for y in temp:
        dir_name = lammps_path + 'FeV' + '_' + str(x) + '_' + str(y) + 'K'
        dirs = os.mkdir(dir_name)
        shutil.copy(eam, dir_name)
        shutil.copy(position_footer, dir_name)  
        shutil.copy(position_header, dir_name)  #change lattice parameter
        shutil.copy(libmeam, dir_name)
        
        rename = data.replace("latt_par", str(x)).replace("tmp", str(y)).replace("system", "FeV") 
        with open(parent_dir +'FeV_' + str(x) + '_' + str(y) +'K.in','w') as out_msg:
            out_msg.write(rename)
        shutil.move(parent_dir +'FeV_' + str(x) + '_' + str(y) +'K.in', dir_name)
        
        
# #create the force constants directory that uses the .csv files from previous calculation

force_constants_dir = os.mkdir(parent_dir + 'Force_constants')
force_constants_path = "C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\Force_constants\\"
bvk_py_file = parent_dir + 'BvK Class BCC np.py'
with open(bvk_py_file,'r') as msg:
            data_f = msg.read()
for x in vols:
    for y in temp:
        dir_name_f = force_constants_path + 'FeV' + '_' + str(x) + '_' + str(y) + 'K'
        dirs_f = os.mkdir(dir_name_f)
        #shutil.copy(bvk_py_file, dir_name_f)
        rename_bvk = data_f.replace("latt_par", str(x)).replace("tmp", str(y))
        with open(force_constants_path +'BvK' + '_' + str(x) + '_' + str(y) + '.py','w') as out_msg:
              out_msg.write(rename_bvk)
        shutil.move(force_constants_path +'BvK' +'_' + str(x) + '_' + str(y) + '.py', dir_name_f)
        
#creates the phonopy directory (generates the FORCE_CONSTANTS file needed to compute phonon dispersions)

phonopy_dir = os.mkdir(parent_dir + 'Phonopy')
phonopy_path = "C:\\Users\\biknb\\Downloads\\Cesar\\Phonons_0.5\\ord\\Phonopy\\"
disp_gen_file = parent_dir + 'dispersion_generator.py'
bandconf_file = parent_dir + 'band.conf'
poscar_file   = parent_dir + 'POSCAR'
meshconf_file     = parent_dir + 'mesh.conf'
with open(disp_gen_file,'r') as msg:
            data_f = msg.read()
for x in vols:
    for y in temp:
        dir_name_disp = phonopy_path + 'FeV' + '_' + str(x) + '_' + str(y) + 'K'
        dirs_dis = os.mkdir(dir_name_disp)
        shutil.copy(bandconf_file, dir_name_disp)
        shutil.copy(meshconf_file, dir_name_disp)
        rename_disp = data_f.replace("latt_param", str(x)).replace("tmp", str(y))
        
        with open(phonopy_path +'disp_gen' + '_' + str(x) + '_' + str(y) + '.py','w') as out_msg:
              out_msg.write(rename_disp)
        shutil.copy(phonopy_path +'disp_gen' +'_' + str(x) + '_' + str(y) + '.py', dir_name_disp)
        #shutil.move(disp_gen_file, phonopy_path)

#change lattice parameter in poscar file "latt_param", if not needed, comment all below this line
with open(poscar_file,'r') as msg:
            data_p = msg.read()
for x in vols:
    for y in temp:
        dir_name_disp = phonopy_path + 'FeV' + '_' + str(x) + '_' + str(y) + 'K'
        shutil.copy(poscar_file, dir_name_disp)
        rename_lat = data_p.replace('latt_param', str(x))
        with open(phonopy_path +'POSCAR','w') as out_msg:
              out_msg.write(rename_lat)
        shutil.copy(phonopy_path +'POSCAR', dir_name_disp)
