#!/usr/bin/zsh

INPUT_FILE="$1" # file containing the data, e.g. "data.dat"
OUTPUT_DIR="$2" # directory where the output file will be saved, e.g. "output/"
MODEL="$3" # model name, e.g. "Dirac_d", "Majorana_q", etc.
index=$4 # index of the core (used for parallel processing)
num_param=$5 # total number of parameter points in input file

# THE FOLLOWING PATHS MUST BE CHANGED ACCORDING TO YOUR SYSTEM
WORK_DIR="/home/lu750495/Flavoured_DM" # working directory where the script is located, must be changed according to your project structure
MICROMEGAS_DIR="/home/lu750495/software/micromegas_6.1.15" # path to micrOMEGAs installation, must be changed according to your installation

# Create output directory and files
if [ -d "$OUTPUT_DIR$index" ]; then
    rm -r $OUTPUT_DIR$index
fi
mkdir $OUTPUT_DIR$index
touch $OUTPUT_DIR$index/relic_abundances.txt
touch $OUTPUT_DIR$index/missing_topologies.txt
touch $OUTPUT_DIR$index/channels.txt
echo -e "rel_abundance\ttotal_xs\tann_qq\tann_cc\tann_bb\tann_tt\tann_qc\tann_qb\tann_qt\tann_ct\tann_ee\tann_mumu\tann_tata\tann_emu\tann_eta\tann_muta\tann_hh\tann_ZZ\tann_WW\tann_vv\tDD_exclusion\tproton_SI_X\tproton_SI_X~\tproton_SD_X\tproton_SD_X~\tneutron_SI_X\tneutron_SI_X~\tneutron_SD_X\tneutron_SD_X~\tSModelS_exclusion\ttopology\tr_value" >> $OUTPUT_DIR$index/relic_abundances.txt
echo -e "# Each parameter point is represented by a block of lines with order: LLP, prompt, off grid" >> $OUTPUT_DIR$index/missing_topologies.txt
echo -e "# relic abundance + channels first line, ID cross sections + channels second line" >> $OUTPUT_DIR$index/channels.txt

# Change to the working directory and activate the Python environment to run micrOMEGAs, change the paths according to your installation
source /home/lu750495/software/env_python3_9_6/bin/activate
cd $MICROMEGAS_DIR
MOMODEL=$MODEL$index/
cd $MOMODEL
for (( i=$index; i<$num_param; i+=48 )) # Loop through the parameter points in the input file, here we have 48 cores available for parallel processing, change this number according to your system
do
    python3 $WORK_DIR/write_params.py $WORK_DIR/$INPUT_FILE $WORK_DIR/$OUTPUT_DIR$index/ $MODEL $i # Write the parameters for the current index to a micrOMEGAs input file
    OUTPUT_FILE=$WORK_DIR/$OUTPUT_DIR$index/output.txt
    timeout 600s ./main $WORK_DIR/$OUTPUT_DIR$index/data.par > $OUTPUT_FILE # Run micrOMEGAs with the generated input file, timeout is set to 600 seconds (10 minutes) to avoid long hangs
    EXIT_CODE=$?
    if [ $EXIT_CODE -eq 124 ]; then
        echo -e "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0" >> $WORK_DIR/$OUTPUT_DIR$index/relic_abundances.txt
        echo -e "LLP: 0" >> $WORK_DIR/$OUTPUT_DIR$index/missing_topologies.txt
        echo -e "Prompt: 0" >> $WORK_DIR/$OUTPUT_DIR$index/missing_topologies.txt
        echo -e "Off grid: 0" >> $WORK_DIR/$OUTPUT_DIR$index/missing_topologies.txt
        echo "Timeout occurred at index $i"
        rm $WORK_DIR/$OUTPUT_DIR$index/data.par
        continue
    fi
    python3 $WORK_DIR/write_relicabundance.py $OUTPUT_FILE $WORK_DIR/$OUTPUT_DIR$index/ $MOMODEL $MICROMEGAS_DIR # Write the relic abundance and other results to the output file
     python3 $WORK_DIR/write_channels.py $OUTPUT_FILE $WORK_DIR/$OUTPUT_DIR$index/ $MOMODEL # Write the channels to the output file
    rm $OUTPUT_FILE
    rm $WORK_DIR/$OUTPUT_DIR$index/data.par
done

date
echo "Core "$index" is done."
