import os
import pytest
# from bs4 import BeautifulSoup

"""zebratest850@gmail.com"""
"""Zebratest901@gmail.com"""
"""Zebra#123456789"""
"""Both accounts should have one printer each , 850account should have only 4 designs od 40611,12,13,14 and 901 should not have any design in mydesigns"""
# ####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_Template_Management && pytest test_Android_Template_Management_Exec.py --html=reports/report_test_Android_Template_Management_Exec.py.html --self-contained-html"
a = os.system(cmd)

cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_Social_Login && pytest test_Android_Social_Login_Exec.py --html=report_test_social_loginpy.html --self-contained-html"
a = os.system(cmd)

cmd = "cd /Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/TestExecution/test_Others && pytest test_Android_Others.py --html=report_test_others.html --self-contained-html"
a = os.system(cmd)