import pytest
import os

# Define the paths to your test files
# Loop through the test files and run each one

cmd = "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Help && pytest test_Help_Android.py"
a = os.system(cmd)

cmd = "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Printer_Management && pytest test_Printer_Management.py"
a = os.system(cmd)

cmd = "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Registration && pytest test_Registration_Android.py"
# Run the combined command
a = os.system(cmd)

cmd = "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Template_Management_JK && pytest test_Template_Management_Android_JK.py"
a = os.system(cmd)

cmd = "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Data_Sources && pytest test_Data_Sources_Android.py"
a = os.system(cmd)


