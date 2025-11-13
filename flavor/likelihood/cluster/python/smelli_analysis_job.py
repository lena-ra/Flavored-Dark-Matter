# Imports
import os, re, pickle, json, sys
import pandas as pd
from datetime import datetime
from smelli import GlobalLikelihood


# PARSE INPUTS
# input/output directories
wcxf_directory   = str(sys.argv[1]) # path to input/WCxf directory
output_directory = str(sys.argv[2]) # path to output directory
# parameter point range to analyze
start_point      = int(sys.argv[3]) # starting param point
n_points         = int(sys.argv[4]) # number of parampoints
end_point        = start_point + n_points # determine last point to analyze


# SETTINGS:
# specify whether the full output should be generated (minimalistic output is always generated)
full_output = True
# determine the number of leading observables to keep in minimalistic output
min_details = 3
# threshold for the log-likelihood ratio when a point should be considered as accepted/rejected
log_likelihood_threshold  = -2
observable_pull_threshold = 2
# fixed or dynamic CKM computation
fixed_CKM = True # Determine whether the CKM should be computed for each parameter point individually or once for the SM value. (The former can lead to a crashing of the code if there are large NP effects in B-dacys.)
# list of sub likelihoods that should be included (uncomment the ones relevant for the specific analysis, or use all)
likelihoods_included = None # [
    # 'fast_likelihood_quarks_fixckm.yaml' # use only one of the fist two likelihoods depending on your CKM choice
    # ,'fast_likelihood_quarks.yaml' # use only one of the fist two likelihoods depending on your CKM choice
    # ,'fast_likelihood_leptons.yaml'
    # ,'likelihood_ewpt.yaml'
    # ,'likelihood_eeww.yaml'
    # ,'likelihood_lept.yaml'
    # ,'likelihood_rd_rds.yaml'
    # ,'likelihood_lfu_fccc.yaml'
    # ,'likelihood_lfu_fcnc.yaml'
    # ,'likelihood_bcpv.yaml'
    # ,'likelihood_bqnunu.yaml'
    # ,'likelihood_lfv.yaml'
    # ,'likelihood_zlfv.yaml'
    # ,'likelihood_higgs.yaml'
#]


#------------------------------------------------------------------------

def main():
    # Create the output directory if it does not exist yet
    os.makedirs(output_directory, exist_ok=True)
    # print info
    start_log()
    start_time = datetime.now()
    write_log("START: " + str(start_time) + "\n")
    write_log("DIRECTORIES:")
    write_log(" - Input (WCxf): " + wcxf_directory)
    write_log(" - Output:       " + output_directory + "\n")
    write_log("SETTINGS:")
    write_log(" - CKM fixed:   " + str(fixed_CKM))
    write_log(" - Likelihoods: " + str(likelihoods_included))
    write_log(" - Threshold for log likelihood ratio:   " + str(log_likelihood_threshold))
    write_log(" - Threshold for SM pull of observables: " + str(observable_pull_threshold) + "\n")

    # create the global likelihood instance
    print("initializing global likelihood", end='\r')
    gl = GlobalLikelihood(eft='SMEFT', basis='Warsaw', fix_ckm=fixed_CKM, include_likelihoods=likelihoods_included)
    
    # list of all global likelihood points
    gl_points = read_wcxf(wcxf_directory, gl)

    # compute log likelihood and observable table for all points
    results, results_min = determine_likelihoods(gl_points)
    
    # export results
    # minimal
    with open(os.path.join(output_directory, "results_min.json"), "w") as f_json:
        json.dump(results_min, f_json, indent=4)
    # full
    if full_output:
        with open(os.path.join(output_directory, "results.dat"), "wb") as f:
            pickle.dump(results, f)

    # write log with overview info
    write_summary(gl_points, results)

    # print end time
    end_time = datetime.now()
    write_log("\n" + "END: " + str(end_time) + "\n")
    write_log("DURATION: " + str(end_time-start_time) + "\n")


#------------------------------------------------------------------------


def read_wcxf(dir,gl):
    print("reading WCxf input files", end='\r')
    points = {}
    
    # create a global likelihood point for each file in the WCxf directory
    for filename in sorted(os.listdir(dir), key=lambda x:(len(x),x[1:]))[start_point:end_point]:
        f = os.path.join(dir, filename)
        # checking if it is a file
        if os.path.isfile(f):
            # ignore files that are not loadable
            try:
                # extract id of parameter point from filename
                point_id = int(re.search("\d+", filename)[0])
                # generate global likelihood point and associate it to the id of the point
                points.update({point_id : gl.parameter_point(f)})
            except:
                pass

    write_log("Number of input WCxf files: " + str(len(points)) + " ")

    return points


