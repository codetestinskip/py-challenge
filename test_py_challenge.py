#
# Author: M.Inskip
# Date: 2018-04-18
# Version 0.1
#
# Python version 3.7.3
#
# Execute the script: python test_py_challenge.py
#
# Script to test py_challenge.py
#
# Please amend Python reference as appropriate

# modules imports

import unittest
from py_challenge import process_argument
from py_challenge import confirm_folder_exists
from py_challenge import create_list_of_json_files_from_folder
from py_challenge import ingest_json_file

class PyChallengeTestCase(unittest.TestCase):
    """Test py_challenge.py"""
    def test_process_argument(self):
        """Test arguments parser accepts folder name"""
        parser_args = process_argument(['data'])
        self.assertEqual(parser_args.folder,'data')

    def test_confirm_folder_exists(self):
        """Test whether a folder does not exist"""
        folder_exists = confirm_folder_exists('tmp_folder')
        self.assertFalse(folder_exists)

    def test_create_list_of_json_files_from_folder(self):
        """Test to list all json files in a folder"""
        list_of_json_files = create_list_of_json_files_from_folder('data')
        self.assertEqual(list_of_json_files,['data/split_ac.fastq.data.json', 'data/split_ab.fastq.data.json', 'data/split_ae.fastq.data.json', 'data/split_aa.fastq.data.json', 'data/split_ad.fastq.data.json'])

    def test_ingest_json_file(self):
        """Test to list all json files in a folder"""
        ingested_json = ingest_json_file('data/split_ac.fastq.data.json')
        self.assertNotEqual(ingested_json, None)

if __name__ == '__main__':
    unittest.main()
