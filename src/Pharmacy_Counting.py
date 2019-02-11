import os
import csv
import re
import sys
from collections import OrderedDict

dir = os.getcwd().split('\\')
dir = '\\'.join(dir)
os.chdir(dir)

args = list(sys.argv)
input_dir = args[1]
output_dir = args[2]

drug_count = {}
drug_total_cost = {}

with open(input_dir) as f:
    header = f.readline().strip().split(',')
    drug_name_index = header.index('drug_name')
    drug_cost_index = header.index('drug_cost')

    for line in csv.reader(f, skipinitialspace=True):
        cost = float(re.sub("[^\d\.]", "", line[drug_cost_index]))
        drug_count[line[drug_name_index]] = drug_count.get(line[drug_name_index], 0) + 1
        drug_total_cost[line[drug_name_index]] = drug_total_cost.get(line[drug_name_index], 0) + cost

drug_total_cost = OrderedDict(sorted(drug_total_cost.items(), key=lambda x: x[1], reverse=True))

with open(output_dir,'w') as file:
    file.write('drug_name,num_prescriber,total_cost' + '\n')

    for key in drug_total_cost:
        file.write(key + ',' + str(drug_count.get(key)) + ',' + str(drug_total_cost.get(key)) + '\n')




