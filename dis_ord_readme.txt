1: Generate "SPOSCAR" using "POSCAR" and phonopy cmd: "phonopy -d --dim="10 10 10"
2: Files needed for LAMMPS run:
    -Library.meam
    -FeV.meam
    -atoms_positions.data (only for header purposes)
    -SPOSCAR (for footer purpose in "dis_atoms_positions.data")
    -.in (Read positions from "dis_atoms_positions.data")
3: The "atoms_position.data" are created using "lammps script ordered composition ..... py" (this file doesn't depend on temp, only in lattice parameter)
4: The "atoms_positions.data" are copied to each LAMMPS directory manually to their respective lattice parameter directories.
5: Then after copying "atoms_positions.data" to each LAMMPS directory, run "get_disordered_str_from_SPOSCAR_V2_all.py" to get disorder structure file "dis_atoms_positions.data" so that we can now run LAMMPS.
6: Use "dispersion_generator_disordered.py" for dispersions.
7: For vib. entropy, run "vib_entropy_from_phonopy_pdos.py"


NOTE: The "ideal_unit" file is not needed for the dispersion generator.

