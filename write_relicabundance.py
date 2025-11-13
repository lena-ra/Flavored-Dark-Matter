import numpy as np
import sys
import os.path

# This script reads the output of micrOMEGAs and writes the relic abundance, annihilation cross sections, direct detection constraints, and missing topologies to a file.
# Run this script with python3 write_relicabundance.py <input_file> <output_path> <model_dir>

input_file = sys.argv[1] # file containing the output of micrOMEGAs
output_path = sys.argv[2] # path to the output directory where the results will be saved
model_dir = sys.argv[3] # name of the model directory in micrOMEGAs

micromegas_path = sys.argv[4] + model_dir # path to the micrOMEGAs directory, must be changed according to your installation

# save r value and topology information from SModelS output
# if SModelS output is not available, set r value to 0 and topology to "none"
# if SModelS output is available, save the topology and r value

totalxs_LLP = 0
totalxs_prompt = 0
totalxs_offgrid = 0
r_value = 0

if os.path.isfile(micromegas_path + "smodels.slha.smodels"):
    topo_file = open(micromegas_path + "smodels.slha.smodels", "r")
    topo_content = topo_file.readlines()
    indices = [i for i, x in enumerate(topo_content) if "=====" in x]
    for line in topo_content:
        if "Txnames:" in line:
            topo = line.split()[1]
        if "The highest r value is" in line:
            r_value = float(line.split()[6])
            search = line.split()[8]
        if "Total cross-section for missing topologies with displaced decays" in line:
            totalxs_LLP = float(line[line.index(":"):].split()[1])
        if "Total cross-section for missing topologies with prompt decays" in line:
            totalxs_prompt = float(line[line.index(":"):].split()[1])
        if "Total cross-section for topologies outside the grid" in line:
            totalxs_offgrid = float(line[line.index(":"):].split()[1])
    topo_file.close()

if r_value >= 1:
    smodels = search
else:
    smodels = "SMS_not_excluded"
    topo = "none"

with open(output_path+"missing_topologies.txt", "a") as f:
    if totalxs_LLP != 0:
        i_min = indices[-4]+3
        i_max = indices[-3]
        f.write("LLP: ")
        for i, line in enumerate(topo_content[i_min:i_max]):
            f.write("[" + line.split()[1] + ", " + line.split()[5][:-1] + ", " + line.split()[6] + "]")
            if i != i_max-i_min-1:
                f.write(", ")
    else:
        f.write("LLP: 0")
    f.write("\n")
    if totalxs_prompt != 0:
        i_min = indices[-3]+3
        i_max = indices[-2]
        f.write("Prompt: ")
        for i, line in enumerate(topo_content[i_min:i_max]):
            f.write("[" + line.split()[1] + ", " + line.split()[5][:-1] + ", " + line.split()[6] + "]")
            if i != i_max-i_min-1:
                f.write(", ")
    else:
        f.write("Prompt: 0")
    f.write("\n")
    if totalxs_offgrid != 0:
        i_min = indices[-2]+3
        i_max = indices[-1]
        f.write("Off grid: ")
        for i, line in enumerate(topo_content[i_min:i_max]):
            f.write("[" + line.split()[1] + ", " + line.split()[5][:-1] + ", " + line.split()[6] + "]")
            if i != i_max-i_min-1:
                f.write(", ")
    else:
        f.write("Off grid: 0")
    f.write("\n")

f.close()

