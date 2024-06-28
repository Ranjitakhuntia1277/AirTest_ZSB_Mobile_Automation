import pytest
import os

import sys

args = sys.argv[1:]

# Filter arguments that start with a hyphen
hyphen_args = [arg.lstrip('-') for arg in args if arg.startswith('-')]

# Print the filtered arguments
print("Arguments starting with a hyphen:", hyphen_args)

hm = {"Help" : "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Help && pytest test_Help_Android.py",
"Printer Management" : "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Printer_Management && pytest test_Printer_Management.py",
"Registration" : "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Registration && pytest test_Registration_Android.py",
"Data Sources" : "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Data_Sources && pytest test_Data_Sources_Android.py",
"Delete Account" : "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Delete_Account && pytest test_Delete_Account_Android.py"}


for cmd in hyphen_args:
    if cmd in hm:
        print(hm[cmd])
        a = os.system(cmd)

if len(hyphen_args)==0:
    for key,value in hm.items():
        print(value)
        os.system(value)



