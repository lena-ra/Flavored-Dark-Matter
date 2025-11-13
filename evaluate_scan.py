import numpy as np
import matplotlib.pyplot as plt 
import pickle
import os
import pandas as pd

# This is an example script to read the output of a scan and evaluate the results.

# Define output file with results
scan_name = "Majorana_d_scan" # Change this to the name of your scan
results_file = open(scan_name + "/" + scan_name + "_results.txt", "w")
results_file.write("Results of " + scan_name + "\n")

# Read ID limits from files
def read_ID(channel):
    file = open("ID_limits/"+channel+"_combined.txt")
    file.readline()
    lines = file.readlines()
    m_DM = []
    sigmav = []
    for line in lines:
        m_DM.append(float(line.split()[0]))
        sigmav.append(float(line.split()[1]))
    file.close()
    return np.array(m_DM), np.array(sigmav)

m_DM, sigmav_b = read_ID("b")
m_DM, sigmav_c = read_ID("c")
m_DM, sigmav_e = read_ID("e")
m_DM, sigmav_h = read_ID("h")
m_DM, sigmav_mu = read_ID("mu")
m_DM, sigmav_nu = read_ID("nu")
m_DM, sigmav_q = read_ID("q")
m_DM, sigmav_t = read_ID("t")
m_DM, sigmav_tau = read_ID("tau")
m_DM, sigmav_W = read_ID("W")
m_DM, sigmav_Z = read_ID("Z")

