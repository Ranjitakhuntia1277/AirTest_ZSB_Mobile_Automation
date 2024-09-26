import pytest
import subprocess
import json
import os

import sys
from api_calls import *

args = sys.argv[1:]

# Filter arguments that start with a hyphen
hyphen_args = [arg.lstrip('-') for arg in args if arg.startswith('-')]

# Print the filtered arguments
print("Arguments starting with a hyphen:", hyphen_args)

generated_list_json = json.dumps(hyphen_args)

# Call the second script with the JSON string as an argument
subprocess.run(['python', '../../left_and_exec_id.py', generated_list_json])

hm={
"Template_Management":"cd C:\\Users\\tr5927\\Desktop\\ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Template_Management && pytest test_Android_Template_Management_Exec.py",
"Social Login" : "cd C:\\Users\\JD4936\\Documents\\New_ZSB_Automation\\ZSB_Mobile\\TestExecution\\test_Social_Login && pytest test_Android_Social_Login_Exec.py",
}

from ...store import *

start_execution_loop(execID)

for cmd in hyphen_args:
    if cmd in hm:
        print(hm[cmd])
        a = os.system(cmd)

if len(hyphen_args) == 0:
    for key, value in hm.items():
        print(value)
        os.system(value)

end_execution_loop(execID)




# ###""""""""""""With AEMS Report""""""""""""""""""""""""""""""""""""""""""""""""""""""