#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 12:00:41 2023

@author: tanda
"""

import os
import csv

os.chdir("Your/Working/Directory")


input_file = "./Your_RoToR_output_csv(xx_ColonyData_AllPlates).csv"

# Create a directory to store the output CSV files
output_path = "./0_Seperated_files"
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Read the input file and process data
with open(input_file, "r", newline="") as infile:
    reader = csv.reader(infile)
    lines = list(reader)

# Extract the header and remove it from the data
header = lines[0]
data = lines[1:]

# Dictionary to store data for each unique combination of the first and second columns
data_dict = {}

# Process each line and store data in the dictionary
for row in data:
    if len(row) >= 2:
        key = (row[0], row[1])
        if key not in data_dict:
            data_dict[key] = []
        data_dict[key].append(row)

# Write data to separate CSV files
for key, rows in data_dict.items():
    run_name = "Run" + key[0] + "_" + key[1]
    output_file = os.path.join(output_path, run_name + ".csv")

    with open(output_file, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(rows)
    num_rows = len(rows)
    if num_rows != 1536:
        print(f"File {run_name}.csv don't have a correct row number, which is {num_rows} rows.")      
        
        
        
        
        