# Read files and extract data
def read_files(name, results_file=None):
    open_file = open(name+"/"+name+".dat", 'r')
    content_allowed = open_file.readlines()
    header = content_allowed[0].split()[1:]
    values_allowed = np.array([x.split() for x in content_allowed[1:]]).transpose()
    values_allowed = np.array([[float(value) for value in row] for row in values_allowed])
    data_dict_allowed = dict(zip(header, values_allowed))
    open_file.close()

    open_file=open("input_files/"+name+".dat", 'r')
    content_all = open_file.readlines()
    header = content_all[0].split()[1:]
    values_all = np.array([x.split() for x in content_all[1:]]).transpose()
    values_all = np.array([[float(value) for value in row] for row in values_all])
    data_dict_all = dict(zip(header, values_all))
    open_file.close()

    topo_file = open(name+"/selected_topologies.txt", "r")
    topo_file.readline()
    topo_lines = topo_file.readlines()
    topo_file.close()
    promt_topo = []
    LLP_topo = []
    offgrid_topo = []
    promt_num = []
    LLP_num = []
    offgrid_num = []

    for line in topo_lines:
        if "Prompt" in line:
            line_split = line.split(': ')
            if line_split[1] != "0\n":
                topos = line_split[1][1:-2].split('], [')
                for topo in topos:
                    signature = topo[11:]
                    if signature not in promt_topo:
                        promt_topo.append(signature)
                        promt_num.append(1)
                    else:
                        promt_num[promt_topo.index(signature)] += 1
        if "LLP" in line:
            line_split = line.split(': ')
            if line_split[1] != "0\n":
                topos = line_split[1][1:-2].split('], [')
                for topo in topos:
                    signature = topo[11:]
                    if signature not in LLP_topo:
                        LLP_topo.append(signature)
                        LLP_num.append(1)
                    else:
                        LLP_num[LLP_topo.index(signature)] += 1
        if "Off grid" in line:
            line_split = line.split(': ')
            if line_split[1] != "0\n":
                topos = line_split[1][1:-2].split('], [')
                for topo in topos:
                    signature = topo[11:]
                    if signature not in offgrid_topo:
                        offgrid_topo.append(signature)
                        offgrid_num.append(1)
                    else:
                        offgrid_num[offgrid_topo.index(signature)] += 1
    if len(promt_topo) > 0:
        promt_topo_num_pairs = list(zip(promt_topo, promt_num))
        promt_topo_num_pairs.sort(key=lambda x: x[1], reverse=True)
        promt_topo, promt_num = zip(*promt_topo_num_pairs)
        promt_topo = list(promt_topo)
        promt_num = list(promt_num)
    if len(LLP_topo) > 0:
        LLP_topo_num_pairs = list(zip(LLP_topo, LLP_num))
        LLP_topo_num_pairs.sort(key=lambda x: x[1], reverse=True)
        LLP_topo, LLP_num = zip(*LLP_topo_num_pairs)
        LLP_topo = list(LLP_topo)
        LLP_num = list(LLP_num)
    if len(offgrid_topo) > 0:
        offgrid_topo_num_pairs = list(zip(offgrid_topo, offgrid_num))
        offgrid_topo_num_pairs.sort(key=lambda x: x[1], reverse=True)
        offgrid_topo, offgrid_num = zip(*offgrid_topo_num_pairs)
        offgrid_topo = list(offgrid_topo)
        offgrid_num = list(offgrid_num)
    
    if "MXC3" in header:
        index_mass = header.index("MXC3")
    if "MXD3" in header:
        index_mass = header.index("MXD3")
    if "MXM3" in header:
        index_mass = header.index("MXM3")
    if "MXS3" in header:
        index_mass = header.index("MXS3")
    num_ex_rel = 0
    num_ex_DD = 0
    num_ex_SMS = 0
    num_ex_ID = 0
    omegas = [0] * len(values_all[0])
    ex_searches = []
    num_searches = []
    rel_channels = []
    id_channels = []
    DD_experiments = []
    num_experiments = []
    ex_SMS = [False] * len(values_all[0])
    ex_topo = []
    num_ex_topo = [] 
    ex_ID = [False] * len(values_all[0])
    ex_DD = [False] * len(values_all[0])
    points_read = 0
    for j in range(48):
        file = open(name+"/core_"+str(j)+"/relic_abundances.txt", "r")
        line = file.readline()  
        line_content = line.split('\t')
        index_omega = line_content.index('rel_abundance')
        index_DD = line_content.index('DD_exclusion')
        index_SMS = line_content.index('SModelS_exclusion')
        index_topo = line_content.index('topology')
        line = file.readlines()
        file.close()
        points_read += len(line)
        if os.path.exists(name+"/core_"+str(j)+"/channels.txt"):
            file_ch = open(name+"/core_"+str(j)+"/channels.txt", "r")
            file_ch.readline()
            lines_ch = file_ch.readlines()
        k=0
        for i in np.arange(j,len(content_all)-1,48):
            if k < len(line):
                lsplit = line[k].split()
                omega = float(lsplit[index_omega])
                omegas[i] = omega
                DD_ex = lsplit[index_DD]
                SMS_ex = lsplit[index_SMS]
                m = values_all[index_mass][i]
                if os.path.exists(name+"/core_"+str(j)+"/channels.txt") and len(lines_ch) > 2*k:
                    rel_channels.append(lines_ch[2*k][9:-1])
                    id_channels.append(lines_ch[2*k+1][9:-1])
                if omega - 0.1*omega > 0.12 or omega + 0.1*omega < 0.12:
                    num_ex_rel+=1
                if DD_ex != 'not_excluded' and omega != 0.0:
                    num_ex_DD+=1
                    ex_DD[i] = True
                    if DD_ex not in DD_experiments:
                        DD_experiments.append(DD_ex)
                        num_experiments.append(1)
                    else:
                        num_experiments[DD_experiments.index(DD_ex)] += 1
                if SMS_ex != 'SMS_not_excluded' and omega != 0.0:
                    num_ex_SMS+=1
                    ex_SMS[i] = True
                    topo = lsplit[index_topo].split(',')[0]
                    if topo not in ex_topo:
                        ex_topo.append(topo)
                        num_ex_topo.append(1)
                    else:
                        num_ex_topo[ex_topo.index(topo)] += 1
                    if SMS_ex not in ex_searches:
                        ex_searches.append(SMS_ex)
                        num_searches.append(1)
                    else:
                        num_searches[ex_searches.index(SMS_ex)] += 1
                if float(lsplit[line_content.index('ann_qq')]) > np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_q))) or float(lsplit[line_content.index('ann_cc')]) > np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_c))) or float(lsplit[line_content.index('ann_bb')]) > np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_b))) or float(lsplit[line_content.index('ann_tt')]) > np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_t))) or float(lsplit[line_content.index('ann_qc')]) > 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_q))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_c)))) or float(lsplit[line_content.index('ann_qb')]) > 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_q))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_b)))) or float(lsplit[line_content.index('ann_qt')]) > 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_q))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_t)))) or float(lsplit[line_content.index('ann_ct')]) > 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_c))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_t)))) or float(lsplit[line_content.index('ann_ee')]) > np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_e))) or float(lsplit[line_content.index('ann_mumu')]) > np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_mu))) or float(lsplit[line_content.index('ann_tata')]) > np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_tau))) or float(lsplit[line_content.index('ann_emu')]) > 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_e))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_mu)))) or float(lsplit[line_content.index('ann_eta')]) > 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_e))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_tau)))) or float(lsplit[line_content.index('ann_muta')]) > 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_mu))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_tau)))) or float(lsplit[line_content.index('ann_hh')]) > np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_h))) or float(lsplit[line_content.index('ann_ZZ')]) > np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_Z))) or float(lsplit[line_content.index('ann_WW')]) > np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_W))) or float(lsplit[line_content.index('ann_vv')]) > np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_nu))):
                    num_ex_ID+=1
                    ex_ID[i] = True
                k+=1
    
    if len(ex_searches) > 0:
        ex_searches_num_pairs = list(zip(ex_searches, num_searches))
        ex_searches_num_pairs.sort(key=lambda x: x[1], reverse=True)
        ex_searches, num_searches = zip(*ex_searches_num_pairs)
        ex_searches = list(ex_searches)
        num_searches = list(num_searches)
    if len(ex_topo) > 0:
        ex_topo_num_pairs = list(zip(ex_topo, num_ex_topo))
        ex_topo_num_pairs.sort(key=lambda x: x[1], reverse=True)
        ex_topo, num_ex_topo = zip(*ex_topo_num_pairs)
        ex_topo = list(ex_topo)
        num_ex_topo = list(num_ex_topo)
    if len(DD_experiments) > 0:
        DD_experiments_num_pairs = list(zip(DD_experiments, num_experiments))
        DD_experiments_num_pairs.sort(key=lambda x: x[1], reverse=True)
        DD_experiments, num_experiments = zip(*DD_experiments_num_pairs)
        DD_experiments = list(DD_experiments)
        num_experiments = list(num_experiments)

    # Flavor constraints
    ex_flavor = [False] * len(values_allowed[0])
    num_ex_flavor = 0
    flavor_observables = []
    num_observables = []
    j=0
    for i in range(30):
        if os.path.exists(name+"/results_"+str(i)+".dat"):
            with open(name+"/results_"+str(i)+".dat", "rb") as file:
                results = pickle.load(file)
                for i in range(len(results)):
                    if results[i+1+j]['likelihoods']['global'] <= -2:
                        ex_flavor[i+j] = True # excluded by flavor constraints
                        num_ex_flavor += 1
                        observable = results[i+1+j]['observables']['experiment'].keys()[0]
                        if observable not in flavor_observables:
                            flavor_observables.append(observable)
                            num_observables.append(1)
                        else:
                            num_observables[flavor_observables.index(observable)] += 1
            j+=len(results)
            file.close()
        print("Number of points read: ", points_read)
        results_file.write("Number of points read: " + str(points_read) + "\n")
        print("Number of points excluded by relic abundance: ", num_ex_rel)
        results_file.write("Number of points excluded by relic abundance: " + str(num_ex_rel) + "\n")
        print("Number of points excluded by DD: ", num_ex_DD)
        results_file.write("Number of points excluded by DD: " + str(num_ex_DD) + "\n")
        print("DD experiments that excluded points: ", DD_experiments, " with number of exclusions: ", num_experiments)
        results_file.write("DD experiments that excluded points: " + str(DD_experiments) + " with number of exclusions: " + str(num_experiments) + "\n")
        print("Number of points excluded by SModelS: ", num_ex_SMS)  
        results_file.write("Number of points excluded by SModelS: " + str(num_ex_SMS) + "\n")
        print("Searches that excluded points: ", ex_searches, " with number of exclusions: ", num_searches)
        results_file.write("Searches that excluded points: " + str(ex_searches) + " with number of exclusions: " + str(num_searches) + "\n")
        print("Topology that excluded points: ", ex_topo, " with number of exclusions: ", num_ex_topo)
        results_file.write("Topology that excluded points: " + str(ex_topo) + " with number of exclusions: " + str(num_ex_topo) + "\n")
        print("Number of points excluded by ID: ", num_ex_ID)
        results_file.write("Number of points excluded by ID: " + str(num_ex_ID) + "\n")
        print("Number of remaining points: ", len(values_allowed[0]))
        results_file.write("Number of remaining points: " + str(len(values_allowed[0])) + "\n")
        print("Number of points excluded by flavor constraints: ", num_ex_flavor)
        results_file.write("Number of points excluded by flavor constraints: " + str(num_ex_flavor) + "\n")
        print("Flavor observables that excluded points: ", flavor_observables, " with number of exclusions: ", num_observables)
        results_file.write("Flavor observables that excluded points: " + str(flavor_observables) + " with number of exclusions: " + str(num_observables) + "\n")
        print("-------------------------------------------------------------------------------")
        results_file.write("-------------------------------------------------------------------------------\n")

    return data_dict_allowed, data_dict_all, omegas, promt_topo, promt_num, LLP_topo, LLP_num, offgrid_topo, offgrid_num, ex_SMS, ex_flavor, points_read,  num_ex_rel, num_ex_DD, num_ex_flavor, num_ex_SMS, num_ex_ID, ex_ID, ex_DD, DD_experiments, num_experiments, rel_channels, id_channels

