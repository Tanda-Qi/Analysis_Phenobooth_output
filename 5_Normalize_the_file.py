#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:11:24 2023

@author: tanda

Normalize the colony sizes with WT
"""

import csv
import pandas as pd
import numpy as np
import os


def normalization(a, b):
    global divisor
    global mean_WT

    df = pd.read_csv(a)
    list_of_WT = []

    with open(a, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if 'A1160' in row[0]:
                list_of_WT.append(float(row[1]))

    divisor = np.median(list_of_WT)  # 取所有WT的中位数
    mean_WT = np.mean(list_of_WT)

    df.iloc[:, 1:] = df.iloc[:, 1:] / divisor

    df.to_csv(b, index=False)



os.chdir("Your/Working/Directory") #CHANGE accordingly
times=["48h","96h"]
list_of_conditions=["Your list of condition"] #CHANGE accordingly

output_dir = "5_Normalized"
os.makedirs(output_dir, exist_ok=True)
log_file = open("5_Normalized/log_Normalization.txt", "w")

for time in times:
    for condition in list_of_conditions:
        for plate_number in range(1,3):
            for technical in range(1,4):
                output_path = f"./5_Normalized/{time}/{condition}"
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                output_file = f"./5_Normalized/{time}/{condition}/{condition}_{time}_Plate{plate_number}_T{technical}.csv"
                input_file = f"./4_Blank_excluded/{time}/{condition}/{condition}_{time}_Plate{plate_number}_T{technical}.csv"
                if os.path.exists(input_file):
                    normalization(input_file, output_file)
                    log_message = f"Normalization complete. WT median is {divisor}, WT mean is {mean_WT}. New CSV file created: {output_file}\n"
                    log_file.write(log_message)
                else:
                    log_message = f"Input file '{input_file}' does not exist. Skipping this combination.\n"
                    log_file.write(log_message)

# Close the log file
log_file.close()
                   



