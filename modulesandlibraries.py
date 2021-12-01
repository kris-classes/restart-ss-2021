# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:21:18 2021

@author: weenf
"""

import os

f1 = open("diary.txt", "r")
print(f1.read())
f1.close()

#opens a file/creates if non existant
f2 = open("diary2.txt", "w")
f2.write("writing in my diary file")
f2.close

#Gets the current working directory
wd = os.getcwd()
print(wd)
#lists the current directory
os.listdir()
#creates a new directory
os.mkdir("newfolder2")
os.listdir()
os.rmdir("newFolder2")
os.listdir()
os.getlogin()


#JSON
import json
dump = json.dumps([5, "this is a dump test"])
print(dump)
#Load function converts JSON string into python Dictionary
load = json.loads('["this is a load test"]')
print(load)