#------------------------------------------------------------------------


def determine_likelihoods(likelihood_points):
    # output dictionary containing likelihood dictionaries and observable tables for each point
    output_list = {}
    output_list_min = {}
    # counter and length
    counter = 0
    n_points = str(len(likelihood_points))

    # loop over points
    for point_id, point in likelihood_points.items():
        counter += 1
        print(str(counter) + "/" + n_points, end='\r')

        try:
            # compute the log-likelihood dictionary
            dict = point.log_likelihood_dict()
            # determine observable table and sort by pull w.r.t. SM
            obst = point.obstable().sort_values('pull SM', ascending=False)
            # add results to output
            output_list.update({point_id : {'likelihoods' : dict , 'observables' : obst}})
            # create minimalistic output            
            df = obst[['pull exp.','pull SM']].astype(float)
            obst_min = pd.concat([
                df.nlargest(1, 'pull exp.'),                          # keep observable with largest pull w.r.t. experiment
                df.loc[df['pull exp.'] >= observable_pull_threshold], # keep all observables with pull w.r.t. experiment above threshold
                df.nlargest(1, 'pull SM'),                            # keep observable with largest pull w.r.t. SM
                df.loc[df['pull SM'] >= observable_pull_threshold],   # keep all observables with pull w.r.t. SM above threshold
                df.nsmallest(min_details, 'pull SM')                  # keep min_details observables with smallest pull w.r.t. SM
            ]).drop_duplicates()                                      # delete duplicates
            obst_min = {str(index): row.values.tolist() for index, row in obst_min.iterrows()}
            output_list_min.update({point_id : {'likelihood' : dict['global'] , 'observables' : obst_min}})
        except:
            # this can occure if the dynamic CKM computation is turned on and large NP contributions to B decays are present
            output_list.update({point_id : {'likelihood' : None , 'observables' : None}})
            output_list_min.update({point_id : {'likelihood' : -999999 , 'observables' : None}})

    return output_list, output_list_min


#------------------------------------------------------------------------


def write_summary(points, results):
    # number of points
    points_count = len(points)
    # counter
    counter_pass = 0
    counter_fail = 0
    counter_none = 0

    obstable_list = []

    # loop over results
    for point_id, point in results.items():
        try:
            if point['likelihoods']['global'] > log_likelihood_threshold:
                counter_pass += 1
            else:
                counter_fail += 1
            # collect list of all observable tables
            obstable_list.append(point['observables'])
        except:
            counter_none += 1

    write_log("Number of points passed:    " + str(counter_pass) + " (" + str(100.*counter_pass/points_count) + "%)")
    write_log("Number of points failed:    " + str(counter_fail) + " (" + str(100.*counter_fail/points_count) + "%)")
    write_log("Number of points crashed:   " + str(counter_none) + " (" + str(100.*counter_none/points_count) + "%)" + "\n")

    # determine observables with above threshold pull w.r.t the SM
    large_pull_obs = {}

    # get all observables present in the observable tables and initialize with count 0
    for index, obs in obstable_list[0].iterrows():
        large_pull_obs.update({index: 0})

    # increase counter by one unit if pull above threshold
    for obstable_entry in obstable_list:
        for index, obs in obstable_entry.iterrows():
            if obs['pull SM'] >= observable_pull_threshold:
                large_pull_obs[index] += 1
    
    # remove zero count observables
    large_pull_obs = {x:y for x,y in sorted(large_pull_obs.items(), key=lambda item: -item[1]) if y!=0}

    # output summary
    write_log("Summary of most relevant observables and how often their pull is above threshold:")
    write_log(str(large_pull_obs))


#------------------------------------------------------------------------

# start a fresh log file
def start_log():
    # create log file
    with open(os.path.join(output_directory, "smelli_run.log"), "w") as log:
        log.write("smelli analysis\n")

# print to terminal and write to log file
def write_log(message):
    print(message)
    with open(os.path.join(output_directory, "smelli_run.log"), "a") as log:
        log.write("\n" + str(message))


#------------------------------------------------------------------------


# call main routine
if __name__ == "__main__":
    main()