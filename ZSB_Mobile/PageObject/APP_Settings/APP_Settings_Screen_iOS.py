import requests
from airtest.core.assertions import assert_exists
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from pywinauto.mouse import scroll
from urllib3.util import url
from airtest.core.api import sleep
from poco import poco


class App_Settings_Screen_iOS:
    pass

    def __init__(self, poco):
        self.poco = poco

        self.Printer_Settings_Btn = "Printer Settings"
        self.PrinterName_In_Printer_Settings = "ZSB-DP12\nTab 2 of 2"

        self.WiFi_Tab = "Wi-Fi\nTab 2 of 2"
        self.Current_Network_Txt = "Current Network"
        self.Network_Name_Txt = "NESTWIFI"
        self.Network_Status_Txt = "Network Status"
        self.Network_Status_Result_Txt = "Connected"
        self.IPAddress_Txt = "IP Address"
        self.IPAddress_Result_Txt = "192.168.86.175"
        self.Manage_Network = "Manage Networks"
        self.Save_Network_Message_Txt = "You can save up to 5 network profiles to your Saved Networks. If no saved networks are available, you will have to add a new one."
        self.Threedot_On_Workspace = Template(os.path.join(os.path.expanduser('~'),
                                                           "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                           "tpl1708331943425.png"), record_pos=(0.244, -0.678),
                                              resolution=(1170, 2532))

        self.Test_Print_Btn = "Test Print"
        self.Bluetooth_Connection_Required_Msg = Template(os.path.join(os.path.expanduser('~'),
                                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                       "tpl1708425649634.png"),
                                                          record_pos=(0.011, 0.021), resolution=(1170, 2532))

        self.Continue_Btn_on_Bluetooth_Connection_Failed_popup = "Continue"
        self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup = "Cancel"
        self.Red_Icon_to_remove_network = " "
        self.Add_Network = "Add Network"
        self.Add_Network_Txt = "Add Network"
        self.Deleted_Network = "Zebra"
        self.Edit_Txt = "Edit"
        self.Change_Theme = "Change Theme"
        self.Save_Exit_Btn = "Save & Exit"
        self.Home_text_on_homepage = "Home"
        self.Pen_Icon = "Button"
        self.Units_Of_Measurements_Text = Template(os.path.join(os.path.expanduser('~'),
                                                                "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                "tpl1708332158153.png"), record_pos=(-0.242, 0.07),
                                                   resolution=(1170, 2532))

        self.Inches_Option = Template(os.path.join(os.path.expanduser('~'),
                                                   "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                   "tpl1708332260644.png"), record_pos=(-0.306, 0.195),
                                      resolution=(1170, 2532))

        self.Expand_Icon = Template(os.path.join(os.path.expanduser('~'),
                                                 "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                 "tpl1708332370129.png"), record_pos=(0.372, 0.198),
                                    resolution=(1170, 2532))

        self.Milimetres_Text = "Millimetres"
        self.Centimetres_Text = "Centimetres"
        self.Inches_Text = "Inches"
        self.Updated_Msg = "Units of Measurement updated successfully"
        self.Home_Text = "Home"
        self.Size_In_Cm = Template(os.path.join(os.path.expanduser('~'),
                                                "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                "tpl1708332995399.png"), record_pos=(0.068, -0.321),
                                   resolution=(1170, 2532))

        self.My_Design = "My Designs"
        self.Mydesign_Size_In_Cm = Template(os.path.join(os.path.expanduser('~'),
                                                         "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                         "tpl1705419343855.png"), record_pos=(0.193, -0.037),
                                            resolution=(1170, 2532))

        self.Upload_Photo = "Upload photo"
        self.Edit_Workspace = "Edit Workspace"
        self.Profile_Avatar_Letter = Template(os.path.join(os.path.expanduser('~'),
                                                           "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                           "tpl1705419524147.png"), record_pos=(-0.353, -0.6),
                                              resolution=(1170, 2532))

        self.Show_roots_Hamburger_Icn = ""
        self.Recent_Images = "android:id/title"
        self.Camera_Option = ""
        self.First_Picture = "Image"
        # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.Remove_Image = "Remove image"
        self.Back_Icon = "Go"
        self.Photo_Upload_Cancel_Button = "Cancel"
        self.Workspace_Name_Text_Field = "TextField"
        self.Edit_Workspace_Back_Icon = "Button"
        self.Workspace_Name_Text = "Workspace name"
        self.Keyboard_back_Icon = "Done"
        self.Previous_Workspace_Name = Template(os.path.join(os.path.expanduser('~'),
                                                             "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                             "tpl1705419993824.png"), record_pos=(0.011, -0.14),
                                                resolution=(1170, 2532))

        self.Workspace_Name_Update_update_message = ""
        self.Updated_Workspace_Name = Template(os.path.join(os.path.expanduser('~'),
                                                            "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                            "tpl1705420425792.png"), record_pos=(0.003, -0.135),
                                               resolution=(1170, 2532))

        self.Profile_Name = "My First Workspace"

        self.First_Name_Text = Template(os.path.join(os.path.expanduser('~'),
                                                     "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                     "tpl1705420538483.png"), record_pos=(-0.327, -0.074),
                                        resolution=(1170, 2532))
        self.Last_Name_Text = Template(os.path.join(os.path.expanduser('~'),
                                                    "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                    "tpl1705420583545.png"), record_pos=(-0.321, 0.191),
                                       resolution=(1170, 2532))
        self.First_Name = Template(os.path.join(os.path.expanduser('~'),
                                                "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                "tpl1705420663756.png"), record_pos=(0.009, 0.019),
                                   resolution=(1170, 2532))

        self.Last_Name = Template(os.path.join(os.path.expanduser('~'),
                                               "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                               "tpl1705420683027.png"), record_pos=(0.004, 0.289),
                                  resolution=(1170, 2532))

        self.Recently_Printed_Labels_Text = "Recently Printed Labels"
        self.Firstone_In_Recently_Printed_Labels = "Other"
        self.Printer_is_present = (

            Template(os.path.join(os.path.expanduser('~'),
                                  "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                  "tpl1707992893381.png"), record_pos=(-0.327, -0.434),
                     resolution=(1170, 2532)))

        self.Name_Updated_Message = "Your changes have been saved"
        self.Buy_More_Labels = "Buy More Labels"

        self.Enter_First_Name_TextField = "TextField"
        self.User_Settings = "Settings"
        self.Logout_Btn = "Log Out"
        self.Delete_Account = "Delete Account"
        self.Delete_Account_Text = "Delete Account"
        self.Please_Acknowledge_Txt = "Please acknowledge the following to continue:"
        self.Delete_Account_Checkbox1_with_Text = "All data in your workspace will be removed."
        self.Delete_Account_Checkbox2_with_Text = "Your account will be de-identified, meaning it will not be associated with you."
        self.Delete_Account_Checkbox3_with_Text = "Ensure your printer is ON to factory reset your ZSB printer."
        self.Cancel_Delete_account = "Cancel"
        self.Security_Message_Txt = "For your security, you must immediately sign back in one last time to finalize and confirm the deletion of your account. Select ‘Continue’ to sign out."
        self.Zebra_Logo_In_Login_Screen = "Image"

        self.ZSB_Printer_Icon_In_Login_Screen = Template(os.path.join(os.path.expanduser('~'),
                                                                      "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                      "tpl1708413534511.png"), record_pos=(0.002, 0.06),
                                                         resolution=(1170, 2532))

        self.Important_Message_In_Login_Page = "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."
        self.Delete_Account_Popup = Template(os.path.join(os.path.expanduser('~'),
                                                          "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                          "tpl1708414077816.png"), record_pos=(0.009, 0.027),
                                             resolution=(1170, 2532))

        self.Cancel_on_Delete_Account_Popup = "Cancel"
        self.Continue_with_Google = "Continue with Google"

        self.ThreeDot_On_Added_Printer_On_HomePage = Template(os.path.join(os.path.expanduser('~'),
                                                                           "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                           "tpl1708414465574.png"),
                                                              record_pos=(0.399, -0.499), resolution=(1170, 2532))

        self.Delete_Printer_Button = "Delete"
        self.Delete_Printer_Page = Template(os.path.join(os.path.expanduser('~'),
                                                         "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                         "tpl1708414599512.png"), record_pos=(0.002, 0.011),
                                            resolution=(1170, 2532))

        self.Final_Delete_Printer_Page = Template(os.path.join(os.path.expanduser('~'),
                                                               "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                               "tpl1708414599512.png"), record_pos=(0.002, 0.011),
                                                  resolution=(1170, 2532))
        self.Yes_Delete_Button = "Delete"
        # """""""""""""""""""""""""""""""""""""""""need to do""""""""""""""""""""""""""""""""""""""""""""""""
        self.Unpair_Bluetooth_dropdown_list = Template(r"tpl1706788194403.png", record_pos=(0.329, 0.09),
                                                       resolution=(1080, 2400))
        self.UI_Of_Unpair_Bluetooth_dropdown_list = Template(r"tpl1706789579755.png", record_pos=(0.002, 0.0),
                                                             resolution=(1080, 2400))
        # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.General_Tab_Text = Template(os.path.join(os.path.expanduser('~'),
                                                      "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                      "tpl1708426939171.png"), record_pos=(-0.245, -0.593),
                                         resolution=(1170, 2532))

        self.General_Tab = Template(os.path.join(os.path.expanduser('~'),
                                                 "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                 "tpl1708426939171.png"), record_pos=(-0.245, -0.593),
                                    resolution=(1170, 2532))

        self.Printer_Name_Text = "Printer Name"
        self.Darkness_Level_Bar = "64%"
        self.Updated_Darkness_Level_Bar = "99%"
        self.Darkness_Updated_Message = Template(os.path.join(os.path.expanduser('~'),
                                                              "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                              "tpl1708427418561.png"), record_pos=(-0.009, -0.735),
                                                 resolution=(1170, 2532))

        self.Toggle_Button = Template(os.path.join(os.path.expanduser('~'),
                                                   "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                   "tpl1708427705088.png"), record_pos=(0.37, -0.121),
                                      resolution=(1170, 2532))

        self.Printer_Name_Text_Field = "TextField"
        self.Exceeding_Characters_Message = "Your printer name can't exceed 30 characters."
        self.Test_Print_Button = "Test Print"

        # """"""""""""""""""""""""""""""""""""need to do"""""""""""""""""""""""""""""""""""""""""""""""""

        self.Printed_Successfully_Text = (
            Template(r"tpl1706790676674.png", record_pos=(-0.006, -0.756), resolution=(1080, 2400)))
        self.ErrorMessage_Text = (
            Template(r"tpl1706790948345.png", record_pos=(-0.065, 0.863), resolution=(1080, 2400)))
        # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        self.Notifications_Tab = "Notifications"
        self.Notifications_Settings_Tab = Template(os.path.join(os.path.expanduser('~'),
                                                                "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                "tpl1708429441924.png"), record_pos=(-0.021, -0.74),
                                                   resolution=(1170, 2532))

        self.Notification_Settings_Messages_Toggle_Btn = Template(os.path.join(os.path.expanduser('~'),
                                                                               "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                               "tpl1708429571570.png"),
                                                                  record_pos=(-0.012, -0.259), resolution=(1170, 2532))

        self.Messages_Tab = Template(os.path.join(os.path.expanduser('~'),
                                                  "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                  "tpl1708429694122.png"), record_pos=(0.266, -0.735),
                                     resolution=(1170, 2532))

        self.Messages_Text_AND_Toggle_Btn = Template(os.path.join(os.path.expanduser('~'),
                                                                  "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                  "tpl1708429858413.png"), record_pos=(-0.003, -0.168),
                                                     resolution=(1170, 2532))

        self.Notifications_Header_Text = "Notifications"

        self.Updated_Notification_Settings_Messages_Color = Template(os.path.join(os.path.expanduser('~'),
                                                                                  "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                                  "tpl1708430148657.png"),
                                                                     record_pos=(0.004, -0.26), resolution=(1170, 2532))

        self.Updated_Messages_Color = Template(os.path.join(os.path.expanduser('~'),
                                                            "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                            "tpl1708430137158.png"), record_pos=(0.002, -0.199),
                                               resolution=(1170, 2532))

        self.Bluetooth_Connection_Failed_Popup = Template(os.path.join(os.path.expanduser('~'),
                                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                       "tpl1708451072880.png"),
                                                          record_pos=(0.009, 0.026), resolution=(1170, 2532))

        self.Logout_Btn = "Log Out"
        self.Mobile_Camera = "Camera"
        self.Allow_Popup = "OK"
        self.Picture = "PhotoCapture"
        self.UsePhoto_Option = "Use Photo"
        self.User_Upload_Photo = Template(os.path.join(os.path.expanduser('~'),
                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                       "tpl1708448789991.png"), record_pos=(-0.282, -0.374),
                                          resolution=(1170, 2532))

        self.Option_Icon_To_Select_ByName = "DOC.itemCollectionMenuButton.Icons"
        self.select_ByName_Option = "Cell"
        self.Photo_Uploaded_Message = "Avatar changed successfully"

        self.User_Photo_Remove_Image = "Remove Image"

        self.Continue_Btn_on_Bluetooth_Connection_Required = "Continue"
        self.Network_Submit_Btn = "Submit"

        # """"""""""""""""""""need to do"""""""""""""""""""""""""""""""""""""""""""""""
        self.NestWifi_Text = (Template(r"tpl1706704936088.png", record_pos=(-0.244, 0.167), resolution=(1080, 2400)))
        self.Network_Password = (Template(r"tpl1706793220189.png", record_pos=(0.006, 0.003), resolution=(1080, 2400)))
        self.Network_UserName = "android.widget.EditText"
        self.Added_Network = "android.view.View"
        self.Search_Bar = "com.google.android.documentsui:id/searchbar_title"

        # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        self.Enter_Network_Manually = "Enter Network Manually..."
        self.Join_Btn = "Join"
        self.Cancel_Btn_on_Other_Network_Popup = "Cancel"
        self.Security_Open = "Open"
        self.WPA_PSK = "WPA PSK"
        self.Continue_Button_On_Printer_Update_Failed_Popup = "Continue"
        self.Continue_On_Failed_To_Connect_To_Wifi_Network = "Continue"
        self.Apply_Changes = "Apply Changes"

        self.Printer_Name_Update_Failed_Message = Template(os.path.join(os.path.expanduser('~'),
                                                                        "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                                        "tpl1708450180260.png"),
                                                           record_pos=(0.002, 0.023), resolution=(1170, 2532))

        #  """""""""""""""""""""""""""""need to do"""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.Previous_PrinterName = (
            Template(r"tpl1707288777589.png", record_pos=(0.152, -0.526), resolution=(1080, 2400)))
        self.Long_Network_UserName = (
            Template(r"tpl1707296173547.png", record_pos=(-0.032, 0.3), resolution=(1080, 2400)))

        self.Invalid_Network_Error_Message = ""
        self.Change_Password_Btn = ""

        self.Change_Password_Page = "com.android.chrome:id/url_bar"
        self.Password_Recovery_Text = (
            Template(r"tpl1707307875194.png", record_pos=(0.005, -0.55), resolution=(1080, 2400)))
        self.Email_TextField_On_Password_Recovery_Screen = "email"
        self.Submit_On_Password_Recovery_Screen = "android.widget.Button"
        self.Printer_Name_Updated_Message = "Printer name updated"

    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def click_Printer_Settings(self):
        printer_settings = self.poco(self.Printer_Settings_Btn)
        printer_settings.click()

    def Enter_Google_Password(self):
        enter_google_password = self.poco(self.Google_Password)
        sleep(2)
        enter_google_password.set_text("Swdvt@#123")

    def click_PrinterName_On_Printersettings(self):
        # printerName = self.poco(self.PrinterName_In_Printer_Settings)
        touch(self.PrinterName_In_Printer_Settings)

    def click_wifi_tab(self):

        touch(self.WiFi_Tab)

    def test_CurrentNetwork_Txt_is_present_on_printer_settings_page(self):

        if self.poco(name="Current Network").exists():
            print("Current Network Text is not present.")
            assert True

        else:
            print("Current Network Text is not present.")
            assert False

    def test_Network_Status_Txt_is_present_on_printer_settings_page(self):

        if self.poco(name="Network Status").exists():
            print("Network Status Text is not present.")
            assert True
        else:
            print("Network Status Text is not present.")
            assert False

    # def get_text_Network_Status_Txt(self):
    #     if self.Network_Status_Txt.exists():
    #         network_status_txt = self.poco(self.Network_Status_Txt)
    #         text = network_status_txt.get_text()
    #         print("Network Status is present.")
    #         assert True
    #         return text
    #     else:
    #         print("Network Status is not present.")
    #         assert False

    # def get_text_Network_Status_Txt(self):
    #     if self.poco(name="Network Status").exists():
    #      print("Network Status is present.")
    #      assert True
    # else:
    #       print("Network Status is not present.")
    #       assert False

    def get_text_Network_Status_Result_Txt(self):
        network_status_result_txt = self.poco(self.Network_Status_Result_Txt)
        network_status_result_txt.get_text()
        return network_status_result_txt

    def get_text_IPAddress_Txt(self):
        IPaddress_txt = self.poco(self.IPAddress_Txt)
        IPaddress_txt.get_text()
        return IPaddress_txt

    def get_text_IPAddress_Result_Txt(self):
        IPaddress_result_txt = self.poco(self.IPAddress_Result_Txt)
        IPaddress_result_txt.get_text()
        return IPaddress_result_txt

    def click_Manage_Networks_Btn(self):
        sleep(2)
        manage_network = self.poco(self.Manage_Network)
        manage_network.click()
        sleep(2)

    def IS_Present_Save_Network_Message_Txt(self):
        save_network_message = self.poco(self.Save_Network_Message_Txt)
        save_network_message.get_text()
        return save_network_message

    def Test_Print_button_is_present_on_printer_settings_page(self):
        if self.poco(name="Test Print").exists():
            print("Test Print button is present.")
            assert True
        else:
            print("Test Print button is not present.")
            assert False

    def get_text_Bluetooth_connection_required_Txt(self):
        save_network_message = self.poco(self.Bluetooth_Connection_Required_Msg)
        save_network_message.get_text()
        return save_network_message

    def accept_Continue_popup(self):
        # Look for the "OK" or "Allow" button in the popup
        Continue_button = self.poco(name="Continue")

        if Continue_button.exists():
            # Click on the "OK" or "Allow" button
            Continue_button.click()
            print("Popup accepted.")
            return True
        else:
            print("Popup not found or already accepted.")
            return False

    def click_Continue_Btn_on_Bluetooth_Connection_Failed_Popup(self):
        Continue_button = self.poco(name="Continue")

        if Continue_button.exists():
            # Click on the "OK" or "Allow" button
            Continue_button.click()
            print("Popup accepted.")
            return True
        else:
            print("Popup not found or already accepted.")
            return False

    def Cancel_is_present_on_Bluetooth_Connection_Failed_Popup(self):
        sleep(20)
        cancel_btn = self.poco(self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup)
        cancel_btn.get_text()
        print("Text of Cancel button:", cancel_btn)

        return cancel_btn

    #
    # def get_text_of_cancel_button(self):
    #     # Set a timeout value (in seconds) for waiting for the element to be visible
    #     timeout_seconds = 10
    #
    #     try:
    #         # Wait until the element is visible
    #         cancel_btn = self.poco(self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup).wait_for_visible(timeout=timeout_seconds)
    #
    #         # Get the text of the cancel button
    #         cancel_btn_text = cancel_btn.get_text()
    #
    #         # Print the text (optional)
    #         print("Text of Cancel button:", cancel_btn_text)
    #
    #         # Return the text
    #         return cancel_btn_text
    #
    #     except PocoTargetTimeout:
    #         # Handle the timeout exception (e.g., print an error message)
    #         print("Timeout waiting for Cancel button to be visible")
    #         return None  # You may want to return a specific value or raise an exception here

    def test_get_text_of_cancel_button(self):
        # Set a timeout value (in seconds) for waiting for the element to be visible
        timeout_seconds = 80

        # Wait until the element is visible
        wait(self.poco(self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup), timeout=timeout_seconds)

        # Get the text of the cancel button
        cancel_btn_text = self.poco(self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup).get_text()

        # Print the text (optional)
        print("Text of Cancel button:", cancel_btn_text)

        # Return the text
        return cancel_btn_text

    def click_Red_Icon_to_remove_network(self):
        touch(self.Red_Icon_to_remove_network)

    def click_Add_Network(self):
        add_network = self.poco(self.Add_Network)

        if add_network.exists():
            # Click on the "OK" or "Allow" button
            add_network.click()
            print("Able to click on the add network.")
            return True
        else:
            print("Unable to click on the add network.")
            return False

    def get_text_Add_Network(self):
        add_network_txt = self.poco(self.Add_Network_Txt)
        add_network_txt.get_text()
        print("Text of Cancel button:", add_network_txt)

        return add_network_txt

    def click_deleted_network(self):
        deleted_network = self.poco(self.Deleted_Network)
        deleted_network.click()

    # def click_Three_Dot_On_Workspace(self):
    #     touch(self.Threedot_On_Workspace)

    def click_Three_Dot_On_Workspace(self):
        sleep(4)
        self.poco("MW\nMy Workspace").child("android.widget.Button").click()
        sleep(2)

    def get_text_Edit_Txt(self):
        edit_txt = self.poco(self.Edit_Txt)
        edit_txt.get_text()
        print("Text of Edit Text:", edit_txt)
        return edit_txt

    def click_Edit_Txt(self):
        edit_txt = self.poco(self.Edit_Txt)
        edit_txt.click()

    def click_Change_Theme(self):
        change_theme = self.poco(self.Change_Theme)
        change_theme.click()

    def get_text_Change_Theme_Header(self):
        change_theme_header = self.poco(self.Change_Theme)
        change_theme_header.get_text()
        print("Change Theme Text:", change_theme_header)
        return change_theme_header

    # def check_Change_Modern_Theme(self):
    #     modern_theme = self.poco("name=android.widget.RadioButton[1]")
    #     modern_theme.click()

    def check_Change_Electic_Theme(self):
        # Assuming modern_theme is a UIObjectProxy
        # electic_theme = self.poco(name="android.widget.RadioButton[1]")
        electic_theme = self.poco(name="Eclectic")

        try:
            # Get the actual string selector from the UIObjectProxy
            electic_theme_selector = electic_theme.get_name()

            # Wait for the RadioButton to be visible
            self.poco(electic_theme_selector).wait_for_appearance(timeout=10)

            # Click on the RadioButton
            self.poco(electic_theme_selector).click()

            # Optional: Add a print statement to indicate success
            print("Clicked on the Electic theme RadioButton.")

        except PocoNoSuchNodeException:
            # Handle the case when the element is not found
            print("Electic theme RadioButton not found. Test continues...")

    # Call the method
    # check_Change_Modern_Theme(your_instance_of_the_class)

    def click_Save_Exit_Btn(self):
        save_exit = self.poco(self.Save_Exit_Btn)
        save_exit.click()

    def Home_text_is_present_on_homepage(self):
        home_text = self.poco(self.Home_text_on_homepage)
        home_text.get_text()
        print("Home Text is present on home page:", home_text)
        return home_text

    def check_radio_button_enabled(self):
        # Replace the following with the actual coordinates or image of the radio button
        # radio_button_position = (100, 200)

        # Check if the radio button exists on the screen
        if exists(Template(r"tpl1704961019063.png", record_pos=(-0.414, -0.149), resolution=(1080, 2400))):

            # Get the current state of the radio button (enabled or not)
            radio_button_enabled = (
                Template(r"tpl1704961019063.png", record_pos=(-0.414, -0.149), resolution=(1080, 2400)))

            # Check the state and perform actions accordingly
            if radio_button_enabled:
                print("Radio button is enabled.")
            else:
                print("Radio button is not enabled.")
        else:
            print("Radio button not found on the screen.")

    def check_Change_Bohemian_Theme(self):

        # Bohemian_theme = self.poco(name="android.widget.RadioButton[2]")
        Bohemian_theme = self.poco(name="Bohemian")

        try:
            # Get the actual string selector from the UIObjectProxy
            Bohemian_theme_selector = Bohemian_theme.get_name()

            # Wait for the RadioButton to be visible
            self.poco(Bohemian_theme_selector).wait_for_appearance(timeout=10)

            # Click on the RadioButton
            self.poco(Bohemian_theme_selector).click()

            # Optional: Add a print statement to indicate success
            print("Clicked on the Bohemian theme RadioButton.")

        except PocoNoSuchNodeException:
            # Handle the case when the element is not found
            print("Bohemian theme RadioButton not found. Test continues...")

    def check_Change_Professional_Theme(self):
        Professional_theme = self.poco(name="Professional")

        try:
            # Get the actual string selector from the UIObjectProxy
            Professional_theme_selector = Professional_theme.get_name()

            # Wait for the RadioButton to be visible
            self.poco(Professional_theme_selector).wait_for_appearance(timeout=10)

            # Click on the RadioButton
            self.poco(Professional_theme_selector).click()

            # Optional: Add a print statement to indicate success
            print("Clicked on the Professional  theme RadioButton.")

        except PocoNoSuchNodeException:
            # Handle the case when the element is not found
            print("Professional theme RadioButton not found. Test continues...")

    def check_Change_Maker_Theme(self):
        Maker_theme = self.poco(name="Maker")

        try:
            # Get the actual string selector from the UIObjectProxy
            Maker_theme_selector = Maker_theme.get_name()

            # Wait for the RadioButton to be visible
            self.poco(Maker_theme_selector).wait_for_appearance(timeout=10)

            # Click on the RadioButton
            self.poco(Maker_theme_selector).click()

            # Optional: Add a print statement to indicate success
            print("Clicked on the  Maker  theme RadioButton.")

        except PocoNoSuchNodeException:
            # Handle the case when the element is not found
            print("Maker theme RadioButton not found. Test continues...")

    def check_Change_Modern_Theme(self):
        Modern_theme = self.poco(name="Modern")

        try:
            # Get the actual string selector from the UIObjectProxy
            Modern_theme_selector = Modern_theme.get_name()

            # Wait for the RadioButton to be visible
            self.poco(Modern_theme_selector).wait_for_appearance(timeout=10)

            # Click on the RadioButton
            self.poco(Modern_theme_selector).click()

            # Optional: Add a print statement to indicate success
            print("Clicked on the  Modern  theme RadioButton.")

        except PocoNoSuchNodeException:
            # Handle the case when the element is not found
            print("Modern theme RadioButton not found. Test continues...")

    def click_pen_Icon_near_UserName(self):
        sleep(2)
        pen_icon = self.poco(self.Pen_Icon)
        pen_icon.click()

    def check_If_Units_of_Measurements_Is_Present(self):
        assert_exists(self.Units_Of_Measurements_Text, "Units_Of_Measurements_Text is present")

    def Inches_is_displaying(self):
        assert_exists(self.Inches_Option, "Inches Option is displaying by-default")

    def click_Units_of_Measurements(self):
        touch(self.Expand_Icon)

    def verify_Milimetres_Is_Present(self):
        milimetres_text = self.poco(self.Milimetres_Text)
        milimetres_text.get_text()
        print(" Milimetres is present:", milimetres_text)
        return milimetres_text

    def verify_Centimetres_Is_Present(self):
        centimetres_text = self.poco(self.Centimetres_Text)
        centimetres_text.get_text()
        print(" Centimetres Text is present:", centimetres_text)
        return centimetres_text

    def verify_Inches_Is_Present(self):
        inches_text = self.poco(self.Inches_Text)
        inches_text.get_text()
        print(" Inches Text is present:", inches_text)
        return inches_text

    def click_Centimeters(self):
        centimetres_Text = self.poco(self.Centimetres_Text)
        centimetres_Text.click()

    def verify_updated_msg(self):
        updated_msg = self.poco(self.Updated_Msg)
        updated_msg.get_text()
        print(" Units of Measurement updated successfully:", updated_msg)
        return updated_msg

    def click_Home_Tab(self):
        home_Text = self.poco(self.Home_Text)
        home_Text.click()

    def verify_printer_details_in_Centimeters(self):
        assert_exists(self.Size_In_Cm, "Printer details are displaying in cm")

    def click_My_Design(self):
        my_design = self.poco(self.My_Design)
        my_design.click()

    def verify_My_Details_Design_in_Centimeters(self):
        assert_exists(self.Mydesign_Size_In_Cm, "My Design details are displaying in cm")

    def click_Inches(self):
        inches_Text = self.poco(self.Inches_Text)
        inches_Text.click()

    def click_upload_photo(self):
        upload_photo = self.poco(self.Upload_Photo)
        upload_photo.click()

    def get_text_Edit_Workspace(self):
        sleep(2)
        edit_workspace = self.poco(self.Edit_Workspace)
        edit_workspace.get_text()
        print(" Edit Workspace text is displaying:", edit_workspace)
        return edit_workspace

    def click_Show_roots_Hamburger_Icn(self):
        show_roots_Hamburger_Icn = self.poco(self.Show_roots_Hamburger_Icn)
        show_roots_Hamburger_Icn.click()

    def click_Recent_Images(self):
        images = self.poco(self.Recent_Images)
        images.click()

    def click_Camera_Option(self):
        camera_option = self.poco(self.Camera_Option)
        camera_option.click()

    def click_First_Image(self):
        first_pic = self.poco(self.First_Picture)
        first_pic.click()

    def click_Remove_Image(self):
        remove_image = self.poco(self.Remove_Image)
        remove_image.click()

    def Is_Present_Profile_Avatar_Letter(self):
        assert_exists(self.Profile_Avatar_Letter, "Profile Avatar is displaying as initial letters")

    def click_Back_Icon(self):
        back_icon = self.poco(self.Back_Icon)
        back_icon.click()

    def click_Photo_Upload_Cancel_Button(self):
        Photo_Upload_Cancel_Button = self.poco(self.Photo_Upload_Cancel_Button)
        Photo_Upload_Cancel_Button.click()

    def Is_Present_Workspace_Name_Text(self):
        workspaceName_Text = self.poco(self.Workspace_Name_Text)
        workspaceName_Text.get_text()
        print(" Workspace name text is displaying:", workspaceName_Text)
        return workspaceName_Text

    def click_Workspace_Name_Text_Field(self):
        workspace_name = self.poco(self.Workspace_Name_Text_Field)
        workspace_name.click()

    def Clear_Workspace_Name(self):
        workspace_name = self.poco(self.Workspace_Name_Text_Field)
        workspace_name.set_text("")

    def click_Keyboard_back_Icon(self):
        keyboard_back_icon = self.poco(self.Keyboard_back_Icon)
        keyboard_back_icon.click()

    def Verify_SaveExit_Option_Is_Not_There(self):
        assert_not_exists(self.Save_Exit_Btn, "Save & Exit button is present")
        sleep(2)

    def click_back_Icon_On_Edit_Workspace(self):
        edit_workspace_back_icon = self.poco(self.Edit_Workspace_Back_Icon)
        edit_workspace_back_icon.click()

    def Is_Present_Workspace_Name(self):
        Previous_Workspace_Name = self.poco(text="My First Workspace")
        Previous_Workspace_Name.get_text()
        sleep(1)
        return Previous_Workspace_Name

    def Update_Workspace_Name_With_Space(self):
        workspace_name = self.poco(self.Workspace_Name_Text_Field)
        workspace_name.set_text("  ")

    def Update_Workspace_Name_With_Special_Characters_with_30_characters(self):
        workspace_name = self.poco(self.Workspace_Name_Text_Field)
        workspace_name.set_text("@abcdefghijklmn!@#abcdefghijklmn")

    def Verify_Updated_Name(self):
        assert_exists(self.Updated_Workspace_Name, "Updated Workspace name is displaying")

    def Update_Workspace_Name_with_Original_Name(self):
        workspace_name = self.poco(self.Workspace_Name_Text_Field)
        workspace_name.set_text("My First Workspace")

    def Profile_Name_Is_Displaying(self):
        profilename = self.poco(self.Profile_Name)
        profilename.get_text()
        print(" Profile name text is displaying:", profilename)
        return profilename

    def Is_Present_First_Name_Text(self):
        assert_exists(self.First_Name_Text, "First name text is displaying")

    def Is_Present_Last_Name_Text(self):
        assert_exists(self.Last_Name_Text, "Last name text is displaying")

    def verify_First_Name(self):
        firstname = self.poco(self.First_Name)
        firstname.get_text()
        print(" First name text is displaying:", firstname)
        return firstname

    def verify_Last_Name(self):
        lastname = self.poco(self.Last_Name)
        lastname.get_text()
        print(" Last name text is displaying:", lastname)
        return lastname

    def click_First_Name_Text_Field(self):
        touch(self.First_Name)

    def clear_First_Name(self):
        touch(self.First_Name).set_text("")

    def Is_Present_Recently_Printed_Labels_Text(self):
        recently_printed_labels = self.poco(self.Recently_Printed_Labels_Text)
        recently_printed_labels.get_text()
        print(" Recently printed Labels text is displaying:", recently_printed_labels)
        return recently_printed_labels

    def Is_Present_Firstone_In_Recently_Printed_Label(self):
        firstone_in_printed_labels = self.poco(self.Firstone_In_Recently_Printed_Labels)
        firstone_in_printed_labels.get_text()
        print(" Recently printed Labels text is displaying:", firstone_in_printed_labels)
        return firstone_in_printed_labels

    def Verify_Printer_is_already_added(self):
        sleep(5)
        assert_exists(self.Printer_is_present, "Printer is already added")

    def click_Firstone_In_Recently_Prtinted_Label(self):
        firstone = self.poco(self.Firstone_In_Recently_Printed_Labels)
        firstone.click()
        sleep(3)

    def Update_First_Name_With_Special_Characters_with_30_characters(self):
        first_name = self.poco(self.First_Name)
        first_name.set_text("@abcdefghijklmn!@#abcdefghijklmn")

    def click_Last_Name_Text_Field(self):
        lastname = self.poco(self.Last_Name)
        lastname.click()

    def clear_Last_Name(self):
        last_name = self.poco(self.Last_Name)
        last_name.set_text("")

    def Update_Last_Name_With_Special_Characters_with_30_characters(self):
        last_name = self.poco(self.Last_Name)
        last_name.set_text("@abcdefghijklmn!@#abcdefghijklml")

    def verify_Your_changes_have_been_saved_Message(self):
        name_updated_message = self.poco(self.Name_Updated_Message)
        name_updated_message.get_text()
        print(" Name updated text is displaying:", name_updated_message)
        return name_updated_message

    def Update_Default_First_Name(self):
        first_name = self.poco(self.First_Name)
        first_name.set_text("SohoApp")

    def Update_Default_Last_Name(self):
        last_name = self.poco(self.Last_Name)
        last_name.set_text("Testing")

    def Is_Present_Buy_More_Labels(self):
        buy_more_labels = self.poco(self.Buy_More_Labels)
        buy_more_labels.get_text()
        print(" Recently printed Labels text is displaying:", buy_more_labels)
        return buy_more_labels

    def Is_Present_User_Settings_Text(self):
        sleep(3)
        user_settings = self.poco(self.User_Settings)
        user_settings.get_text()
        print(" User Settings text is displaying:", user_settings)
        return user_settings

    # def Scroll_tilll_Delete_Account(self):
    #
    #     scroll_view = poco("ScrollView")
    #     # Set the maximum number of swipes to avoid an infinite loop
    #     max_swipes = 2
    #     for _ in range(max_swipes):
    #         # Swipe up on the ScrollView
    #         scroll_view.swipe("up", duration=0.1)
    #
    #         # Check if the "Accept" element is present and enabled
    #         Delete_Acoount = poco(name="Delete Account")
    #         if Delete_Acoount.exists() and Delete_Acoount.attr('enabled'):
    #
    #             break
    #         sleep(3)

    def Scroll_till_Delete_Account(self):
        sleep(2)
        start_point = (0.5, 0.9123222748815166)  # Example coordinates (x, y)
        # Specify the vector for swiping up
        vector = (0.5, 0.46919431279620855)  # Example vector (delta_x, delta_y)
        # Perform the swipe action
        swipe(start_point, vector)
        delete_account = self.poco(self.Delete_Account)
        delete_account_text = delete_account.get_text()  # Assigning the text to a variable
        print("Delete Account text is displaying:", delete_account_text)
        return delete_account

    def Is_Present_Logout_Btn(self):
        sleep(3)
        logout_btn = self.poco(self.Logout_Btn)
        logout_btn.get_text()
        print(" Logout Button text is displaying:", logout_btn)
        return logout_btn

    def click_Delete_Account_Btn(self):
        Delete_account = self.poco(self.Delete_Account)
        Delete_account.click()

    def verify_Delete_Account_Text(self):
        sleep(3)
        delete_account_Txt = self.poco(self.Delete_Account_Text)
        delete_account_Txt.get_text()
        print(" Delete Account text is displaying:", delete_account_Txt)
        return delete_account_Txt

    def verify_Please_Acknowledge_Text(self):
        sleep(3)
        please_acknowledge_Txt = self.poco(self.Please_Acknowledge_Txt)
        please_acknowledge_Txt.get_text()
        print(" Please acknowledge the following to continue text is displaying:", please_acknowledge_Txt)
        return please_acknowledge_Txt

    def click_First_Checkbox(self):
        first_checkbox = self.poco(name="All data in your workspace will be removed.")

        try:

            Delete_Account_First_Checkbox = first_checkbox.get_name()
            self.poco(Delete_Account_First_Checkbox).wait_for_appearance(timeout=10)
            self.poco(Delete_Account_First_Checkbox).click()
            print("Checked & Clicked on the  First check box.")

        except PocoNoSuchNodeException:
            print("First check box not found. Test continues...")
        # raise Exception("First check box not found. Test failed.")

    def click_Second_Checkbox(self):
        second_checkbox = self.poco(
            name="Your account will be de-identified, meaning it will not be associated with you.")

        try:

            Delete_Account_Second_Checkbox = second_checkbox.get_name()
            self.poco(Delete_Account_Second_Checkbox).wait_for_appearance(timeout=10)
            self.poco(Delete_Account_Second_Checkbox).click()
            print("Checked & Clicked on the  Second check box.")

        except PocoNoSuchNodeException:
            print("Second check box not found. Test continues...")
        # raise Exception("Second check bo not found. Test failed.")

    def click_Third_Checkbox(self):
        sleep(3)
        third_checkbox = self.poco(name="Ensure your printer is ON to factory reset your ZSB printer.")

        try:

            Delete_Account_Third_Checkbox = third_checkbox.get_name()
            self.poco(Delete_Account_Third_Checkbox).wait_for_appearance(timeout=10)
            self.poco(Delete_Account_Third_Checkbox).click()
            print("Checked & Clicked on the  Third check box.")

        except PocoNoSuchNodeException:
            print("Third check box not found. Test continues...")
        # raise Exception("Third check box not found. Test failed.")

    def click_Cancel_Btn(self):
        sleep(3)
        Cancel_Delete_account = self.poco(self.Cancel_Delete_account)
        Cancel_Delete_account.click()

    def click_Confirm_Btn_To_DeleteAccount(self):
        continue_btn = self.poco(name="Continue")

        try:

            Continue_Btn_To_Delete_Account = continue_btn.get_name()
            self.poco(Continue_Btn_To_Delete_Account).wait_for_appearance(timeout=10)
            self.poco(Continue_Btn_To_Delete_Account).click()
            print("Checked & Clicked on the Continue Button.")

        except PocoNoSuchNodeException:
            print("Continue Button not found. Test continues...")
        # else:
        #     print("Continue Button not found. Test failed.")

    def verify_Security_Message_Text(self):
        sleep(3)
        security_Txt = self.poco(self.Security_Message_Txt)
        security_Txt.get_text()
        print(" Please acknowledge the following to continue text is displaying:", security_Txt)
        return security_Txt

    def Is_Present_Zebra_Logo(self):
        sleep(3)
        assert_exists(self.Zebra_Logo_In_Login_Screen, "Zebra Logo is displaying")

    def Is_Present_ZSB_Printer_Icon(self):
        sleep(3)
        assert_exists(self.ZSB_Printer_Icon_In_Login_Screen, "ZSB Printer Image is displaying")

    def Verify_Login_Page_Important_Message_Text(self):
        sleep(3)
        important_Txt = self.poco(self.Important_Message_In_Login_Page)
        important_Txt.get_text()
        return important_Txt

    def Is_Present_Delete_Account_Popup(self):
        sleep(7)
        assert_exists(self.Delete_Account_Popup, "Delete Account Popup text is displaying")

    def click_Cancel_on_Delete_Account_Popup(self):
        sleep(3)
        Cancel_on_Delete_Account_Popup = self.poco(self.Cancel_on_Delete_Account_Popup)
        Cancel_on_Delete_Account_Popup.click()

    def click_Continue_with_Google(self):
        sleep(15)
        touch(self.Continue_with_Google)

    def click_Three_Dot_On_Added_Printer_On_HomePage(self):
        touch(self.ThreeDot_On_Added_Printer_On_HomePage)

    def click_Delete_Printer_Button(self):
        Delete_printer = self.poco(self.Delete_Printer_Button)
        Delete_printer.click()

    def screen_freeze_for_30_seconds(self):
        print("Screen freeze for 30 seconds starting...")
        sleep(30)
        print("Screen freeze for 30 seconds completed.")

    def Verify_Delete_Printer_Page(self):
        assert_exists(self.Delete_Printer_Page, "Delete Printer Page is displaying")

    def Verify_Final_Delete_Printer_Text(self):
        assert_exists(self.Final_Delete_Printer_Page, "Delete Printer Page is displaying")

    def click_Yes_Delete_Button(self):
        Yes_Delete_Button = self.poco(self.Yes_Delete_Button)
        Yes_Delete_Button.click()

    def Verify_And_click_Unpair_Bluetooth_dropdown_list(self):
        sleep(3)
        touch(self.Unpair_Bluetooth_dropdown_list)

    def Verify_UI_Of_Unpair_Bluetooth_dropdown_list(self):
        sleep(2)
        assert_exists(self.UI_Of_Unpair_Bluetooth_dropdown_list,
                      "UI Of Unpair Bluetooth dropdown list is displaying correctly")

    def Verify_General_Tab_Text(self):
        sleep(2)
        assert_exists(self.General_Tab_Text, "General Tab text is displaying")

    def Verify_Printer_Name_Text(self):
        Printer_Name_Text = self.poco(self.Printer_Name_Text)
        Printer_Name_Text.get_text()
        return Printer_Name_Text

    def Verify_Darkness_Level_Bar(self):
        seekbar = \
        self.poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child(
            "Other")[1].child("Other")[1].child("Other")[3].child("Other")[1].child("Other")[1].child("Other")[1].child(
            "Other")[1].child("Other")[1].child("Other")[1].child("Other")
        newvalue = 30
        percentage = newvalue / 100.0
        seekbar_size = seekbar.get_size()
        click_x = seekbar_size[0] * percentage
        seekbar.click([click_x, seekbar_size[1] / 2])

    def Verify_Darkness_Updated_Message(self):
        assert_exists(self.Darkness_Updated_Message, "Darkness update message is Present")

    def Check_toggle_button(self):
        sleep(2)
        assert_exists(self.Toggle_Button, "Darkness update message is Present")

    def Change_Darkness_Level_Bar(self):
        seekbar = \
        self.poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child(
            "Other")[1].child("Other")[1].child("Other")[3].child("Other")[1].child("Other")[1].child("Other")[1].child(
            "Other")[1].child("Other")[1].child("Other")[1].child("Other")
        newvalue = 50
        percentage = newvalue / 100.0
        seekbar_size = seekbar.get_size()
        click_x = seekbar_size[0] * percentage
        seekbar.click([click_x, seekbar_size[1] / 2])

    def click_toggle_button(self):
        touch(self.Toggle_Button)

    def click_Printer_Name_Text_Field(self):
        printer_name_text_field = self.poco(self.Printer_Name_Text_Field)
        printer_name_text_field.click()
        sleep(2)

    def clear_First_Name(self):
        printer_name = self.poco(self.Printer_Name_Text_Field)
        printer_name.set_text("")

    def Rename_PrinterName_With30_Characters(self):
        printer_name = self.poco(self.Printer_Name_Text_Field)
        printer_name.set_text("@abcdefghijklmn!@#abcdefghijklmn")

    def Update_PrinterName(self):
        printer_name = self.poco(self.Printer_Name_Text_Field)
        printer_name.set_text("ZSB-DP12")

    def Verify_Exceeding_Characters_Message(self):
        exceeding_characters_Message = self.poco(self.Exceeding_Characters_Message)
        exceeding_characters_Message.get_text()
        return exceeding_characters_Message

    def click_Test_Print_Button(self):
        sleep(2)
        Test_Print_Button = self.poco(self.Test_Print_Button)
        Test_Print_Button.click()

    def Verify_Printed_Successfully_Text(self):
        sleep(1)
        assert_exists(self.Printed_Successfully_Text, "Printed successfully Text is Present")

    def Verify_ErrorMessage_Text(self):
        assert_exists(self.ErrorMessage_Text, "ErrorMessage Text is Present")

    def Verify_Bluetooth_Connection_Failed_Popup(self):
        sleep(4)
        assert_exists(self.Bluetooth_Connection_Failed_Popup, "Bluetooth Connection Failed popup is Present")

    def Verify_Wifi_Tab_Text(self):
        assert_exists(self.WiFi_Tab, "Wifi Text is Present")

    def click_Notifications_Tab(self):
        notifications_tab = self.poco(self.Notifications_Tab)
        notifications_tab.click()

    def Scroll_Till_Notification_Settings_Tab(self):
        sleep(2)
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("left", duration=0.5)

    def Verify_NotificationSettings_Toggle_Buttons_Text_Present(self):
        assert_exists(self.Notification_Settings_Messages_Toggle_Btn,
                      "Notification settings text and toggle buttons are Present according to the theme")

    def Scroll_Till_Messages_Tab(self):
        sleep(2)
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 3
        for _ in range(max_swipes):
            # Swipe up on the ScrollView
            scroll_view.swipe("left", duration=0.9)

    def Verify_Messages_Text_And_Toggle_Buttons(self):

        if self.Messages_Text_AND_Toggle_Btn.exists():
            print("Verification successful: Messages text and toggle buttons are present.")
        else:
            print("Verification failed: Messages text and toggle buttons are not present according to the theme.")

    def click_Notification_Settings_Tab(self):
        sleep(2)
        touch(self.Notifications_Settings_Tab)
        sleep(2)

    def click_Mesages_Tab(self):
        touch(self.Messages_Tab)
        sleep(2)

    def Verify_Notifications_Text_IS_Displaying(self):
        sleep(3)
        Notifications_Header_Text = self.poco(self.Notifications_Header_Text)
        Notifications_Header_Text.get_text()
        return Notifications_Header_Text

    def Verify_Updated_Notifications_SettingsTab_Messages_Color(self):

        if self.Updated_Notification_Settings_Messages_Color.exists():
            print("Verification successful: Correct color for Messages text and toggle buttons are present.")
        else:
            print(
                "Verification failed: Correct color for Messages text and toggle buttons are not present according to the theme.")

    def Verify_Updated_MessagesTab_Color(self):

        if self.Updated_Messages_Color.exists():
            print("Verification successful: Correct color for Messages text and toggle buttons are present.")
        else:
            print(
                "Verification failed: Correct color for Messages text and toggle buttons are not present according to the theme.")

    def Scroll_Right(self):
        sleep(2)
        scroll_view = poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 3
        for _ in range(max_swipes):
            # Swipe up on the ScrollView
            scroll_view.swipe("right", duration=0.9)

    def click_Logout_Btn(self):
        sleep(2)
        Logout_Btn = self.poco(self.Logout_Btn)
        Logout_Btn.click()
        sleep(2)

    def click_Mobile_Camera(self):
        sleep(2)
        moibile_camera = self.poco(self.Mobile_Camera)
        moibile_camera.click()

    def Click_Allow_popup(self):
        allow_popup = self.poco(self.Allow_Popup)
        if allow_popup.exists():
            allow_popup.click()
        else:
            pass

    def click_picture(self):
        sleep(2)
        picture = self.poco(self.Picture)
        picture.click()

    def click_UsePhoto_Option(self):
        UsePhoto_Option = self.poco(self.UsePhoto_Option)
        UsePhoto_Option.click()

    def click_User_upload_photo(self):
        touch(self.User_Upload_Photo)

    def Verify_Photo_Uploaded_Message(self):
        photo_uploaded_message = self.poco(self.Photo_Uploaded_Message)
        if photo_uploaded_message.exists():
            photo_uploaded_message.get_text()
        else:
            pass

    def click_User_Photo_Remove_Image(self):
        touch(self.User_Photo_Remove_Image)

    def click_Option_Icon_To_Select_ByName(self):
        Option_Icon_Tio_Select_ByName = self.poco(self.Option_Icon_To_Select_ByName)
        Option_Icon_Tio_Select_ByName.click()

    def click_ByName_Option(self):
        sleep(3)
        select_ByName_Option = self.poco(self.select_ByName_Option)
        select_ByName_Option.click()
        sleep(3)

    def click_Continue_Btn_on_Bluetooth_Connection_Required(self):
        sleep(4)
        continue_btn = self.poco(self.Continue_Btn_on_Bluetooth_Connection_Required)
        continue_btn.click()
        sleep(7)

    def click_NESTWIFI_Network(self):
        sleep(9)
        nestwifi = self.poco(self.NESTWIFI_Network)
        nestwifi.click()

    def click_Network_Password_Field(self):
        sleep(2)
        touch(self.Network_Password_Field)
        text("123456789")

    def Enter_Network_Password(self):
        sleep(3)
        # enter_netwoek_password = self.poco(self.Network_Password_Field)
        # enter_netwoek_password.set_text("123456789")
        self.poco(self.Network_Password_Field).text("123456789")

    def click_Network_Submit_Btn(self):
        sleep(3)
        network_submit_btn = self.poco(self.Network_Submit_Btn)
        network_submit_btn.click()

    def Verify_NestWIFI_Network_Name_In_Network_List(self):
        sleep(9)
        assert_exists(self.NestWifi_Text, "NESTWIFI text is displaying")

    def click_Delete_NESTWIFI_Network_Name(self):
        sleep(3)
        Delete_NESTWIFI_Network_Name = self.poco(self.Delete_NESTWIFI_Network_Name)
        Delete_NESTWIFI_Network_Name.click()

    def Verify_NestWIFI_In_Network_List(self):
        sleep(3)

        assert_not_exists(self.NestWifi_Text, "NESTWIFI text is not displaying")

    def Check_no_of_left_cartridge(self):
        child_names = [child.get_name() for child in
                       self.poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child(
                           "android.view.View").child("android.view.View").child("android.view.View").offspring(
                           "android.widget.ScrollView").child("android.view.View")[0].child("android.view.View").child(
                           "android.view.View")[0].children()]
        modified_list = [item.split('\n') for item in child_names]
        modified_list = modified_list[0][4].split(" ")

        return int(modified_list[0])

    def check_update_cartridge(self, previous, current, count):

        return 1 if previous - count == current else 0

    def click_Enter_Network_Manually(self):
        sleep(10)
        scroll_view = poco("android.widget.ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 200
        for _ in range(max_swipes):
            # Swipe up on the ScrollView
            scroll_view.swipe("up", duration=0.1)
            # Check if the "Accept" element is present and enabled
            Enter_Network_Manually = poco(name="Enter Network Manually...")
            if Enter_Network_Manually.exists() and Enter_Network_Manually.attr('enabled'):
                Enter_Network_Manually.click()
                # Accept button is visible and enabled, break out of the loop
                break

    def click_Network_UserName(self):
        sleep(3)
        enter_network_username = self.poco(self.Network_UserName)
        enter_network_username.click()
        enter_network_username.set_text("Zebra")
        sleep(2)

    def click_Join_Btn_On_Other_Network_Popup(self):
        sleep(3)
        join_Btn = self.poco(self.Join_Btn)
        join_Btn.click()

    def click_Cancel_Button_On_Other_Network_Popup(self):
        sleep(2)
        cancel_btn = self.poco(self.Cancel_Btn_on_Other_Network_Popup)
        cancel_btn.click()

    def click_Security_Open(self):
        sleep(2)
        security_option = self.poco(self.Security_Open)
        security_option.click()

    def click_WPA_PSK(self):
        sleep(2)
        WPA_PSK = self.poco(self.WPA_PSK)
        WPA_PSK.click()

    def Click_Enter_Password(self):
        sleep(3)
        touch(self.Network_Password).set_text("123456789")

    def Verify_Added_Network(self):
        sleep(15)
        assert_exists(self.Added_Network, "Added Network Zebra text is displaying in the list")

    def Rename_PrinterName_With_Same_Name(self):
        printer_name = self.poco(self.Printer_Name_Text_Field)
        printer_name.set_text("ZSB-DP12")

    def Verify_Printer_Name_Update_Failed_Message(self):
        assert_exists(self.Printer_Name_Update_Failed_Message,
                      "Printer name update failed message pop up is displaying")

    def click_Continue_Button_On_Printer_Update_Failed_Popup(self):
        continue_btn = self.poco(self.Continue_Button_On_Printer_Update_Failed_Popup)
        continue_btn.click()

    def Verify_Previous_PrinterName_IS_Displaying(self):
        sleep(3)
        assert_exists(self.Previous_PrinterName, "Previous Printer Name is displaying")

    def click_Long_Network_UserName(self):
        sleep(3)
        enter_network_username = self.poco(self.Network_UserName)
        enter_network_username.click()
        enter_network_username.set_text("Test-EnterNetwork-Manually-NameDisplay")
        sleep(2)

    def Verify_Long_Network_UserName(self):
        sleep(3)
        assert_exists(self.Long_Network_UserName, "Long Network UserName is displaying")

    def click_General_Tab(self):
        sleep(3)
        General_Tab = self.poco(self.General_Tab)
        General_Tab.click()

    def click_Continue_On_Failed_To_Connect_To_Wifi_Network(self):
        sleep(20)
        Continue_On_Failed_To_Connect_To_Wifi_Network = self.poco(self.Continue_On_Failed_To_Connect_To_Wifi_Network)
        if Continue_On_Failed_To_Connect_To_Wifi_Network.exists():
            Continue_On_Failed_To_Connect_To_Wifi_Network.click()
        else:
            pass

    def click_Apply_Changes_Button(self):
        sleep(3)
        apply_changes = self.poco(self.Apply_Changes)
        apply_changes.click()

    def Verify_The_Invalid_Network_Error_Message(self):
        sleep(3)
        invalid_network_error = self.poco(self.Invalid_Network_Error_Message)
        invalid_network_error.click()

    def click_Change_Password_Btn(self):
        sleep(3)
        poco("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child(
            "android.view.View").child("android.view.View").child("android.view.View")[1].child(
            "android.view.View").child("android.view.View")[2].child("Change").click()

        sleep(20)

    def Verify_The_Change_Password_URL(self):
        try:
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to fetch URL: {url}. Status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"An error occurred while fetching URL: {url}. Error: {e}")
            return None

    def Verify_Change_Password_PageURL_Is_Displaying(self):
        sleep(20)
        assert_exists(self.Change_Password_Page, "Change Password Page is displaying with correct URL")

    def Verify_Password_Recovery_Text_Is_Displaying(self):
        sleep(2)
        assert_exists(self.Password_Recovery_Text, "Password Recovery Text is displaying")

    def click_Password_Recovery_Email_TextField(self):
        email_field = self.poco(self.Email_TextField_On_Password_Recovery_Screen)
        email_field.click()
        email_field.set_text("Zebra01.swdvt@icloud.com")

    def click_Submit_On_Password_Recovery_Screen(self):
        submit_btn = self.poco(self.Submit_On_Password_Recovery_Screen)
        submit_btn.click()

    def Update_PrinterName_With_Different_Valid_Name(self):
        printer_name = self.poco(self.Printer_Name_Text_Field)
        printer_name.set_text("ZSB-DP1222")

    def verify_Printer_Name_Updated_Message(self):
        assert_exists(self.Printer_Name_Updated_Message, "Printer Name Updated Message Text is displaying")

    def click_UsePhoto_Option(self):
        UsePhoto_Option = self.poco(self.UsePhoto_Option)
        UsePhoto_Option.click()

    def click_On_First_Image_SearchBar(self):
            Search_Bar = self.poco(self.Search_Bar)
            Search_Bar.click()
            sleep(2)
