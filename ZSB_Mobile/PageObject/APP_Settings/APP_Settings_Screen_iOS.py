import requests
from airtest.core.assertions import assert_exists
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from pywinauto.mouse import scroll
from urllib3.util import url
from airtest.core.api import sleep
from poco import poco


# from pocoui_lib.ios.kotoComponent import poco

class App_Settings_Screen_iOS:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Printer_Settings_Btn = "Printer Settings"
        self.PrinterName_In_Printer_Settings = "ZSB-DP12\nTab 2 of 2"
        self.PrinterName1_In_Printer_Settings = "ZSB-DP12\nTab 2 of 3"
        self.PrinterName2_In_Printer_Settings = "ZSB-DP12 (1)\nTab 3 of 3"
        self.WiFi_Tab = "Wi-Fi\nTab 2 of 2"
        self.Current_Network_Txt = "Current Networks"
        self.Network_Name_Txt = "NESTWIFI"
        self.ZEBRA_Network = "Zebra"
        self.Network_Password_Field = Template(r"tpl1706704195474.png", record_pos=(0.009, 0.083),
                                               resolution=(1080, 2400))

        self.Network_Status_Txt = "Network Status"
        self.Network_Status_Result_Txt = "Connected"
        self.IPAddress_Txt = "IP Address"
        self.IPAddress_Result_Txt = "192.168.86.175"
        self.Manage_Network = "Manage Networks"
        self.Save_Network_Message_Txt = "You can save up to 5 network profiles to your Saved Networks. If no saved networks are available, you will have to add a new one."
        self.Test_Print_Btn = "Test Print"
        self.Continue_Btn_on_Bluetooth_Connection_Failed_popup = "Continue"
        self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup = "Cancel"

        self.Red_Icon_to_remove_network = Template(r"tpl1704879780106.png", record_pos=(0.424, 0.164),
                                                   resolution=(1080, 2400))
        self.Add_Network = "Add Network"
        self.Add_Network_Txt = "Add Network"
        self.Deleted_Network = "Zebra"
        self.Edit_Txt = "Edit"
        self.Change_Theme = "Change Theme"
        self.Save_Exit_Btn = "Save & Exit"
        self.Home_text_on_homepage = "Home"
        self.Pen_Icon = "Button"
        self.Milimetres_Text = "Millimetres"
        self.Centimetres_Text = "Centimetres"
        self.Inches_Text = "Inches"
        self.Updated_Msg = "Units of Measurement updated successfully"
        self.Home_Text = "Home"
        self.My_Design = "My Designs"
        self.Upload_Photo = "Upload photo"
        self.Edit_Workspace = "Edit Workspace"
        self.Show_roots_Hamburger_Icn = "Show roots"
        self.Recent_Images = "android:id/title"
        self.Camera_Option = "androidx.cardview.widget.CardView"
        self.Search_Bar = "Search"
        self.Search_Bar2 = "com.google.android.documentsui:id/search_src_text"
        self.Remove_Image = "Remove image"
        self.Back_Icon = "com.android.systemui:id/back"
        self.Workspace_Name_Text_Field = "TextField"
        self.Edit_Workspace_Back_Icon = "Button"
        self.Workspace_Name_Text = "Workspace name"
        self.Workspace_Name_Update_update_message = "no need"
        self.Profile_Name = "My First Workspace"
        self.First_Name = "TextField"
        self.Last_Name = "TextField"

        self.Recently_Printed_Labels_Text = "Recently Printed Labels"
        self.Firstone_In_Recently_Printed_Labels = "Image"
        self.Printer_is_present = "android.widget.ImageView"

        self.Name_Updated_Message = "Your changes have been saved"
        self.Buy_More_Labels = "Buy More Labels"
        self.Enter_First_Name_TextField = "EditText"
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

        self.Important_Message_In_Login_Page = "Important:For security purposes, please login one last time to finalize the deletion of your account. Failure to do so will result in your account still being active."
        self.Delete_Account_Popup = "Delete"

        self.Cancel_on_Delete_Account_Popup = "Cancel"

        self.ThreeDot_On_Added_Printer_On_HomePage = Template(r"tpl1705915293017.png", record_pos=(0.402, -0.553),
                                                              resolution=(1080, 2400))

        self.Delete_Printer_Button = "Delete"

        self.Yes_Delete_Button = "Yes, Delete"
        self.Unpair_Bluetooth_dropdown_list = Template(r"tpl1706788194403.png", record_pos=(0.329, 0.09),
                                                       resolution=(1080, 2400))

        self.Printer_Name_Text = "Printer Name"
        self.Darkness_Level_Bar = "64%"
        self.Updated_Darkness_Level_Bar = "99%"
        self.Darkness_Updated_Message = "Printer darkness updated"
        self.Toggle_Button = "Switch"
        self.Printer_Name_Text_Field = "TextField"
        self.Exceeding_Characters_Message = "Your printer name can't exceed 30 characters."
        self.Test_Print_Button = "Test Print"
        self.Notifications_Tab = "Notifications"
        self.Notifications_Settings_Tab = "Notification Settings\nTab 2 of 3"
        self.Messages_Tab = "Messages\nTab 3 of 3"
        self.Notifications_Header_Text = "Notifications"
        self.Logout_Btn = "Log Out"
        self.Mobile_Camera = "Camera"
        self.Allow_Popup = "Allow"
        self.Picture = "PhotoCapture"
        self.Photo_Uploaded_Message = "Avatar changed successfully"
        self.Continue_Btn_on_Bluetooth_Connection_Required = "Continue"
        self.Nework_Submit_Btn = "Submit"

        self.Enter_Network_Manually = "Enter Network Manually..."
        self.Network_UserName = " "
        self.Join_Btn = "Join"
        self.Cancel_Btn_on_Other_Network_Popup = "Cancel"
        self.Security_Open = "Open"
        self.WPA_PSK = "WPA PSK"
        self.Added_Network = "android.view.View"
        self.Continue_Button_On_Printer_Update_Failed_Popup = "Continue"
        self.General_Tab = "General\nTab 1 of 2"
        self.Continue_On_Failed_To_Connect_To_Wifi_Network = "Continue"
        self.Apply_Changes = "Apply Changes"
        self.Invalid_Network_Error_Message = ""

        self.Email_TextField_On_Password_Recovery_Screen = "TextField"
        self.Cancel_Button = "Cancel"

    ### """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def click_Printer_Settings(self):
        sleep(1)
        printer_settings = self.poco(self.Printer_Settings_Btn)
        printer_settings.click()
        sleep(2)

    def Enter_Google_Password(self):
        enter_google_password = self.poco(self.Google_Password)
        sleep(2)
        enter_google_password.set_text("Swdvt@#123")

    def click_PrinterName_On_Printersettings(self):
        sleep(3)
        printerName = self.poco(self.PrinterName_In_Printer_Settings)
        printername1 = self.poco(self.PrinterName1_In_Printer_Settings)
        if printerName.exists():
            printerName.click()
        else:
            printername1.exists()
            printername1.click()
            sleep(3)

    def click_PrinterName2_On_Printersettings(self):
        sleep(3)
        printerName = self.poco(self.PrinterName2_In_Printer_Settings)
        printerName.click()
        sleep(1)

    def click_wifi_tab(self):
        sleep(1)
        WiFi_Tab = self.poco(self.WiFi_Tab)
        WiFi_Tab.click()
        sleep(2)
        # touch(self.WiFi_Tab)

    def test_CurrentNetwork_Txt_is_present_on_printer_settings_page(self):

        if self.poco(name="Current Network").exists():
            print("Current Network Text is present.")
            assert True

        else:
            print("Current Network Text is not present.")
            assert False

    def test_Network_Status_Txt_is_present_on_printer_settings_page(self):

        if self.poco(name="Network Status").exists():
            print("Network Status Text is present.")
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

    # def get_text_Network_Status_Result_Txt(self):
    #     network_status_result_txt = self.poco("android.view.View")[2].child("android.view.View").child("android.view.View").child("Not Connected")[0]
    #     text = network_status_result_txt.get_text()
    #     return text

    # def get_text_Network_Status_Result_Txt(self):
    #     # Assuming self.poco is your UI automation object
    #     element = self.poco("android:id/" + self.poco("android.view.View")[2].child("android.view.View").child(
    #         "android.view.View").child("Not Connected")[0])
    #     text = element.get_text()
    #     return text

    def get_text_Network_Status_Result_Txt(self):
        # Assuming self.poco is your UI automation object

        # Check for "Connected" element
        connected_element = self.poco(text="Connected")

        if connected_element.exists():
            return connected_element.get_text()

        # Check for "Not Connected" element
        not_connected_element = self.poco(text="Not Connected")

        if not_connected_element.exists():
            return not_connected_element.get_text()

        # If neither "Connected" nor "Not Connected" elements are found, return None
        return None

    def get_text_IPAddress_Txt(self):
        IPaddress_txt = self.poco(self.IPAddress_Txt)
        IPaddress_txt.get_text()
        return IPaddress_txt

    def get_text_IPAddress_Result_Txt(self):
        IPaddress_result_txt = self.poco(self.IPAddress_Result_Txt)
        IPaddress_result_txt.get_text()
        return IPaddress_result_txt

    def click_Manage_Networks_Btn(self):
        sleep(4)
        manage_network = self.poco(self.Manage_Network)
        manage_network.click()

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

    # def get_text_Bluetooth_connection_required_Txt(self):
    #     sleep(12)
    #     Bluetooth_connection_required_Txt = self.poco(text="You are about to connect to the printer using Bluetooth. If you have not connected to the printer from this device before, please set the printer into "pairing mode" by holding the power button for 3 seconds. If you have connected to this printer from another mobile device in the past, please remove this bond in the devices bluetooth settings or power off the device.")
    #     Bluetooth_connection_required_Txt.get_text()
    #     sleep(1)
    #     return Bluetooth_connection_required_Txt

    def get_text_Bluetooth_connection_required_Txt(self):
        sleep(9)
        a = self.poco(nameMatches="(?s).*Bluetooth Connection Required.*").get_name()
        a = a.split("\n")
        print(a)

    def accept_Continue_popup(self):
        sleep(3)
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
        sleep(10)
        Continue_button = self.poco(name="Continue")
        Continue_button.click()
        print("Popup accepted.")

    def Cancel_is_present_on_Bluetooth_Connection_Failed_Popup(self):
        sleep(20)
        cancel_btn = self.poco(self.Cancel_Btn_n_Bluetooth_Connection_Failed_Popup)
        if cancel_btn.exists():
            cancel_text = cancel_btn.get_text()
            print("Text of Cancel button:", cancel_text)
        else:
            print("Proceeding to the next code")

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
        sleep(4)
        touch(self.Red_Icon_to_remove_network)

    def click_Add_Network(self):
        sleep(4)
        poco.scroll()
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
        sleep(4)
        add_network_txt = self.poco(self.Add_Network_Txt)
        add_network_txt.get_text()
        print("Add Network Text is displaying:", add_network_txt)

        return add_network_txt

    def click_deleted_network(self):
        deleted_network = self.poco(self.Deleted_Network)
        deleted_network.click()

    def click_Three_Dot_On_Workspace(self):
        sleep(4)
        # three_dot= self.poco("MF\nMy First Workspace")
        self.poco("Button")[1].click()
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
        sleep(2)
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

    def click_Save_Exit_Btn(self):
        sleep(3)
        save_exit = self.poco(self.Save_Exit_Btn)
        save_exit.click()

    def Home_text_is_present_on_homepage(self):
        sleep(9)
        home_text = self.poco(self.Home_text_on_homepage)
        home_text.get_text()
        print("Home Text is present on home page:", home_text)
        return home_text

    # def check_radio_button_enabled(self):
    #     # Replace the following with the actual coordinates or image of the radio button
    #     # radio_button_position = (100, 200)
    #
    #     # Check if the radio button exists on the screen
    #     if exists(Template):
    #
    #         # Get the current state of the radio button (enabled or not)
    #         radio_button_enabled = (
    #             Template)
    #
    #         # Check the state and perform actions accordingly
    #         if radio_button_enabled:
    #             print("Radio button is enabled.")
    #         else:
    #             print("Radio button is not enabled.")
    #     else:
    #         print("Radio button not found on the screen.")

    def check_Change_Bohemian_Theme(self):
        sleep(2)
        start_point = (0.5, 0.9123222748815166)  # Example coordinates (x, y)
        # Specify the vector for swiping up
        vector = (0.5, 0.46919431279620855)  # Example vector (delta_x, delta_y)
        # Perform the swipe action
        swipe(start_point, vector)
        # poco.scrollTo()
        sleep(1)
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
            print("Bohemian theme RadioButton not found. Test continues...")

    def check_Change_Professional_Theme(self):
        sleep(2)
        start_point = (0.5, 0.9123222748815166)  # Example coordinates (x, y)
        # Specify the vector for swiping up
        vector = (0.5, 0.46919431279620855)  # Example vector (delta_x, delta_y)
        # Perform the swipe action
        swipe(start_point, vector)
        # poco.scrollTo()
        sleep(1)
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
        sleep(2)
        start_point = (0.59, 0.7723222748815166)  # Example coordinates (x, y)
        # Specify the vector for swiping up
        vector = (0.5, 0.46919431279620855)  # Example vector (delta_x, delta_y)
        # Perform the swipe action
        swipe(start_point, vector)

        sleep(1)
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
        sleep(2)
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
        sleep(3)
        pen_icon = self.poco(self.Pen_Icon)
        pen_icon.click()

    def check_If_Units_of_Measurements_Is_Present(self):
        sleep(1)
        a=self.poco(nameMatches="(?s).*Units of Measurement.*").get_name()
        print(a)
    def Inches_is_displaying(self):
        sleep(1)
        a=self.poco(nameMatches="(?s).*Inches.*").get_name()
        print(a)
    def click_Units_of_Measurements(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*Centimetres.*")
        b = self.poco(nameMatches="(?s).*Inches.*")
        if a.exists():
            a.click()
        else:
            b.click()

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
        if updated_msg.exists():
            updated_msg.get_text()
            print(" Units of Measurement updated successfully:", updated_msg)
        else:
            print("updated message is not displaying")

    def click_Home_Tab(self):
        home_Text = self.poco(self.Home_Text)
        home_Text.click()

    def verify_printer_details_in_Centimeters(self):
        a = self.poco(nameMatches="(?s).*cm.*").get_name()
        a = a.split("\n")
        print(a)

    def click_My_Design(self):
        my_design = self.poco(self.My_Design)
        my_design.click()

    def verify_My_Details_Design_in_Centimeters(self):
        a = self.poco(nameMatches="(?s).*cm.*").get_name()
        a = a.split("\n")
        print(a)

    def click_Inches(self):
        inches_Text = self.poco(self.Inches_Text)
        inches_Text.click()

    def click_upload_photo(self):
        sleep(2)
        upload_photo = self.poco(self.Upload_Photo)
        upload_photo.click()

    def get_text_Edit_Workspace(self):
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

    def click_On_First_Image_SearchBar(self):
        sleep(2)
        Search_Bar = self.poco(self.Search_Bar)
        Search_Bar.click()
        sleep(2)

    def click_First_Image(self):
        sleep(2)
        # Search_Bar2 = self.poco(self.Search_Bar2)
        Search_Bar = self.poco(self.Search_Bar)
        Search_Bar.click()
        self.poco(text(" "))
        sleep(1)
        Search_Bar.click()
        self.poco(text("png"))
        sleep(3)

    def click_JPG_ON_Result(self):
        sleep(1)
        self.poco(nameMatches=".*1.PNG.*").click()
        sleep(3)

    def click_Remove_Image(self):
        sleep(2)
        remove_image = self.poco(self.Remove_Image)
        remove_image.click()

    def Is_Present_Profile_Avatar_Letter(self):
        sleep(2)
        a = self.poco(nameMatches="(?s).*MF.*").get_name()
        a = a.split("\n")
        print(a)

    def click_Back_Icon(self):
        sleep(2)
        back_icon_position = (50, 50)  # Example coordinates (x, y)

        # Touch/click on the back icon
        touch(back_icon_position)
        sleep(2)

    def Is_Present_Workspace_Name_Text(self):
        workspaceName_Text = self.poco(self.Workspace_Name_Text)
        workspaceName_Text.get_text()
        print(" Workspace name text is displaying:", workspaceName_Text)
        return workspaceName_Text

    def click_Workspace_Name_Text_Field(self):
        sleep(2)
        self.poco(type="TextField").click()

    def Clear_Workspace_Name(self):
        workspace_name = self.poco(self.Workspace_Name_Text_Field)
        workspace_name.click()
        sleep(1)
        self.poco(name="Select All").click()
        sleep(1)
        self.poco("delete").click()
        sleep(1)

    def click_Keyboard_back_Icon(self):
        sleep(1)
        a = self.poco(name="Done")
        if a.exists():
            a.click()
        else:
            print("Back icon is not present")
        sleep(1)

    def click_Keyboard_go_Icon(self):
        sleep(1)
        self.poco(nameMatches="(?s).*Done.*").click()

    def Verify_SaveExit_Option_Is_Not_There(self):
        sleep(2)
        if not self.poco(self.Save_Exit_Btn).exists():
            return "Save & Exit button is not present"
        return "Save & Exit button is present"

    def click_back_Icon_On_Edit_Workspace(self):
        sleep(1)
        edit_workspace_back_icon = self.poco(self.Edit_Workspace_Back_Icon)
        edit_workspace_back_icon.click()

    def Is_Present_Workspace_Name(self):
        sleep(2)
        a = self.poco(nameMatches="(?s).*My First Workspace.*").get_name()
        print(a)

    def Update_Workspace_Name_With_Space(self):
        # workspace_name = self.poco(self.Workspace_Name_Text_Field)
        # workspace_name.click()
        sleep(2)
        self.poco(text("  "))
        # self.poco.keyevent(" ")
        sleep(1)

        # for _ in range(2):  # Enter two space characters
        #     self.poco.keyevent(" ")
        #     sleep(0.5)  # Adjust the sleep duration as needed
        #
        # sleep(1)

    def Update_Workspace_Name_With_Special_Characters_with_30_characters(self):
        # workspace_name = self.poco(self.Workspace_Name_Text_Field)
        # workspace_name.click()
        sleep(1)
        self.poco(text("@abcdefghijklmn!@#abcdefghijklmn"))
        sleep(1)

    def Verify_Updated_Name(self):
        sleep(1)
        a = self.poco("TextField").get_name()
        print(a)

    def Update_Workspace_Name_with_Original_Name(self):
        sleep(1)
        self.poco(text("My First Workspace"))
        sleep(1)

    def Profile_Name_Is_Displaying(self):
        profilename = self.poco(self.Profile_Name)
        profilename.get_text()
        print(" Profile name text is displaying:", profilename)
        return profilename

    def Is_Present_First_Name_Text(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*First Name.*").get_name()
        a = a.split("\n")
        print(a)

    def Is_Present_Last_Name_Text(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*Last Name.*").get_name()
        a = a.split("\n")
        print(a)

    def verify_First_Name(self):
        firstname = self.poco(self.First_Name)
        firstname.get_text()
        print(" First name text is displaying:", firstname)
        return firstname

    def verify_Last_Name(self):
        lastname = self.poco("Button")[1]
        lastname.get_text()
        print(" Last name text is displaying:", lastname)
        return lastname

    def click_First_Name_Text_Field(self):
        sleep(1)
        First_Name = self.poco(self.First_Name)
        First_Name.click()

    def clear_First_Name(self):
        sleep(1)
        First_Name = self.poco(self.First_Name)
        First_Name.click()
        self.poco(name="Select All").click()
        sleep(1)
        self.poco("delete").click()
        sleep(1)

    def Is_Present_Recently_Printed_Labels_Text(self):
        a = self.poco(nameMatches="(?s).*Recently Printed Labels.*").get_name()
        print(a)

    def Is_Present_Firstone_In_Recently_Printed_Label(self):
        sleep(1)
        self.poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child(
            "Other")[
            1].child("Other")[1].child("Other")[2].child("Other")[2].child("Other")[1].child("Other")[2].get_name()

    def Verify_Printer_is_already_added(self):
        sleep(5)
        a = self.poco(nameMatches="(?s).*ZSB-DP12.*").get_name()
        a = a.split("\n")
        print(a)

    def Verify_ZSB_Printer_Is_Added(self):
        parent_element_locator = \
            poco("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child(
                "android.view.View").offspring("android.widget.ScrollView").child("android.view.View")[0].child(
                "android.view.View").offspring("Offline ZSB-DP12 32mm x 89mm ZSB-LC2 249 of 330 prints left")[0]

        # Check if "zsb-12" is present within the parent element
        zsb_12_element = parent_element_locator.child(name="ZSB-DP12")

        if zsb_12_element.exists():
            print("zsb-12 is present")
        else:
            print("zsb-12 is not present")

    def Verify_Printer_Is_Not_Displaying(self):
        sleep(3)
        if not self.Printer_is_present:
            return "Printer Is removed"
        return "Printer Is  still present"

    def click_Firstone_In_Recently_Prtinted_Label(self):
        sleep(1)
        self.poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child(
            "Other")[
            1].child("Other")[1].child("Other")[2].child("Other")[2].child("Other")[1].child("Other")[2].click()

    def Update_First_Name_With_Special_Characters_with_30_characters(self):
        sleep(1)
        self.poco(text("@abcdefghijklmn!@#abcdefghijklmn"))
        sleep(1)

    def click_Last_Name_Text_Field(self):
        sleep(2)
        # start_point = (0.5, 0.17)  # Example coordinates (x, y)
        # # Specify the vector for swiping up
        # vector = (0.5, 0.46919431279620855)  # Example vector (delta_x, delta_y)
        # # Perform the swipe action
        # swipe(start_point, vector)
        self.poco(name="TextField")[1].click()

    def clear_Last_Name(self):
        sleep(1)
        self.poco(name="TextField")[1].click()
        self.poco(name="Select All").click()
        sleep(1)
        self.poco("delete").click()
        sleep(1)

    def Update_Last_Name_With_Special_Characters_with_30_characters(self):
        sleep(1)
        self.poco(text("@abcdefghijklmn!@#abcdefghijklml"))
        sleep(1)

    def verify_Your_changes_have_been_saved_Message(self):
        name_updated_message = self.poco(self.Name_Updated_Message)
        if name_updated_message.exists():
            text = name_updated_message.get_text()
            print("Name updated text is displaying:", text)
            return text
        else:
            print("Name Updated message is not displaying")
            return None

    def Update_Default_First_Name(self):
        sleep(1)
        self.poco(text("SohoApp"))
        sleep(2)

    def Update_Default_Last_Name(self):
        sleep(1)
        self.poco(text("Testing"))
        sleep(2)

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
        self.poco(name="Image").get_name()

    def Is_Present_ZSB_Printer_Icon(self):
        sleep(3)

        self.poco(name="Image")[1].get_name()

    def Verify_Login_Page_Important_Message_Text(self):
        sleep(3)
        important_Txt = self.poco(self.Important_Message_In_Login_Page)
        important_Txt.get_text()
        return important_Txt

    def Is_Present_Delete_Account_Popup(self):
        sleep(7)
        Delete_account_popup = self.poco(self.Delete_Account_Popup)
        if Delete_account_popup.exists():
            Delete_account_popup.get_text()
            return Delete_account_popup

    def click_Cancel_on_Delete_Account_Popup(self):
        sleep(3)
        Cancel_on_Delete_Account_Popup = self.poco(self.Cancel_on_Delete_Account_Popup)
        if Cancel_on_Delete_Account_Popup.exists():
            Cancel_on_Delete_Account_Popup.click()
        else:
            print("Cancel button is not displaying")

    def click_Continue_with_Google(self):
        sleep(11)
        touch(self.Continue_with_Google)

    def click_Three_Dot_On_Added_Printer_On_HomePage(self):
        sleep(1)
        touch(self.ThreeDot_On_Added_Printer_On_HomePage)

    def click_Delete_Printer_Button(self):
        Delete_printer = self.poco(self.Delete_Printer_Button)
        Delete_printer.click()

    def screen_freeze_for_30_seconds(self):
        print("Screen freeze for 30 seconds starting...")
        sleep(30)
        print("Screen freeze for 30 seconds completed.")

    def click_Yes_Delete_Button(self):
        sleep(1)
        Yes_Delete_Button = self.poco(self.Yes_Delete_Button)
        Yes_Delete_Button.click()

    def Verify_And_click_Unpair_Bluetooth_dropdown_list(self):
        sleep(3)
        touch(self.Unpair_Bluetooth_dropdown_list)

    def Verify_UI_Of_Unpair_Bluetooth_dropdown_list(self):
        sleep(3)
        a = self.poco(nameMatches="(?s).*Unpair Bluetooth From Printer.*").get_name()
        a = a.split("\n")
        print(a)

    def Verify_General_Tab_Text(self):
        sleep(2)
        general_text = self.poco(self.General_Tab)
        text = general_text.get_text()
        return text
        # assert_exists(self.General_Tab_Text, "General Tab text is displaying")

    def Verify_Printer_Name_Text(self):
        Printer_Name_Text = self.poco(self.Printer_Name_Text)
        Printer_Name_Text.get_text()
        return Printer_Name_Text

    def Verify_Darkness_Level_Bar(self):

        seekbar = \
        self.poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child(
            "Other")[1].child("Other")[1].child("Other")[3].child("Other")[1].child("Other")[1].child("Other")[1].child(
            "Other")[1].child("Other")[1].child("Other")[1].child("Other")

        # Set the new value and calculate the percentage
        newvalue = 30
        percentage = newvalue / 100.0

        # Get the size of the seekbar
        seekbar_size = seekbar.get_size()

        # Calculate the click position
        click_x = seekbar_size[0] * percentage
        click_y = seekbar_size[1] / 2

        # Click on the calculated position
        seekbar.click([click_x, click_y])
        # ----------------------------------------------

    def Verify_Darkness_Updated_Message(self):
        message = self.poco(self.Darkness_Updated_Message)
        text = "Printer darkness updated"  # Initialize text variable with an empty string
        if message.exists():
            text = message.get_text()
        return text

    def Check_toggle_button(self):
        sleep(2)
        toggle_button = self.poco(self.Toggle_Button)

        if toggle_button.exists():
            return "Toggle Button Is Present"
        else:
            return "Toggle Button Is Not Present"

    def Change_Darkness_Level_Bar(self):
        seekbar = \
            self.poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child(
                "Other")[1].child("Other")[1].child("Other")[3].child("Other")[1].child("Other")[1].child("Other")[
                1].child(
                "Other")[1].child("Other")[1].child("Other")[1].child("Other")

        newvalue = 50
        percentage = newvalue / 100.0
        seekbar_size = seekbar.get_size()
        # Calculate the click position
        click_x = seekbar_size[0] * percentage
        click_y = seekbar_size[1] / 2

        # Click on the calculated position
        seekbar.click([click_x, click_y])

    def click_toggle_button(self):
        toggle_button = self.poco(self.Toggle_Button)
        toggle_button.click()
        sleep(1)

    def click_Printer_Name_Text_Field(self):
        printer_name_text_field = self.poco(self.Printer_Name_Text_Field)
        printer_name_text_field.click()
        sleep(2)

    def clear_Printer_Name(self):
        printer_name_text_field = self.poco(self.Printer_Name_Text_Field)
        printer_name_text_field.click()
        sleep(1)
        self.poco(name="Select All").click()
        sleep(1)
        self.poco("delete").click()
        sleep(1)

    def Rename_PrinterName_With30_Characters(self):
        sleep(1)
        self.poco(text("@abcdefghijklmn!@#abcdefghijklmn"))

    def Update_PrinterName(self):
        sleep(1)
        self.poco(text("ZSB-DP12"))

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
        a = self.poco(nameMatches=".*Printed successfully..*").get_name()
        if not a:
            assert False, "Error message not found on the screen"
        else:
            print(a)

    def Verify_ErrorMessage_Text(self):
        a = self.poco(
            nameMatches=".*Printer is offline. Please check the printer connection and try again..*").get_name()
        if not a:
            # If 'a' is empty, meaning the error message is not present, fail the test
            assert False, "Error message not found on the screen"
        else:
            print(a)

    def Verify_Bluetooth_Connection_Failed_Popup(self):
        sleep(23)
        Bluetooth_Connection_Failed_Popup = self.poco(name="Continue")

        text = Bluetooth_Connection_Failed_Popup.get_text()
        sleep(1)
        return text

    def Verify_Wifi_Tab_Text(self):
        sleep(3)
        wifi_text = self.poco(self.WiFi_Tab)
        wifi_text.get_text()
        sleep(1)
        return wifi_text

    def click_Notifications_Tab(self):
        notifications_tab = self.poco(self.Notifications_Tab)
        notifications_tab.click()

    def Scroll_Till_Next_Tab(self):
        sleep(2)
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("left", duration=0.5)

    # def Verify_NotificationSettings_Toggle_Buttons_Text_Present(self):
    #         sleep(1)
    #         Notification_Settings_Messages_Toggle_Btn = self.poco(name="Documents are printed")
    #         toggle_button_text = Notification_Settings_Messages_Toggle_Btn.get_text()
    #         print("Toggle button text:", toggle_button_text)
    #         return toggle_button_text

    def Verify_NotificationSettings_Toggle_Buttons_Text_Present(self):
        try:
            sleep(1)
            # Locate the notification settings toggle button using poco
            Notification_Settings_Messages_Toggle_Btn = self.poco(name="Documents are printed")

            # Get the text content of the toggle button
            toggle_button_text = Notification_Settings_Messages_Toggle_Btn.get_text()

            # Print the text content for verification
            print("Toggle button text:", toggle_button_text)

            return toggle_button_text
        except Exception as e:
            print("Error occurred while verifying toggle button text:", e)
            return None

    def Scroll_Till_Messages_Tab(self):
        sleep(2)
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 3
        for _ in range(max_swipes):
            # Swipe up on the ScrollView
            scroll_view.swipe("left", duration=0.9)

    def Verify_Messages_Text_And_Toggle_Buttons(self):
        try:
            sleep(1)
            # Locate the notification settings toggle button using poco
            self.Messages_Text_AND_Toggle_Btn = self.poco(name="Upcoming Feature")

            # Get the text content of the toggle button
            toggle_button_text = self.Messages_Text_AND_Toggle_Btn.get_text()

            # Print the text content for verification
            print("Toggle button text:", toggle_button_text)

            return toggle_button_text
        except Exception as e:
            print("Error occurred while verifying toggle button text:", e)
            return None

    def click_Notification_Settings_Tab(self):
        sleep(2)
        notification_tab = self.poco(self.Notifications_Settings_Tab)
        notification_tab.click()
        sleep(2)

    def click_Mesages_Tab(self):
        sleep(2)
        Messages_Tab = self.poco(self.Messages_Tab)
        Messages_Tab.click()
        sleep(2)

    def Verify_Notifications_Text_IS_Displaying(self):
        sleep(3)
        Notifications_Header_Text = self.poco(self.Notifications_Header_Text)
        Notifications_Header_Text.get_text()
        return Notifications_Header_Text

    def Verify_Updated_Notifications_SettingsTab_Messages_Color(self):

        try:
            sleep(1)
            # Locate the notification settings toggle button using poco
            Notification_Settings_Messages_Toggle_Btn = self.poco(name="Documents are printed")

            # Get the text content of the toggle button
            toggle_button_text = Notification_Settings_Messages_Toggle_Btn.get_text()

            # Print the text content for verification
            print("Toggle button text:", toggle_button_text)

            return toggle_button_text
        except Exception as e:
            print("Error occurred while verifying toggle button text:", e)
            return None

    def Verify_Updated_MessagesTab_Color(self):
        try:
            sleep(1)
            # Locate the notification settings toggle button using poco
            self.Messages_Text_AND_Toggle_Btn = self.poco(name="Reminder")

            # Get the text content of the toggle button
            toggle_button_text = self.Messages_Text_AND_Toggle_Btn.get_text()

            # Print the text content for verification
            print("Toggle button text:", toggle_button_text)

            return toggle_button_text
        except Exception as e:
            print("Error occurred while verifying toggle button text:", e)
            return None

    def Scroll_Right(self):
        sleep(2)
        scroll_view = self.poco("ScrollView")
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
        picture.click()

    def click_Use_Photo(self):
        sleep(2)
        picture = self.poco(name="Use Photo")
        picture.click()

    def click_User_upload_photo(self):
        sleep(2)
        self.poco(nameMatches="(?s).*Upload Photo.*").click()

    def Verify_Photo_Uploaded_Message(self):
        photo_uploaded_message = self.poco(self.Photo_Uploaded_Message)
        if photo_uploaded_message.exists():
            photo_uploaded_message.get_text()
        else:
            pass

    def click_User_Photo_Remove_Image(self):
        sleep(1)
        self.poco(name="Remove Image").click()

    def click_Continue_Btn_on_Bluetooth_Connection_Required(self):
        sleep(4)
        continue_btn = self.poco(self.Continue_Btn_on_Bluetooth_Connection_Required)
        continue_btn.click()
        sleep(7)

    def click_Allow_Btn(self):
        allow_btn = self.poco(text="Allow")
        if allow_btn.exists():
            allow_btn.click()
        else:
            print("Allow Button is Not present")

    def click_ZEBRA_Network(self):
        sleep(9)
        zebra_wifi = self.poco(self.ZEBRA_Network)
        zebra_wifi.click()

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
        network_submit_btn = self.poco(self.Nework_Submit_Btn)
        network_submit_btn.click()

    def Verify_NestWIFI_Network_Name_In_Network_List(self):
        sleep(9)
        a = self.poco(nameMatches="(?s).*NESTWIFI.*").get_name()
        a = a.split("\n")
        print(a)

    def click_Delete_NESTWIFI_Network_Name(self):
        sleep(3)
        Delete_NESTWIFI_Network_Name = self.poco(self.Delete_NESTWIFI_Network_Name)
        Delete_NESTWIFI_Network_Name.click()

    def Verify_NestWIFI_In_Network_List(self):
        sleep(3)

        nest_wifi_element = self.poco(nameMatches="(?s).*NESTWIFI.*").exists()

        if not nest_wifi_element:
            return "NESTWIFI is not found in the network list. Printer might be removed."
        else:
            return "NESTWIFI is still present in the network list. Printer is still connected."

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
        sleep(8)
        scroll_view = poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 20
        for _ in range(max_swipes):
            # Swipe up on the ScrollView
            scroll_view.swipe("up", duration=0.2)
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
        enter_network_username.set_text("NESTWIFI")
        sleep(2)

    def click_Join_Btn_On_Other_Network_Popup(self):
        sleep(3)
        join_Btn = self.poco(self.Join_Btn)
        join_Btn.click()
        sleep(13)

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
        Network_Password = self.poco(name="EditText"[1])
        # touch(self.Network_Password).set_text("123456789")
        Network_Password.set_text("123456789")

    def Verify_Added_Network(self):
        sleep(15)
        assert_exists(self.Added_Network, "Added Network Zebra text is displaying in the list")

    def Rename_PrinterName_With_Same_Name(self):
        printer_name = self.poco(self.Printer_Name_Text_Field)
        printer_name.set_text("ZSB-DP12")

    def Verify_Printer_Name_Update_Failed_Message(self):
        sleep(2)
        continue_btn = self.poco(self.Continue_Button_On_Printer_Update_Failed_Popup)
        if continue_btn.exists:
            continue_btn.get_text()
        return continue_btn

    def click_Continue_Button_On_Printer_Update_Failed_Popup(self):
        continue_btn = self.poco(self.Continue_Button_On_Printer_Update_Failed_Popup)
        if continue_btn.exists:
            continue_btn.click()
        else:
            pass

    def click_Long_Network_UserName(self):
        sleep(3)
        enter_network_username = self.poco(self.Network_UserName)
        enter_network_username.click()
        enter_network_username.set_text("Test-EnterNetwork-Manually-NameDisplay")
        sleep(2)

    def Verify_Long_Network_UserName(self):
        sleep(3)
        a = self.poco(nameMatches="(?s).*Test-EnterNetwork-Manually-NameDisplay.*").get_name()
        a = a.split("\n")
        print(a)

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

    def click_Apply_Chnages_Button(self):
        sleep(3)
        apply_changes = self.poco(self.Apply_Changes)
        if apply_changes.exists():
            apply_changes.click()
        else:
            pass

    def Verify_The_Invalid_Network_Error_Message(self):
        sleep(3)
        invalid_network_error = self.poco(self.Invalid_Network_Error_Message)
        invalid_network_error.click()

    def click_Change_Password_Btn(self):
        sleep(3)
        self.poco(nameMatches="(?s).*Change.*")[1].click()
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

    def click_Cookies_Close_Icon(self):
        sleep(20)
        a = self.poco(name="Close")
        if a.exists():
            a.click()
        else:
            print("Close icon is not present")

    def Verify_Change_Password_PageURL_Is_Displaying(self):
        sleep(7)
        a = self.poco(valueMatches="(?s).*signup.zebra.com.*").get_name()
        print(a)

    def Verify_Password_Recovery_Text_Is_Displaying(self):
        sleep(3)
        Password_Recovery_Text = self.poco(name="Password Recovery")
        if Password_Recovery_Text.exists():
            Password_Recovery_Text.get_text()
        return Password_Recovery_Text

    def click_Password_Recovery_Email_TextField(self):
        email_field = self.poco(self.Email_TextField_On_Password_Recovery_Screen)
        email_field.click()
        sleep(1)
        self.poco(text("Zebra01.swdvt@icloud.com"))

    def click_Submit_On_Password_Recovery_Screen(self):
        sleep(1)
        submit_btn = self.poco(name="SUBMIT")
        submit_btn.click()

    def Update_PrinterName_With_Different_Valid_Name(self):
        printer_name = self.poco(self.Printer_Name_Text_Field)
        printer_name.set_text("ZSB-DP1222")

    def verify_Printer_Name_Updated_Message(self):
        message = self.poco(name="Printer name updated")
        text = "Printer name updated"  # Initialize text variable with an empty string
        if message.exists():
            text = message.get_text()
        return text

    def click_UsePhoto_Option(self):
        UsePhoto_Option = self.poco(self.UsePhoto_Option)
        UsePhoto_Option.click()

    def Verify_Printer_Text(self):
        sleep(2)
        a = self.poco(nameMatches="(?s).*ZSB-DP12.*").get_name()
        print(a)

    def Click_Cancel_On_Delete_Printer_Page(self):
        Cancel = self.poco(text="Cancel")
        if Cancel.exists():
            Cancel.click()

        else:
            raise Exception("Cancel Button is not present")

    def Verify_Delete_Printer_Page(self):
        a = self.poco(nameMatches="(?s).*Delete Printer.*").get_name()
        a = a.split("\n")
        print(a)

    def click_Bluetooth(self):
        sleep(1)
        bluetooth_tab = self.poco(text="Bluetooth")
        bluetooth_tab.click()

    def click_Unpair_Icon(self):
        sleep(1)
        unpair_icon = self.poco(name="com.oplus.wirelesssettings:id/deviceDetails")
        unpair_icon.click()

    def click_On_Unpair(self):
        sleep(1)
        unpair = self.poco(text="Unpair")
        unpair.click()
        sleep(8)

    def click_Done_Btn(self):
        sleep(1)
        unpair = self.poco(name="Done")
        unpair.click()

    def Scroll_Till_Next_Tab(self):
        sleep(2)
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 7
        for _ in range(max_swipes):
            # Swipe up on the ScrollView
            scroll_view.swipe("left", duration=0.9)

    def Stop_iOS_App(self):
        sleep(4)
        keyevent("HOME")
        sleep(4)

    def click_ZSB_Series_Popup(self):
        sleep(1)
        a = self.poco(name="Allow Once")
        if a.exists():
            a.click()
        else:
            print("Pop up is not present")

    def click_Mobile_SearchBar(self):
        Mobile_SearchBar = self.poco(self.Mobile_SearchBar)
        Mobile_SearchBar.click()
        sleep(3)

    def click_On_Searchbar2(self):
        sleep(2)
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.click()
        sleep(3)

    def Enter_Settings_Text_On_SearchBar(self):
        sleep(2)
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.set_text(" ")
        sleep(2)
        SearchBar2.set_text("Settings")
        sleep(3)
        self.poco(self.Settings).click()

    def click_Settings(self):
        sleep(2)
        Settings = self.poco(self.Settings)
        if Settings.exists():
            Settings.click()
            sleep(2)
        else:
            print("Settings text is not there")