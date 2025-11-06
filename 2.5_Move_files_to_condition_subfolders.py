#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 13:55:22 2023

@author: tanda
"""

import os
import shutil
os.chdir("Your/Working/Directory") 

times=["48h","96h"] #change according to you data
for time in times:

    # Input folder containing files
    input_folder = "./2_Rearranged_to_subfolders/{time}/"
    
    
    # Create output folder
    output_folder = "./2_Rearranged_to_subfolders/{time}/"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through files in the input folder
    for filename in os.listdir(input_folder):
        
        input_filepath = os.path.join(input_folder, filename)
        if os.path.isfile(input_filepath):
            # Extract the prefix before the first underscore
            prefix = filename.split("_")[0]

    
            # Create subfolder if it doesn't exist
            subfolder_path = os.path.join(output_folder, prefix)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
    
            # Move the file to the appropriate subfolder
            output_filepath = os.path.join(subfolder_path, filename)
            shutil.move(input_filepath, output_filepath)
    
    print("Files moved to subfolders.")


