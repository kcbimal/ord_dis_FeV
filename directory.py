import os
import shutil

def create_directory(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            # print(f"Directory '{path}' created successfully.")
        except FileExistsError:
            print(f"Error: Directory '{path}' could not be created.")
    else:
        print(f"Directory '{path}' already exists.")

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        # print(f"File '{source}' copied to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{source}' not found.")

def replace_text_in_file(file_path, old_text, new_text):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        
        file_content = file_content.replace(old_text, new_text)
        
        with open(file_path, 'w') as file:
            file.write(file_content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        
if __name__ == "__main__":
    
    temperatures = [200, 300, 400]  # You can add more temperature values if needed
    compositions = [0.5]  # Different composition values (Ni0.5Ti0.5)
    
    for Temp in temperatures:
        for composition in compositions:
            par_dir = "C:\\Users\\biknb\\Downloads\\Cesar\\Spring_2024\\NiTi\\"
            main_dir = "MD_Simulations"
            create_directory(main_dir)
    
            # Create subdirectories
            temp_dir = os.path.join(main_dir, f"MD_simulations_{Temp}K")
            comp_dir = os.path.join(temp_dir, f"Ni{composition}Ti{1-composition}")
            ordered_dir = os.path.join(comp_dir, "Ordered_compositions")
            random_dir = os.path.join(comp_dir, "Random_compositions")
            sub_dirs = [temp_dir, comp_dir, ordered_dir, random_dir]
            for i in range(1, 6):
                sub_dirs.append(os.path.join(random_dir, f"Simulation {i}"))

            for dir_path in sub_dirs:
                create_directory(dir_path)
            
            # Copy files
            ordered_files = ["NiTi.library.meam", "NiTi.meam", "NiTi_external_positions_input_file.in", f"lammps script ordered simulation {composition}.py"]
            for file in ordered_files:
                source = os.path.join(par_dir, file)
                if os.path.exists(source):
                    destination = os.path.join(ordered_dir, file)
                    copy_file(source, destination)
                else:
                    print(f"Error: File '{file}' not found in '{par_dir}'.")

            random_files = ["NiTi.library.meam", "NiTi.meam", "NiTi_external_positions_input_file.in", "lammps script random config atoms running positions and simulation.py"]
            for i in range(1, 6):
                for file in random_files:
                    source = os.path.join(par_dir, file)
                    if os.path.exists(source):
                        destination = os.path.join(random_dir, f"Simulation {i}", file)
                        copy_file(source, destination)
                        if file == "lammps script random config atoms running positions and simulation.py":
                            replace_text_in_file(destination, "= 0.5", f"= {composition}")
                    else:
                        print(f"Error: File '{file}' not found in '{par_dir}'.")
