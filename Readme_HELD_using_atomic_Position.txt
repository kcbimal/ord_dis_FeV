1: generate atomic position file "atoms_positions.data" using “lammps script ordered simulation....py”
2: for ordered structure, 
		a) run phonopy "phonopy -d --dim="10 10 10" to create a supercell of 10X10X10 using POSCAR of 2 atoms.
		b) use “get_atom_position_by_type_from_SPOSCAR.py” to generate an ordered atomic position 
                   (this use files: "SPOSCAR" for positions and "atoms_positions.data" for header.)
3: Thus, instead of defining supercell, the lammps input file “FeV_external_positions_lammps_input_file.in” reads atomic positions using the atomic position 
   file created in second step.
4: run LAMMPS to create dump files.
5: create “ideal_FeV_B2_tempK_unit”  in LAMMPS dir. using "ideal_to_ideal-unit_lammps.py".
6: run HELD (FCs)
7: Run "create_POSCAR_from_SPOSCAR.py" to get POSCAR
		keep  "replace_POSCAR_1_1.sh" in phonopy folder to change #of atoms in POSCAR
                run   "replace_POSCAR_1_1.sh"
8: Run Phonopy (Dispersion generator)
9: run PDOS for sigma = 0.1
10: run “vib_entropy_pdos_bkc.py” to calculate vibrational entropy. (NOTE:  Don’t forget to normalize DOS in this code.)

####Run .sh file #####
#In the Anaconda prompt shell, use "bash multirun.sh"
#In Mobaxterm terminal, use "./multirun.sh"