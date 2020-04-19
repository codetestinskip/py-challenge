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
import py_challenge
#from py_challenge import process_argument
#from py_challenge import confirm_folder_exists
#from py_challenge import create_list_of_json_files_from_folder
#from py_challenge import ingest_json_file
#from py_challenge import obtain_seqlen_value
#from py_challenge import wrap_up_all_seqlen_values_into_a_list
#from py_challenge import calculate_total_for_all_seqlen_values

class PyChallengeTestCase(unittest.TestCase):
    """Test py_challenge.py"""
    def test_process_argument(self):
        """Test arguments parser accepts folder name"""
        parser_args = py_challenge.process_argument(['data'])
        self.assertEqual(parser_args.folder,'data')

    def test_confirm_folder_exists(self):
        """Test whether a folder does not exist"""
        folder_exists = py_challenge.confirm_folder_exists('tmp_folder')
        self.assertFalse(folder_exists)

    def test_create_list_of_json_files_from_folder(self):
        """Test to list all json files in a folder"""
        list_of_json_files = py_challenge.create_list_of_json_files_from_folder('data')
        self.assertEqual(list_of_json_files,['data/split_ac.fastq.data.json', 'data/split_ab.fastq.data.json', 'data/split_ae.fastq.data.json', 'data/split_aa.fastq.data.json', 'data/split_ad.fastq.data.json'])

    def test_ingest_json_file(self):
        """Test if json files are ingested"""
        ingested_json = py_challenge.ingest_json_file('data/split_ac.fastq.data.json')
        self.assertNotEqual(ingested_json, None)

    def test_obtain_seqlen_value(self):
        """Test if seqlen values are valid"""
        json_value = py_challenge.obtain_seqlen_value([{'seqlen': 4173}],'seqlen')
        self.assertEqual(json_value, [4173])

    def wrap_up_all_seqlen_values_into_a_list(self):
        """Test putting seqlen into a list"""
        seqlen_list = py_challenge.obtain_seqlen_value('data/split_ac.fastq.data.json', 'data/split_ab.fastq.data.json', 'data/split_ae.fastq.data.json', 'data/split_aa.fastq.data.json', 'data/split_ad.fastq.data.json','seqlen')
        self.assertNotEqual(ingested_json, None)

    def calculate_total_for_all_seqlen_values(self):
        """Test calculating the seqlen values"""
        calculated_value = py_challenge.calculate_total_for_all_seqlen_values([1,2,3,4,5])
        self.assertEqual(calculated_value, 15)

if __name__ == '__main__':
    unittest.main()
