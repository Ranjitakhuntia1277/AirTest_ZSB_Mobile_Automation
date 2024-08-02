import pytest
import os

# Define the paths to your test files
# Loop through the test files and run each one


cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_App_Settings && pytest test_Android_App_Settings.py --html=reports/report_test_Android_App_Settings.py.html --self-contained-html"
a = os.system(cmd)

cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_Help && pytest test_Help_Android.py --html=report_test_Help.html --self-contained-html"
a = os.system(cmd)

cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_Printer_Management && pytest test_Printer_Management.py --html=report_test_Printer_Management.html --self-contained-html"
a = os.system(cmd)

cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_Registration && pytest test_Registration_Android.py --html=report_test_Registration.html --self-contained-html"
a = os.system(cmd)

cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_Delete_Account && pytest test_Delete_Account_Android.py --html=report_test_Delete_Account.html --self-contained-html"
a = os.system(cmd)

cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_Data_Sources && pytest test_Data_Sources_Android.py --html=report_test_Data_Sources.html --self-contained-html"
a = os.system(cmd)