# --------------------------------------
# Analysis of a scan
# --------------------------------------

# Read data
data_dict_allowed, data_dict_all, omegas, promt_topo, promt_num, LLP_topo, LLP_num, offgrid_topo, offgrid_num, ex_SMS, ex_flavor, points_read, num_ex_rel, num_ex_DD, num_ex_flavor, num_ex_SMS, num_ex_ID, ex_ID, ex_DD, DD_experiments, num_experiments, rel_channels, id_channels = read_files(scan_name, results_file=results_file)

print("Percentage of points excluded by relic abundance: ", num_ex_rel/points_read*100)
results_file.write("Percentage of points excluded by relic abundance: " + str(num_ex_rel/points_read*100) + "\n")
print("Percentage of points excluded by SModelS: ", num_ex_SMS/points_read*100)
results_file.write("Percentage of points excluded by SModelS: " + str(num_ex_SMS/points_read*100) + "\n")
print("Percentage of points excluded by DD: ", num_ex_DD/points_read*100)
results_file.write("Percentage of points excluded by DD: " + str(num_ex_DD/points_read*100) + "\n")
print("Percentage of points excluded by ID: ", num_ex_ID/points_read*100)
results_file.write("Percentage of points excluded by ID: " + str(num_ex_ID/points_read*100) + "\n")
print("Percentage of points excluded by flavor constraints: ", num_ex_flavor/len(data_dict_allowed["MXM1"])*100)
results_file.write("Percentage of points excluded by flavor constraints: " + str(num_ex_flavor/len(data_dict_allowed["MXM1"])*100) + "\n")
print("-------------------------------------------------------------------------------")
results_file.write("-------------------------------------------------------------------------------\n")

