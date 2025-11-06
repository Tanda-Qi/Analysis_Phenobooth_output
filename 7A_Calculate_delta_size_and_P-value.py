#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:06:18 2023

@author: tanda
"""
import os
import csv
import numpy as np
from scipy.stats import ttest_ind


os.chdir("Your/Working/Directory") #CHANGE accordingly

# 读取文件内容到两个字典中
def read_file(file_path):
    data_dict = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[0]
            value = float(row[1])
            if key in data_dict:
                data_dict[key].append(value)
            else:
                data_dict[key] = [value]
    return data_dict

# 计算中位数差值、中位数fold change和T-test
def analyze_data(dict1, dict2):
    results = []
    for key in dict1:
        if key in dict2:
            values1 = dict1[key]
            values2 = dict2[key]
            median_diff = np.median(values1) - np.median(values2)
            median_fold_change = np.median(values1) / np.median(values2)
            t_stat, p_value = ttest_ind(values1, values2)
            results.append([key, median_diff, median_fold_change, p_value])
    return results



#make log file
log_path = "./7_Delta_size_P_value/"
if not os.path.exists(log_path):
    os.makedirs(log_path)
log_file = open("7_Delta_size_P_value/log_Calculation.txt", "w")

#start analysis
times=["48h","96h"]
list_of_conditions=["Your list of condition"] #CHANGE accordingly

for time in times:
    for condition in list_of_conditions:
        
        file1_path = f"./6_Merged/{time}/{condition}_Merged.csv"
        file2_path = "./6_Merged/48h/YPD30C_Merged.csv"
        if os.path.exists(file1_path):
            data_dict1 = read_file(file1_path)
            data_dict2 = read_file(file2_path)
            log_message = f"Input file {file1_path} found.\n"
            log_file.write(log_message)
        else:
            log_message = f"Cannot find inpit file{file1_path}.\n"
            log_file.write(log_message)
# 读取文件内容到字典中

        
        # 分析数据并得到结果
        results = analyze_data(data_dict1, data_dict2)
        
        # 将结果写入csv文件
        output_path = f"./7A_Delta_size_P_value/{time}/"
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        output_file = f'./7A_Delta_size_P_value/{time}/{time}_{condition}_vs_48h_YPD30.csv'
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Strain', 'Median_delta_size', 'Median_fold_change', 'P-value'])
            writer.writerows(results)
        log_message = f"Output file saved as {output_file}.\n"
        log_file.write(log_message)

        
# Close the log file
log_file.close()

