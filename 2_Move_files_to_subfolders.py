#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 12:35:49 2023

@author: tanda
"""

import os
import shutil
os.chdir("Your/Working/Directory")

# Input folder containing CSV files
input_folder = "./1_Renamed_files"

# Create subfolders for different keywords
#Here because I took photos on two different day, so each condition will have 2 time point
output_folders = {
    "48": "./2_Rearranged_to_subfolders/48h",
    "96": "./2_Rearranged_to_subfolders/96h"
}

for keyword, output_folder in output_folders.items():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

# Iterate through files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        input_filepath = os.path.join(input_folder, filename)

        with open(input_filepath, "r", newline="") as infile:
            header = infile.readline()  # Read the header

            # Identify the keyword
            keyword_found = None
            for key in output_folders.keys():
                if key in filename:
                    keyword_found = key
                    break

            if keyword_found:
                output_folder = output_folders[keyword_found]
                output_filepath = os.path.join(output_folder, filename)

                shutil.copyfile(input_filepath, output_filepath)
                print(f"Moved {filename} to {output_folder}")
            else:
                print(f"No matching keyword found for {filename}")

