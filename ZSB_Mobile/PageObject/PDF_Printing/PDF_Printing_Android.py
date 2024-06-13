import requests
import self
from airtest.core.android import android
from airtest.core.api import *
from airtest.core.api import sleep
from urllib3.util import url
import os
# from setuptools.config._validate_pyproject.formats import url

from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from poco.exceptions import PocoNoSuchNodeException
from pocoui_lib.android.kotoComponent import poco


class PDF_Printing_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Files_Folder = "Files"
        self.Drive_Folder = "Drive"
        self.Mobile_SearchBar = "com.google.android.apps.nexuslauncher:id/hotseat"
        self.Drive_SearchBar = "com.google.android.apps.nbu.files:id/open_search_bar_text_view"
        self.Searchbar2 = "com.google.android.apps.nexuslauncher:id/input"
        self.Drive_SearchBar2 = "com.google.android.apps.nbu.files:id/search_box"
        self.PDF_ON_Result = "com.google.android.apps.nbu.files:id/title"
        self.Suggestion_PDF_File_From_Drive = "android.widget.TextView"
        self.Suggestion_PDF_File = "com.google.android.apps.nbu.files:id/search_suggestion_text"

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
        sleep(10)
        a = self.poco(nameMatches="(?s).*Edit Label.*").get_name()
        print(a)

    # def Verify_The_Printer_As_Online2(self):
    #     a = self.poco(nameMatches="(?s).*Online.*")
    #     if a.exists():
    #        a.get_name()
    #        a.split("\n")
    #        print("Printer Is Online")
    #        return
    #
    # def Select_The_Online_Printer(self):
    #     sleep(2)
    #     if self.poco(nameMatches="(?s).*ZSB-DP.*").exists():
    #        self.poco(nameMatches="(?s).*ZSB-DP.*").click()
    #        sleep(1)
    #     b= self.poco(nameMatches="(?s).*ZSB-DP.*").parent().child()[1]
    #     if b.exists():
    #         sleep(1)
    #         b.click()
    #         sleep(1)
    #     else:
    #         c = self.poco(nameMatches="(?s).*ZSB-DP.*").parent().child()[0]
    #         if c.exists():
    #             sleep(1)
    #             c.click()

    def Verify_The_Printer_As_Online(self):
        sleep(1)
        printer_info = self.poco(nameMatches="(?s).*Online.*")
        if printer_info.exists():
            printer_info.get_name()
            # printer_info.split("\n")
            return
            # if "Online" in printer_info:
            #     print("Printer Is Online")
            #     return  # Exit if the printer is found online
        else:
            self.poco(nameMatches="(?s).*ZSB-DP.*").click()
            sleep(1)

    def Select_The_Online_Printer(self):
        sleep(1)
        printer_info = self.poco(nameMatches="(?s).*Online.*")
        if self.poco(nameMatches="(?s).*ZSB-DP.*").parent().child()[1].exists():
            self.poco(nameMatches="(?s).*ZSB-DP.*").parent().child()[1].click()
            sleep(1)

        # Recheck after first interaction
        # printer_info = self.poco(nameMatches="(?s).*Online.*")
        if printer_info.exists():
            printer_info.get_name()
            # printer_info.split("\n")
            return
        else:
            printer_info = self.poco(nameMatches="(?s).*Online.*")
        if self.poco(nameMatches="(?s).*ZSB-DP.*").parent().child()[2].exists():
            self.poco(nameMatches="(?s).*ZSB-DP.*").parent().child()[2].click()
            sleep(1)
        # printer_info = self.poco(nameMatches="(?s).*Online.*")
        if printer_info.exists():
            printer_info.get_name()
            # printer_info.split("\n")
            return
        raise Exception("Printer is not online after all checks.")



    def click_Print_Option_On_PDF_Printing(self):
        sleep(1)
        poco.scroll()
        sleep(1)
        print = self.poco(name="Print")
        print.click()

    def Verify_Print_Complete_Popup(self):
        sleep(1)
        if self.poco(nameMatches="(?s).*Print complete.*").exists():
            a = self.poco(nameMatches="(?s).*Print complete.*").get_name()
            print(a)

    def Verify_No_Warning_Popup(self):
        a = self.poco(
            textMatches="(?s).*Ensure printer is Online and reshare the PDF to use this feature. ).*").get_name()
        a.split("\n")
        print(a)

    def Verify_Status_Of_The_Printer_As_Offline(self):
        sleep(1)
        a = poco(nameMatches="(?s).*(Offline).*").get_name()
        a.split("\n")
        print(a)

    def Verify_Warnning_Popup_For_Printer_IS_Offline(self):
        sleep(1)
        a = self.poco(
            textMatches="(?s).*Ensure printer is Online and reshare the PDF to use this feature. ).*").get_name()
        a.split("\n")
        print(a)

    def click_Adobe_From_The_List(self):
        sleep(2)
        SearchBar2 = self.poco(self.Searchbar2)
        SearchBar2.set_text(" ")
        sleep(3)
        SearchBar2.set_text("Adobe")
        sleep(3)
        self.poco(name="Adobe Acrobat").click()
        sleep(3)

    def click_Adobe_Folder(self):
        sleep(3)
        if self.poco(name="Adobe Acrobat").exists():
            self.poco(name="Adobe Acrobat").click()
            sleep(2)
        else:
            print("Adobe folder is not there")
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
        ok_btn = self.poco(name="Ok")
        ok_btn.click()

    def click_Mobile_Recent_App_Icon(self):
        sleep(1)
        self.poco(name="com.android.systemui:id/recent_apps").click()

    def Select_ZSB_App(self):
        sleep(4)
        if self.poco(textMatches=".*ZSB Series.*").exists():
            self.poco(textMatches=".*ZSB Series.*").click()
        else:
            poco.scroll()
            sleep(1)
            self.poco(textMatches=".*ZSB Series.*").click()

    def click_Share_Option(self):
        sleep(1)
        self.poco(name="Share").click()

    def Click_On_PDF_Print_Review_BackIcon(self):
        self.poco(name="Open navigation menu").click()
        sleep(10)

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
        sleep(2)
        custom_label = self.poco(name="Custom")
        custom_label.click()

    def click_Start_Range_Filed(self):
        self.poco(name="1").click()

    def click_Change_Start_Range(self):
        sleep(1)
        if self.poco(name="2").exists():
            self.poco(name="2").click()
        else:
            self.poco(name="1").click()

    def click_End_Range_Filed(self):
        sleep(1)
        self.poco(name="2").click()

    def Verify_There_IS_NO_1_Option_Is_Available(self):
        sleep(2)
        if not self.poco(name="1").exists():
            print("1 is not present")

    def click_Send_Copy_For_Google_Drive_Files(self):
        sleep(2)
        self.poco(text="Send a copy").click()

    def click_Send_File_For_Files(self):
        sleep(1)
        self.poco(text="Send file…").click()

    def click_Rotation_To_Current(self):
        sleep(1)
        self.poco(name="Current").click()

    def click_Edit_Label(self):
        sleep(2)
        if self.poco(nameMatches="(?s).*Edit Label.*").exists():
            self.poco(nameMatches="(?s).*Edit Label.*").click()
        else:
            sleep(1)
            poco.scroll()
            self.poco(nameMatches="(?s).*Edit Label.*").click()

    def click_Rotation_Option(self):
        self.poco("android.widget.Button")[2].click()

    def click_Done_Btn(self):
        sleep(1)
        self.poco(name="Done").click()

    def click_Change_End_Range(self):
        sleep(1)
        self.poco(name="1").click()

    def click_Edit_Option(self):
        sleep(1)
        touch(Template(r"tpl1716657104135.png", record_pos=(0.044, -0.931), resolution=(1080, 2400)))

    def Select_Text_Area_To_Edit(self):
        sleep(2)
        self.poco("android.widget.Button")[2].click()

    def click_OK_Button_On_Popup(self):
        sleep(1)
        self.poco(name="Ok").click()

    def Select_2nd_Printer(self):
        sleep(1)
        self.poco(nameMatches="(?s).*ZSB-DP.*").click()
        sleep(1)
        if self.poco(nameMatches="(?s).*ZSB-DP.*").parent().child()[1].exists():
            self.poco(nameMatches="(?s).*ZSB-DP.*").parent().child()[1].click()
        else:
            self.poco(nameMatches="(?s).*ZSB-DP.*").parent().child()[2].exists()
            self.poco(nameMatches="(?s).*ZSB-DP.*").parent().child()[2].click()
            sleep(1)

    def click_OK_Button_On_Popup_If_Printer_Is_Offline(self):
        sleep(1)
        if self.poco(name="Ok").exists():
            self.poco(name="Ok").click()

    def Verify_Print_Preview_page_For_Printer_Online_And_Not_Added(self):
        sleep(9)
        a = self.poco(nameMatches="(?s).*Edit Label.*")

        if a.exists():
            a.get_name()
            print(a)
        else:
            b = self.poco(nameMatches="(?s).*Printers not found.*")
            if b.exists():
                b.get_name()
                print(b)

    def click_Current_Label_Range_Option(self):
        custom_label = self.poco(name="Current")
        custom_label.click()

    def Verify_Current_Label_Range_Option_Is_Selected(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*Current.*").get_name()
        print(a)

    def click_All_Label_Range_Option(self):
        sleep(1)
        self.poco(nameMatches="(?s).*All.*").click()

    def Verify_Done_Button_Is_Present(self):
        a = self.poco(nameMatches="(?s).*Done.*").get_name()
        print(a)

    def Verify_Cancel_Button_Is_Present(self):
        a = self.poco(nameMatches="(?s).*Cancel.*").get_name()
        print(a)

    def click_Cancel_Button(self):
        self.poco(nameMatches="(?s).*Cancel.*").click()

    def click_Left_Arrow_of_PDF_On_Preview_Screen(self):
        sleep(1)
        self.poco("android.widget.Button")[2].click()

    def click_Right_Arrow_of_PDF_On_Preview_Screen(self):
        sleep(1)
        self.poco("android.widget.Button")[3].click()

    def Verify_Print_Complete_Popup_Should_Not_present_Again(self):
        a = self.poco(nameMatches="(?s).*Print complete.*")
        if not a.exists():
            print("Print Complete pop up is not displaying again")
        else:
            print("Print Complete pop up is displaying again")

    def Move_To_Page_No_3(self):
        sleep(1)
        if self.poco("android.widget.Button")[3].exists():
            self.poco("android.widget.Button")[3].click()
            sleep(1)
            self.poco("android.widget.Button")[3].click()

    def click_And_Enter_Copies_Number_Field(self):
        sleep(1)
        poco.scroll()
        Copies_Number_Field = self.poco(name="android.widget.EditText")
        Copies_Number_Field.click()
        sleep(1)
        Copies_Number_Field.set_text(" ")
        sleep(1)
        Copies_Number_Field.set_text("3")

    def click_Default_End_Range_Filed(self):
        sleep(1)
        self.poco(name="1").click()

    def click_Change_Start_Range_To_3(self):
        sleep(1)
        self.poco(name="1").click()
        sleep(1)
        self.poco(name="3").click()

    def click_Change_End_Range_To_6(self):
        sleep(1)
        if self.poco(name="1").exists():
            self.poco(name="1").click()
            sleep(1)
            self.poco(name="6").click()

    def Verify_Range_1_Is_Displaying(self):
        sleep(1)
        a = self.poco(nameMatches="(?s).*1.*")
        if not a.exists():
            a.get_name()
            print(a)

    def Switch_To_Different_App(self):
        sleep(2)
        keyevent("KEYCODE_APP_SWITCH")
        sleep(1)
        keyevent("KEYCODE_APP_SWITCH")
        sleep(1)

    def click_2nd_Page_Option(self):
        sleep(1)
        self.poco("android.widget.Button")[1].click()

    def click_1st_Page_Option(self):
        sleep(1)
        self.poco("android.widget.Button")[0].click()

    def Verify_Print_Complete_Popup_IS_Not_Displaying(self):
        sleep(1)
        if not self.poco(nameMatches="(?s).*Print complete.*").exists():
            print("Print complete popup is not displaying.")
        else:
            print("Print complete popup is displaying.")

    def Verify_Default_Copies_Values_Is_1(self):
        sleep(1)
        self.poco(name="android.widget.EditText").get_name()

    def Update_Copies_Value(self):
        sleep(1)
        self.poco(name="android.widget.EditText").click()
        poco(text("5"))

    def Update_Copies_Value_To_Special_Characters(self):
        sleep(1)
        Copies_Number_Field = self.poco(name="android.widget.EditText").click()
        Copies_Number_Field.set_text(" ")
        sleep(1)
        Copies_Number_Field.set_text("@&777")

    def Update_Copies_Value_To_10(self):
        sleep(1)
        Copies_Number_Field = self.poco(name="android.widget.EditText").click()
        Copies_Number_Field.set_text(" ")
        sleep(1)
        Copies_Number_Field.set_text("10")

    def Verify_Total_Labels(self):
        sleep(1)
        a = poco(nameMatches="(?s).*Total of.*").get_name()
        print(a)

    def Verify_ZSB_APP_Option_Is_Not_There(self):
        sleep(4)
        if not self.poco(textMatches=".*ZSB Series.*").exists():
            print("ZSB Series is not present")
        else:
            poco.scroll()
            sleep(1)
            if not self.poco(textMatches=".*ZSB Series.*").exists():
                print("ZSB Series is not present")
            else:
                raise AssertionError("ZSB Series is present")

    def click_Search_Icon_On_Adobe(self):
        sleep(5)
        self.poco(text="Search").click()

    def click_PDF_From_The_Adobe_List(self):
            sleep(2)
            self.poco(name="com.adobe.reader:id/search_src_text").click()
            self.poco(text(" "))
            sleep(3)
            self.poco(text("pdf"))

    def click_ON_Three_Dot_On_Adobe_PDF(self):
        sleep(8)
        if self.poco(name="com.adobe.reader:id/fileName").exists():
           self.poco(name="com.adobe.reader:id/fileName").click()
        # sleep(4)
        # self.poco(name="com.adobe.reader:id/file_overflow_icon").click()


    def click_Share_On_Adobe(self):
        sleep(4)
        self.poco(name="com.adobe.reader:id/classic_viewer_share_file").click()

    def click_Send_A_Copy_On_Adobe(self):
        sleep(2)
        self.poco(text="Send a copy").click()

    def click_Common_Design(self):
        sleep(2)
        self.poco(name="Common Designs").click()

    def click_First_Image_ON_The_List(self):
        sleep(3)
        self.poco(name="android.view.View").click()
        sleep(3)

    def click_firstimage_on_firstone(self):
        sleep(4)
        self.poco(name="android.view.View").click()

    def click_print_Button(self):
        sleep(4)
        self.poco(name="Print").click()

    def click_Print2_button(self):
        sleep(4)
        if self.poco(name="Print").exists():
            self.poco(name="Print").click()
        else:
            poco.scroll()
            sleep(2)
            self.poco(name="Print").click()

    def click_Back_Icon(self):
        sleep(1)
        self.poco(name="android.widget.Button").click()

    def click_And_Enter_Invalid_Number_In_Copies_Number_Field(self):
        def click_And_Enter_Copies_Number_Field(self):
            sleep(1)
            poco.scroll()
            Copies_Number_Field = self.poco(name="android.widget.EditText")
            Copies_Number_Field.click()
            sleep(1)
            Copies_Number_Field.set_text(" ")
            sleep(1)
            Copies_Number_Field.set_text(".")

    def Verify_Print_Is_GreyedOut(self):
        sleep(1)
        if not self.poco(name="Print").exists():
            print("Print is greyed out")
        else:
            print("print is displaying")

    def click_And_Enter_2Copies_Number_Field(self):
        sleep(1)
        poco.scroll()
        Copies_Number_Field = self.poco(name="android.widget.EditText")
        Copies_Number_Field.click()
        sleep(1)
        Copies_Number_Field.set_text(" ")
        sleep(1)
        Copies_Number_Field.set_text("2")

    def Verify_Printer_Not_Found_Popup(self):
        sleep(5)
        a= self.poco(nameMatches="(?s).*Printer Not Found.*")
        if a.exists():
           a.get_name()
           print(a)

    def click_Continue_Button(self):
        sleep(2)
        if self.poco(name="Continue").exists():
            self.poco(name="Continue").click()