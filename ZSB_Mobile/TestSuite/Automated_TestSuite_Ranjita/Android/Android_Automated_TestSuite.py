import pytest
import os

# Define the paths to your test files
# Loop through the test files and run each one

cmd = "cd C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APP_Settings && pytest test_Android_App_Settings.py"
# Run the combined command
a = os.system(cmd)

# cmd = "cd C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Smoke_Test && pytest test_Android_Smoke_Test.py --html=reports/report.html"
# a = os.system(cmd)

# cmd = "cd C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Notification.py"
# a = os.system(cmd)
#
# cmd = "cd C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Printing.py"
# a = os.system(cmd)

# cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Settings_And_APS_Others.py"
# a = os.system(cmd)
#
# cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Printer_Discover.py"
# a = os.system(cmd)
#
# cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Print_Preview_Options.py"
# a = os.system(cmd)