import pytest
import os

# Define the paths to your test files

# Loop through the test files and run each one




cmd = "cd C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Others && pytest test_Android_Others.py"

# Run the combined command
a = os.system(cmd)


cmd = "cd C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Template_Management && pytest test_Android_Template_Management_Exec.py"
a = os.system(cmd)


cmd = "cd C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Social_Login && pytest test_Android_Social_Login_Exec.py"

a = os.system(cmd)
