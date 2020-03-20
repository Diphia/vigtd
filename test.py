#!/usr/bin/python3
# test.py
# diphia@2020
# This script is used to 

from task_object import task

if __name__=="__main__":
    temp_task = task('task1','TODO','2020-03-21')
    print(temp_task.get_offset_day())
