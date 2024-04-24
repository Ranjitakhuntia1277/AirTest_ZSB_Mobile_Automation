import subprocess

import requests
import self
from airtest.core.api import *
from airtest.core.api import sleep
from urllib3.util import url

# from setuptools.config._validate_pyproject.formats import url

from ZSB_Mobile.Common_Method import Common_Method
from poco.exceptions import PocoNoSuchNodeException
from pocoui_lib.android.kotoComponent import poco
import os


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
        self.Available_Printer_To_Print = ""
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
        self.Print_job_sent_successfully_Message = ""
        self.Print_job_IS_IN_Progress_Message = ""
        self.Cancel_Button_On_The_Printing_InProgress_Notification = ""
        self.Arrow_Icon = "com.android.printspooler:id/destination_spinner"
        self.Print_Icon_Option = "com.android.printspooler:id/print_button"
        self.Expand_Icon = "com.android.printspooler:id/expand_collapse_icon"
        self.Copies_Number_Field = "com.android.printspooler:id/copies_edittext"
        self.Three_Dot_On_Added_Printer = ""
        self.Clear_Print_Queue = "Clear Print Queue"
        self.Cancelling_Driver_Job_Is_Displaying = ""
        self.Use_ZSB_Series_Popup_Is_Displaying = ""
        self.OK_Button_On_The_Popup = "OK"
        self.GoogleDrive_SearchBar = "com.google.android.apps.docs:id/open_search_bar_text_view"
        self.GoogleDrive_SearchBar2 = "com.google.android.apps.docs:id/search_text"
        self.Suggestion_PDF_File_From_Drive = "com.google.android.apps.docs:id/title_text_view"
        self.Three_Dot_Icon_Next_To_Drive_PDF = "com.google.android.apps.docs:id/action_show_menu"

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
        three_dot = self.poco(self.Three_Dot_Icon_Next_To_Drive_PDF)
        three_dot.click()
        sleep(2)

    def click_On_Share_Option(self):
        sleep(2)
        Share_Option = self.poco(self.Share_Option)
        Share_Option.click()
        sleep(2)

    def click_Suggestion_PDF_File(self):
        Suggestion_PDF_File = self.poco(self.Suggestion_PDF_File)
        Suggestion_PDF_File.click()
        sleep(3)

    def click_Suggestion_PDF_File_From_Drive(self):
        Suggestion_PDF_File = self.poco(self.Suggestion_PDF_File_From_Drive)
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
        sleep(2)
        ZSB_Series = self.poco(self.Turn_ON_ZSB_Series_Printer)
        ZSB_Series.click()

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
        Printer_Status_AS_Offline = self.poco(textMatches=".*ZSB Series - Offline*")
        if Printer_Status_AS_Offline:
            return "Printer status Is Displaying as Offline"
        return "Printer status Is not Displaying as Offline"

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
        Cancelling_Driver_Job_Is_Displaying = self.poco(self.Cancelling_Driver_Job_Is_Displaying)
        Cancelling_Driver_Job_Is_Displaying.get_text()
        print(" Cancelling Driver Job is displaying:", Cancelling_Driver_Job_Is_Displaying)
        return Cancelling_Driver_Job_Is_Displaying

    def Verify_Use_ZSB_Series_Popup_Is_Displaying(self):
        Use_ZSB_Series_Popup_Is_Displaying = self.poco(self.Use_ZSB_Series_Popup_Is_Displaying)
        Use_ZSB_Series_Popup_Is_Displaying.get_text()
        print(" Use ZSB Series popup is displaying:", Use_ZSB_Series_Popup_Is_Displaying)
        return Use_ZSB_Series_Popup_Is_Displaying

    def click_On_OK_Button_On_The_Popup(self):
        sleep(1)
        OK_Button = self.poco(self.OK_Button_On_The_Popup)
        if OK_Button.exists():
            OK_Button.click()
            sleep(2)

    def Clear_The_Error_Status_On_The_Printer(self):
        pass

    def Printer_Is_Not_Displaying(self):
        pass

    def click_On_Cancel_Btn_On_The_Popup(self):
        pass

    def Verify_Job_Is_Cancelled(self):
        pass
