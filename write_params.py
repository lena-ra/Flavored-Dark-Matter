import numpy as np
import sys

# This script writes the parameter file data.par for micrOMEGAs from a given input file and a specified index.

output_directory = sys.argv[2] # directory where the output file will be saved
model = sys.argv[3] # model name, e.g. "Dirac_d", "Majorana_d", etc.
index_data = int(sys.argv[4]) # index of the data point to be written, e.g. 0 for the first point

data_file = sys.argv[1] # file containing the data, e.g. "data.dat"
open_file=open(data_file, 'r')
content = open_file.readlines()
header = content[0].split()[1:]
values = np.array([x.split() for x in content[1:]]).transpose()
data_dict = dict(zip(header, values))

with open(output_directory+"data.par", 'w') as output:
    output.write("# model parameters \n")
    if "Dirac_d" in model or "Majorana_d" in model or "Dirac_e" in model or "Majorana_e" in model or "Dirac_u" in model or "Majorana_u" in model:
        for i in range(len(header)-5):
            output.write(header[i]+" " + str(data_dict[header[i]][index_data]) + "\n")
        output.write(header[-4]+" " + str(data_dict[header[-4]][index_data])+ "\n")
        output.write(header[-3]+" " + str(data_dict[header[-3]][index_data])+ "\n")
        output.write(header[-2]+" " + str(data_dict[header[-2]][index_data])+ "\n")
        output.write(header[-1]+" " + str(data_dict[header[-1]][index_data]))
    if "Dirac_q" in model or "Majorana_q" in model:
        for i in range(len(header)-6):
            output.write(header[i]+" " + str(data_dict[header[i]][index_data]) + "\n")
        output.write(header[-5]+" " + str(data_dict[header[-5]][index_data])+ "\n")
        output.write(header[-4]+" " + str(data_dict[header[-4]][index_data])+ "\n")
        output.write(header[-3]+" " + str(data_dict[header[-3]][index_data])+ "\n")
        output.write(header[-2]+" " + str(data_dict[header[-2]][index_data])+ "\n")
        output.write(header[-1]+" " + str(data_dict[header[-1]][index_data]))
    if "Dirac_l" in model or "Majorana_l" in model:
        for i in range(len(header)-7):
            output.write(header[i]+" " + str(data_dict[header[i]][index_data]) + "\n")
        output.write(header[-6]+" " + str(data_dict[header[-6]][index_data])+ "\n")
        output.write(header[-5]+" " + str(data_dict[header[-5]][index_data])+ "\n")
        output.write(header[-4]+" " + str(data_dict[header[-4]][index_data])+ "\n")
        output.write(header[-3]+" " + str(data_dict[header[-3]][index_data])+ "\n")
        output.write(header[-2]+" " + str(data_dict[header[-2]][index_data])+ "\n")
        output.write(header[-1]+" " + str(data_dict[header[-1]][index_data]))
    if "Real" in model or "Complex" in model:
        for i in range(len(header)-7):
            output.write(header[i]+" " + str(data_dict[header[i]][index_data]) + "\n")
        output.write(header[-4]+" " + str(data_dict[header[-4]][index_data]) + "\n")
        output.write(header[-3]+" " + str(data_dict[header[-3]][index_data]) + "\n")
        output.write(header[-2]+" " + str(data_dict[header[-2]][index_data]))
output.close()
