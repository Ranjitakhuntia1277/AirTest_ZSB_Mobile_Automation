import sys

import pytest
import os
# import sys
# sys.path.append(r'C:\Users\rk1277\Desktop\ZSB_Automation')

"""""""""""""""""PreConditions-: Printer should be added to these 2 accounts. 
1.Gmail Account-: zebra21.dvt@gmail.com//Swdvt@#123
2.Zebra Email Account-: Zebra01.swdvt@icloud.com//Testing@12345
3.FaceBook Email Account-: username - zebra03.swdvt@gmail.com//Zebra#123456789""""""
4. Microsoft OneDrive Account-: swdvt.zebra@outlook.com///Swdvt@123
# #####"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Notification.py --html=reports/report_test_APS_Notification.py.html --self-contained-html"
a = os.system(cmd)

cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Printing.py --html=reports/report_test_APS_Printing.py.html --self-contained-html"
a = os.system(cmd)

cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Settings_And_APS_Others.py --html=reports/report_test_APS_Settings_And_APS_Others.py.html --self-contained-html"
a = os.system(cmd)

cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Print_Preview_Options.py --html=reports/report_test_APS_Print_Preview_Options.py.html --self-contained-html"
a = os.system(cmd)

cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_APS_Testcases && pytest test_APS_Printer_Discover.py --html=reports/report_test_APS_Printer_Discover.py.html --self-contained-html"
a = os.system(cmd)

cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_App_Settings && pytest test_Android_App_Settings.py --html=reports/report_test_Android_App_Settings.py.html --self-contained-html"
a = os.system(cmd)
# #
cmd = "cd C:\\Users\\rk1277\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_PDF_Printing && pytest test_Android_PDF_Printing.py --html=reports/report_test_Android_PDF_Printing.py.html --self-contained-html"
a = os.system(cmd)
