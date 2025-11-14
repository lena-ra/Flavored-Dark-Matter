# Flavored Dark Matter Phenomenology Tool Chain 

This repository contains a tool chain for calculating phenomenological constraints on flavored dark matter models using `micrOMEGAs` \[[2312.14894](https://arxiv.org/abs/2312.14894)\], `SModelS` \[[2409.12942](https://arxiv.org/abs/2409.12942)\], and flavor physics tools used in the paper \[[2511.10490](https://arxiv.org/pdf/2511.10490)\]. The models considered involve a dark matter flavor triplet that couples to Standard Model fermions via a mediator, with different flavors of SM fermions leading to distinct phenomenological signatures.

## Directory Structure

This directory contains the code for running calculations and the input files, as well as the `FeynRules` \[[1310.1921](https://arxiv.org/abs/1310.1921)\], `UFO` \[[2304.09883](https://arxiv.org/abs/2304.09883)\], and `CalcHEP` \[[1207.6082](https://arxiv.org/abs/1207.6082)\] model files for 20 different flavored dark matter models.

### Core Files

| File | Description |
|------|-------------|
| `job_run_micromegas.sh` | SLURM cluster script example for running calculations |
| `run_micromegas.sh` | Script called by the job runner that executes `micrOMEGAs` |
| `evaluate_scan.py` | Example script for evaluating output results |

### Directories

- **`CalcHEP_files/`** - Contains `CalcHEP` model files for all 20 flavored dark matter models
- **`FeynRules_files/`** - Contains `FeynRules` model files for all 20 flavored dark matter models
- **`files_for_micromegas/`** - Contains the main.c file for `micrOMEGAs` (place in the model directory) and the settings file for `SModelS` (`smodels_parameters.ini`) that should be placed in the `include` directory of `micrOMEGAs`.
- **`flavor/`** - Contains tools for flavor physics analysis including SMEFT matching with `Matchete` (`matching/`) and global likelihood analysis with `smelli` (`likelihood/`)
- **`input_files/`** - Contains parameter files (`.dat` extension)
  - First line: header with parameter names matching the model
  - Subsequent lines: parameter values
- **`ID_limits/`** - Indirect detection limits (one file per channel)
- **`UFO_files/`** - Contains `UFO` model files for all 20 flavored dark matter models

## Dark matter model files

The models are specified by the dark matter particle type (real or complex scalar, Dirac or Majorana fermion) and the SM fermion that the particles couple to. The SM fermions are:

- Right-handed up-type quarks (u)
- Right-handed down-type quarks (d)
- Left-handed quark doublet (q)
- Right-handed leptons (e)
- Left-handed lepton doublet (l)

Different dark matter models can be combined by loading two or more `FeynRules` model files and adding the respective Lagrangians to produce the `UFO` or `CalcHEP` file of this model.

All masses for the dark matter and mediator particles are expected to be given after EWSB. The couplings between the DM field, the mediator and the SM fermions is split into the real and imaginary part (indicated by Re and Im at the end of the variable name). 

## How to Calculate Constraints

### Prerequisites

> **Important:** `micrOMEGAs` must be installed (which can be downloaded from [https://lapth.cnrs.fr/micromegas/](https://lapth.cnrs.fr/micromegas/), we used `v6.1.15`) and the corresponding model directory must be set up in order to run the calculations. If multiple cores are used for parallel processing, the model directory should be created multiple times, once for each core.

Now, follow these steps to run your calculations:

### Step 1: Prepare Input
```bash
# Place your parameter file in the input_files folder
cp your_parameters.dat input_files/
```

An example parameter file is provided in the `input_files` directory. Ensure that the parameters match the model you are using.

### Step 2: Run Calculations
```bash
# Modify job_run_micromegas.sh with your parameter set name and other settings
# Modify run_micromegas.sh with the correct paths of your working directory and micrOMEGAs installation
# Then submit the job
sbatch job_run_micromegas.sh
```

**Note:** The `job_run_micromegas.sh` script is designed for SLURM cluster environments and should serve as inspiration for other job schedulers or local execution setups. Adapt the script according to your computing environment.

This will create a folder with your parameter set name containing the results. All allowed parameter points will be stored in a `.dat` file with the same name as the parameter set where the first line is the header and the following lines are the parameter values. The missing topologies of the allowed points will be stored in a separate file called `selected_topologies.txt` where for every parameter point, the topologies are listed in terms of LLP, prompt, and off-grid. The main annihilation channels for indirect detection and the freeze out process will be stored in another separate file called `selected_channels.txt` where for every parameter point, the channels are listed in terms of the main annihilation processes.

### Step 3: Evaluate Results
```bash
# Use the evaluation script to analyze the output
python3 evaluate_scan.py
```

This will read the results from the output files and generate a summary of how many points are allowed by all constraints, which topologies are missing, and can be used to generate plots of the allowed parameter space.

### Step 4: Apply Flavor Constraints
```bash
# Navigate to the flavor directory for additional analysis
cd flavor/
```

Use the tools in the `flavor/` directory to perform flavor physics analysis:
- **Matching**: Use `matching/WCxf.nb` to convert parameter points to Wilson coefficients in `WCxf` format
- **Likelihood Analysis**: Use `likelihood/smelli.ipynb` to calculate global likelihood ratios and apply flavor constraints using `smelli`

This step will further constrain the allowed parameter space by incorporating precision flavor physics measurements and electroweak observables. As an input for the analysis, the output `.dat` file from Step 2 should be used so that only points allowed by previous constraints are considered.
