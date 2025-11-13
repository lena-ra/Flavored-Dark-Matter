#!/usr/bin/zsh

#SBATCH -N 48 # number nodes
#SBATCH -n 48 # number tasks
#SBATCH -c 1 # core per task
#SBATCH -t 06:00:00 # time required
#SBATCH -o # output file

output="Majorana_d_scan" # name of output directory e.g. "Majorana_d_scan"
file="input_files/Majorana_d_scan.dat" # input file
model="Majorana_d" # model name, e.g. "Dirac_d", "Majorana_q", etc.
num_param=9999 # number of parameters to scan

# Execute jobs in parallel
echo "Start"
date
if [ -d $output ]; then
    rm -r $output
fi
mkdir $output
cp job_run_micromegas.sh $output/job_run_micromegas.sh # Copy the script to the output directory
for (( i=0; i<48; i+=1 ))
do
    srun -N 1 -n 1 ./run_micromegas.sh $file $output"/core_" $model $i $num_param &
done
wait
python3 merge_relic_abundance.py $output $file # Merge the files containing the relic abundance and other results
echo "End"
date
