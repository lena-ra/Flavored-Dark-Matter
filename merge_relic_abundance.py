import numpy as np
import sys
import os

# This script merges the relic abundance results from multiple cores and applies constraints.

name = sys.argv[1] # name of output directory
data_file = sys.argv[2] # name of input data file
open_file=open(data_file, 'r')
content = open_file.readlines()
header = content[0].split()[1:]
values = np.array([x.split() for x in content[1:]]).transpose()
data_dict = dict(zip(header, values))
open_file.close()
open_file = open(data_file[:-4]+"_params.dat", 'r')
param_content = open_file.readlines()
open_file.close()
omegas_file = open(name+"/constraints.txt", "w")
topo_file = open(name+"/selected_topologies.txt", "w")
channels_file = open(name+"/selected_channels.txt", "w")
params_file = open(name+"/"+name+".dat", "w")
params_file.write(content[0])
selected_params_file = open(name+"/"+name+"_params.dat", "w")
selected_params_file.write(param_content[0])
if "MXC3" in header:
    index_mass = header.index("MXC3")
if "MXD3" in header:
    index_mass = header.index("MXD3")
if "MXM3" in header:
    index_mass = header.index("MXM3")
if "MXS3" in header:
    index_mass = header.index("MXS3")

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

# Read the ID limits for different channels
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

num_omegas = 0
points_read = 0
for j in range(48):
    file = open(name+"/core_"+str(j)+"/relic_abundances.txt", "r")
    file_topo = open(name+"/core_"+str(j)+"/missing_topologies.txt", "r")
    file_channels = open(name+"/core_"+str(j)+"/channels.txt", "r")
    line = file.readline()
    line_topo = file_topo.readline()
    line_content = line.split('\t')
    index_omega = line_content.index('rel_abundance')
    index_DD = line_content.index('DD_exclusion')
    index_SMS = line_content.index('SModelS_exclusion')
    if j == 0:
        omegas_file.write(line) # write header
        topo_file.write(line_topo) # write header
        channels_file.write(file_channels.readline()) # write header
    line = file.readlines()
    line_topo = file_topo.readlines()
    line_channels = file_channels.readlines()
    points_read += len(line)
    k=0
    for i in np.arange(j,len(content)-1,48): # loop over all points in the file per core
        if k < len(line):
            lsplit = line[k].split()
            omega = float(lsplit[index_omega])
            DD_ex = lsplit[index_DD]
            SMS_ex = lsplit[index_SMS]
            m = float(values[index_mass][i])
            # Check if relic abundance is in the correct range
            if omega - 0.1*omega <= 0.12 and omega + 0.1*omega >= 0.12:
                # Check if direct detection and SModelS exclusion are not violated
                if DD_ex == 'not_excluded' and SMS_ex == 'SMS_not_excluded':
                    # Check if the annihilation cross sections are below the ID limits
                    if float(lsplit[line_content.index('ann_qq')]) < np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_q))) and float(lsplit[line_content.index('ann_cc')]) < np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_c))) and float(lsplit[line_content.index('ann_bb')]) < np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_b))) and float(lsplit[line_content.index('ann_tt')]) < np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_t))) and float(lsplit[line_content.index('ann_qc')]) < 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_q))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_c)))) and float(lsplit[line_content.index('ann_qb')]) < 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_q))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_b)))) and float(lsplit[line_content.index('ann_qt')]) < 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_q))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_t)))) and float(lsplit[line_content.index('ann_ct')]) < 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_c))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_t)))) and float(lsplit[line_content.index('ann_ee')]) < np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_e))) and float(lsplit[line_content.index('ann_mumu')]) < np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_mu))) and float(lsplit[line_content.index('ann_tata')]) < np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_tau))) and float(lsplit[line_content.index('ann_emu')]) < 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_e))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_mu)))) and float(lsplit[line_content.index('ann_eta')]) < 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_e))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_tau)))) and float(lsplit[line_content.index('ann_muta')]) < 0.5*(np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_mu))) + np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_tau)))) and float(lsplit[line_content.index('ann_hh')]) < np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_h))) and float(lsplit[line_content.index('ann_ZZ')]) < np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_Z))) and float(lsplit[line_content.index('ann_WW')]) < np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_W))) and float(lsplit[line_content.index('ann_vv')]) < np.exp(np.interp(np.log(m), np.log(m_DM), np.log(sigmav_nu))):
                        # Write the selected points to the output files
                        omegas_file.write(line[k])
                        topo_file.write(line_topo[k*3])
                        topo_file.write(line_topo[k*3+1])
                        topo_file.write(line_topo[k*3+2])
                        channels_file.write(line_channels[k*2])
                        channels_file.write(line_channels[k*2+1])
                        params_file.write(content[i+1])
                        selected_params_file.write(param_content[i+1])
                        num_omegas+=1
            k+=1

print("accepted number of points: ", num_omegas)
print("number of read points: ", points_read)
