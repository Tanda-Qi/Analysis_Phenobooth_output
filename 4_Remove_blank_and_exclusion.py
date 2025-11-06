#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:05:44 2023

@author: tanda
"""
import os
import csv

def exclusion(a,b,c):
    input_file1 = open(a, 'r')
    exclusion_file1 = open(b, 'r')
    output_file1 = open(c, 'w')
    
    input_reader = csv.reader(input_file1)
    exclusion_reader = csv.reader(exclusion_file1)
    output_writer = csv.writer(output_file1)
    
    # 建立一个exclusion_list，用于存储exclusion_file的第三列的内容
    exclusion_list = []
    for row in exclusion_reader:
        exclusion_list.append(row[0])
    
    # 遍历input_file，如果input_file的第三列的内容不在exclusion_list中，则写入output_file
    for row in input_reader:
        if row[2] not in exclusion_list:
            output_writer.writerow([row[2],row[5]])
            
            

os.chdir("/Users/user/The University of Manchester Dropbox/Qi Tanda/Working/23-08_Query_ncRNA_screening/Analysis query strain screening in SGA conditions/Analysis/Input_files")

times=["48h","96h"]
list_of_conditions=["Your list of condition"] #CHANGE accordingly

output_dir = "4_Blank_excluded"
os.makedirs(output_dir, exist_ok=True)

log_file = open("4_Blank_excluded/log_removing.txt", "w")

exclusion_file = "./Your_exclusion_list.csv" #CHANGE accordingly



for time in times:
    for condition in list_of_conditions:
        for plate_number in range(1,3):
            for technical in range(1,4):

                output_path = f"./4_Blank_excluded//{time}/{condition}/"
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                output_file = f"./4_Blank_excluded/{time}/{condition}/{condition}_{time}_Plate{plate_number}_T{technical}.csv"
                input_file = f"./3_Name_filled/{time}/{condition}/{condition}_{time}_Plate{plate_number}_T{technical}.csv"
                if os.path.exists(input_file):
                    exclusion(input_file,exclusion_file,output_file)
                    log_message = f"Replacement complete. New CSV file created: {output_file}\n"
                    log_file.write(log_message)
                else:
                    log_message = f"Input file '{input_file}' does not exist. Skipping this combination.\n"
                    log_file.write(log_message)

                   
                   
# Close the log file
log_file.close()
