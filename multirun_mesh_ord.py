import os

# Given volumes and temp
vols = [2.85, 2.86, 2.87, 2.88, 2.89, 2.90, 2.91, 2.92, 2.93, 2.94, 2.95, 2.96, 2.97, 2.98, 2.99, 3.00]
temp = 300

# Loop through directories
for vol in vols:
    root = f'FeV_{vol}_{temp}K'
    directory = fr'C:\Users\bkc\Downloads\Cesar\Phonons_0.5\ord\Phonopy\{temp}\{root}'
    
    if os.path.exists(directory):
        os.chdir(directory)
        command = "phonopy -p -s mesh.conf"
        os.system(command)
    else:
        print(f"Directory '{directory}' not found.")
