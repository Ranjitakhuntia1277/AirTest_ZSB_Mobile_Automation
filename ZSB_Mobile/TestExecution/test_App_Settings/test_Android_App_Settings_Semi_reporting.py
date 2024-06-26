import inspect

from airtest.core.api import *
from compose import errors
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from setuptools import logging
from ...PageObject.Robofinger import test_robo_finger
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...TestSuite.api_call import *
from ...TestSuite.store import *


# logging.getLogger("airtest").setLevel(logging.ERROR)
# logging.getLogger("adb").setLevel(logging.ERROR)

class Android_App_Settings:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)

connect_device("Android:///")

"""""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
aps_notification = APS_Notification(poco)

"""""""""""""""""""""""Change Password part needs to be verified manually"""""""""""""""""""""""""""""


# #### bug id-SMBM-2773
def test_AppSettings_TestcaseID_47913():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Install the Zsb app and login with user id'],
        2: [2, 'Click on the add printer button'],
        3: [3, 'Once the Bluetooth pairing is done, select the available WIFI AP'],
        4: [4,
            'Once the WIFI connection is done and you get the "Registering your printer" message on mobile display, turn OFF the WIFI AP'],
        5: [5, 'Turn ON the WIFI AP after some time (approx. 2 min)'],
        6: [6,
            'Observe the printer registration process. Check printer registration should resume from the point when the network connection got dropped']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Install the Zsb app and login with user id
        start_time = time.time()

        """Verify ZSB app doesn't stuck in Printer registration process when there is a network drop."""""

        common_method.tearDown()
        # test_robo_finger()
        # sleep(6)
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        """"verify home text is displaying on the home screen"""
        app_settings_page.Home_text_is_present_on_homepage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click on the add printer button
        start_time = time.time()

        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on Add printer tab"""""
        add_a_printer_screen.click_Add_A_Printer()
        """"click on the start button"""
        add_a_printer_screen.click_Start_Button()
        login_page.click_Allow_ZSB_Series_Popup()
        add_a_printer_screen.Verify_Lets_Make_Sure_Text()
        add_a_printer_screen.Click_Next_Button()
        """"Verify searching for your printer text"""
        add_a_printer_screen.Verify_Searching_for_your_printer_Text()
        """"verify select your printer text"""
        add_a_printer_screen.Verify_Select_your_printer_Text()
        """"select 2nd printer which you want to add"""
        add_a_printer_screen.click_2nd_Printer_Details_To_Add()
        """""click on select button"""
        add_a_printer_screen.click_Select_Button_On_Select_Your_Printer_Screen()
        """"verify pairing your printer text"""
        add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
        """"accept Bluetooth pairing popup 1"""
        add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
        """"accept Bluetooth pairing popup 2"""
        add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
        """"verify pairing your printer text"""
        add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
        """"accept Bluetooth pairing popup 1"""
        add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
        """"accept Bluetooth pairing popup 2"""
        add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Once the Bluetooth pairing is done, select the available WIFI AP
        start_time = time.time()

        """Verify Connect Wi-fi Network Text"""
        add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
        """"click on connect button on connect wifi network screen"""
        add_a_printer_screen.click_Connect_Btn_On_Connect_Wifi_Network_Screen()
        add_a_printer_screen.click_Password_Field_On_Join_Network()
        add_a_printer_screen.click_Submit_Button_ON_Join_Network()
        """"verify need the printer driver text"""
        add_a_printer_screen.Verify_Need_the_Printer_Driver_Text()
        """""verify registering your printer text"""
        add_a_printer_screen.Verify_Registering_your_Printer_Text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Once the WIFI connection is done and you get the "Registering your printer" message on mobile display, turn OFF the WIFI AP
        start_time = time.time()

        """"Turn OFF the WIFI & Turn on again after some time (approx. 2 min)"""
        aps_notification.disable_wifi()
        sleep(120)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Turn ON the WIFI AP after some time (approx. 2 min)
        start_time = time.time()

        aps_notification.enable_wifi()
        sleep(7)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Observe the printer registration process. Check printer registration should resume from the point when the network connection got dropped
        start_time = time.time()

        """"click on finish setup button"""
        add_a_printer_screen.click_Finish_Setup_Button()
        """stop the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


####### bug id---SMBM-2778
def test_AppSettings_TestcaseID_50031():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Test user login mobile app'],
        2: [2, 'Click Print Settings > printer tab > General'],
        3: [3,
            'Click Test Print button. Check test label prints out successfully and a toast message shows up: "Test label printed successfully to <Printer name>"'],
        4: [4, 'Open printer header. Check printer current status is Cover Open'],
        5: [5, 'Click Test Print Button again']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Test user login mobile app
        start_time = time.time()

        """Check the error message prompted when print test page and printer head open or offline"""

        """printer should be online"""
        """start the app"""
        common_method.tearDown()
        sleep(3)
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify home text is displaying on the home screen"""
        app_settings_page.Home_text_is_present_on_homepage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click Print Settings > printer tab > General
        start_time = time.time()

        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on printer settings tab"""""
        app_settings_page.click_Printer_Settings()
        """"click on printer name on printer settings page"""
        app_settings_page.click_PrinterName_On_Printersettings()
        """verify printer name text"""
        app_settings_page.Verify_Printer_Name_Text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click Test Print button. Check test label prints out successfully and a toast message shows up: "Test label printed successfully to <Printer name>"
        start_time = time.time()

        """click test print button"""
        app_settings_page.click_Test_Print_Button()
        """""""POP UP FOR MANUAL INTERVENTION"""""""
        common_method.Show_popup_To_Verify_Printout_Manually()
        """"Verify Printed successfully text"""
        app_settings_page.Verify_Printed_Successfully_Text()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Open printer header. Check printer current status is Cover Open
        start_time = time.time()

        """"Open the printer cover manually"""
        """""""POP UP FOR MANUAL INTERVENTION"""""""
        common_method.Show_popup_To_Open_The_Printer_Cover_Manually()
        """click test print button"""
        app_settings_page.click_Test_Print_Button()
        """""verify error message of cover open"""
        app_settings_page.Verify_ErrorMessage_Text()
        """""Cover close on the printer manually"""""
        """""""POP UP FOR MANUAL INTERVENTION"""""""
        common_method.Show_popup_To_Close_The_Printer_Cover_Manually()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click Test Print Button again
        start_time = time.time()

        """"click on test print"""
        app_settings_page.click_Test_Print_Button()
        """"Verify Printed successfully text"""
        app_settings_page.Verify_Printed_Successfully_Text()
        """stop the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


## #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ###bug id-SMBM-2160
def test_AppSettings_TestcaseID_49709():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, "Sign in test account with printer added, go to Printer settings/Printer name/Wi-Fi tab"],
        2: [2, "Click Manage Networks option, pair Bluetooth if needed. Click Add Network option"],
        3: [3,
            'When the networks list displayed, click "Enter Network Manually" option, input the prepared network which name is long (Here it is "Test-EnterNetwork-Manually-NameDisplay", total 38 characters), input pw if needed then submit it. Check the added network in the list. Check the name is shown correctly and the delete button is able to click (Some characters maybe hidden, that\'s acceptable)'],
        4: [4, "Exit manage network and re-enter it. Check the added network is still displayed in the list."],
        5: [5, "Try to sort or delete the network. Check all functions work."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Sign in test account with printer added, go to Printer settings/Printer name/Wi-Fi tab
        start_time = time.time()

        """Manage network- Check able to manage network with long name"""

        """"printer should be online & wifi should be connected"""
        """start the app"""
        common_method.tearDown()
        """click on hamburger menu icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on printer settings"""
        app_settings_page.click_Printer_Settings()
        """"click on printer name on  printer settings"""
        app_settings_page.click_PrinterName_On_Printersettings()
        """click on wifi tab"""
        app_settings_page.click_wifi_tab()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click Manage Networks option, pair Bluetooth if needed. Click Add Network option
        start_time = time.time()

        app_settings_page.click_Manage_Networks_Btn()
        """""""""""""Click on continue button on the Bluetooth Connection required popup"""""""
        app_settings_page.accept_Continue_popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"""""""verify the continue button and click on that"""""
        app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()
        sleep(5)
        """"""""""Verify the Add Network text & button & click on that"""""""""""
        app_settings_page.click_Add_Network()
        sleep(3)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: When the networks list displayed, click "Enter Network Manually" option, input the prepared network which name is long...
        start_time = time.time()

        """""""""""""Verify Add network page is opening and verify the text"""""""
        app_settings_page.get_text_Add_Network()
        app_settings_page.click_Enter_Network_Manually()
        app_settings_page.click_Long_Network_UserName()
        app_settings_page.click_Join_Btn_On_Other_Network_Popup()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Exit manage network and re-enter it. Check the added network is still displayed in the list.
        start_time = time.time()

        app_settings_page.click_Continue_On_Failed_To_Connect_To_Wifi_Network()
        app_settings_page.Verify_Long_Network_UserName()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Try to sort or delete the network. Check all functions work.
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Printer_Settings()
        """"click on the red icon to delete the added network name"""
        app_settings_page.click_Red_Icon_to_remove_network()
        """stop the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


##"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ####bug id-SMBM-2163
def test_AppSettings_TestcaseID_49711():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Sign in test account with printer added and the printer is Online status (connected to a valid network already), go to Printer settings/Printer name/Wi-Fi tab. Check current connected Wi-Fi is correct."],
        2: [2,
            "Click Manage Networks option, pair Bluetooth if needed. Click Add Network option. Check the network Wi-Fi is shown correctly."],
        3: [3, "Select the network which cannot resolve the Zebra host. Check the network can be added to the list."],
        4: [4,
            "Sort the network to the first priority and apply the changes. Check there is a prompt message for the user which lets them know the network is invalid for the printer. Or, if there is no prompt message, check it will connect to the second priority network in 5 minutes."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Sign in test account with printer added and the printer is Online status (connected to a valid network already), go to Printer settings/Printer name/Wi-Fi tab. Check current connected Wi-Fi is correct.
        start_time = time.time()

        """Manage networks- Check there is a prompt message when applying to the network which can't resolve Zebra host"""

        """start the app"""
        common_method.tearDown()
        """click on hamburger menu icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on printer settings"""
        app_settings_page.click_Printer_Settings()
        """"click on printer name on  printer settings"""
        app_settings_page.click_PrinterName_On_Printersettings()
        """click on wifi tab"""
        app_settings_page.click_wifi_tab()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click Manage Networks option, pair Bluetooth if needed. Click Add Network option.
        start_time = time.time()

        app_settings_page.click_Manage_Networks_Btn()
        """"verify bluetooth connection required text"""
        app_settings_page.get_text_Bluetooth_connection_required_Txt()
        app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
        app_settings_page.click_Allow_Btn()
        app_settings_page.click_Add_Network()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Select the network which cannot resolve the Zebra host. Check the network can be added to the list.
        start_time = time.time()

        app_settings_page.click_Enter_Network_Manually()
        app_settings_page.click_Long_Network_UserName()
        app_settings_page.click_Join_Btn_On_Other_Network_Popup()
        app_settings_page.click_Continue_On_Failed_To_Connect_To_Wifi_Network()
        app_settings_page.Verify_Long_Network_UserName()
        app_settings_page.click_Apply_Chnages_Button()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Sort the network to the first priority and apply the changes. Check there is a prompt message...
        start_time = time.time()

        """""Currently there is no error message displaying so Couldnot automate, it is blocked due to SMBM-2163"""""""""""
        """"Verify The error message manually if it is displaying"""
        """""""POP UP FOR MANUAL INTERVENTION"""""""
        common_method.Show_popup_For_Error_Message_Manually()
        ### app_settings_page.Verify_The_Invalid_Network_Error_Message()
        """stop the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_50326():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            "Sign in test account, go to Printer settings/Printer name/Wi-fi tab. Check current connected Wi-Fi is correct."],
        2: [2, "Click Manage network, pair Bluetooth if needed. Check able to see the 'Add network' option."],
        3: [3,
            "Click on Add network button, select a network to add. Check the network is added successfully to the added network list."],
        4: [4, "Delete one of added networks. Check the deleted network is disappeared from the added network list."],
        5: [5,
            "Sort the network and exit manage network page, go to home page. Check the printer is online status. Check able to print test label."],
        6: [6,
            "Go to device's settings, disconnect the printer Bluetooth (Or use another device, sign in same user, make sure the printer is not paired then perform below steps)."],
        7: [7,
            "Back to ZSB Series, click manage network, pair Bluetooth if needed. Check the network is the top one sorted in step 5."],
        8: [8, "Repeat step 3 to 5. Check all steps work."]
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Sign in test account, go to Printer settings/Printer name/Wi-fi tab. Check current connected Wi-Fi is correct.
        start_time = time.time()

        """Manage Network- Check able to add/delete/sort network when printer bt paired/unpaired in device""""""

        """"App should be in logged in condition & printer should be added """"
        """"""connect with Another wifi Network except NESTWIFI"""

        """"start the app"""
        common_method.tearDown()
        """"click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Printer_Settings()
        app_settings_page.click_PrinterName_On_Printersettings()
        app_settings_page.click_wifi_tab()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click Manage network, pair Bluetooth if needed. Check able to see the 'Add network' option.
        start_time = time.time()

        app_settings_page.click_Manage_Networks_Btn()
        app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Required()
        """"accept Bluetooth pairing popup 1"""
        add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
        """"accept Bluetooth pairing popup 2"""
        add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
        """"accept Bluetooth pairing popup 1"""
        add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
        """"accept Bluetooth pairing popup 2"""
        add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click on Add network button, select a network to add. Check the network is added successfully to the added network list.
        start_time = time.time()

        app_settings_page.click_Add_Network()
        app_settings_page.click_ZEBRA_Network()
        app_settings_page.click_Network_Password_Field()
        app_settings_page.click_Network_Submit_Btn()
        app_settings_page.Verify_NestWIFI_Network_Name_In_Network_List()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Delete one of added networks. Check the deleted network is disappeared from the added network list.
        start_time = time.time()

        app_settings_page.click_Red_Icon_to_remove_network()
        app_settings_page.Verify_NestWIFI_In_Network_List()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Sort the network and exit manage network page, go to home page. Check the printer is online status. Check able to print test label.
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Home_Tab()
        app_settings_page.Verify_Printer_is_already_added()
        """stop the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Go to device's settings, disconnect the printer Bluetooth (Or use another device, sign in same user, make sure the printer is not paired then perform below steps).
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Back to ZSB Series, click manage network, pair Bluetooth if needed. Check the network is the top one sorted in step 5.
        start_time = time.time()

        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Repeat step 3 to 5. Check all steps work.
        start_time = time.time()

        sleep(20)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


#
# # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_AppSettings_TestcaseID_45688():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Click Printer Settings > select Printer Tab (E.g: ZSB-DP12) > Select Wi-Fi tab'],
        2: [2,
            'Check below options display on the tab: Current network, Network Status, IP Address. Manage Networks button should be enabled in blue. Under the Manage Networks button, there is a prompt message like "You can save up to 5 network profiles to your Saved networks. If no saved networks are available, you will have to add a new one."'],
        3: [3,
            'Click on Manage networks button. Check the "Bluetooth Connection Required" dialog pops up, with text: "You are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into "pairing mode" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices Bluetooth settings or power off the device."'],
        4: [4,
            'Finish the pair process if needed. Check after finishing, retrieve the My Saved Networks, and ensure the "Add Network" button at the bottom is displayed.'],
        5: [5,
            'Click the red icon to remove the current network. Check the network can be removed successfully and the "Add Network" button is enabled.'],
        6: [6,
            'Click Add Network button to add back the network. Check the previously deleted network can be added back.'],
        7: [7, 'Login to web portal and sign in with the same account.'],
        8: [8, 'Repeat Step 2 to go to Web Portal WiFi Settings.'],
        9: [9, 'Check it has the following message: "Wi-Fi networks can only be managed via the ZSB app."'],
        10: [10, 'Check below options display on Web portal: Current Network, Network Status, IP Address.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Click Printer Settings > select Printer Tab (E.g: ZSB-DP12) > Select Wi-Fi tab
        start_time = time.time()

        """""""""Verify Wifi Settings"""""

        """""Install the latest production app on the phone & printer should be added and it should be connected to wifi"""""""""
        """""""""Create the object for Login page & Common_Method page to reuse the methods"""""""""""
        #
        # :
        """""Check whether App is installed or not"""
        common_method.tearDown()
        """" Allow pop up before login for the fresh installation"""""
        login_page.click_LoginAllow_Popup()
        """""for the first installation click on the zsb series popup"""
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Menu_HamburgerICN()
        """""click on the printer settings tab"""
        app_settings_page.click_Printer_Settings()
        """""click on the printer tab"""
        app_settings_page.click_PrinterName_On_Printersettings()
        app_settings_page.click_General_Tab()
        """"Verify the Test print button text & tab"""
        app_settings_page.Test_Print_button_is_present_on_printer_settings_page()
        """""""""" click on the wifi tab option"""""""""""

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check below options display on the tab: Current network, Network Status, IP Address. Manage Networks button should be enabled in blue. Under the Manage Networks button, there is a prompt message like "You can save up to 5 network profiles to your Saved networks. If no saved networks are available, you will have to add a new one."
        start_time = time.time()

        app_settings_page.click_wifi_tab()
        """""""""validate the Current network text"""""
        app_settings_page.test_CurrentNetwork_Txt_is_present_on_printer_settings_page()
        """""""Validate the Network status text is present on the printer settings screen"""""""
        app_settings_page.test_Network_Status_Txt_is_present_on_printer_settings_page()
        """"validate network status result text on the printer settings screen"""
        app_settings_page.get_text_Network_Status_Result_Txt()
        """"""""" Verify IP address text is present on the printer settings screen"""""""""
        app_settings_page.get_text_IPAddress_Txt()
        """""""""Verify the message You can save upto 5 network profiles to your saved networks after Manage Networks"""
        app_settings_page.IS_Present_Save_Network_Message_Txt()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Click on Manage networks button. Check the "Bluetooth Connection Required" dialog pops up, with text: "You are about to connect to the printer using Bluetooth..."
        start_time = time.time()

        """""""verify manage networks text is present & clickable"""""""
        app_settings_page.click_Manage_Networks_Btn()
        """""""""""""Click on continue button on the Bluetooth Connection required popup"""""""
        app_settings_page.accept_Continue_popup()
        login_page.click_Allow_ZSB_Series_Popup()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Finish the pair process if needed. Check after finishing, retrieve the My Saved Networks, and ensure the "Add Network" button at the bottom is displayed.
        start_time = time.time()

        """""""""Verify the Cancel button on the Bluetooth_Connection_Failed_Popup"""""
        app_settings_page.Cancel_is_present_on_Bluetooth_Connection_Failed_Popup()
        """"""""""verify the continue button and click on that"""""
        app_settings_page.click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Click the red icon to remove the current network. Check the network can be removed successfully and the "Add Network" button is enabled.
        start_time = time.time()

        """"""""""Verify the red remove icon next to the network name"""""
        app_settings_page.click_Red_Icon_to_remove_network()
        sleep(5)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Click Add Network button to add back the network. Check the previously deleted network can be added back.
        start_time = time.time()

        """"""""""Verify the Add Network text & button & click on that"""""""""""
        app_settings_page.click_Add_Network()
        sleep(3)
        """""""""""""Verify Add network page is opening and verify the text"""""""
        app_settings_page.get_text_Add_Network()
        app_settings_page.click_Enter_Network_Manually()
        app_settings_page.click_Network_UserName()
        app_settings_page.click_Join_Btn_On_Other_Network_Popup()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Login to web portal and sign in with the same account.
        start_time = time.time()

        """""test case 7 to 10 need to check on Web portal manually"""
        """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
        common_method.Show_popup_For_Web_Portal_Verification_Manually()
        """stop the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Repeat Step 2 to go to Web Portal WiFi Settings.
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 9: Check it has the following message: "Wi-Fi networks can only be managed via the ZSB app."
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 10: Check below options display on Web portal: Current Network, Network Status, IP Address.
        start_time = time.time()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45876():
    """	Check basic functions work well after upgrading"""

    """"Setup:
    1. The previous version has already been installed in test device
    2. Sign in the test account, with 1 printer added
    3. There is at least one design in My designs"""""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            'APK upgrade install (Android) or Test Flight upgrade install (iOS) the latest build\nCheck that the app should be installed/updated to the latest build successfully\n(SMBM-2179,SMBM-1884)Check the user account of setup 2 is keep logged in'],
        2: [2, 'Check that the printer is still associated to this account'],
        3: [3, 'Go to My designs, select any design to print\nCheck the label can be printed out successfully'],
        4: [4, 'Go to Common designs, select any designs to print\nCheck the label can be printed out successfully'],
        5: [5, 'Go to Printer Settings, update printer\'s name\nCheck printer name can be updated successfully'],
        6: [6,
            'Open any PDF file, then share to ZSB Series, print the file\nCheck the file can be printed out successfully'],
        7: [7, 'Open printer cover\nCheck the status on home page is shown as "Cover Open"'],
        8: [8, 'Close the printer cover\nCheck the status back to "Online"']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block

    try:
        # Step 1: APK upgrade install (Android) or Test Flight upgrade install (iOS) the latest build
        # Check that the app should be installed/updated to the latest build successfully
        # (SMBM-2179, SMBM-1884) Check the user account of setup 2 is keep logged in
        start_time = time.time()

        """start the app"""""
        common_method.tearDown()
        common_method.Stop_The_App()
        # ##common_method.uninstall_app()
        # ##common_method.install_Older_app()
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        common_method.Stop_The_App()
        common_method.Start_The_App()
        app_settings_page.Home_text_is_present_on_homepage()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Check that the printer is still associated to this account
        start_time = time.time()

        """""""Verify the Already added Printer"""
        app_settings_page.Verify_Printer_is_already_added()
        common_method.Stop_The_App()
        #### common_method.uninstall_app()
        # ####common_method.install_app()
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        common_method.Stop_The_App()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        app_settings_page.Home_text_is_present_on_homepage()
        app_settings_page.Verify_Printer_is_already_added()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Go to My designs, select any design to print
        # Check the label can be printed out successfully
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_My_Design()
        add_a_printer_screen.click_FirstOne_In_MyDesign()
        add_a_printer_screen.click_Print_Option()
        add_a_printer_screen.click_Print_Button()
        """"Verify manually it should print successfully"""
        add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Go to Common designs, select any designs to print
        # Check the label can be printed out successfully
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        add_a_printer_screen.click_Common_Design_Tab()
        add_a_printer_screen.click_FirstOne_Design_In_Common_Design()
        add_a_printer_screen.click_FirstOne_In_Common_Design()
        add_a_printer_screen.click_Print_Option()
        add_a_printer_screen.click_Print_Button()
        add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()
        add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 5: Go to Printer Settings, update printer's name
        # Check printer name can be updated successfully
        start_time = time.time()

        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_Printer_Settings()
        app_settings_page.click_PrinterName_On_Printersettings()
        app_settings_page.click_Printer_Name_Text_Field()
        app_settings_page.Update_PrinterName_With_Different_Valid_Name()
        app_settings_page.verify_Printer_Name_Updated_Message()
        app_settings_page.click_Printer_Name_Text_Field()
        app_settings_page.Update_PrinterName()
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 6: Open any PDF file, then share to ZSB Series, print the file
        # Check the file can be printed out successfully
        start_time = time.time()

        aps_notification.Stop_Android_App()
        aps_notification.click_Mobile_SearchBar()
        aps_notification.click_On_Searchbar2()
        aps_notification.Enter_Files_Text_On_SearchBar()
        aps_notification.click_Files_Folder()
        aps_notification.click_Drive_Searchbar()
        aps_notification.click_Drive_Searchbar2()
        aps_notification.click_PDF_File_From_The_List()
        aps_notification.click_Suggestion_PDF_File()
        aps_notification.click_PDF_ON_Result()
        aps_notification.click_ON_Three_Dot()
        aps_notification.click_Print_Option()
        aps_notification.Verify_Print_Review_Page()
        aps_notification.click_Save_AS_PDF()
        aps_notification.click_All_Printers()
        aps_notification.Verify_Print_job_sent_successfully_Message()
        aps_notification.Stop_Android_App()
        common_method.Start_The_App()
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 7: Open printer cover
        # Check the status on home page is shown as "Cover Open"
        start_time = time.time()

        """""The below steps need to be verified manually""""""""""""""
            7. Open printer cover
            """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
        common_method.Show_popup_To_Open_The_Printer_Cover_Manually()
        """Check the status on home page is shown as "Cover Open"""""
        aps_notification.Verify_Printer_Status_AS_HeadOpen()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 8: Close the printer cover
        # Check the status back to "Online"
        start_time = time.time()

        """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
        common_method.Show_popup_To_Close_The_Printer_Cover_Manually()
        aps_notification.Verify_Printer_Status_Is_Present()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


#     ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45901():
    """Update Auto label feed setting(disable), check setting sync in mobile and web portal, open and close printer cover, then print a test label"""
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Mobile App with test user.'],
        2: [2,
            'Click "Printer Settings" in the left menu, select a Printer, and the Printer Settings page General tab opened.'],
        3: [3,
            'Update "Auto Label Feed on Printer Cover Close" value (make sure all the following test steps are covered)'],
        4: [4, 'Login WebPortal with the same account.'],
        5: [5,
            'Open printer setting > printer > general tab, check the Feed On Head Close value will sync to Web Portal.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1  # Initialize stepId before the try-except block

    try:
        # Step 1: Login Mobile App with test user
        start_time = time.time()

        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify printer is already added"""
        app_settings_page.Verify_Printer_is_already_added()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Click "Printer Settings" in the left menu, select a Printer, and the Printer Settings page General tab opened
        start_time = time.time()

        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on Printer settings tab"""
        app_settings_page.click_Printer_Settings()
        """"click on printer name on the printer settings page"""
        app_settings_page.click_PrinterName_On_Printersettings()
        """verify general tab text"""
        app_settings_page.Verify_General_Tab_Text()
        """"verify printer name text"""
        app_settings_page.Verify_Printer_Name_Text()
        """verify darkness level bar is present & change the darkness level"""
        app_settings_page.Verify_Darkness_Level_Bar()
        """"change the darkness level"""
        app_settings_page.Change_Darkness_Level_Bar()
        """verify the darkness updated message"""
        app_settings_page.Verify_Darkness_Updated_Message()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Update "Auto Label Feed on Printer Cover Close" value and perform subsequent checks
        start_time = time.time()

        """Verify auto Label Feed On Printer Cover Close value enable/disable option"""
        app_settings_page.Check_toggle_button()
        """click on the toggle button"""
        app_settings_page.click_toggle_button()
        """stop the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Login WebPortal with the same account
        start_time = time.time()

        """""""web portal part needs to be verified Manually"""""""
        """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
        common_method.Show_popup_For_Web_Portal_Verification_Manually()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

        # Step 5: Open printer setting > printer > general tab, check the Feed On Head Close value will sync to Web Portal
        start_time = time.time()

        sleep(10)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass", exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


