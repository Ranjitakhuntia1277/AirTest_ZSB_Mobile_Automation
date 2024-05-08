#from poco import poco
import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ZSB_Mobile.PageObject.Others.Others import Others
from ZSB_Mobile.Common_Method import *
from ZSB_Mobile.PageObject.Social_Login.Social_Login import Social_Login
from ZSB_Mobile.PageObject.Others.api_call import *

import os

class test_Others():
    pass

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
#start_app("com.zebra.soho_app")
sleep(3.0)

login_page = Login_Screen(poco)
others = Others(poco)
common_method=Common_Method(poco)
social_login = Social_Login(poco)

execID = 926616

deviceDetails(execID,"Pixel 7 Pro","14.0.11")
insert_tool_version(execID,"2")


def test_Others_TestcaseID_47972():
    pass

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    try:
        common_method.wait_for_element_appearance_namematches("Open navigation menu")
    except:
        pass
    start_main(execID)
    start_execution_loop(execID)
    stepID = "47972"
    stepName = "Verify the Label Alignment Demo feature"
    initialize_cases_hierarchy(execID, "0,47972,Verify the Label Alignment Demo feature")

    start_set_up(execID, stepID, stepName)
    stepID = "0"
    stepTypeName = ""
    stepName =  "On a mobile device, from the menu click Printer Settings."
    ordinalNum = 1

    try:

        login_page.click_Menu_HamburgerICN()

        sleep(1)

        """ Select the Printer Settings """
        others.click_Printer_Settings()

        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)

    except:
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Fail", 0)

    stepID = "1"
    stepTypeName = ""
    stepName = "Select the printer under test and then select General."
    ordinalNum = 2

    try:
        others.swipe_left()
        """ Select a printer """
        others.select_first_printer()
        sleep(2)
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)
    except:
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Fail", 0)

    stepID = "2"
    stepTypeName = ""
    stepName = "Click on the i button next to the Feed on Cover Close text."
    ordinalNum = 3

    try:
        """ Click on the icon """
        others.click_icon()
        sleep(1)
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)
    except:
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Fail", 0)

    stepID = "3"
    stepTypeName = ""
    stepName = "Click on the Label Alignment Demo button."
    ordinalNum = 4

    try:
        """Click On the Demo video"""
        others.click_demo_video()
        sleep(5)
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)
    except:
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Fail", 0)

    stepID = "4"
    stepTypeName = ""
    stepName = "Once the video starts playing, click navigate through the video."
    ordinalNum = 5

    try:
        others.click_on_the_vedio_while_playing()
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)
    except:
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Fail", 0)

    stepID = "5"
    stepTypeName = ""
    stepName = "Click any area of mobile screen Check the video pop-up will be dismissed "
    ordinalNum = 6

    try:
        """Close The Demo Video"""
        others.close_demo_video()

        """Check if closed"""
        if not others.check_demo_video_closed():
            raise Exception("demo video not closed")
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)
    except:
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Fail", 0)

    start_cleanup(execID,0,"cleanup1")
    end_cleanup(execID,0)
    end_execution_loop(execID)
    end_main(execID,0)
    end_execution(execID)

def test_Others_TestcaseID_45874():
    pass

    stop_app("com.zebra.soho_app")
    start_app("com.zebra.soho_app")
    try:
        common_method.wait_for_element_appearance_namematches("Open navigation menu")
    except:
        pass
    start_main(execID)
    stepID = "45874"
    stepName = "Verify the Label Alignment Demo feature"

    initialize_cases_hierarchy(execID, "0,45874,Check the version number displays well on different OS")
    start_set_up(execID, stepID, stepName)

    expected_version_no = "1.4.5538"
    stepID = "5"
    stepTypeName = ""
    stepName = "Click on the Hamburger icon on the Home page"
    ordinalNum = 0

    try:
        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)
    except:
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Fail", 0)

    stepID = "5"
    stepTypeName = ""
    stepName = "Check the version number at the bottom is displayed completely, and same to the version number as the test version installed"
    ordinalNum = 1

    try:
        """get the version number of the current device"""
        actual_version_no = others.get_the_version_no()

        """If version number not same generate error"""
        if expected_version_no != actual_version_no:
            raise Exception("Version no did not match")
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Pass", 0)
    except:
        insert_step(execID, ordinalNum, stepID, stepTypeName, stepName, "Fail", 0)

    start_cleanup(execID, 1, "cleanup2")
    end_cleanup(execID, 0)
    end_main(execID, 0)
