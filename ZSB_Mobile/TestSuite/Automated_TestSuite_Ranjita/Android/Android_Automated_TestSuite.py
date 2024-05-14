import pytest
import os
# import sys
# sys.path.append(r'C:\Users\rk1277\Desktop\ZSB_Automation')


cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_App_Settings && pytest test_Android_App_Settings.py --html=reports/report_test_Android_App_Settings.py.html"
# Run the combined command
a = os.system(cmd)
#
# cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Smoke_Test && pytest test_Android_Smoke_Test.py"
# a = os.system(cmd)
#
# cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Notification.py"
# a = os.system(cmd)
#
# cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Printing.py"
# a = os.system(cmd)
#
# cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Settings_And_APS_Others.py"
# a = os.system(cmd)
#
# cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Printer_Discover.py"
# a = os.system(cmd)
#
# cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Print_Preview_Options.py"
# a = os.system(cmd)