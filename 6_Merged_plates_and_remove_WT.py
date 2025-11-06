#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:09:12 2023

@author: tanda
"""
import os
import glob
import csv

os.chdir("Your/Working/Directory") #CHANGE accordingly
times=["48h","96h"]
list_of_conditions=["Your list of condition"] #CHANGE accordingly

for time in times:
    for condition in list_of_conditions:
        input_path = f"./5_Normalized/{time}/{condition}/"
        file_pattern = os.path.join(input_path, "*.csv")
        csv_files = glob.glob(file_pattern)
        
        output_path = f"./6_Merged/{time}/"
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        output_file = os.path.join(output_path, f"{condition}_Merged.csv")
        
        # merge csv
        merged_csv = []
        for csv_file in csv_files:
            with open(csv_file, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                rows = [row for row in reader]
                merged_csv.extend(rows)
        
        # Delete WT in the data
        merged_csv = [row for row in merged_csv if 'A1160' not in row]
    
        # 按照第一列的值排序
        merged_csv = sorted(merged_csv, key=lambda x: x[0])
        
        # 如果合并后的文件不为空，则保存
        if len(merged_csv) > 0:
            # 将合并后的结果保存为新的CSV文件
            with open(output_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(merged_csv)
    
            print(f"Merged files saved to {output_file}")
        else:
            print(f"No data to merge for {output_file}. Skipping.")
