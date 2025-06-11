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

- Python 3.6 or above
- [AutoDock Vina](http://vina.scripps.edu/) installed and added to PATH
- Ligands and receptor prepared in PDBQT format

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
python docking_batch.py
