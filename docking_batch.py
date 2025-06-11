import os
import subprocess

# === Parameters ===

# Receptor file (PDBQT format)
receptor = "YOUR_RECEPTOR.pdbqt"  # ← Replace with your receptor file

# Directory containing ligand PDBQT files
ligand_dir = "YOUR_LIGAND_FOLDER/"  # ← Replace with your ligand directory

# Output directory for docking results
output_dir = "results/"
os.makedirs(output_dir, exist_ok=True)

# Docking box center coordinates
center_x = "XXX"  # ← Replace with pocket center X
center_y = "XXX"  # ← Replace with pocket center Y
center_z = "XXX"  # ← Replace with pocket center Z

# Docking box dimensions (size)
size_x = "XX"  # ← Replace with box size X
size_y = "XX"  # ← Replace with box size Y
size_z = "XX"  # ← Replace with box size Z

# Path to AutoDock Vina executable
vina_exe = "vina"  # Change if vina is not in PATH

# === Batch Docking Loop ===

for ligand_file in os.listdir(ligand_dir):
    if ligand_file.endswith(".pdbqt"):
        ligand_path = os.path.join(ligand_dir, ligand_file)
        ligand_name = os.path.splitext(ligand_file)[0]
        out_path = os.path.join(output_dir, f"{ligand_name}_out.pdbqt")
        log_path = os.path.join(output_dir, f"{ligand_name}.log")

        # Construct the Vina command
        cmd = [
            vina_exe,
            "--receptor", receptor,
            "--ligand", ligand_path,
            "--center_x", center_x,
            "--center_y", center_y,
            "--center_z", center_z,
            "--size_x", size_x,
            "--size_y", size_y,
            "--size_z", size_z,
            "--out", out_path,
            "--log", log_path
        ]

        print(f"Docking {ligand_file} ...")
        subprocess.run(cmd)

print("All docking jobs completed.")
