This pipeline processes raw Phenobooth (Singer Instrument, UK) output files to generate strain fitness data based on colony sizes (pixel counts).
It includes data cleaning, strain annotation, normalization, technical replicate merging, and statistical analysis.


**Pipeline Overview**

**1. Plate Identification & Organization**

(Python scripts: 0–2.5)
	•	Identify plate numbers from raw Phenobooth outputs.
	•	Separate data for each plate.
	•	Rename each plate using experimental condition names defined in the Summary file.
	•	Reallocate plates into condition-specific subfolders (condition, timepoints).

**2. Strain Annotation & Normalization**
(Python scripts: 3–6)
	•	Convert colony coordinates to strain names using a user-provided key file.
	•	Normalize each colony to the wild-type (WT) strain (WT name must be defined in the script).
	•	Merge technical replicates.
	•	Exclude unwanted strains (e.g., contamination, border colonies, WT) using an exclusion file.

**3. Statistical Analysis**
(Python scripts: 7)
	•	Calculate mean, median, standard deviation, and p-values for all strains across conditions.
	•	Generate final relative fitness results.

**NB**. In the script, a list of condition and timepoint are provided as a list. Please change them accordingly.

⸻

**Requirements**

To run this pipeline, prepare the following files:
	1.	Raw Phenobooth output
	•	Use directly; no modification required.
	
	2.	Phenobooth_output_Summary.csv
	•	Rename the first column to your experiment condition identifier. The naming format must follow: condition_time_plate#_technical#
	
	3.	Key file
	•	Maps plate coordinates to strain names.
	
	4.	Exclusion file
	•	Lists strains to remove (contamination, border strains, WT, etc.)
  

Example of all the fliles are provided in the folder "Example_input_and_key_files/"
  
