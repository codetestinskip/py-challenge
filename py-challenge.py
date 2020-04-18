#
# Author: M.Inskip
# Date: 2018-04-18
# Version 0.1
#
# Python version 3.7.3  
#
# Execute the script: python py-challenge.py
#
# Please amend Python reference as appropriate

# Import required libraries
#
import json, argparse, os
from pathlib import Path


# Function definitions
#
def process_argument():
    """ function to generate arguments including folder argument """
    parser = argparse.ArgumentParser(
            prog = 'python py-challenge.py',
            description="Python script utility that finds a total of `seqlen` values in all files matching `*.data.json` pattern that are found in a given folder"
            )
    
    parser.add_argument('folder')
    args = parser.parse_args()
    
    return args

def confirm_folder_exists(folder):
    """ function to check existence of a folder """
    if not os.path.exists(folder):
        print("Specified folder does not appear to exist in the current path")
        exit

def create_list_of_json_files_from_folder(folder):
    """ function to list all json files in the folder """
    json_file_full_path = []
    for file_name in os.listdir(folder):
        if file_name.endswith(".data.json"):
           json_file_full_path.append(os.path.join(folder, file_name))  

    return json_file_full_path

def ingest_json_file(json_file_name):
    """ function to ingest json file """
    json_data = [json.loads(line) for line in open(json_file_name, 'r')]
    #print(json_data[1])
    return(json_data)

def obtain_seqlen_value(json_data):
    """ function to iterate through json data to identify seqlen value """
    seqlen_values_list = []
    for data_element in json_data:
        if isinstance(data_element['seqlen'],int):
            seqlen_values_list.append(data_element['seqlen'])
        else:
             print("Invalid value for seqlen " + str(data_element['seqlen']))
    return(seqlen_values_list)

def wrap_up_all_seqlen_values_into_a_list(all_json_files):
    """ function to iterate through all the json files and return a single consolidated list """
    all_seqlen_values_list = []
    for json_file in all_json_files:
        #print("Processing " + json_file)
        json_data = ingest_json_file(json_file)
        all_seqlen_values_list.extend(obtain_seqlen_value(json_data))
    return(all_seqlen_values_list)

def calculate_total_for_all_seqlen_values(all_seqlen_value_list):
    """ function to total all seqlen values """
    seqlen_total = sum(all_seqlen_value_list)
    print("seqlen value total: " + str(seqlen_total))


if __name__ == "__main__":
    args = process_argument()
    confirm_folder_exists(args.folder)
    all_json_files_list = create_list_of_json_files_from_folder(args.folder)
    all_seqlen_values_list = wrap_up_all_seqlen_values_into_a_list(all_json_files_list)
    calculate_total_for_all_seqlen_values(all_seqlen_values_list)

    


    