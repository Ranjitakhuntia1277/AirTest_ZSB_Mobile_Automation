import sys

import pytest
import os
import subprocess
import platform
# import sys
# sys.path.append(r'C:\Users\rk1277\Desktop\ZSB_Automation')

"""""""""""""""""PreConditions-: 
    zebratest850@gmail.com
    Zebratest901@gmail.com
    Zebra#123456789
    Both accounts should have one printer each , 850account should have only 4 designs od 40611,12,13,14 and 901 should not have any design in mydesigns
# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if platform.system() == "Windows":
    cmd = "cd C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Social_Login && pytest test_Android_Social_Login_Exec.py --html=report_test_social_loginpy.html --self-contained-html"
    a = os.system(cmd)

    cmd = "cd C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Others && pytest test_Android_Others.py --html=report_test_others.html --self-contained-html"
    a = os.system(cmd)

else:

    # cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_Template_Management && pytest test_Android_Template_Management_Exec.py --html=report_test_template_management_exec.html --self-contained-html"
    # a = os.system(cmd)

    cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_Social_Login && pytest test_Android_Social_Login_Exec.py --html=report_test_social_loginpy.html --self-contained-html"
    a = os.system(cmd)

    cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_Others && pytest test_Android_Others.py --html=report_test_others.html --self-contained-html"
    a = os.system(cmd)