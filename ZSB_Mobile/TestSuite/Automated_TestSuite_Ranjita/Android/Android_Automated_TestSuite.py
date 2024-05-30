import sys

import pytest
import os
# import sys
# sys.path.append(r'C:\Users\rk1277\Desktop\ZSB_Automation')

"""""""""""""""""PreConditions-: Printer should be added to these 2 accounts. 
1.Gmail Account-: zebra21.dvt@gmail.com//Swdvt@#123
2.Zebra Email Account-: Zebra01.swdvt@icloud.com//Testing@12345"""""""""""""""""




cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Notification.py --html=reports/report_test_APS_Notification.py.html"
a = os.system(cmd)

cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Printing.py --html=reports/report_test_APS_Printing.py.html"
a = os.system(cmd)

cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Settings_And_APS_Others.py --html=reports/report_test_APS_Settings_And_APS_Others.py.html"
a = os.system(cmd)

cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Print_Preview_Options.py --html=reports/report_test_APS_Print_Preview_Options.py.html"
a = os.system(cmd)

cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Printer_Discover.py --html=reports/report_test_APS_Printer_Discover.py.html"
a = os.system(cmd)

cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_App_Settings && pytest test_Android_App_Settings.py --html=reports/report_test_Android_App_Settings.py.html"
a = os.system(cmd)
# #
cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Smoke_Test && pytest test_Android_Smoke_Test.py --html=reports/report_test_Android_Smoke_Test.py.html"
a = os.system(cmd)