print("Promt topologies: ", promt_topo[:10])
results_file.write("Promt topologies: " + str(promt_topo[:10]) + "\n")
print(promt_num[:10])
results_file.write("Number of promt topologies: " + str(promt_num[:10]) + "\n")
print("\n")
results_file.write("\n")
print("LLP topologies: ", LLP_topo[:10])
results_file.write("LLP topologies: " + str(LLP_topo[:10]) + "\n")
print(LLP_num[:10])
results_file.write("Number of LLP topologies: " + str(LLP_num[:10]) + "\n")
print("\n")
results_file.write("\n")
print("Off grid topologies: ", offgrid_topo[:10])
results_file.write("Off grid topologies: " + str(offgrid_topo[:10]) + "\n")
print(offgrid_num[:10])
results_file.write("Number of off grid topologies: " + str(offgrid_num[:10]) + "\n")
print("-------------------------------------------------------------------------------")
results_file.write("-------------------------------------------------------------------------------\n")

rel_channels_summary = []
num_rel_channels = []
id_channels_summary = []
num_id_channels = []
for i in range(len(rel_channels)):
    channels = rel_channels[i].split("\t")
    if channels[0] not in rel_channels_summary:
        rel_channels_summary.append(channels[0])
        num_rel_channels.append(1)
    else:
        num_rel_channels[rel_channels_summary.index(channels[0])] += 1
    channels = id_channels[i].split("\t")
    if channels[0] not in id_channels_summary:
        id_channels_summary.append(channels[0])
        num_id_channels.append(1)
    else:
        num_id_channels[id_channels_summary.index(channels[0])] += 1

rel_channels_num_pairs = list(zip(rel_channels_summary, num_rel_channels))
rel_channels_num_pairs.sort(key=lambda x: x[1], reverse=True)
rel_channels_summary, num_rel_channels = zip(*rel_channels_num_pairs)
rel_channels_summary = list(rel_channels_summary)
num_rel_channels = list(num_rel_channels)
id_channels_num_pairs = list(zip(id_channels_summary, num_id_channels))
id_channels_num_pairs.sort(key=lambda x: x[1], reverse=True)
id_channels_summary, num_id_channels = zip(*id_channels_num_pairs)
id_channels_summary = list(id_channels_summary)
num_id_channels = list(num_id_channels)

print("Dominant channels for relic abundance: ", rel_channels_summary, " with number of occurences: ", num_rel_channels)
results_file.write("Dominant channels for relic abundance: " + str(rel_channels_summary) + " with number of occurences: " + str(num_rel_channels) + "\n")
print("Dominant channels for ID: ", id_channels_summary, " with number of occurences: ", num_id_channels)
results_file.write("Dominant channels for ID: " + str(id_channels_summary) + " with number of occurences: " + str(num_id_channels) + "\n")
print("-------------------------------------------------------------------------------")
results_file.write("-------------------------------------------------------------------------------\n")