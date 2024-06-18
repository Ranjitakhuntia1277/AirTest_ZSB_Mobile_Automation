from ZSB_Mobile.TestSuite.api_call import *
execID = 935943

deviceDetails(execID, "Pixel 7 Pro", "testing")
insert_tool_version(execID, "2")


start_execution_loop(execID)

initialize_cases_hierarchy(execID, "0,458,Registration"
                                   "|458,45855,Verify create a brand  "
                                   "|458,45859,Verify sign in with "
                                   "|458,45860,Verify sign in as "
                                   "|458,45861,Verify sign in sign out with "
                                   "|458,45863,Verify sign in sign out with "
                                   "|458,45868,Verify reset password "
                                   "|458,45869,Verify Order Model "
                                   "|458,45862,Verify sign in sign out "
                                   "|458,45877,Verify create a brand new ")

# initialize_cases_hierarchy(execID, "0,47972,Verify the Label Alignment Demo feature"
#                                    "|47972,47973,Verify the Printer Demo feature"
#                                    "|0,45678,sample1"
#                                    "|45678,45789,sample2"
#                                    "|0,46897,outer sample")


print("ok")



