import sys

import pytest
import os
import subprocess
import platform
# import sys
# sys.path.append(r'C:\Users\rk1277\Desktop\ZSB_Automation')


"""""""""""""""""PreConditions-: Printer should be added to these 2 accounts. 
    run ------ python3 -m pip install pytz on terminal before executing
# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if platform.system() == "Windows":
    cmd = "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Help && pytest test_Help_Android.py --html=report_test_Help.html --self-contained-html"
    a = os.system(cmd)

    cmd = "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Printer_Management && pytest test_Printer_Management.py --html=report_test_Printer_Management.html --self-contained-html"
    a = os.system(cmd)

    cmd = "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Registration && pytest test_Registration_Android.py --html=report_test_Registration.html --self-contained-html"
    a = os.system(cmd)

    cmd = "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Delete_Account && pytest test_Delete_Account_Android.py --html=report_test_Delete_Account.html --self-contained-html"
    a = os.system(cmd)

    cmd = "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Data_Sources && pytest test_Data_Sources_Android.py --html=report_test_Data_Sources.html --self-contained-html"
    a = os.system(cmd)

else:
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