# ## #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def test_Smoke_Test_TestcaseID_45882():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1,
            'Go to My Design, select design1 to print (Sign in One Drive if needed). Check the design preview loaded successfully.'],
        2: [2, 'Select several columns to print. Check the selected columns can be printed out correctly.'],
        3: [3, 'Back to My Designs, select design2 to print. Check the design preview loaded successfully.'],
        4: [4, 'Select several columns to print. Check the selected columns can be printed out correctly.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # Step 1: Go to My Design, select design1 to print. Check the design preview loaded successfully.
        start_time = time.time()

        """Verify sign in with non-Zebra account, check the design linked different format file from One Drive can be printed out successfully"""

        common_method.tearDown()
        common_method.Clear_App()
        common_method.Start_The_App()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_loginBtn()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        login_page.click_Loginwith_Google()
        login_page.Loginwith_Added_Email_Id()
        login_page.click_Menu_HamburgerICN()
        app_settings_page.click_My_Design()
        add_a_printer_screen.click_FirstOne_In_MyDesign()
        add_a_printer_screen.click_Print_Option()
        add_a_printer_screen.Verify_Design_Preview_Screen_With_Details()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 2: Select several columns to print. Check the selected columns can be printed out correctly.
        start_time = time.time()

        add_a_printer_screen.click_Print_Button()
        """"Verify manually it should print successfully"""
        """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
        common_method.Show_popup_To_Verify_Printout_Manually()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 3: Back to My Designs, select design2 to print. Check the design preview loaded successfully.
        start_time = time.time()

        add_a_printer_screen.click_The_Back_Icon_Of_Print_Review_Screen()
        add_a_printer_screen.click_SecondOne_In_MyDesign()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # Step 4: Select several columns to print. Check the selected columns can be printed out correctly.
        start_time = time.time()

        add_a_printer_screen.click_Print_Option()
        add_a_printer_screen.click_Print_Button()
        """"Verify manually it should print successfully"""
        """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
        common_method.Show_popup_To_Verify_Printout_Manually()
        common_method.Stop_The_App()
        """""The below step needs to be verified manually"""
        """"""""""2. Sign in the same account on Web portal, create design1, add text object, and link One Drive file with xlsx format. Create design2, add text object, and link One Drive file with csv format"""""""""
        """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
        common_method.Show_popup_For_Design_Verification_On_Web_Portal_Manually()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


# # ## """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# #f

def test_Smoke_Test_TestcaseID_45900():
    current_function_name = inspect.currentframe().f_code.co_name
    test_case_id = current_function_name.split("_")[-1]

    test_steps = {
        1: [1, 'Login Mobile App with test user.'],
        2: [2,
            'Click "Printer Settings" in the left menu, select a Printer, and open the Printer Settings page General tab.'],
        3: [3,
            'Update "Auto Label Feed on Printer Cover Close" value (make sure all the following test steps are covered). If "Auto Label Feed on Printer Cover Close" is Disable, switch the box to Enable. Check notification and toast show Printer settings have been updated. Open printer head and close printer head, check printer will auto feed one label. Open printer head and change another media, close printer head, printer will auto feed one label. Click on Test Print button, check test label is printed out.'],
        4: [4, 'Login WebPortal with the same account.'],
        5: [5,
            'Open printer setting > printer > general tab, check the Feed On Head Close value will sync to Web Portal.']
    }

    start_time_main = time.time()
    start_main(execID, leftId[test_case_id])

    stepId = 1

    try:
        # step 1: Login Mobile App with test user.
        start_time = time.time()

        """Update Auto label feed setting(enable), check setting sync in mobile and web portal, open and close printer cover, then print a test label"""

        """start the app"""
        common_method.tearDown()
        login_page.click_LoginAllow_Popup()
        login_page.click_Allow_ZSB_Series_Popup()
        """"verify printer is already added"""
        app_settings_page.Verify_Printer_is_already_added()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 2: Click "Printer Settings" in the left menu, select a Printer, and open the Printer Settings page General tab.
        start_time = time.time()

        """click on the hamburger icon"""
        login_page.click_Menu_HamburgerICN()
        """"click on Printer settings tab"""
        app_settings_page.click_Printer_Settings()
        """"click on printer name on the printer settings page"""
        app_settings_page.click_PrinterName_On_Printersettings()
        """verify general tab text"""
        app_settings_page.Verify_General_Tab_Text()
        """"verify printer name text"""
        app_settings_page.Verify_Printer_Name_Text()
        """verify darkness level bar is present & change the darkness level"""
        app_settings_page.Verify_Darkness_Level_Bar()
        """"change the darkness level"""
        app_settings_page.Change_Darkness_Level_Bar()
        """verify the darkness updated message"""
        app_settings_page.Verify_Darkness_Updated_Message()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 3: Update "Auto Label Feed on Printer Cover Close" value and perform related checks.
        start_time = time.time()

        """Verify auto Label Feed On Printer Cover Close value enable/disable option"""
        app_settings_page.Check_toggle_button()
        """click on the toggle button"""
        app_settings_page.click_toggle_button()
        """stop the app"""
        common_method.Stop_The_App()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 4: Login WebPortal with the same account.
        start_time = time.time()

        """""""web portal part needs to be verified Manually"""""""
        """""""POP UP FOR MANUAL INTERVENTION"""""""""""""""
        common_method.Show_popup_For_Darkness_Level_Verification_On_Web_Portal_Manually()

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

        # step 5: Open printer setting > printer > general tab, check the Feed On Head Close value will sync to Web Portal.
        start_time = time.time()

        sleep(8)

        exec_time = (time.time() - start_time) / 60
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
                    exec_time)
        stepId += 1

    except Exception as e:
        insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
        insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
        insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
        raise Exception(str(e))

    finally:
        exec_time = (time.time() - start_time_main) / 60
        end_main(execID, leftId[test_case_id], exec_time)


