#!/usr/bin/zsh

# path to directory containing all (and only) WCxf files that should be analyzed
WCxf_directroy=PATH/TO/WCxf/FILES/... # MODIFY PATH!

# count the number of WCxf files
WCxf_COUNT=$(ls -1 "$WCxf_directroy" | wc -l)

# determine size of batches that are submitted as seperate jobs
BATCH_SIZE=500 # IF YOU MODIFY THIS NUMBER, YOU MIGHT ALSO HAVE TO MODIFY THE TIME BELOW!

# determine the number of jobs to be submitted [round_up(WCxf_COUNT/BATCH_SIZE)]
JOB_COUNT=$((($WCxf_COUNT + $BATCH_SIZE - 1)/$BATCH_SIZE))

# path to script that runs an individual job
JOB_SCRIPT=PATH/TO/.../shell/srun-job.sh # MODIFY PATH!
# JOB_SCRIPT=srun-job.sh

# path to script that merges the results of the individual job
MERGE_SCRIPT=PATH/TO/.../python/merge_smelli_jobs.py # MODIFY PATH!

# output directory
OUTPUT_directory=PATH/TO/DIRECTORY/TO/STORE/OUTPUT/... # MODIFY PATH!

# python path
# CUSTOM_PYTHON_PATH=$HOME/software/venv/python-3_11_9-smelli/bin/activate # MODIFY PATH!
CUSTOM_PYTHON_PATH=PATH/TO/VENV/.../bin/activate # MODIFY PATH!


# Create a temporary SLURM script with appropriate resources
cat <<EOT > temp_slurm_script.sh
#!/usr/bin/zsh

#SBATCH --job-name=smelli          # Job name
#SBATCH --output=output_%j.txt     # Output file (%j expands to jobID)
#SBATCH --error=error_%j.txt       # Error file (%j expands to jobID)
#SBATCH --nodes=${JOB_COUNT}                  # Nodes used in total
#SBATCH --ntasks=${JOB_COUNT}                 # Ask for 1 MPI tasks
#SBATCH --cpus-per-task=1          # CPUs per task
#SBATCH --time=06:00:00            # Run time of hh:mm:ss

# start of slurm script
echo "START"
date 

# print values of SLURM environment variables
echo "slurm host is"
echo \$SLURMD_NODENAME
echo "slurm queue is"
echo \$SLURM_JOB_PARTITION
echo "slurm working directory absolute is"
echo \$SLURM_SUBMIT_DIR
echo "slurm batch id"
echo \$SLURM_JOB_ID
echo "slurm job name from me is"
echo \$SLURM_JOB_NAME

# source python environment if not using the defoult python version
source $CUSTOM_PYTHON_PATH

# generate sub jobs
for (( i=0; i<$JOB_COUNT; i+=1 ))
do
    srun -N 1 -n 1 $JOB_SCRIPT $WCxf_directroy $OUTPUT_directory/batch_\$i \$((\$i * $BATCH_SIZE)) $BATCH_SIZE &
done

wait # wait for all srun jobs to finish

echo "jobs finished"
date

echo "merging results"
python3 $MERGE_SCRIPT $OUTPUT_directory

echo "END"

date

EOT

# send the generated SLURM script to the queue
sbatch temp_slurm_script.sh

# delete the temporary SLURM script
rm temp_slurm_script.sh
