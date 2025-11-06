#!/bin/bash



###################################################################
#Script Name	: Run_python.sh                                                                                          
#Author       	: Tanda Qi                       
#Email         	: tanda.qi@gmail.com    
#Details		: Run python scripts for analysing Phenobooth outputs
###################################################################

#$ ./Run_python.sh


echo "-------------running 0_seperate_the_file_by_run_and_plates.py--------------"
python3 0_seperate_the_file_by_run_and_plates.py
sleep 1


echo "-------------running 1_Rename_the_files.py--------------"
python3 1_Rename_the_files.py
sleep 1


echo "-------------running 2_Move_files_to_subfolders.py and 2.5_Move_files_to_condition_subfolders.py--------------"
python3 2_Move_files_to_subfolders.py
python3 2.5_Move_files_to_condition_subfolders.py
sleep 1

echo "-------------running 3_Fill_the_name.py--------------"
python3 3_Fill_the_name.py
sleep 1


echo "-------------running 4_Remove_blank_and_exclusion.py--------------"
python3 4_Remove_blank_and_exclusion.py
sleep 1

echo "-------------running 5_Normalize_the_file.py--------------"
python3 5_Normalize_the_file.py
sleep 1

echo "-------------running 6_Merged_plates_and_remove_WT.py--------------"
python3 6_Merged_plates_and_remove_WT.py
sleep 1

echo "-------------running 7A_Calculate_delta_size_and_P-value.py--------------"
python3 7A_Calculate_delta_size_and_P-value.py
sleep 1


echo "-------------Pipeline completed--------------"