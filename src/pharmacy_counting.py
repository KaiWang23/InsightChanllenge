import csv
import re
import sys
from collections import OrderedDict

# read in arguments from shell command
args = list(sys.argv)
input_dir = args[1]
output_dir = args[2]

# create dictionary to store results
drug_count = {}
drug_total_cost = {}

# read input line by line
with open(input_dir) as f:
    # read in header, strip whitespaces then split by comma
    header = f.readline().strip().split(',')
    id_index = header.index('id')
    drug_name_index = header.index('drug_name')
    drug_cost_index = header.index('drug_cost')

    # use csv reader to handle comma separated input
    for line in csv.reader(f, skipinitialspace=True):
        # skip current line if it's empty
        if not ''.join(line).strip():
            continue
        # skip current line if id/drug_name/drug_cost do not meet requirement
        if not line[id_index] or not line[drug_name_index] or not line[drug_cost_index]:
            continue
        # drug cost should be numeric
        try:
            cost = float(line[drug_cost_index])
        except ValueError:
            print('drug cost is not numeric')
            continue
        # get numerics from cost and convert to floating number
        # cost = float(re.sub("[^\d\.]", "", line[drug_cost_index]))

        # increment num_prescriber by 1 when a drug appears
        drug_count[line[drug_name_index]] = drug_count.get(line[drug_name_index], 0) + 1
        # add cost to total cost in dictionary
        drug_total_cost[line[drug_name_index]] = drug_total_cost.get(line[drug_name_index], 0) + cost

# sort by value of dict in descending order
drug_total_cost = OrderedDict(sorted(drug_total_cost.items(), key=lambda x: x[1], reverse=True))

with open(output_dir,'w') as file:
    # write header
    file.write('drug_name,num_prescriber,total_cost' + '\n')

    for key in drug_total_cost:
        # convert drug_total_cost to int when output the result
        file.write(key + ',' + str(drug_count.get(key)) + ',' + str(int(drug_total_cost.get(key))) + '\n')




