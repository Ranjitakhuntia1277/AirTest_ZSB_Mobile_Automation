import os
import pytest
from bs4 import BeautifulSoup

# Define the paths to your test files
# test_files = [
#     "C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Template_Management\\test_Android_Template_Management_Exec.py",
#     "C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Social_Login\\test_Android_Social_Login_Exec.py"
# ]
#
# for index, test_file in enumerate(test_files, start=1):
#     html_report_filename = f"report_test_{index}.html"
#     pytest.main([test_file, f"--html={html_report_filename}", "--self-contained-html"])


cmd = "cd C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Template_Management && pytest test_Android_Template_Management_Exec.py"
# Run the combined command
a = os.system(cmd)





