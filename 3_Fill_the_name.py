#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:35:44 2023

@author: tanda
"""

import os
import csv

os.chdir("Your/Working/Directory") #CHANGE accordingly
times=["48h","96h"]
list_of_conditions=["Your list of condition"] #CHANGE accordingly
"""
Conditions=[
    "AMM37C",
    "AMM45C",
    "AMMH2O2",
    "AMM4Agar",
    "AMMnoFe",
    "AMMPosa",
    "AMMVori",
    "AMMItra"
]
"""
output_dir = "./3_Name_filled"
os.makedirs(output_dir, exist_ok=True)
log_file = open("./3_Name_filled/log_for_filling_the_name.txt", "w")


for time in times:
    for condition in list_of_conditions:
        for plate_number in range(1,3):
            for technical in range(1,4):
        
                input_file = f"./2_Rearranged_to_subfolders/{time}/{condition}/{condition}_{time}_Plate{plate_number}_T{technical}.csv"
                if not os.path.exists(input_file):
                    log_message = f"Input file '{input_file}' does not exist. Skipping this combination.\n"
                    log_file.write(log_message)
                    continue

                output_path = f"./3_Name_filled/{time}/{condition}/"
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                output_file = f"./3_Name_filled/{time}/{condition}/{condition}_{time}_Plate{plate_number}_T{technical}.csv"
                selected_key_file = f"./Your_key_file_{plate_number}.csv" #CHANGE accordingly

                
                # Read the selected key file and store its data in a dictionary
                key_data = {}
                with open(selected_key_file, "r", newline="") as keyfile:
                    key_reader = csv.reader(keyfile)
                    for row in key_reader:
                        if len(row) >= 3:
                            key_data[(row[1], row[2])] = row[0]
                
                # Process the input file and replace specific cells using the key
                output_data = []
                
                with open(input_file, "r", newline="") as infile:
                    reader = csv.reader(infile)
                    header = next(reader)
                    output_data.append(header)
                
                    for row in reader:
                        if len(row) >= 5 and (row[3], row[4]) in key_data:
                            row[2] = key_data[(row[3], row[4])]  # Replace the third column using the key
                        output_data.append(row)
                
                # Write the processed data to the output file
                with open(output_file, "w", newline="") as outfile:
                    writer = csv.writer(outfile)
                    writer.writerows(output_data)
                
                log_message = f"Replacement complete. New CSV file created: {output_file}\n"
                log_file.write(log_message)
               
               
# Close the log file
log_file.close()
