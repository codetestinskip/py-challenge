#
# Author: M.Inskip
# Date: 2018-04-18
# Version 0.1
#
# Python version 3.7.3
#
# Execute the script: python py_challenge.py
#
# Please amend Python reference as appropriate

# Import required libraries
#
import json
import argparse
import os
import sys


# Function definitions
#
def process_argument(args):
    """function to generate arguments including folder argument"""
    parser = argparse.ArgumentParser(
        prog='python py_challenge.py',
        description='''Python script utility that finds a total of `seqlen`
        values in all files matching `*.data.json` pattern that are found in a given folder'''
        )
    parser.add_argument('folder')
    return parser.parse_args(args)

def confirm_folder_exists(folder):
    """function to check existence of a folder"""
    if not os.path.exists(folder):
        print("Specified folder does not appear to exist in the current path")
        exit

def create_list_of_json_files_from_folder(folder):
    """function to list all json files in the folder"""
    json_file_full_path = []
    for file_name in os.listdir(folder):
        if file_name.endswith(".data.json"):
            json_file_full_path.append(os.path.join(folder, file_name))

    return json_file_full_path

def ingest_json_file(json_file_name):
    """function to ingest json file"""
    with open(json_file_name, 'r') as file:
        json_data = [json.loads(line) for line in file]
    #json_data = [json.loads(line) for line in open(json_file_name, 'r')]
    return json_data

def obtain_seqlen_value(json_data, element):
    """function to iterate through json data to identify seqlen value"""
    seqlen_values_list = []
    for data_element in json_data:
        if isinstance(data_element[element], int):
            seqlen_values_list.append(data_element[element])
        else:
            print("Invalid value for seqlen " + str(data_element[element]))
    return seqlen_values_list

def wrap_up_all_seqlen_values_into_a_list(all_json_files, element):
    """function to iterate through all the json files and return a single consolidated list"""
    all_seqlen_values_list = []
    for json_file in all_json_files:
        json_data = ingest_json_file(json_file)
        all_seqlen_values_list.extend(obtain_seqlen_value(json_data, element))
    return all_seqlen_values_list

def calculate_total_for_all_seqlen_values(all_seqlen_value_list):
    """function to total all seqlen values"""
    seqlen_total = sum(all_seqlen_value_list)
    print("seqlen value total: " + str(seqlen_total))


if __name__ == "__main__":
    ARGS = process_argument(sys.argv[1:])
    confirm_folder_exists(ARGS.folder)
    ALL_JSON_FILES_LIST = create_list_of_json_files_from_folder(ARGS.folder)
    ALL_SEQLEN_VALUES_LIST = wrap_up_all_seqlen_values_into_a_list(ALL_JSON_FILES_LIST, "seqlen")
    calculate_total_for_all_seqlen_values(ALL_SEQLEN_VALUES_LIST)