# Read the output of micrOMEGAs and extract the relic abundance, annihilation cross sections, and direct detection constraints
def read_omega(file):
    open_file=open(file, 'r')
    content = open_file.readlines()
    ann_qq = 0
    ann_cc = 0
    ann_bb = 0
    ann_tt = 0
    ann_qc = 0
    ann_qb = 0
    ann_qt = 0
    ann_ct = 0
    ann_ee = 0
    ann_mumu = 0
    ann_tata = 0
    ann_emu = 0
    ann_eta = 0
    ann_muta = 0
    ann_hh = 0
    ann_ZZ = 0
    ann_WW = 0
    ann_vv = 0
    
    for line in content:
        if line[:3] == "Xf=":
            omega = float(line.split()[1][6:])
        if "annihilation cross section" in line:
            xs = float(line.split()[3])
        if "-> u u~" in line or "-> u d~" in line or "-> u~ d" in line or "-> u s~" in line or "-> u~ s" in line or "-> d d~" in line or "-> d s~" in line or "-> d~ s" in line or "-> s s~" in line:
            ann_qq += xs*float(line.split()[4])
        if "-> c c~" in line:
            ann_cc = xs*float(line.split()[4])
        if "-> b b~" in line:
            ann_bb = xs*float(line.split()[4])
        if "-> t t~" in line:
            ann_tt = xs*float(line.split()[4])
        if "-> u c~" in line or "-> u~ c" in line:
            ann_qc = xs*float(line.split()[4])
        if "-> u t~" in line or "-> u~ t" in line:
            ann_qt = xs*float(line.split()[4])
        if "-> c t~" in line or "-> c~ t" in line:
            ann_ct = xs*float(line.split()[4])
        if "-> d b~" in line or "-> d~ b" in line or "-> s b~" in line or "-> s~ b" in line:
            ann_qb = xs*float(line.split()[4])
        if "-> e- e+" in line:
            ann_ee = xs*float(line.split()[4])
        if "-> a e- e+" in line:
            ann_ee += xs*float(line.split()[5])
        if "-> mu- mu+" in line:
            ann_mumu = xs*float(line.split()[4])
        if "-> a mu- mu+" in line:
            ann_mumu += xs*float(line.split()[5])
        if "-> ta- ta+" in line:
            ann_tata = xs*float(line.split()[4])
        if "-> a ta- ta+" in line:
            ann_tata += xs*float(line.split()[5])
        if "-> e- mu+" in line or "-> e+ mu-" in line:
            ann_emu = xs*float(line.split()[4])
        if "-> e- ta+" in line or "-> e+ ta-" in line:
            ann_eta = xs*float(line.split()[4])
        if "-> mu- ta+" in line or "-> mu+ ta-" in line:
            ann_muta = xs*float(line.split()[4])
        if "->  H H" in line:
            ann_hh = xs*float(line.split()[4])
        if "-> Z Z" in line:
            ann_ZZ = xs*float(line.split()[4])
        if "-> W+ W-" in line:
            ann_WW = xs*float(line.split()[4])
        if "-> ve ve~" in line or "-> vm vm~" in line or "-> vt vt~" in line or "-> ve vt~" in line or "-> ve~ vt" in line or "-> vm vt~" in line or "-> vm~ vt" in line or "-> ve vm~" in line or "-> ve~ vm" in line:
            ann_vv = xs*float(line.split()[4])
        if "Not excluded by" in line:
            DD = "not_excluded"
        if "Excluded by" in line:
            DD = line.split()[2]
        if " proton  SI" in line:
            elm = line.split()
            proton = str(float(elm[2])) + "\t" + str(float(elm[3][1:-1])) + "\t" + str(float(elm[5])) + "\t" + str(float(elm[6][1:-1]))
        if " neutron SI" in line:
            elm = line.split()
            neutron = str(float(elm[2])) + "\t" + str(float(elm[3][1:-1])) + "\t" + str(float(elm[5])) + "\t" + str(float(elm[6][1:-1]))
    open_file.close()
    return omega, xs, ann_qq, ann_cc, ann_bb, ann_tt, ann_qc, ann_qb, ann_qt, ann_ct, ann_ee, ann_mumu, ann_tata, ann_emu, ann_eta, ann_muta, ann_hh, ann_ZZ, ann_WW, ann_vv, DD, proton, neutron

Omega, xs, ann_qq, ann_cc, ann_bb, ann_tt, ann_qc, ann_qb, ann_qt, ann_ct, ann_ee, ann_mumu, ann_tata, ann_emu, ann_eta, ann_muta, ann_hh, ann_ZZ, ann_WW, ann_vv, DD, proton, neutron = read_omega(input_file)

# Write the results to a file, the file relic_abundances.txt should have been created before running this script with a corresponding header

with open(output_path+"relic_abundances.txt", "a") as f:
    f.write(str(Omega)+"\t"+str(xs)+"\t"+str(ann_qq)+"\t"+str(ann_cc)+"\t"+str(ann_bb)+"\t"+str(ann_tt)+"\t"+str(ann_qc)+"\t"+str(ann_qb)+"\t"+str(ann_qt)+"\t"+str(ann_ct)+"\t"+str(ann_ee)+"\t"+str(ann_mumu)+"\t"+str(ann_tata)+"\t"+str(ann_emu)+"\t"+str(ann_eta)+"\t"+str(ann_muta)+"\t"+str(ann_hh)+"\t"+str(ann_ZZ)+"\t"+str(ann_WW)+"\t"+str(ann_vv)+"\t"+str(DD)+"\t"+proton+"\t"+neutron+"\t"+smodels+"\t"+topo+"\t"+str(r_value)+"\n")

f.close()
