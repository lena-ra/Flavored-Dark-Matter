# Imports
import os, re, pickle, json, sys
# import pandas as pd
from datetime import datetime
from smelli import GlobalLikelihood


# PARSE INPUTS
# output directories
output_directory = str(sys.argv[1]) # path to output directory

log_likelihood_threshold  = -2
observable_pull_threshold = +2


#------------------------------------------------------------------------

def main(): 
    # combined results
    combined_results = {}
    
    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(output_directory):
        for filename in files:
            # consider only non-hidden json files 
            if filename.endswith('.json') and not filename.startswith('.'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as json_file:
                    try:
                        # load the results of one run from the file
                        results = json.load(json_file)
                        # combine the results from different runs
                        combined_results.update(results)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON from file {filename}: {e}")
    
    # sort the merged dictionary by its keys
    combined_results = dict(sorted(combined_results.items()))
    
    # write the summary
    write_summary(combined_results)
    


#------------------------------------------------------------------------


def write_summary(results):
    # number of points
    points_count = len(results)
    print("length is ")
    print(points_count)
    # counter
    counter_pass = 0
    counter_fail = 0
    counter_none = 0

    # determine observables with above threshold pull w.r.t the SM
    large_pull_obs = {}

    # loop over results
    for point_id, point in results.items():
        try:
            # check if global likelihood is above or below threshold
            if point['likelihood'] > log_likelihood_threshold:
                counter_pass += 1
            else:
                counter_fail += 1
        except:
            counter_none += 1
        
        # collect observables with pulls (w.r.t. SM) above threshold
        for obs, val in point['observables'].items():
            if val[1] >= observable_pull_threshold:
                if obs in large_pull_obs:
                    large_pull_obs[obs] += 1
                else:
                    large_pull_obs.update({obs: 1})
    
    start_log()
    write_log(" - Threshold for log likelihood ratio:     " + str(log_likelihood_threshold))
    write_log(" - Threshold for SM pull of observables: " + str(observable_pull_threshold) + "\n")
    write_log("Number of points passed:    " + str(counter_pass) + " (" + str(100.*counter_pass/points_count) + "%)")
    write_log("Number of points failed:    " + str(counter_fail) + " (" + str(100.*counter_fail/points_count) + "%)")
    write_log("Number of points crashed:   " + str(counter_none) + " (" + str(100.*counter_none/points_count) + "%)" + "\n")
    
    # remove zero count observables
    large_pull_obs = {x:y for x,y in sorted(large_pull_obs.items(), key=lambda item: -item[1]) if y!=0}

    # output summary
    write_log("Summary of most relevant observables and how often their pull (compared to the SM) is above threshold:")
    write_log(str(large_pull_obs))



#------------------------------------------------------------------------

# start a fresh log file
def start_log():
    with open(os.path.join(output_directory, "smelli_summary.log"), "w") as log:
        log.write("smelli analysis summary\n")

# print to terminal and write to log file
def write_log(message):
    print(message)
    with open(os.path.join(output_directory, "smelli_summary.log"), "a") as log:
        log.write("\n" + str(message))


#------------------------------------------------------------------------


# call main routine
if __name__ == "__main__":
    main()