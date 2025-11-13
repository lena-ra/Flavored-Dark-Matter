import numpy as np
import sys

# This script reads the output of micrOMEGAs and writes the relic abundance and channels to a file.

input_file = sys.argv[1] # file containing the output of micrOMEGAs
output_path = sys.argv[2] # path to the output directory where the results will be saved

def read_omega(file):
    open_file=open(file, 'r')
    content = open_file.readlines()
    for line in content:
        if line[:3] == "Xf=":
            Omega = line.split()[1][6:]
        if "annihilation cross section" in line:
            xs = line.split()[3]
        if "# Relative contributions in % are displayed" in line:
            index1 = content.index(line)
        if "=====  LHC constraints with SModelS  =====" in line:
            index2 = content.index(line)
        if "contribution of processes" in line:
            index3 = content.index(line)
        if "Photon flux  for angle of sight" in line:
            index4 = content.index(line)
    channels = ""
    for i in range(min([len(content[index1+1:index2-2]), 5])):
        channels += "\t"+str(content[index1+1+i][(content[index1+1+i].index("%")+2):-2])
    id_channels = ""
    for i in range(min([len(content[index3+1:index4]), 5])):
        line = content[index3+1+i].split()
        info = line[line.index("->")+1:-1]
        id_channels += "\t"+info[0]
        for j in range(len(info)-1):
            id_channels += " " + info[j+1]
    open_file.close()
    return Omega, channels, xs, id_channels

Omega, channels, xs, id_channels = read_omega(input_file)

with open(output_path+"channels.txt", "a") as f:
    f.write(Omega+channels+"\n")
    f.write(xs+id_channels+"\n")

f.close()