# # #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""Add printer"""


# def test_Smoke_Test_TestcaseID_45885():
#     """Add a printer- use a printer which has ever been registered before and require a decommission."""
#
#     """Step 1 needs to be verifiedManually """
#     """""1.Turn on the testing printer, wait about 1 min, use a toothpick to press the button on the printer back for about 30s to do a decommission
#     Check during this process, the power button is flashing yellow light and then white light, finally turn to blue flashing light and will auto feed the barcode info label. """
#
#     """"decommission the added printer and then execute"""
#     """start the app"""
#     common_method.tearDown()
#     login_page.click_LoginAllow_Popup()
#     login_page.click_Allow_ZSB_Series_Popup()
#     login_page.click_Menu_HamburgerICN()
#     add_a_printer_screen.click_Add_A_Printer()
#     """"click on the start button"""
#     add_a_printer_screen.click_Start_Button()
#     login_page.click_Allow_ZSB_Series_Popup()
#     add_a_printer_screen.Verify_Lets_Make_Sure_Text()
#     add_a_printer_screen.Click_Next_Button()
#     """"Verify searching for your printer text"""
#     add_a_printer_screen.Verify_Searching_for_your_printer_Text()
#     """"verify select your printer text"""
#     add_a_printer_screen.Verify_Select_your_printer_Text()
#     """"select 2nd printer which you want to add"""
#     add_a_printer_screen.click_2nd_Printer_Details_To_Add()
#     """""click on select button"""
#     add_a_printer_screen.click_Select_Button_On_Select_Your_Printer_Screen()
#     """"verify pairing your printer text"""
#     add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
#     """"verify pairing your printer text"""
#     add_a_printer_screen.Verify_Pairing_Your_Printer_Text()
#     """"accept Bluetooth pairing popup 1"""
#     add_a_printer_screen.Accept_Bluetooth_pairing_Popup1()
#     """"accept Bluetooth pairing popup 2"""
#     add_a_printer_screen.Accept_Bluetooth_pairing_Popup2()
#     """Verify Connect Wi-fi Network Text"""
#     add_a_printer_screen.Verify_Connect_Wifi_Network_Text()
#     """"click on connect button on connect wifi network screen"""
#     add_a_printer_screen.click_Connect_Btn_On_Connect_Wifi_Network_Screen()
#     add_a_printer_screen.click_Password_Field_On_Join_Network()
#     add_a_printer_screen.click_Submit_Button_ON_Join_Network()
#     """"verify need the printer driver text"""
#     add_a_printer_screen.Verify_Need_the_Printer_Driver_Text()
#     """""verify registering your printer text"""
#     add_a_printer_screen.Verify_Registering_your_Printer_Text()
#     """"click on finish setup button"""
#     add_a_printer_screen.click_Finish_Setup_Button()
#     common_method.Stop_The_App()
#     common_method.Start_The_App()
#     app_settings_page.Verify_Printer_is_already_added()
#     """stop the app"""
#     common_method.Stop_The_App()
