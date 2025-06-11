# AutoDocking-Pipeline

A lightweight Python script for batch molecular docking using AutoDock Vina.

This tool allows you to automatically dock multiple ligands to a single receptor using predefined docking box parameters. It is suitable for high-throughput docking workflows in structural biology or drug discovery.

---

## Features

- Batch docking of multiple ligands (PDBQT format)
- Customizable docking box (center and size)
- Simple output handling (poses + logs)
- No external Python libraries required (uses only `os` and `subprocess`)

---

## Requirements

- Python 3.6+
- AutoDock Vina installed and accessible via `vina` in command line
- Ligands and receptor files in `.pdbqt` format

---

## Usage

### 1. Prepare files

- Place your receptor file (e.g., `receptor.pdbqt`)
- Place all ligand `.pdbqt` files into a folder, e.g., `ligands/`
- Modify the `docking_batch.py` script to fill in:
  - Receptor file path
  - Ligand folder path
  - Docking box center and size (x, y, z)

### 2. Run the script

```bash
AutoDocking-Pipeline/
├── docking_batch.py
├── README.md
├── LICENSE
├── results/               # Output folder
├── ligands/               # Input ligands
└── docs/
    └── usage.md           # User instructions

### 3. Results will be saved in the results/ folder.

## Citation

If you use this pipeline, please cite:

> Wang XR. (2025). *AutoDocking-Pipeline: A Python script for batch molecular docking*. Zenodo. https://doi.org/10.5281/zenodo.15641479
