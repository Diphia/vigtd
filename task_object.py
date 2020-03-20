#!/usr/bin/python3
# task_object.py
# diphia@2020
# This script is used to set the task object

import os
from datetime import date,datetime

class task(object):
    def __init__(self, name, tag, ddl):
        self.name = name
        self.tag = tag
        self.ddl = ddl
    def get_name(self):
        return self.name
    def get_tag(self):
        return self.tag
    def get_ddl(self):
        return self.ddl
    def get_offset_day(self):
        today = datetime.today().strftime("%Y-%m-%d")
        today_obj = datetime.strptime(today,"%Y-%m-%d")
        ddl_obj = datetime.strptime(self.ddl,"%Y-%m-%d")
        offset_obj = ddl_obj - today_obj
        offset = offset_obj.days
        return offset
