import requests
import self
from airtest.core.android import android
from airtest.core.api import *
from airtest.core.api import sleep
from urllib3.util import url

# from setuptools.config._validate_pyproject.formats import url

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ZSB_Mobile.PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ZSB_Mobile.PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from poco.exceptions import PocoNoSuchNodeException
from pocoui_lib.android.kotoComponent import poco


class PDF_Printing_Android:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Mobile_Search_Bar = ""
        self.Files_Folder = "Files"
        self.Drive_Folder = "Drive"
        self.Three_Dot_Icon_Next_To_PDF = "More options"
        self.PDF_Share_Option = "com.google.android.apps.docs:id/title"
        self.Print_Option = "Print"
        self.Notification_Is_Not_Displaying = "android:id/text"
        self.Notification_To_Login = "android:id/text"
        self.Downloads_Tab = "com.google.android.apps.nbu.files:id/search_suggestion_text"
        self.Mobile_SearchBar = "com.google.android.apps.nexuslauncher:id/hotseat"
        self.Drive_SearchBar = "com.google.android.apps.nbu.files:id/open_search_bar_text_view"
        self.Searchbar2 = "com.google.android.apps.nexuslauncher:id/input"
        self.Drive_SearchBar2 = "com.google.android.apps.nbu.files:id/search_box"
        self.Settings = "Settings"
        self.Connected_Devices = "android:id/title[1]"
        self.ZSB_Series = "android:id/title"
        self.Turn_ON_ZSB_Series_Printer = "android:id/switch_widget"
        self.Mobile_back_icon = "Navigate up"
        self.Mobile_Footer_Back_Icon = "com.android.systemui:id/back"
        self.Suggestion_PDF_File = "com.google.android.apps.nbu.files:id/search_suggestion_text"
        self.PDF_ON_Result = "com.google.android.apps.nbu.files:id/title"
        self.Print_Review_Page = "com.android.printspooler:id/preview_page"
        self.Save_AS_PDF = "com.android.printspooler:id/title"
        self.All_Printers = "All printers…"
        self.Share_Option = "com.google.android.apps.nbu.files:id/share_action"
        self.Print_job_IS_IN_Progress_Message = ""
        self.Cancel_Button_On_The_Printing_InProgress_Notification = ""
        self.Cancelling_Driver_Job_Is_Displaying = "Cancelled"
        self.Use_ZSB_Series_Popup_Is_Displaying = ""
        self.Arrow_Icon = "com.android.printspooler:id/destination_spinner"
        self.Print_Icon_Option = "com.android.printspooler:id/print_button"
        self.Expand_Icon = "com.android.printspooler:id/expand_collapse_icon"
        self.Copies_Number_Field = "com.android.printspooler:id/copies_edittext"
        self.Clear_Print_Queue = "Clear Print Queue"
        self.OK_Button_On_The_Popup = "android:id/button1"
        self.GoogleDrive_SearchBar = "com.google.android.apps.docs:id/open_search_bar_text_view"
        self.GoogleDrive_SearchBar2 = "com.google.android.apps.docs:id/search_text"
        self.Suggestion_PDF_File_From_Drive = "android.widget.TextView"
        self.Three_Dot_Icon_Next_To_Drive_PDF = "com.google.android.apps.docs:id/action_show_menu"
        self.ThreeDot_On_Added_Printer_On_HomePage = (
            Template(r"tpl1715066652101.png", record_pos=(0.407, -0.553), resolution=(1080, 2400)))
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


    def click_Mobile_SearchBar(self):
        Mobile_SearchBar = self.poco(self.Mobile_SearchBar)
        Mobile_SearchBar.click()
        sleep(3)

    def click_On_Searchbar2(self):
        sleep(2)
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.click()
        sleep(3)

    def Enter_Files_Text_On_SearchBar(self):
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.set_text(" ")
        sleep(2)
        SearchBar2.set_text("Files")
        sleep(2)
        self.poco(self.Files_Folder).click()
        sleep(3)

    def Enter_Drive_On_Searchbar(self):
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.set_text(" ")
        sleep(2)
        SearchBar2.set_text("Drive")
        sleep(2)
        self.poco(self.Drive_Folder).click()
        sleep(3)

    def click_Drive_Searchbar(self):
        sleep(3)
        SearchBar = self.poco(self.Drive_SearchBar)
        if SearchBar.exists():
            SearchBar.click()
            sleep(3)
        else:
            self.poco(self.Drive_SearchBar2).click()

    def Verify_Print_Preview_page(self):
        sleep(9)
        a = self.poco(nameMatches="(?s).*Edit Label.*").get_name()
        print(a)

    def Verify_The_Printer_As_Online(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*Printer (Online).*").get_name()
        a.split("\n")
        print(a)

    def click_Print_Option_On_PDF_Printing(self):
        poco.scroll()
        sleep(1)
        print=self.poco(name="Print")
        print.click()

    def Verify_Print_Complete_Popup(self):
        a=self.poco(nameMatches="(?s).*Print Complete.*").get_name()
        print(a)

    def Verify_No_Warning_Popup(self):
        a = self.poco(textMatches="(?s).*Ensure printer is Online and reshare the PDF to use this feature. ).*").get_name()
        a.split("\n")
        print(a)

    def Verify_Status_Of_The_Printer_As_Offline(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*Printer (Offline)).*").get_name()
        a.split("\n")
        print(a)

    def Verify_Warnning_Popup_For_Printer_IS_Offline(self):
        sleep(1)
        a = self.poco(textMatches="(?s).*Ensure printer is Online and reshare the PDF to use this feature. ).*").get_name()
        a.split("\n")
        print(a)

    def click_Adobe_From_The_List(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        SearchBar2.set_text(" ")
        sleep(3)
        SearchBar2.set_text("Adobe")
        sleep(3)

    def click_PDF_From_The_List(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        SearchBar2.set_text(" ")
        sleep(3)
        SearchBar2.set_text("pdf")
        sleep(3)

    def click_Suggestion_PDF(self):
        Suggestion_PDF_File = self.poco(self.Suggestion_PDF_File)
        if Suggestion_PDF_File.exists():
            Suggestion_PDF_File.click()
            sleep(3)
        else:
            self.poco(name="com.google.android.apps.nbu.files:id/title").click()
            sleep(3)

    def click_PDF_From_Result(self):
        sleep(1)
        PDF_ON_Result = self.poco(self.PDF_ON_Result)
        PDF_ON_Result.click()
        sleep(3)

    def click_On_OK_Button_On_PrinterOffline_Popup(self):
        sleep(1)
        ok_btn=self.poco(name="Ok")
        ok_btn.click()

    def click_Mobile_Recent_App_Icon(self):
        sleep(1)
        self.poco(name="com.android.systemui:id/recent_apps").click()

    def Select_ZSB_App(self):
        sleep(2)
        poco.scroll()
        sleep(1)
        self.poco(textMatches=".*ZSB Series.*").click()

    def click_Share_Option(self):
        sleep(1)
        self.poco(name="Share").click()

    def Click_On_PDF_Print_Review_BackIcon(self):
        self.poco(name="Open navigation menu").click()

    def Verify_Label_Print_Range_Is_Selected_AS_All(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*All.*").get_name()
        print(a)

    def Verify_Current_Label_Print_Option_IS_Displaying(self):
        a = self.poco(nameMatches="(?s).*Current.*").get_name()
        print(a)

    def Verify_Custom_Label_Print_Option_IS_Displaying(self):
        a = self.poco(nameMatches="(?s).*Custom.*").get_name()
        print(a)

    def click_Custom_Label_Range_Option(self):
        custom_label=self.poco(name="Custom")
        custom_label.click()

    def click_Start_Range_Filed(self):
        self.poco(name="1").click()

    def click_Chnage_Start_Range(self):
        sleep(1)
        self.poco(name="2").click()

    def click_End_Range_Filed(self):
        sleep(1)
        self.poco(name="2").click()

    def Rotate_The_Print_Preview_Screen(self):
        def rotate_device(orientation):
            """
            Rotate the device.
            :param orientation: 'natural', 'left', 'right' or 'upsidedown'
            """
            if orientation == 'natural':
                orientation = 0
            elif orientation == 'left':
                orientation = 1
            elif orientation == 'right':
                orientation = 3
            elif orientation == 'upsidedown':
                orientation = 2
            else:
                raise ValueError("Invalid orientation value. Use 'natural', 'left', 'right', or 'upsidedown'.")

            android.set_orientation(orientation)
            sleep(2)  # Add a delay to allow the device to rotate

        # Rotate the device to landscape mode (left)
        rotate_device('left')
        print("Device rotated to landscape mode (left)")

        # Add any additional code here to interact with the app in landscape mode

        # Rotate the device back to normal portrait mode
        rotate_device('natural')
        print("Device rotated back to normal portrait mode")

    def Verify_Print_Preview_Page_After_Rotation(self):
        pass



