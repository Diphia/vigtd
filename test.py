#!/usr/bin/python3
# test.py
# diphia@2020
# This script is used to 

import os

CONTEXT_LOC = os.environ['HOME']+'/.vigtd_context/'
test_file = CONTEXT_LOC + 'test.csv'

from utilities import remove_line_from_file

if __name__=="__main__":
    remove_line_from_file(test_file,6)
