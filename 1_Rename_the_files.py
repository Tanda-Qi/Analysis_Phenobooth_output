#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 12:15:17 2023

@author: tanda
"""

import os
import csv

os.chdir("Your/Working/Directory")

# Read the key file and store its data in a dictionary
key_file = "./Your_Renamed_RoToR_Summary.csv"

key_data = {}
with open(key_file, "r", newline="") as keyfile:
    key_reader = csv.reader(keyfile)
    next(key_reader)  # Skip header
    for row in key_reader:
        if len(row) >= 3:
            key_data[(row[1], row[2])] = row[0]

# Directory containing CSV files
input_folder = "./0_Seperated_files/"
output_folder = "./1_Renamed_files/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through files in the directory
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        input_filepath = os.path.join(input_folder, filename)
        output_filepath = os.path.join(output_folder, filename)

        with open(input_filepath, "r", newline="") as infile, open(output_filepath, "w", newline="") as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # Write the header
            writer.writerow(next(reader))

            renamed = False  # Track if file has been renamed
            
            for row in reader:
                if len(row) >= 2:
                    element1, element2 = row[0], row[1]
                    if (element1, element2) in key_data and not renamed:
                        new_filename = key_data[(element1, element2)] + ".csv"
                        renamed_filepath = os.path.join(output_folder, new_filename)
                        os.rename(output_filepath, renamed_filepath)
                        print(f"Renamed {filename} to {new_filename}")
                        renamed = True
                        writer.writerow(row)
                    else:
                        writer.writerow(row)  # Write the row to the output file
