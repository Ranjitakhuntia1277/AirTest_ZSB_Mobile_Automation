from ZSB_Mobile.PageObject.Others.api_call import *
execID = 926616

deviceDetails(execID,"Pixel 7 Pro","14.0.11")
insert_tool_version(execID,"2")

start_main(execID)
start_execution_loop(execID)
stepID = "47972"
stepName = "Verify the Label Alignment Demo feature"
# initialize_cases_hierarchy(execID, "0,47972,Verify the Label Alignment Demo feature")

start_set_up(execID, stepID, stepName)
start_set_up(execID, stepID, stepName)

stepID = "0"
stepTypeName = ""
stepName = "On a mobile device, from the menu click Printer Settings."
ordinalNum = 1

insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)

stepID = "1"
stepTypeName = ""
stepName = "Select the printer under test and then select General."
ordinalNum = 2


insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)


stepID = "2"
stepTypeName = ""
stepName = "Click on the i button next to the Feed on Cover Close text."
ordinalNum = 3


insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)


stepID = "3"
stepTypeName = ""
stepName = "Click on the Label Alignment Demo button."
ordinalNum = 4


insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)


stepID = "4"
stepTypeName = ""
stepName = "Once the video starts playing, click navigate through the video."
ordinalNum = 5

insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)

stepID = "5"
stepTypeName = ""
stepName = "Click any area of mobile screen Check the video pop-up will be dismissed "
ordinalNum = 6

insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)

start_cleanup(execID,0,"cleanup1")
end_cleanup(execID,0)
end_execution_loop(execID)
end_main(execID,0)
end_execution(execID)


start_main(execID)
stepID = "45874"
stepName = "Verify the Label Alignment Demo feature"

# initialize_cases_hierarchy(execID, "1,45874,Check the version number displays well on different OS")
start_set_up(execID, stepID, stepName)

expected_version_no = "1.4.5538"
stepID = "5"
stepTypeName = ""
stepName = "Click on the Hamburger icon on the Home page"
ordinalNum = 0
insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)

stepID = "5"
stepTypeName = ""
stepName = "Check the version number at the bottom is displayed completely, and same to the version number as the test version installed"
ordinalNum = 1

insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)

start_cleanup(execID, 1, "cleanup2")
end_cleanup(execID, 0)
end_main(execID, 0)

















