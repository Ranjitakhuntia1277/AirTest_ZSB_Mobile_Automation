import subprocess

import requests
import self
from airtest.core.api import *
from airtest.core.api import sleep
from setuptools.config import expand
from urllib3.util import url

# from setuptools.config._validate_pyproject.formats import url

from ZSB_Mobile.Common_Method import Common_Method
from poco.exceptions import PocoNoSuchNodeException
from pocoui_lib.android.kotoComponent import poco
import os
import subprocess


class APS_Notification:
    pass

    def __init__(self, poco):
        self.poco = poco
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
        self.ThreeDot_On_Added_Printer_On_HomePage = (Template(r"tpl1715066652101.png", record_pos=(0.407, -0.553), resolution=(1080, 2400)))
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def click_Device_Files_Folder(self):
        start_app("com.android.documentsui")
        wait(Template("files_app.png"), timeout=10)
        touch(Template("downloads_folder.png"))

    def click_Files_Folder(self):
        sleep(3)
        Files_Folder = self.poco(self.Files_Folder)
        if Files_Folder.exists():
            Files_Folder.click()
            sleep(2)
        else:
            print("Files folder is not there")
        sleep(3)

    def click_Drive_Folder(self):
        sleep(3)
        Drives_Folder = self.poco(self.Drive_Folder)
        if Drives_Folder.exists():
            Drives_Folder.click()
            sleep(2)
        else:
            print("Drives folder is not there")
        sleep(3)

    def click_PDF_File_From_The_List(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        SearchBar2.set_text(" ")
        sleep(3)
        SearchBar2.set_text("pdf")
        sleep(3)

    def click_PDF_File_From_The_Google_DriveList(self):
        sleep(2)
        SearchBar2 = self.poco(self.GoogleDrive_SearchBar2)
        SearchBar2.set_text(" ")
        sleep(3)
        SearchBar2.set_text("pdf")
        sleep(3)

    def click_JPG_Image_File_From_The_List(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        SearchBar2.set_text(" ")
        sleep(3)
        SearchBar2.set_text("jpg")
        sleep(3)

    def click_JPG_Image_File_From_The_Google_DriveList(self):
        sleep(2)
        SearchBar2 = self.poco(self.GoogleDrive_SearchBar2)
        SearchBar2.set_text(" ")
        sleep(3)
        SearchBar2.set_text("jpg")
        sleep(3)

    def click_PNG_Image_File_From_The_List(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        SearchBar2.set_text(" ")
        sleep(3)
        SearchBar2.set_text("png")
        sleep(3)

    def click_PNG_Image_File_From_The_Google_DriveList(self):
        sleep(2)
        SearchBar2 = self.poco(self.GoogleDrive_SearchBar2)
        SearchBar2.set_text(" ")
        sleep(3)
        SearchBar2.set_text("png")
        sleep(3)

    def click_ON_Three_Dot(self):
        sleep(2)
        three_dot = self.poco(self.Three_Dot_Icon_Next_To_PDF)
        three_dot.click()
        sleep(2)

    def click_ON_Three_Dot_Next_To_Drive_PDF(self):
        sleep(2)
        self.poco("android.widget.TextView")[2].click()
        sleep(2)

    def click_On_Share_Option(self):
        sleep(2)
        Share_Option = self.poco(self.Share_Option)
        Share_Option.click()
        sleep(2)

    def click_Suggestion_PDF_File(self):
        Suggestion_PDF_File = self.poco(self.Suggestion_PDF_File)
        if  Suggestion_PDF_File.exists():
            Suggestion_PDF_File.click()
            sleep(3)
        else:
            self.poco(name="com.google.android.apps.nbu.files:id/title").click()
            sleep(3)


    def click_Suggestion_PDF_File_From_Drive(self):
        sleep(1)
        Suggestion_PDF_File = self.poco(self.Suggestion_PDF_File_From_Drive)
        if Suggestion_PDF_File.exists():
           Suggestion_PDF_File.click()
           sleep(3)


    def click_PDF_ON_Result(self):
        PDF_ON_Result = self.poco(self.PDF_ON_Result)
        PDF_ON_Result.click()
        sleep(3)

    def click_PDF_Share_Option(self):
        PDF_Share_Option = self.poco(text="Share")
        PDF_Share_Option.click()
        sleep(3)

    def click_Print_Option(self):
        sleep(2)
        Print_Option = self.poco(text="Print")
        Print_Option.click()
        sleep(3)

    def Verify_Notification_Is_Not_Displaying(self):
        sleep(2)
        if not self.Notification_Is_Not_Displaying:
            return "Notification Is not Displaying"
        return "Notification Is  Displaying"

    def Verify_Notification_To_Login(self):
        Notification_To_Login = self.poco(self.Notification_To_Login)
        if Notification_To_Login.exists():
            Notification_To_Login.get_text()
        print(" Please Login pop up is displaying:", Notification_To_Login)
        return Notification_To_Login

    def click_Available_Printer_To_Print(self):
        sleep(1)
        Available_Printer = self.poco(text="ZSB-DP12")
        if Available_Printer.exists():
            Available_Printer.click()
            sleep(4)
        else:
            print(" Printer is not displaying:")

    def click_Available_Printer2_To_Print(self):
        sleep(2)
        Available_Printer = self.poco(text="ZSB-DP12(1)")
        if Available_Printer.exists():
            Available_Printer.click()
            sleep(4)
        else:
            print(" Printer is not displaying:")

    def click_Downloads(self):
        Downloads = self.poco(self.Downloads_Tab)
        Downloads.click()
        sleep(3)

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

    def click_Google_Drive_SearchBar(self):
        sleep(3)
        searchbar = self.poco(self.GoogleDrive_SearchBar)
        if searchbar.exists():
            searchbar.click()
            sleep(3)
        else:
            self.poco(self.GoogleDrive_SearchBar).click()

    def click_Google_Drive_SearchBar2(self):
        sleep(3)
        searchbar = self.poco(self.GoogleDrive_SearchBar2)
        if searchbar.exists():
            searchbar.click()
            sleep(3)
        else:
            self.poco(self.GoogleDrive_SearchBar2).click()

    def click_Drive_Searchbar2(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        if SearchBar2.exists():
            SearchBar2.click()
        else:
            print("Searchbar is not there")

    def Enter_Download_Text_On_SearchBar(self):
        sleep(2)
        SearchBar2 = self.poco(self.Drive_SearchBar2)
        SearchBar2.set_text("Download")
        sleep(3)

    def Verify_Print_job_sent_successfully_Message(self):
        print_job_sent_message = self.poco(text="Print Job sent successfully.")
        if print_job_sent_message.exists():
            print_job_sent_message.get_text()
            print(" Print job sent message is displaying correctly:", print_job_sent_message)
            return print_job_sent_message
        else:
            print(" Print job sent message is not displaying correctly")

    def click_Settings_Tab(self):
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.set_text("Settings")
        sleep(3)

    def click_Settings(self):
        sleep(2)
        Settings = self.poco(self.Settings)
        if Settings.exists():
            Settings.click()
            sleep(2)
        else:
            print("Settings text is not there")

    def click_Connected_Devices(self):
        sleep(2)
        Connected_Devices = self.poco(text="Connected devices")
        if Connected_Devices.exists():
            Connected_Devices.click()
            sleep(3)
        else:
            print("Connected Devices element not found")

    def click_Connection_Preferences(self):
        sleep(2)
        Connection_Preferences = self.poco(text="Connection preferences")
        if Connection_Preferences.exists():
            Connection_Preferences.click()
            sleep(3)
        else:
            print("Connection Preferences element not found")

    def click_Printing_Tab(self):
        sleep(2)
        printing_tab = self.poco(text="Printing")
        if printing_tab.exists():
            printing_tab.click()
            sleep(3)
        else:
            print("Printing Tab element not found")

    def click_ZSB_Series(self):
        sleep(2)
        ZSB_Series = self.poco(text="ZSB Series")
        if ZSB_Series.exists():
            ZSB_Series.click()
            sleep(3)
        else:
            print("ZSB_Series element not found")

    def get_all_designs_in_recently_printed_labels(self, index=6):
        try:
            self.check_element_exists_name_or_text_matches("Recently")
            arr = self.get_all_designs_in_my_designs()
            temp = []
            for i in arr:
                if "prints left" not in i:
                    temp.append(i)
            return temp

        except:
            return []

    def click_Turn_ON_ZSB_Series_Printer(self):
        sleep(3)
        ZSB_Series = self.poco(self.Turn_ON_ZSB_Series_Printer)
        ZSB_Series.click()
        # if self.poco(text="Service disabled").exists():
        #     self.poco(self.Turn_ON_ZSB_Series_Printer).click()
        # elif self.poco(nameMatches="(?s).*ZSB-DP.*").exists():
        #     self.poco(self.Turn_ON_ZSB_Series_Printer).click()
        # else:
        #     print("Printer not found or already turned on")



    def click_Turn_OFF_ZSB_Series_Printer(self):
        sleep(3)
        if self.poco(nameMatches="(?s).*ZSB-DP.*").exists():
            self.poco(self.Turn_ON_ZSB_Series_Printer).click()

    def click_Mobile_back_icon(self):
        sleep(2)
        Mobile_back_icon = self.poco(self.Mobile_back_icon)
        if Mobile_back_icon.exists():
            Mobile_back_icon.click()
            sleep(1)
        else:
            print("Back icon is not there")
            sleep(3)

    def click_Mobile_Footer_Back_Icon(self):
        sleep(2)
        searchbar = self.poco(self.GoogleDrive_SearchBar)
        mobile_footer_back_icon = self.poco(self.Mobile_Footer_Back_Icon)
        if searchbar.exists():
            searchbar.click()
        else:
            mobile_footer_back_icon.click()
            sleep(1)

    def Enter_Settings_Text_On_SearchBar(self):
        sleep(2)
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.set_text(" ")
        sleep(2)
        SearchBar2.set_text("Settings")
        sleep(3)
        self.poco(self.Settings).click()

    def Stop_Android_App(self):
        sleep(4)
        keyevent("HOME")
        sleep(4)

    def Verify_Print_Review_Page(self):
        print_preview = self.poco(self.Print_Review_Page)
        if print_preview.exists():
            print_preview.get_text()
            print(" Print Review page is displaying correctly:", print_preview)
            return print_preview
        else:
            print(" Print Review page is not displaying correctly")

    def click_Save_AS_PDF(self):
        sleep(5)
        arrow_icon = self.poco(self.Arrow_Icon)
        save_as_pdf = self.poco(self.Save_AS_PDF)
        if arrow_icon.exists():
            arrow_icon.click()
        else:
            save_as_pdf.click()
        sleep(3)

    def click_All_Printers(self):
        sleep(1)
        All_Printers = self.poco(text="All printers…")
        if All_Printers.exists():
            All_Printers.click()
            sleep(8)
        else:
            print("All_Printers element not found")

    def click_PrinterAll(self):
        save_as_pdf = self.poco(self.All_Printers)
        save_as_pdf.click()
        sleep(2)

    def Verify_Printer_Status_AS_Offline(self):
        sleep(9)
        a = self.poco(textMatches="(?s).*ZSB Series - Offline*").get_name()
        a.split("\n")
        print(a)

    def Verify_Print_job_IS_IN_Progress_Message(self):
        Print_job_IS_IN_Progress_Message = self.poco(self.Print_job_IS_IN_Progress_Message)
        if Print_job_IS_IN_Progress_Message.exists():
            Print_job_IS_IN_Progress_Message.get_text()
            print(" Print job sent message is displaying correctly:", Print_job_IS_IN_Progress_Message)
            return Print_job_IS_IN_Progress_Message
        else:
            print(" Print job sent message is not displaying correctly")

    def click_Cancel_Button_On_The_Printing_InProgress_Notification(self):
        sleep(4)
        cancel_btn = self.poco(self.Cancel_Button_On_The_Printing_InProgress_Notification)
        if cancel_btn.exists():
            cancel_btn.click()
            sleep(2)

    def run_the_command(self, command):
        cmd = command

        # Using os.system() method
        a = os.system(cmd)
        return a

    def TURN_ON_Wifi(self):
        cmd = "adb shell svc wifi enable"
        subprocess.run(cmd, shell=True)

    def Turn_OFF_Wifi(self):
        cmd = "adb shell svc wifi disable"
        subprocess.run(cmd, shell=True)

    def enable_wifi(self):
        try:
            os.system('adb shell svc wifi enable')  # turn off Wi-Fi
        except Exception as e:
            pass

    def disable_wifi(self):
        try:
            os.system('adb shell svc wifi disable')  # turn off Wi-Fi
        except Exception as e:
            pass

    def click_Print_Icon_Option(self):
        sleep(2)
        print_icon = self.poco(self.Print_Icon_Option)
        if print_icon.exists():
            print_icon.click()
            sleep(2)

    def click_Expand_Icon(self):
        sleep(1)
        Expand_Icon = self.poco(self.Expand_Icon)
        if Expand_Icon.exists():
            Expand_Icon.click()
            sleep(2)

    def click_And_Enter_Copies_Number_Field(self):
        sleep(1)
        Copies_Number_Field = self.poco(self.Copies_Number_Field)
        if Copies_Number_Field.exists():
            Copies_Number_Field.click()
            sleep(1)
            Copies_Number_Field.set_text(" ")
            sleep(1)
            Copies_Number_Field.set_text("5")

    def click_And_Enter_50_Copies_Number_Field(self):
        sleep(1)
        Copies_Number_Field = self.poco(self.Copies_Number_Field)
        if Copies_Number_Field.exists():
            Copies_Number_Field.click()
            sleep(1)
            Copies_Number_Field.set_text(" ")
            sleep(1)
            Copies_Number_Field.set_text("50")

    def click_On_Three_Dot_On_Added_Printer(self):
        sleep(1)
        Three_Dot_On_Added_Printer = self.poco(self.Three_Dot_On_Added_Printer)
        if Three_Dot_On_Added_Printer.exists():
            Three_Dot_On_Added_Printer.click()
            sleep(2)

    def click_On_Clear_Print_Queue(self):
        sleep(1)
        Clear_Print_Queue = self.poco(self.Clear_Print_Queue)
        if Clear_Print_Queue.exists():
            Clear_Print_Queue.click()
            sleep(2)

    def Verify_Cancelling_Driver_Job_Is_Displaying(self):
        sleep(7)
        Cancelling_Driver_Job_Is_Displaying = self.poco(self.Cancelling_Driver_Job_Is_Displaying)
        if Cancelling_Driver_Job_Is_Displaying.exists():
            Cancelling_Driver_Job_Is_Displaying.get_text()
        print(" Cancelling Driver Job is displaying:", Cancelling_Driver_Job_Is_Displaying)
        return Cancelling_Driver_Job_Is_Displaying

    def Verify_Use_ZSB_Series_Popup_Is_Displaying(self):
        Use_ZSB_Series_Popup_Is_Displaying = self.poco(self.Use_ZSB_Series_Popup_Is_Displaying)
        if Use_ZSB_Series_Popup_Is_Displaying.exists():
           Use_ZSB_Series_Popup_Is_Displaying.get_text()
        else:
            print(" Use ZSB Series popup is displaying:", Use_ZSB_Series_Popup_Is_Displaying)
            return Use_ZSB_Series_Popup_Is_Displaying

    def click_On_OK_Button_On_The_Popup(self):
        sleep(2)
        OK_Button = self.poco(self.OK_Button_On_The_Popup)
        if OK_Button.exists():
            OK_Button.click()
            sleep(2)

    def Clear_The_Error_Status_On_The_Printer(self):
        pass

    def Printer_Is_Not_Displaying(self):
        sleep(1)
        if not self.poco(nameMatches="(?s).*ZSB-DP.*").exists():
         # self.poco(text="Zebra Technologies").exists():
           print("APS Printing option is off")

    def click_On_Cancel_Btn_On_The_Popup(self):
        cancel_btn = self.poco(name="Cancel")
        cancel_btn.click()

    def Verify_Job_Is_Cancelled(self):
        jab_cancelled=self.poco(name="")
        if jab_cancelled.exists():
            print("Job is Cancelled")

    def Enter_Playstore_Text_On_SearchBar(self):
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.set_text(" ")
        sleep(2)
        SearchBar2.set_text("Play Store")
        sleep(2)
        self.poco(name="Play Store").click()
        sleep(3)

    def click_PlayStore_Result(self):
        sleep(1)
        PlayStore_Result = self.poco(name="Play Store")
        if PlayStore_Result.exists():
            PlayStore_Result.click()
            sleep(2)

    def click_PlayStore_SearchBar(self):
        playstore_searchbar = self.poco(name="android.view.View")
        playstore_searchbar.click()
        playstore_searchbar.set_text(" ")
        sleep(1)
        playstore_searchbar.set_text("ZSB Series")
        sleep(1)
        self.poco(name="Refine search to 'zsb series'").click()
        sleep(2)

    def Verify_Printer_Is_Not_Displaying(self):
        sleep(5)
        if not self.poco(text="Zebra Technologies").exists():
            print("APS Printing option is off")

    def Verify_Centimeter_IS_Displaying_On_Review_Page(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*cm.*").get_name()
        a = a.split("\n")
        print(a)

    def Verify_Inches_IS_Displaying_On_Review_Page(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*.*").get_name()
        print(a)

    def ZSB_Series_Is_Not_Present(self):
        sleep(2)
        ZSB_Series = self.poco(text="ZSB Series")
        if not ZSB_Series.exists():
            print("ZSB Series is not present")
        else:
            print("ZSB_Series element is present")

    def Verify_Cancel_Button_Is_Displaying(self):
        sleep(1)
        Cancel_Button = self.poco(name="Cancel")
        if Cancel_Button.exists():
            Cancel_Button.click()
        sleep(2)

    def Verify_OK_Button_Is_Displaying(self):
        sleep(1)
        Cancel_Button = self.poco(name="OK")
        if Cancel_Button.exists():
            Cancel_Button.click()
        sleep(2)

    def click_Three_Dot_On_Added_Printer_On_HomePage(self):
        sleep(1)
        touch(self.ThreeDot_On_Added_Printer_On_HomePage)

    def click_Clear_Queue_Button(self):
        sleep(1)
        Clear_Queue_Button = self.poco(name="Clear Queue")
        if Clear_Queue_Button.exists():
           Clear_Queue_Button.click()
        sleep(2)

    def Expand_StatusBar(self):
        cmd = "adb shell cmd statusbar expand-notifications"
        subprocess.run(cmd, shell=True)

    def Collapse_StatusBar(self):
        cmd = "adb shell cmd statusbar collapse"
        subprocess.run(cmd, shell=True)

    def click_ON_Three_Dot_To_Print(self):
        sleep(1)
        three_dot= self.poco(name="com.google.android.apps.docs:id/action_show_menu")
        three_dot.click()

    def Verify_Printer_Icon_Is_Present(self):
        sleep(8)
        a = self.poco(nameMatches="(?s).*com.android.settings:id/icon.*").get_name()
        a.split("\n")
        print(a)


    def Verify_Printer_Name_Is_Present(self):
        sleep(3)
        a = self.poco(textMatches="(?s).*ZSB-DP.*").get_name()
        a.split("\n")
        print(a)

    def Verify_Printer_Status_Is_Present(self):
        a = self.poco(textMatches="(?s).*Online.*").get_name()
        print(a)

    def Verify_Labels_left_Is_Present(self):
        a = self.poco(textMatches="(?s).*Labels Left.*").get_name()
        print(a)

    def Verify_Bluetooth_Address_Is_Present(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*com.android.settings:id/subtitle.*").get_name()
        a = a.split("\n")
        print(a)

    def click_ON_Three_Dot_ON_Print_Service_Page(self):
        sleep(4)
        self.poco(name="More options").click()


    def click_Search_On_The_Menu(self):
        sleep(1)
        self.poco(text="Search").click()


    def click_Add_Printer(self):
        sleep(1)
        self.poco(text="Add printer").click()

    def Verify_ZSB_Series_App_Login_Page_Is_Displaying(self):
        sleep(6)
        if self.poco(name="Home").exists():
            print("Home page is displaying")
            sleep(1)
        else:
            self.poco(name="Sign In").exists()
            print("Login page is displaying")

    def Verify_Printer_Status_AS_HeadOpen(self):
        a = self.poco(nameMatches="(?s).*Head Open.*").get_name()
        print(a)

    def Verify_Printer_Status_AS_Paper_Out(self):
        a = self.poco(nameMatches="(?s).*Paper Out.*").get_name()
        print(a)

    def Verify_Printer_Status_AS_Media_LOW(self):
        a = self.poco(nameMatches="(?s).*Media Low.*").get_name()
        print(a)

    def Verify_Longer_Printer_Name_Is_Present(self):
        a = self.poco(nameMatches="(?s).*@abcdefghijklmn!@#abcdefghijklmn.*").get_name()
        print(a)

    def Verify_Turn_ON_Wifi_Popup(self):
         a= self.poco(name="Turn On Your Wifi")
         if a.exists():
             a.get_text()
         else:
             print("Turn On you Wifi pop up is not displaying")

    def Verify_And_Turn_ON_APS(self):
        if self.poco(text="Service disabled").exists():
           self.poco(self.Turn_ON_ZSB_Series_Printer).click()

        else:
            pass

    def Verify_And_Turn_OFF_APS(self):
        if self.poco(nameMatches="(?s).*ZSB-DP.*").exists():
           self.poco(self.Turn_ON_ZSB_Series_Printer).click()

        else:
            pass



