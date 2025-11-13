#!/usr/bin/zsh

# activate python virtual environment 
# (first set up a virtual python environment with a smelli installation and source its .../bin/activate here)
# source $HOME/software/venv/python-3_11_9-smelli/bin/activate # MODIFY PATH!!!
source PATH/TO/VENV/.../bin/activate # MODIFY PATH!

# path to python script running the smelli analysis
SMELLI_SCRIPT=PATH/TO/.../python/smelli_analysis_job.py # MODIFY PATH!!!
echo $SMELLI_SCRIPT

# analyzes $3 parameter points of model $1 starting with parameter point $2
python3 $SMELLI_SCRIPT $1 $2 $3 $4
