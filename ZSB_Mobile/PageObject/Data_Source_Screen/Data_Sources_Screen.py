# LoginFunction.py

import datetime
import random
import string
import fnmatch

from airtest.core.api import *
# import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoNoSuchNodeException
from poco.exceptions import PocoTargetTimeout
import platform
if platform.system() == "Windows":
    def Basic_path(a):
        return os.path.join(os.path.expanduser('~'),
                            "OneDrive - Zebra Technologies\Documents\ZSB\AirTest_ZSB_Mobile_Automation\ZSB_Mobile\\templates", a)

else:
    def Basic_path(a):
        return os.path.join("/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/templates", a)

from ...Common_Method import Common_Method
from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen

login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
common_method = Common_Method(poco)
registration_page = Registration_Screen(poco)


class Data_Sources_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Home = "Home"
        self.My_Data = "My Data"
        self.Add_File = "android.widget.Button"
        self.Upload_File = "android.widget.Button"
        self.File_Data_Source_Device_Local_File = "Local File"
        self.File_Data_Source_Device_GDrive = "Google Drive"
        self.File_Data_Source_Device_OneDrive = "OneDrive"
        self.My_Designs = "My Designs"
        self.Allow_Permission = "com.android.permissioncontroller:id/permission_allow_button"
        self.Print_Btn = "Print"
        self.Photo_Options = "android.view.View"
        self.Camera = "Camera"
        self.Remove_Btn = "Remove"
        self.Cancel_Btn = "Cancel"
        self.HamburgerMenuLocalStorage = "Show roots"
        self.Create_New_Design = "Create New Design"
        self.Create_Btn = "Create"
        self.Camera_Shutter = "com.google.android.GoogleCamera:id/shutter_button"
        self.google_search_feild = "com.google.android.googlequicksearchbox:id/googleapp_hint_text"
        self.google_text_field = "com.google.android.googlequicksearchbox:id/googleapp_search_box"
        self.Bar_Code_Location = Template(Basic_path(r"tpl1707978279280.png"), record_pos=(-0.055, 0.03), resolution=(1080, 2340))
        self.File_Info_Device = []
        self.use_image_button = "com.android.camera:id/done_button"
        self.File_Info_App = []
        self.Name = "Name"
        self.Month = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
                      7: "Jul", 8: "Aug", 9: "Sept", 10: "Oct", 11: "Nov", 12: "Dec"}
        self.List_Empty = "List is empty"
        self.Date_Added = "DATE ADDED"
        self.Continue = "Continue"
        self.Check_Box = "android.widget.CheckBox"
        self.Confirm_Btn = "Confirm"
        self.Label_Range = 0
        self.Use_Local_Contacts = "Use Local Contacts"
        self.Search_Files = Template(Basic_path(r"tpl1705645360605.png"), record_pos=(-0.261, -0.571), resolution=(1080, 2340))
        self.expectedSearchList = ["Tes1.jpg", "Test2.png", "Test3.bmp"]
        self.Sign_In_With_Microsoft = "Sign in with Microsoft"
        self.Sign_In_With_Microsoft_Template = Template(Basic_path("Microsoft_Icon.png"), record_pos=(-0.194, -0.602), resolution=(1080, 2400))
        self.test_45738 = Template(Basic_path(r"tpl1706683702494.png"), record_pos=(0.0, -0.264), resolution=(1080, 2340))
        self.Sign_In_With_Google = "Sign in with Google"
        self.Sign_In_With_Google_Template = Template(Basic_path("Google_Icon.png"), record_pos=(-0.006, 0.017),
            resolution=(1080, 2340))
        self.Select = "Select"
        self.File_Name_Web = ""
        # self.search_File_Name = ""
        self.is_already_linked = Template(Basic_path(r"tpl1706012736859.png"), record_pos=(-0.139, 0.898), resolution=(1080, 2340))
        self.Use_Your_Password_Instead = "idA_PWD_SwitchToPassword"
        self.Enter_Password = Template(Basic_path(r"Password.png"), record_pos=(-0.063, -0.556), resolution=(1080, 2340))
        self.search_Files_In_Link_Files = Template(Basic_path(r"search_files_link_files.png"), record_pos=(-0.247, -0.567),
                                                   resolution=(1080, 2340))

    def click_My_Data(self):
        sleep(3)
        my_data = self.poco(self.My_Data)
        my_data.click()
        sleep(3)

    def click_Add_File(self):
        sleep(2)
        add_file = self.poco(self.Add_File)[-1]
        add_file.wait_for_appearance(timeout=10)
        add_file.click()

    def click_Upload_File(self):
        upload_file = self.poco("android.widget.Button")[-2]
        upload_file.click()
        if self.poco(text="Allow").exists():
            self.poco(text="Allow").click()

    def click_Upload_File_Web(self):
        upload_file = self.poco(self.Upload_File)
        upload_file[3].click()

    def click_Media_Picker_Web(self):
        media_picker = self.poco("android.widget.LinearLayout")[5]
        media_picker.click()

    def click_Link_File(self):
        link_file = self.poco("android.widget.Button")[-3]
        link_file.wait_for_appearance(timeout=10)
        link_file.click()
        sleep(2)

    def chooseAccToLinkFile(self, Acc_Name="Zsb Swdvt"):
        sleep(3)
        account = self.poco(text=Acc_Name)
        count = 5
        while not account.exists() and count != 0:
            self.poco.scroll()
            count -= 1
        account.click()
        sleep(4)
        if self.poco(
                textMatches=".*By continuing, Google will share your name, email address, language preference, and profile picture with ZSB Series. See ZSB Series’s.*").exists():
            self.clickContinueWeb()
        elif self.poco(text="Sign in to ZSB Series").exists():
            self.clickContinueWeb()
        sleep(3)

    def select_File_To_Upload(self, return_name=False):
        name_on_device = self.poco("com.google.android.documentsui:id/item_root")[0].child(
            "android.widget.LinearLayout").child("android.widget.LinearLayout").offspring("android:id/title").get_text()
        self.File_Info_Device.append(name_on_device)
        file = self.poco("com.google.android.documentsui:id/item_root")[0].child("android.widget.LinearLayout").child(
            "android.widget.LinearLayout").offspring("android:id/title")
        file.click()
        if return_name:
            return name_on_device

    def checkWebUploadedFileOnApp(self):
        self.searchName(self.File_Name_Web)
        if self.poco("android.widget.HorizontalScrollView").child()[1] == "DATE ADDED":
            if self.poco("android.widget.HorizontalScrollView").child()[2] == self.File_Name_Web:
                return
            else:
                print("Error! File not uploaded")
                return 1 / 0
        else:
            if self.poco("android.widget.HorizontalScrollView").child()[1] == self.File_Name_Web:
                return
            else:
                print("Error! File not uploaded")
                return 1 / 0

    def verify_File_Data(self, file_name, data_source):
        self.verifyFilePresentInList(file_name, data_source, True, True)

        # name_app = self.poco("android.widget.HorizontalScrollView").child()[-4].get_name()
        # self.File_Info_App.append(name_app)
        # year = datetime.date.today().year
        # date = datetime.date.today().day
        # month = self.Month[datetime.date.today().month]
        # date_app = self.poco("android.widget.HorizontalScrollView").child()[-3].get_name()
        # self.File_Info_App.append(date_app)
        # data_source_app = self.poco("android.widget.HorizontalScrollView").child()[-2].get_name()
        # self.File_Info_App.append(data_source_app)
        # expected_date = str(month) + " " + str(date) + ", " + str(year)
        # self.File_Info_Device.append(expected_date)
        # self.File_Info_Device.append(self.File_Data_Source_Device_Local_File)
        # for i in range(len(self.File_Info_App)):
        #     if self.File_Info_App[i] == self.File_Info_Device[i]:
        #         return
        #     else:
        #         raise Exception("File data does not match")

    def clickMyDesigns(self):
        sleep(6)
        my_designs = self.poco(self.My_Designs)
        my_designs.click()

    def selectDesignCreatedAtSetUp(self):
        self.poco(nameMatches="Showing.*").wait_for_appearance(timeout=10)
        set_up_design = self.poco("android.view.View")[5]
        set_up_design.click()

    def selectDesignCreatedAtSetUpWeb(self):
        self.poco(textMatches="Showing.*").wait_for_appearance(timeout=10)
        set_up_design = self.poco("android.widget.Image")[1]
        set_up_design.click()

    def selectSecondDesign(self):
        self.poco(nameMatches="Showing.*").wait_for_appearance(timeout=10)
        set_up_design = self.poco("android.view.View")[6]
        set_up_design.click()

    def scroll_till_print(self):
        count = 5
        while not self.poco(self.Print_Btn).exists() and count != 0:
            self.poco.scroll()
            count -= 1
        self.poco.scroll()
        sleep(2)

    def clickPrint(self):
        while not self.poco("Print").exists():
            self.poco.scroll()
        self.poco.scroll()
        if self.poco(self.Print_Btn).exists():
            print_btn = self.poco(self.Print_Btn)
        else:
            print_btn = self.poco(text=self.Print_Btn)
        print_btn.wait_for_appearance(timeout=10)
        print_btn.click()

    def verifyPhotoOptions(self):
        photo_options = self.poco(self.Photo_Options)[4]
        photo_options.exists()

    def expandPhotoOptions(self):
        photo_options = self.poco(self.Photo_Options)[4]
        photo_options.click()

    def chooseCameraToClickPhoto(self):
        camera = self.poco(self.Camera)
        camera.wait_for_appearance(timeout=20)
        camera.click()

    def clickPhoto(self):
        click_photo = self.poco(self.Camera_Shutter)
        click_photo.wait_for_appearance(timeout=10)
        click_photo.click()
        sleep(5)
        click_photo.click()

    def clickThreeDotsMyData(self):
        three_dots = self.poco("android.widget.HorizontalScrollView").child("android.view.View").child(
            "android.widget.Button")
        three_dots.click()

    def add_new_tab_in_browser(self):
        try:
            self.poco("com.android.chrome:id/new_tab_view_button").click()
        except:
            self.poco(text="New tab").click()

    def clickRemove(self):
        remove_btn = self.poco(self.Remove_Btn)
        remove_btn.click()

    def clickCancel(self):
        cancel_btn = self.poco(self.Cancel_Btn)
        cancel_btn.wait_for_appearance(timeout=10)
        cancel_btn.click()

    def verifyRemovedSuccessfully(self):
        file_name = self.poco("android.widget.HorizontalScrollView").child()[-4].get_name()
        self.poco(file_name).not_exists()

    def verifyProgressIndicator(self):
        if self.poco(self.Name).exists():
            print("Progress indicator did not appear")
            return 1 / 0
        else:
            return

    def click_google_search_bar(self):
        google_search_bar = self.poco(self.google_search_feild)
        google_search_bar.click()

    def enter_the_text_in_goole(self, String):
        self.poco(self.google_text_field).set_text(String)

    def clickEnter(self):
        keyevent("Enter")

    def click_Menu_HamburgerICNWeb(self):
        sleep(3)
        try:
            self.poco("zsbportal.zebra").click()
        except:
            self.poco("android.widget.Image").click()

    def clickCreateDesignBtn(self):
        if self.poco(text=self.Create_Btn).exists():
            self.poco(text=self.Create_Btn).click()
        else:
            self.poco.scroll()
            self.poco(self.Create_New_Design).click()

    def selectLabelSize(self):
        self.poco("android.view.View")[16].click()

    def set_text(self, value):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(value)

    def clickContinue(self):
        try:
            sleep(20)
            self.poco(self.Continue).click()
        except:
            sleep(10)
            self.poco(name="continueBtn").click()

    def clickContinueWeb(self):
        self.poco(text="Continue").wait_for_appearance(timeout=10)
        self.poco(text="Continue").click()

    def clickAddBarcode(self):
        self.poco(text="Add barcode").wait_for_appearance(timeout=10)
        self.poco(text="Add barcode").click()

    def placeBarcode(self):
        touch(self.Bar_Code_Location)

    def exit_pop_up_after_placing_element_in_new_design(self):
        sleep(2)
        self.poco("android.webkit.WebView").focus([0.1, 0.3]).click()

    def clickAddText(self):
        self.poco(text="Add text").wait_for_appearance(timeout=10)
        self.poco(text="Add text").click()

    def placeText(self):
        touch(Template(Basic_path(r"Text_Location.png"), record_pos=(0.072, 0.32), resolution=(1080, 2400)))

    def exitDesigner(self):
        self.poco("android.widget.Button").wait_for_appearance(timeout=10)
        self.poco("android.widget.Button").click()

    def uploadFileWeb(self):
        self.poco("android.widget.Button")[1].click()

    def selectFileToUploadWeb(self):
        selected_file_name = self.poco("android.widget.LinearLayout")[5].child("android:id/title").get_text()
        self.poco("android.widget.LinearLayout")[5].child("android:id/title").click()
        return selected_file_name

    def setLabelName(self, name):
        self.poco("android.widget.Image")[1].click()
        sleep(2)
        self.poco("android.widget.TextView")[1].click()
        sleep(2)
        self.poco("android.widget.EditText").set_text(name)
        keyevent("Enter")

    def getCurrCount(self, after_swipe=False, scroll_count=1):
        if after_swipe:
            """Change on mac"""
            if scroll_count == 0:
                return (len(self.poco("android.widget.HorizontalScrollView").child()) - 2) // 4
            else:
                return (len(self.poco("android.widget.HorizontalScrollView").child())) // 4
        else:
            if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
                if self.poco("android.widget.HorizontalScrollView").child()[2].get_name() == "DATA SOURCE":
                    return (len(self.poco("android.widget.HorizontalScrollView").child()) - 3) // 3
                return (len(self.poco("android.widget.HorizontalScrollView").child()) - 2) // 2
            elif self.poco("android.widget.HorizontalScrollView").child()[0].get_name() == "DATE ADDED":
                return (len(self.poco("android.widget.HorizontalScrollView").child()) - 2) // 4
            else:
                return len(self.poco("android.widget.HorizontalScrollView").child()) - 1

    # def countNumberOfFiles(self):
    #     count = 0
    #     temp = []
    #     current_last_child = self.poco("android.widget.HorizontalScrollView").child()[-1].get_name()
    #     count += self.getCurrCount()
    #     while True:
    #         common_method.swipe_screen([0.5, 0.9175213675213675], [0.5, 0.080], 1)
    #         for i in range(1, self.getCurrCount()+1):
    #             temp.append(self.poco("android.widget.HorizontalScrollView").child()[i].get_name())
    #         curr_child_list = temp
    #         temp = []
    #         new_last_child = self.poco("android.widget.HorizontalScrollView").child()[-1].get_name()
    #         if current_last_child in curr_child_list:
    #             count += self.getCurrCount() - (curr_child_list.index(new_last_child)+1)
    #             break
    #         else:
    #             count += self.getCurrCount()
    #             current_last_child = new_last_child
    #     return count

    def fileListDisplayed(self, no_of_swipes=False):
        File_List = []
        if self.poco("You don’t have any files").exists():
            return File_List
        scroll_view = self.poco("android.widget.HorizontalScrollView")
        while not self.poco("NAME").exists():
            scroll_view.swipe("right")
        for i in range(5):
            scroll_view.swipe("right")
        # temp = []
        # swipe_count = 0
        # if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
        #     if self.poco("android.widget.HorizontalScrollView").child()[2].get_name() == "DATA SOURCE":
        #         if self.poco("android.widget.HorizontalScrollView").child()[-1].get_name() == "android.view.View":
        #             current_last_child = self.poco("android.widget.HorizontalScrollView").child()[-4].get_name()
        #         else:
        #             current_last_child = self.poco("android.widget.HorizontalScrollView").child()[-3].get_name()
        #     else:
        #         current_last_child = self.poco("android.widget.HorizontalScrollView").child()[-2].get_name()
        # else:
        #     current_last_child = self.poco("android.widget.HorizontalScrollView").child()[-1].get_name()
        # for i in range(1, self.getCurrCount() + 1):
        #     if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
        #         if self.poco("android.widget.HorizontalScrollView").child()[2].get_name() == "DATA SOURCE":
        #             File_List.append(self.poco("android.widget.HorizontalScrollView").child()[3 * i].get_name())
        #         else:
        #             File_List.append(self.poco("android.widget.HorizontalScrollView").child()[2 * i].get_name())
        #     else:
        #         File_List.append(self.poco("android.widget.HorizontalScrollView").child()[i].get_name())
        # while True:
        #     self.poco.scroll()
        #     swipe_count += 1
        #     for i in range(1, self.getCurrCount() + 1):
        #         if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
        #             if self.poco("android.widget.HorizontalScrollView").child()[2].get_name() == "DATA SOURCE":
        #                 temp.append(self.poco("android.widget.HorizontalScrollView").child()[3 * i].get_name())
        #             else:
        #                 temp.append(self.poco("android.widget.HorizontalScrollView").child()[2 * i].get_name())
        #         else:
        #             temp.append(self.poco("android.widget.HorizontalScrollView").child()[i].get_name())
        #     if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
        #         if self.poco("android.widget.HorizontalScrollView").child()[2].get_name() == "DATA SOURCE":
        #             if self.poco("android.widget.HorizontalScrollView").child()[-1].get_name() == "android.view.View":
        #                 new_last_child = self.poco("android.widget.HorizontalScrollView").child()[-4].get_name()
        #             else:
        #                 new_last_child = self.poco("android.widget.HorizontalScrollView").child()[-3].get_name()
        #         else:
        #             new_last_child = self.poco("android.widget.HorizontalScrollView").child()[-2].get_name()
        #     else:
        #         new_last_child = self.poco("android.widget.HorizontalScrollView").child()[-1].get_name()
        #     if current_last_child in temp:
        #         index_from = temp.index(current_last_child) + 1
        #         for i in range(index_from, len(temp)):
        #             File_List.append(temp[i])
        #         if temp[-1] == current_last_child:
        #             break
        #     else:
        #         for i in range(len(temp)):
        #             File_List.append(temp[i])
        #         current_last_child = new_last_child
        #     temp = []
        # while not self.poco("NAME").exists():
        #     scroll_view = self.poco("android.view.View")
        #     scroll_view.swipe("down")
        # if not no_of_swipes:
        #     return File_List
        # else:
        #     return File_List, swipe_count

        prev = []
        File_List = []

        while 1:
            curr = [child.get_name() for child in self.poco("android.widget.HorizontalScrollView").children()]
            for i in curr:
                if ((".png" in i) or (".jpg" in i) or (".txt" in i) or (".csv" in i) or (".xlsx" in i) or (
                        "bmp" in i)) and (i not in File_List):
                    File_List.append(i)

            if prev == curr:
                break
            prev = curr
            self.poco.scroll()
        while not self.poco("NAME").exists():
            scroll_view = self.poco("android.view.View")
            scroll_view.swipe("down")
        return File_List

    def selectFileWithExtension(self, extension):
        prev_last_child = None
        start = 1
        while True:
            child_count = len(self.poco("android.widget.HorizontalScrollView").child())
            curr_last_child = self.poco("android.widget.HorizontalScrollView").child()[child_count - 1].get_name()
            if prev_last_child == curr_last_child:
                break
            for i in range(start, child_count):
                if self.poco("android.widget.HorizontalScrollView").child()[i].get_name().split(".")[1] == extension:
                    self.poco("android.widget.HorizontalScrollView").child()[i].click()
                    return self.poco("android.widget.HorizontalScrollView").child()[i].get_name()
            self.poco.scroll()
            start = 0

    def select_file_link_drive(self, filename):
        prev_last_child = None
        start = 1
        while True:
            child_count = len(self.poco("android.widget.HorizontalScrollView").child())
            curr_last_child = self.poco("android.widget.HorizontalScrollView").child()[child_count - 1].get_name()
            if prev_last_child == curr_last_child:
                break
            for i in range(start, child_count):
                if self.poco("android.widget.HorizontalScrollView").child()[i].get_name() == filename:
                    self.poco("android.widget.HorizontalScrollView").child()[i].click()
                    return self.poco("android.widget.HorizontalScrollView").child()[i].get_name()
            self.poco.scroll()
            start = 0

    def verifyDesign(self, labelname):
        label_name_len = len(labelname)
        if len(self.poco("android.view.View")[5].child()) == 1:
            return
        else:
            print("Label created not found")
            return 1 / 0
        # design_name = poco("android.view.View")[5].child().get_name()
        # if design_name[:label_name_len] == LabelName:
        #     return
        # else:
        #

    def searchName(self, name, search=True):
        sleep(3)
        self.poco("android.widget.EditText").click()
        sleep(2)
        self.poco("android.widget.EditText").set_text(name)
        sleep(2)
        if search:
            self.clickEnter()
        sleep(7)

    def searchExistingName(self):
        if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
            if self.poco("android.widget.HorizontalScrollView").child()[2].get_name() == "DATA SOURCE":
                search_text = self.poco("android.widget.HorizontalScrollView").child()[3].get_name()
            else:
                search_text = self.poco("android.widget.HorizontalScrollView").child()[2].get_name()
        else:
            search_text = self.poco("android.widget.HorizontalScrollView").child()[1].get_name()
        self.searchName(search_text)
        sleep(7)

    def checkIfResultsAreFiltered(self, initial_file_count, final_file_count):
        if initial_file_count <= 1:
            print("Cannot determine please add more than 1 photo")
            return 1 / 0
        else:
            if final_file_count < initial_file_count:
                return
            else:
                print("Files are not filtered")
                return 1 / 0

    def checkFileNotRemovedAfterClickingCancel(self, filename, datasource):
        try:
            self.verifyFilePresentInList(filename, datasource, True)
        except:
            raise Exception("File removed even after clicking cancel")

    def checkFileRemovedSuccessfully(self, filename, datasource):
        try:
            self.verifyFilePresentInList(filename, datasource, True)
            x = 1 / 0
        except ZeroDivisionError:
            raise Exception("File not removed")
        except Exception as e:
            pass
        sleep(3)

    def generateRandomWord(self, length):
        return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))

    def generateRandomWordLetters(self, length):
        return ''.join(random.choice(string.ascii_letters) for i in range(length))

    def checkIfListIsEmpty(self):
        try:
            self.poco(self.List_Empty).wait_for_appearance(timeout=10)
        except:
            raise Exception("List not empty")

    def searchRandomWord(self):
        random_word = self.generateRandomWord(64)
        self.searchName(random_word)
        sleep(7)

    def enterSpecialCharactersInsearchField(self):
        special_char_word = ''.join(
            [random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(12)])
        self.searchName(special_char_word)
        sleep(7)
        if self.poco(self.Date_Added).exists():
            return
        else:
            print("Error pop up")
            return 1 / 0

    def clearTextAndVerifyFileCount(self, initial_count):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text("")
        keyevent("Enter")
        sleep(7)
        count_after_clearing_text = len(self.fileListDisplayed())
        if count_after_clearing_text == initial_count:
            return
        else:
            print("All files not shown on clearing")
            return 1 / 0

    def updateDataConnections_contacts(self):
        drop_down_data_sources = self.poco("android.view.View")[3].child()[2]
        drop_down_data_sources.click()
        local_contacts = self.poco(self.Use_Local_Contacts)
        local_contacts.click()

    def clickAllow(self):
        allow_button = self.poco(self.Allow_Permission)
        allow_button.click()

    def clickAllow_Text(self):
        allow_button = self.poco(text="Allow")
        allow_button.click()

    def chooseAnOption1(self):
        self.poco("android.view.View")[4].child()[1].child()[3].click()

    def chooseAnOption2(self):
        self.poco("android.view.View")[4].child()[1].child()[5].click()

    def chooseAnOption3(self):
        self.poco("android.view.View")[4].child()[1].child()[7].click()

    def verifyIfPreviewIsPresent(self):
        if self.poco("android.widget.ImageView")[1].exists():
            return
        else:
            raise Exception("Preview not shown")

    def checkPrintIsDisabled(self):
        if self.poco("Print", enabled=False).exists():
            pass
        else:
            raise Exception("Print is Enabled")

    def selectLabelRange(self, label_range):
        self.Label_Range = label_range
        checkbox = self.poco(self.Check_Box)
        self.poco("android.widget.ScrollView").child()[5].click()
        checkbox[0].click()
        checkbox[0].click()
        for i in range(label_range):
            checkbox[3 + i].click()

    def clickCheckBox(self, checkbox_number=0):
        checkbox = self.poco(self.Check_Box)
        checkbox[checkbox_number].click()

    def clickLabelRange(self):
        self.poco("android.widget.ScrollView").child()[-7].click()

    def getRowIndex(self):
        return self.poco("android.widget.ScrollView").child()[6].get_name()

    def clickConfirm(self):
        self.poco(self.Confirm_Btn).click()

    def selectPrinter(self):
        printer = self.poco("android.view.View")[6].child()[0]
        printer.click()

    def previewLabelRange(self):
        if self.Label_Range > 9:
            if self.poco("android.widget.ScrollView").child()[5].get_name()[-2:] == str(self.Label_Range):
                return
            else:
                print("Label Range Doesn't match")
                return 1 / 0

        else:
            if self.poco("android.widget.ScrollView").child()[5].get_name()[-1:] == str(self.Label_Range):
                return
            else:
                print("Label Range Doesn't match")
                return 1 / 0

    def clickGoogleDrive(self):
        google_drive = self.poco("android.view.View")[3].child()[1]
        google_drive.click()

    def clickMicrosoftOneDrive(self):
        one_drive = self.poco(nameMatches="(?s).*Microsoft OneDrive.*")
        one_drive.wait_for_appearance(timeout=10)
        one_drive.click()

    def searchTest(self, searchText, subscript_i=0):
        touch(self.Search_Files)
        if searchText == "test":
            """Unable to search"""
            actual_search_list = []
            search_list = self.poco("android.widget.EditText").child().child()
            file_count = len(search_list.child())
            """Unable to find number of files"""
            if file_count == 3:
                for i in range(3):
                    actual_search_list.append(search_list.child()[2 + i].get_name())
            else:
                print("search not functional")
                return 1 / 0

            for i in actual_search_list:
                if i in self.expectedSearchList:
                    return
                else:
                    print(f"{i} is not expected in the search results")
                    return 1 / 0
        elif searchText == "test_i":
            search_list = self.poco("android.widget.EditText").child().child()
            """Unable to search"""
            file_count = len(search_list.child())
            file_name = search_list.child()[2].get_name()
            if file_count == 1:
                if file_name == f"Test{subscript_i}{file_name[-4]}":
                    return
            else:
                print("search not functional")
                return 1 / 0
        elif searchText in ("jpg", ".png", ".bmp"):
            search_list = self.poco("android.widget.EditText").child().child()
            """Unable to find number of files"""
            for i in range(1):
                if search_list.child()[2 + i].get_name[-4] == searchText:
                    return
                else:
                    print(f"File {i} is not a {searchText} file.")
                    return 1 / 0
        else:
            search_list = self.poco("android.widget.EditText").child().child()
            file_count = len(search_list.child())
            """Unable to find number of files"""
            if file_count == 0:
                return

    def verifySignInWithMicrosoft(self):
        try:
            assert_exists(self.Sign_In_With_Microsoft_Template)
            return True
        except:
            return False

    def verifySignInWithGoogle(self):
        try:
            sleep(2)
            self.poco("Sign in with Google").exists()
            return True
        except:
            try:
                assert_exists(self.Sign_In_With_Google_Template)
                return True
            except:
                return False

    def signInWithMicrosoft(self, username, password, click_template=True):
        # if self.poco(self.Sign_In_With_Microsoft).exists():
        #     sign_in_with_microsoft = self.poco(self.Sign_In_With_Microsoft)
        #     sign_in_with_microsoft.click()
        # else:
        sleep(2)
        if click_template:
            touch(self.Sign_In_With_Microsoft_Template)
            sleep(5)
            self.Turn_Off_The_Phone()
            sleep(3)
            self.Turn_ON_The_Phone()
            sleep(3)
        self.Turn_Off_The_Phone()
        sleep(3)
        self.Turn_ON_The_Phone()
        sleep(3)
        try:
            sleep(5)
            self.poco("android.widget.EditText").set_text(username)
        except:
            # username = "zebra03.swdvt@gmail.com"
            self.poco("i0116").set_text(username)
        self.poco(text="Next").click()
        sleep(3)
        self.Turn_Off_The_Phone()
        sleep(3)
        self.Turn_ON_The_Phone()
        sleep(3)
        self.Turn_Off_The_Phone()
        sleep(3)
        self.Turn_ON_The_Phone()
        sleep(3)
        if self.poco(self.Use_Your_Password_Instead).exists():
            self.poco(self.Use_Your_Password_Instead).click()
            sleep(2)
        self.Turn_Off_The_Phone()
        sleep(3)
        self.Turn_ON_The_Phone()
        sleep(3)
        try:
            sleep(5)
            self.poco("android.widget.EditText").set_text(password)
        except:
            # username = "zebra03.swdvt@gmail.com"
            self.poco("i0118").set_text(password)
        # password = "Zebra#123456789"
        # self.poco(text(password))
        self.poco(text="Sign in").click()
        if self.poco("Continue").exists():
            self.clickContinue()

    def enterMicrosoftUsername(self, username):
        sleep(3)
        self.Turn_Off_The_Phone()
        sleep(3)
        self.Turn_ON_The_Phone()
        sleep(3)
        try:
            self.poco("android.widget.EditText").wait_for_appearance(timeout=20)
            self.poco("android.widget.EditText").click()
            self.poco("android.widget.EditText").set_text(username)
        except:
            self.poco("i0116").wait_for_appearance(timeout=20)
            self.poco("i0116").click()
            # username = "zebra03.swdvt@gmail.com"
            self.poco("i0116").set_text(username)
        self.poco(text="Next").click()
        sleep(3)
        self.Turn_Off_The_Phone()
        sleep(3)
        self.Turn_ON_The_Phone()
        sleep(3)

    def checkIfAccPresentLink(self, account):
        start = 0
        end = 1
        while True:
            for i in range(start, len(self.poco("com.google.android.gms:id/list").child()) - end):
                if self.poco("com.google.android.gms:id/list").child()[i].child()[
                    1].get_text() == "Add another account":
                    return False
                elif self.poco("com.google.android.gms:id/list").child()[i].child()[1].child()[1].get_text() == account:
                    return True
            start = 1
            end = 0
            self.poco.scroll()

    def signInWithGoogle(self, username, password):
        if self.poco(self.Sign_In_With_Google).exists():
            sign_in_with_google = self.poco(self.Sign_In_With_Google)
            sign_in_with_google.click()
        else:
            touch(self.Sign_In_With_Google_Template)
        sleep(4)
        if self.poco("com.google.android.gms:id/add_account_chip_title").exists():
            self.poco("com.google.android.gms:id/add_account_chip_title").click()
        self.poco("android.widget.TextView").wait_for_appearance(timeout=10)
        self.poco("android.widget.TextView")[2].click()
        sleep(3)
        if self.poco(text="Close").exists():
            self.poco(text="Close").click()
        try:
            self.poco("identifierId").set_text(username)
        except:
            self.poco("android.widget.EditText").set_text(username)
        sleep(3)
        self.poco(text="Next").click()
        sleep(3)
        self.poco("android.widget.EditText").set_text(password)
        sleep(3)
        self.poco(text="Next").click()
        self.poco.scroll()
        if self.poco(text="Skip").exists():
            self.poco(text="Skip").click()
        if self.poco(text="I agree").exists():
            self.poco(text="I agree").click()
        self.poco.scroll()
        if self.poco(text="Accept").exists():
            self.poco(text="Accept").click()
        if self.poco(text="Continue").exists():
            self.poco(text="Continue").click()
        if self.poco(text="Not now").exists():
            self.poco(text="Not now").click()

    def clickSignIn(self):
        sleep(2)
        signInBtn = self.poco("Sign In")
        signInBtn.click()
        if self.poco("Allow").exists():
            self.poco("Allow").click()
        elif self.poco(text="Allow").exists():
            self.poco(text="Allow").click()
        sleep(4)

    def close_app_reopen_and_click_sign_in(self):
        packagename = "com.zebra.soho_app"
        stop_app(packagename)
        sleep(1)
        start_app(packagename)
        sleep(5)
        self.allowPermissions()
        self.clickSignIn()

    def signInWithEmail(self):
        pocoEle = self.poco(text="Sign In with your email")
        if pocoEle.exists():
            pocoEle.click()
        else:
            self.close_app_reopen_and_click_sign_in()
            pocoEle.click()
        print("Successfully clicked Sign In With Email")
        sleep(2)
        if self.poco("com.android.chrome:id/coordinator").exists():
            self.poco("com.android.chrome:id/coordinator").click()
        keyevent("Enter")
        sleep(2)

    def clickBackArrow(self):
        sleep(2)
        back_arrow = self.poco(name="android.widget.Button", enabled=True)
        back_arrow.wait_for_appearance(timeout=20)
        back_arrow.click()
        sleep(4)

    def checkNoChangeInFileCount(self, initialFileCount):
        file_list = self.fileListDisplayed()
        curr_file_count = len(file_list)
        print(initialFileCount, curr_file_count)
        if initialFileCount == curr_file_count:
            return
        else:
            raise Exception("Number of files are not same as before")

    def checkFilesShownAreSupported(self):
        supported_types = ["jpg", "png", "bmp", "txt", "xlsx", "csv", ""]
        file_list = self.fileListDisplayed()
        for i in file_list:
            if self.substring_after(i, ".") in supported_types:
                return
            else:
                raise Exception(str(i) + " is not of supported format")

    def clickSelect(self):
        select = self.poco(self.Select)
        select.click()

    def substring_after(self, s, delim):
        return s.partition(delim)[2]

    def selectLargeFile(self):
        if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
            search_File_Name = self.poco("android.widget.HorizontalScrollView").child()[4].get_name()
            self.poco("android.widget.HorizontalScrollView").child()[4].click()
            self.clickSelect()
        else:
            search_File_Name = self.poco("android.widget.HorizontalScrollView").child()[2].get_name()
            self.poco("android.widget.HorizontalScrollView").child()[2].click()
            self.clickSelect()

    def selectFile(self):
        if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
            search_File_Name = self.poco("android.widget.HorizontalScrollView").child()[2].get_name()
            self.poco("android.widget.HorizontalScrollView").child()[2].click()
            self.clickSelect()
        else:
            search_File_Name = self.poco("android.widget.HorizontalScrollView").child()[1].get_name()
            self.poco("android.widget.HorizontalScrollView").child()[1].click()
            self.clickSelect()
        return search_File_Name

    def selectExistingFile(self):
        if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
            search_File_Name = self.poco("android.widget.HorizontalScrollView").child()[3].get_name()
            self.poco("android.widget.HorizontalScrollView").child()[3].click()
            self.clickSelect()
        else:
            search_File_Name = self.poco("android.widget.HorizontalScrollView").child()[2].get_name()
            self.poco("android.widget.HorizontalScrollView").child()[2].click()
            self.clickSelect()

        return search_File_Name

    def checkIsAlreadyLinkedPopUp(self):
        try:
            self.poco(nameMatches=".*is already linked.*").wait_for_appearance(timeout=20)
        except:
            raise Exception("File already linked pop up not present.")

    def searchFilesInLinkFiles(self, file_name):
        self.poco("android.widget.EditText").focus([0.5, 0.05]).click()
        self.poco("android.widget.EditText").set_text(file_name)
        keyevent("Enter")

    def verifyFilePresentInList(self, file_name, datasource=None, data=False, verify_date=True):
        if self.poco(self.List_Empty).exists():
            raise Exception(file_name + " File not present")
        file_list = self.fileListDisplayed()
        print(len(file_list), "->", file_list)
        scroll_view = self.poco("android.widget.HorizontalScrollView")
        while not self.poco("DATA SOURCE").exists():
            scroll_view.swipe("left")
        for j in range(5):
            scroll_view.swipe("left")
        """Change on mac"""
        for i in range(len(file_list)):
            if not data:
                print(file_list[i], "fn:", file_name)
                if file_list[i] == file_name:
                    while not self.poco("NAME").exists():
                        scroll_view.swipe("right")
                    for j in range(5):
                        scroll_view.swipe("right")
                    return
            else:
                year = datetime.date.today().year
                date = datetime.date.today().day
                month = self.Month[datetime.date.today().month]
                date_app = self.poco("android.widget.HorizontalScrollView").child()[3 + 4 * i].get_name()
                print(date_app)
                data_source_app = self.poco("android.widget.HorizontalScrollView").child()[4 + 4 * i].get_name()
                print(data_source_app)
                expected_date = str(month) + " " + str(date) + ", " + str(year)
                print(expected_date)
                name_app = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
                print(name_app, file_name)
                if name_app == file_name:
                    if datasource is not None:
                        if datasource == data_source_app:
                            scroll_view = self.poco("android.widget.HorizontalScrollView")
                            while not self.poco("NAME").exists():
                                scroll_view.swipe("right")
                            for j in range(5):
                                scroll_view.swipe("right")
                            return
                    if verify_date:
                        if date_app == expected_date:
                            pass
                        else:
                            if i == len(file_list) - 1:
                                raise Exception("Date not matching")
        raise Exception(file_name + " File not present")

    def clickHome(self):
        home_btn = self.poco(self.Home)
        home_btn.wait_for_appearance(timeout=10)
        home_btn.click()

    def verify_Remove_File_Warning(self, file_type):
        if file_type == "Local File":
            if self.poco("Are you sure you want to remove the local file? All fields using this data source will need to be reconnected to a data source.").exists():
                return
            else:
                raise Exception("Remove file message not matching.")
        else:
            if self.poco("Are you sure you want to remove the local file? All fields using this data source will need to be reconnected to a data source.").exists():
                return
            else:
                raise Exception("Remove file message not matching.")

    # def remove_File_Based_On_DataSource(self, datasource, filename=None, cancel=False, verify=False):
    #     file_list, no_of_swipes = self.fileListDisplayed(True)
    #     scroll_view = self.poco("android.widget.HorizontalScrollView")
    #     curr_child_count = self.getCurrCount(False)
    #     scrolled = False
    #     while not self.poco("DATA SOURCE").exists():
    #         scroll_view.swipe("left")
    #     for i in range(5):
    #         scroll_view.swipe("left")
    #     while no_of_swipes >= 0:
    #         for i in range(curr_child_count):
    #             if not scrolled:
    #                 data_source = self.poco("android.widget.HorizontalScrollView").child()[4 + 4 * i].get_name()
    #                 name_app = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
    #             else:
    #                 data_source = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
    #                 name_app = self.poco("android.widget.HorizontalScrollView").child()[4 * i].get_name()
    #             if data_source == datasource:
    #                 if filename is not None:
    #                     if name_app == filename:
    #                         three_dot = self.poco("android.widget.Button")[i]
    #                         three_dot.click()
    #                         self.clickRemove()
    #                         if verify:
    #                             self.verify_Remove_File_Warning()
    #                         if not cancel:
    #                             self.clickRemove()
    #                         else:
    #                             self.clickCancel()
    #                         return
    #                 else:
    #                     three_dot = self.poco("android.widget.Button")[i]
    #                     three_dot.click()
    #                     self.clickRemove()
    #                     if verify:
    #                         self.verify_Remove_File_Warning()
    #                     if not cancel:
    #                         self.clickRemove()
    #                     else:
    #                         self.clickCancel()
    #                     return name_app
    #         self.poco.scroll()
    #         no_of_swipes -= 1
    #         scrolled = True
    #         curr_child_count = self.getCurrCount(True)
    #     raise Exception("No file with datasource " + datasource)

    # def remove_File_Based_On_DataSource(self, datasource, filename=None, cancel=False, verify=False):
    #     scroll_view = self.poco("android.widget.HorizontalScrollView")
    #     curr_child_count = self.getCurrCount(False)
    #     scrolled = False
    #     while not self.poco("DATA SOURCE").exists():
    #         scroll_view.swipe("left")
    #     for i in range(5):
    #         scroll_view.swipe("left")
    #     prev_arr = []
    #     while True:
    #         curr_arr = []
    #         for i in range(curr_child_count):
    #             if not scrolled:
    #                 name_app = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
    #                 curr_arr.append(name_app)
    #             else:
    #                 name_app = self.poco("android.widget.HorizontalScrollView").child()[4 * i].get_name()
    #                 curr_arr.append(name_app)
    #         if prev_arr == curr_arr:
    #             break
    #         prev_arr = curr_arr
    #         self.poco.scroll()
    #         scrolled = True
    #
    #     while not self.poco("DATA SOURCE").exists():
    #         for i in range(curr_child_count):
    #             if not scrolled:
    #                 data_source = self.poco("android.widget.HorizontalScrollView").child()[4 + 4 * i].get_name()
    #                 name_app = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
    #             else:
    #                 data_source = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
    #                 name_app = self.poco("android.widget.HorizontalScrollView").child()[4 * i].get_name()
    #             if data_source == datasource:
    #                 if filename is not None:
    #                     if name_app == filename:
    #                         three_dot = self.poco("android.widget.Button")[i]
    #                         three_dot.click()
    #                         self.clickRemove()
    #                         if verify:
    #                             self.verify_Remove_File_Warning(datasource)
    #                         if not cancel:
    #                             self.clickRemove()
    #                         else:
    #                             self.clickCancel()
    #                         sleep(7)
    #                         return
    #                 else:
    #                     three_dot = self.poco("android.widget.Button")[i]
    #                     three_dot.click()
    #                     self.clickRemove()
    #                     if verify:
    #                         self.verify_Remove_File_Warning(datasource)
    #                     if not cancel:
    #                         self.clickRemove()
    #                     else:
    #                         self.clickCancel()
    #                     sleep(7)
    #                     return name_app
    #         scroll_view.swipe("down")
    #         curr_child_count = self.getCurrCount(True)
    #     scrolled = False
    #     for i in range(curr_child_count):
    #         if not scrolled:
    #             data_source = self.poco("android.widget.HorizontalScrollView").child()[4 + 4 * i].get_name()
    #             name_app = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
    #         else:
    #             data_source = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
    #             name_app = self.poco("android.widget.HorizontalScrollView").child()[4 * i].get_name()
    #         print("--")
    #         print(data_source)
    #         if data_source == datasource:
    #             if filename is not None:
    #                 if name_app == filename:
    #                     three_dot = self.poco("android.widget.Button")[i]
    #                     three_dot.click()
    #                     self.clickRemove()
    #                     if verify:
    #                         self.verify_Remove_File_Warning(datasource)
    #                     if not cancel:
    #                         self.clickRemove()
    #                     else:
    #                         self.clickCancel()
    #                     sleep(7)
    #                     return
    #             else:
    #                 three_dot = self.poco("android.widget.Button")[i]
    #                 three_dot.click()
    #                 self.clickRemove()
    #                 if verify:
    #                     self.verify_Remove_File_Warning(datasource)
    #                 if not cancel:
    #                     self.clickRemove()
    #                 else:
    #                     self.clickCancel()
    #                 sleep(7)
    #                 return name_app

    def remove_File_Based_On_DataSource(self, datasource, filename=None, cancel=False, verify=False):
        if not self.poco(filename).exists():
            raise Exception(f"No file {filename} with datasource {datasource}")
        scroll_view = self.poco("android.widget.HorizontalScrollView")
        while not self.poco("DATA SOURCE").exists():
            scroll_view.swipe("left")
        for i in range(5):
            scroll_view.swipe("left")
        element = self.poco("android.widget.HorizontalScrollView").child(datasource)
        size = element.attr("size")
        pos = element.attr("pos")
        x = pos[0] + size[0] * .80
        y = pos[1]
        self.poco.click([x, y])
        self.clickRemove()
        if verify:
            self.verify_Remove_File_Warning(datasource)
        if not cancel:
            self.clickRemove()
        else:
            self.clickCancel()
        sleep(7)
        return

    def remove_File(self, cancel=False):
        common_method.swipe_screen([0.9, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 5)
        three_dot = self.poco("android.widget.Button")
        three_dot.click()
        self.clickRemove()
        try:
            self.verify_Remove_File_Warning("Local File")
        except:
            self.verify_Remove_File_Warning("Google Drive")
        if not cancel:
            self.clickRemove()
            sleep(7)
        else:
            self.clickCancel()
        scroll_view = self.poco("android.widget.HorizontalScrollView")
        while not self.poco("NAME").exists():
            scroll_view.swipe("right")
        for i in range(5):
            scroll_view.swipe("right")

    def remove_File_Web(self, cancel=False):
        # common_method.swipe_screen([0.9, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 3)
        three_dot = self.poco("android.widget.Image")[2]
        three_dot.click()
        self.lock_phone()
        wake()
        sleep(3)
        self.poco(text="Remove")[1].click()
        self.lock_phone()
        wake()
        if not cancel:
            self.poco(name="android.widget.Button", textMatches=".*Remove.*").click()
        else:
            self.poco(name="android.widget.Button", text="Cancel").click()

    def checkDriveEmpty(self):
        if len(self.poco("android.view.View")[1].child()) == 3:
            return
        else:
            raise Exception("Drive Not Empty")

    def searchFileInLinkFilesAndUpload(self, filename):
        self.searchFilesInLinkFiles(filename)
        return "Yet to write"

    def searchFileInLocalStorage(self, filename, location="Downloads"):
        self.poco(self.HamburgerMenuLocalStorage).click()
        sleep(2)
        self.poco(text="Recent").click()
        sleep(2)
        self.poco(self.HamburgerMenuLocalStorage).click()
        sleep(2)
        if location == "Downloads":
            self.poco(textMatches="Download.*").click()
        if location == "Documents":
            self.poco(textMatches="Document.*").click()
        sleep(2)
        self.poco(desc="Search").click()
        sleep(2)
        self.poco("com.google.android.documentsui:id/search_src_text").set_text(filename)
        sleep(2)
        self.clickEnter()
        if self.poco("com.google.android.documentsui:id/item_root").child().get_name() != "android.widget.LinearLayout":
            self.poco("com.google.android.documentsui:id/sub_menu").click()
        sleep(2)
        file = self.poco("com.google.android.documentsui:id/item_root")[0]
        file.click()

    def selectFileInLocalStorage(self):
        if self.poco("com.google.android.documentsui:id/item_root").child().get_name() != "android.widget.LinearLayout":
            self.poco("com.google.android.documentsui:id/sub_menu").click()
        sleep(2)
        file_1 = self.poco("com.google.android.documentsui:id/preview_icon").parent().child(
            "android.widget.LinearLayout").child("android.widget.LinearLayout").child("android:id/title")
        file_1.click()
        return file_1.get_text()

    def selectUnSupportedFile(self):
        self.poco(self.HamburgerMenuLocalStorage).click()
        self.poco(name="android:id/title", textMatches=".*Document.*").wait_for_appearance(timeout=10)
        self.poco(name="android:id/title", textMatches=".*Download.*").parent().parent().parent().child()[5].click()
        sleep(2)
        self.poco(desc="Search").click()
        sleep(2)
        self.poco("com.google.android.documentsui:id/search_src_text").set_text(".nlbl")
        sleep(2)
        self.clickEnter()
        if self.poco("com.google.android.documentsui:id/item_root").child().get_name() != "android.widget.LinearLayout":
            self.poco("com.google.android.documentsui:id/sub_menu").click()
        sleep(2)
        file = self.poco("com.google.android.documentsui:id/item_root")[0]
        file.click()

    def selectFilesInLocal(self):
        file_list = []
        prev_list = []
        curr_list = []
        start = 0
        scroll_count = 0
        if self.poco("com.google.android.documentsui:id/item_root").child().get_name() != "android.widget.LinearLayout":
            self.poco("com.google.android.documentsui:id/sub_menu").click()
        while 1:
            file_count = len(
                self.poco("com.google.android.documentsui:id/preview_icon").parent().parent().parent().child())
            print(file_count)
            for i in range(start, file_count - 1):
                print(i)
                filee_name = \
                    self.poco("com.google.android.documentsui:id/preview_icon")[2].parent().parent().parent().child()[
                        i].child("android.widget.LinearLayout").child("android.widget.LinearLayout").child(
                        "android.widget.LinearLayout").child().get_text()
                print(filee_name)
                curr_list.append(filee_name)
                print("curr:", curr_list)

            for name in curr_list:
                if name not in file_list:
                    print(name)
                    file_list.append(name)
                    print("file", file_list)
                    self.poco(text=name).click()
                    sleep(10)
                    self.click_Add_File()
                    sleep(2)
                    self.click_Upload_File()
                    sleep(2)
                    for i in range(scroll_count):
                        self.poco.swipe([0.5, 0.9], [0.5, 0.4])

            print(prev_list)
            if curr_list == prev_list:
                break
            prev_list = curr_list
            curr_list = []
            start = 1
            self.poco.swipe([0.5, 0.9], [0.5, 0.4])
            scroll_count += 1
        return file_list
        # if self.poco("com.google.android.documentsui:id/item_root").child().get_name() != "android.widget.LinearLayout":
        #     self.poco("com.google.android.documentsui:id/sub_menu").click()
        # file_range = len(self.poco("com.google.android.documentsui:id/dir_list").child())
        # file_list = []
        # if self.poco("com.google.android.documentsui:id/item_root")[file_range - 1].child().child()[
        #     0].get_name() != "android.widget.LinearLayout":
        #     current_last_child = \
        #         self.poco("com.google.android.documentsui:id/item_root")[file_range - 2].child().child()[
        #             0].child().child().get_text()
        #     file_count = file_range - 1
        #     pass
        # else:
        #     current_last_child = \
        #         self.poco("com.google.android.documentsui:id/item_root")[file_range - 1].child().child()[
        #             0].child().child().get_text()
        #     file_count = file_range
        # for i in range(file_count):
        #     file_name = self.poco("com.google.android.documentsui:id/item_root")[i].child().child()[
        #         0].child().child().get_text()
        #     file_list.append(file_name)
        # file_1 = self.poco("com.google.android.documentsui:id/item_root")[0]
        # file_1.click()
        # sleep(2)
        #
        # for i in range(1, file_count):
        #     sleep(10)
        #     self.click_Add_File()
        #     sleep(2)
        #     self.click_Upload_File()
        #     sleep(2)
        #     file_i = self.poco("com.google.android.documentsui:id/item_root")[i]
        #     file_i.click()
        # enter_while = True
        # scroll_count = 0
        # while True:
        #     sleep(10)
        #     self.click_Add_File()
        #     sleep(2)
        #     self.click_Upload_File()
        #     sleep(2)
        #     temp = []
        #     scroll_count += 1
        #     for i in range(scroll_count):
        #         self.poco.scroll()
        #     sleep(2)
        #     file_range = len(self.poco("com.google.android.documentsui:id/dir_list").child())
        #     sleep(2)
        #     if self.poco("com.google.android.documentsui:id/item_root")[file_range - 1].child().child()[
        #         0].get_name() != "android.widget.LinearLayout":
        #         new_last_child = \
        #             self.poco("com.google.android.documentsui:id/item_root")[file_range - 2].child().child()[
        #                 0].child().child().get_text()
        #         file_count = file_range - 2
        #         pass
        #     else:
        #         new_last_child = \
        #             self.poco("com.google.android.documentsui:id/item_root")[file_range - 1].child().child()[
        #                 0].child().child().get_text()
        #         file_count = file_range - 1
        #     sleep(2)
        #     if new_last_child == current_last_child:
        #         return file_list
        #     for i in range(file_count):
        #         file_name = self.poco("com.google.android.documentsui:id/item_root")[i].child().child()[
        #             0].child().child().get_text()
        #         temp.append(file_name)
        #     if current_last_child in temp:
        #         index_from = temp.index(current_last_child) + 1
        #     else:
        #         index_from = 0
        #     for i in range(index_from, len(temp)):
        #         sleep(3)
        #         file_list.append(temp[i])
        #         print(file_list)
        #         if not enter_while:
        #             sleep(5)
        #             self.click_Add_File()
        #             sleep(2)
        #             self.click_Upload_File()
        #             sleep(2)
        #             for j in range(scroll_count):
        #                 self.poco.scroll()
        #         file_i = self.poco("com.google.android.documentsui:id/item_root")[i]
        #         print(file_i.child().child()[0].child().child().get_text())
        #         file_i.click()
        #         enter_while = False
        #     current_last_child = new_last_child

    def searchMyDesigns(self, design_name, enter=True):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(design_name)
        if enter:
            self.clickEnter()

    def checkIfAccPresent(self, account):
        start = 0
        end = 1
        while True:
            for i in range(start, len(self.poco("android.widget.ListView").child()) - end):
                if self.poco("android.widget.ListView").child()[i].child().child()[
                    0].get_text() == "Use another account":
                    return False
                elif self.poco("android.widget.ListView").child()[i].child().child()[1].get_text() == account:
                    return True
            start = 1
            end = 0
            self.poco.scroll()

    def addAccountToDevice(self):
        add_acc = self.poco(text="Add account to device")
        add_acc.click()

    def chooseAcc(self, Acc_Name="zebra03.swdvt@gmail.com"):
        account = self.poco(text=Acc_Name)
        count = 5
        while not account.exists() and count != 0:
            self.poco.scroll()
            count -= 1
        account.click()

    def click_GooglemailId(self):
        sleep(4)
        google_mailid = self.poco(self.Google_MailID)
        if google_mailid.exists():
            google_mailid.click()
            sleep(9)

    def wait_for_element_appearance_text(self, element, time_out=15):
        self.poco(text=element).wait_for_appearance(timeout=time_out)

    def sign_In_With_Google(self, password, username=None, wrong_password=False):
        if username is not None:
            try:
                self.poco("android.widget.EditText").wait_for_appearance(timeout=10)
                self.poco("android.widget.EditText").set_text(username)
            except:
                self.poco("identifierId").wait_for_appearance(timeout=10)
                self.poco("identifierId").set_text(username)
            keyevent("Enter")
            self.poco("android.widget.Button")[-1].click()
        self.poco("android.widget.EditText").wait_for_appearance(timeout=10)
        self.poco("android.widget.EditText").set_text(password)
        keyevent("Enter")
        # self.poco("android.widget.Button")[-1].click()
        if wrong_password:
            try:
                self.wait_for_element_appearance_text(
                    "Wrong password. Try again or click ‘Forgot password’ to reset it.")
            except:
                raise Exception(
                    "Error message: \"Wrong password. Try again or click Forgot password to reset it.\" not displayed.")
        else:
            # self.poco("android.widget.Button")[-1].click()
            try:
                scrolls = 5
                while scrolls != 0:
                    self.poco.scroll()
                    scrolls -= 1
                if self.poco(text="Skip").exists():
                    self.poco(text="Skip").click()
            except:
                pass
            try:
                scrolls = 5
                while scrolls != 0:
                    self.poco.scroll()
                    scrolls -= 1
                if self.poco(text="I agree").exists():
                    self.poco(text="I agree").click()
            except:
                pass
            try:
                self.poco(text="Not now").wait_for_appearance(timeout=15)
                self.poco(text="Not now").click()
            except:
                pass

    def signIn_if_on_SSO_page_web(self):
        sleep(3)
        if self.poco(textMatches="(?s).*pi.zebra.com/as/authorization.oauth2.*").exists():
            touch(Template(Basic_path(r"Google_Icon.png"), record_pos=(-0.319, -0.173), resolution=(1080, 2340)))
            self.lock_phone()
            wake()
            try:
                self.poco(text="Sign in with Google").wait_for_appearance(timeout=15)
            except:
                raise Exception("Did not navigate to Sign In with google page")
            account = "zebra02.swdvt@gmail.com"
            if self.checkIfAccPresent(account):
                self.chooseAcc(account)
            else:
                count = 5
                while not self.poco(text="Use another account").exists() and count != 0:
                    self.poco.scroll()
                    count -= 1
                self.click_GooglemailId()
                if self.poco(text="Signed in to Google as").exists():
                    count = 5
                    while not self.poco(text="Add account to device").exists() and count != 0:
                        self.poco.scroll()
                        count-=1
                    self.addAccountToDevice()
                self.sign_In_With_Google("Zebra#123456789", "zebra02.swdvt@gmail.com")

    def checkIfDesignsLoaded(self):
        sleep(10)
        if self.poco(nameMatches=".*Showing.*").exists():
            pass
        else:
            raise Exception("Designs not loaded.")

    def check_if_showing_100_designs_text(self):
        if self.poco(nameMatches="Showing 100 Designs").exists():
            pass
        else:
            raise Exception("\"Showing 100 designs\" text is not displayed.")

    def verifyPreviewShownIsCorrect(self):
        assert_exists(self.test_45738, "Preview shown is correct.")

    def select_All(self, check=True):
        checked_value = common_method.getAttr(self.poco("android.widget.CheckBox"), "checked")
        if checked_value:
            if not check:
                self.poco("android.widget.CheckBox").click()
        else:
            if check:
                self.poco("android.widget.CheckBox").click()

    def labelRangeSelection(self, label_range, confirm=True):
        count=5
        while not self.poco("Print").exists() and count!=0:
            self.poco.scroll()
            count-=1
        checkbox = self.poco(self.Check_Box)
        self.poco("Print").parent().child()[-7].click()
        self.select_All()
        self.select_All(False)
        checked_count = 0
        for i in range(label_range):
            if checkbox[3 + i].exists():
                checkbox[3 + i].click()
                checked_count += 1
        if confirm:
            self.clickConfirm()
        return checked_count

    def first_row_header(self, check=True):
        if self.poco(self.Check_Box, checked=True):
            if not check:
                self.poco(self.Check_Box).click()
        elif self.poco(self.Check_Box, checked=False):
            if check:
                self.poco(self.Check_Box).click()

    def lock_phone(self):
        sleep(5)
        os.system('adb shell input keyevent 26')
        sleep(2)

    def clearAppData(self, app="com.zebra.soho_app"):
        # os.system(f"adb shell pm clear {app}")
        try:
            self.poco("Home").wait_for_appearance(timeout=15)
            sleep(3)
            self.poco("Open navigation menu").click()
            sleep(3)
            self.poco("android.widget.Button").click()
            count = 5
            while not self.poco("Log Out").exists() and count!=0:
                self.poco.scroll()
                count-=1
            self.poco("Log Out").click()
        except:
            pass
        packagename = "com.zebra.soho_app"
        try:
            pass
        finally:
            clear_app(packagename)
            sleep(1)
            start_app(packagename)
            sleep(4)

    def clearBrowsingData(self):
        start_app("com.android.chrome")
        sleep(3)
        self.poco("com.android.chrome:id/menu_button").click()
        try:
            self.poco(textMatches=".* browsing data.*").click()
        except:
            self.poco(text="History").click()
            self.poco(textMatches=".* browsing data.*").click()
        try:
            self.poco("com.android.chrome:id/quick_delete_more_options").click()
        except:
            pass
        self.poco("com.android.chrome:id/spinner").click()
        self.poco(text="All time").click()
        self.poco("com.android.chrome:id/clear_button").click()
        try:
            self.poco(text="Clear").click()
        except:
            pass
        if self.poco(text="Also clear data from these sites?").exists():
            self.poco(text="Delete").click()
        try:
            self.poco("com.android.chrome:id/close_menu_id").click()
        except:
            pass

    def clickOk(self):
        try:
            self.poco(text="OK").wait_for_appearance(timeout=20)
            self.poco(text="OK").click()
        except:
            try:
                ok_image = self.poco(self.use_image_button)
                ok_image.click()
            except:
                try:
                    self.poco(nameMatches=".*done.*").click()
                except:
                    self.poco(desc="Done").click()
        sleep(10)

    def allowPermissions(self):
        try:
            self.poco(text="While using the app").wait_for_appearance(timeout=15)
            self.poco(text="While using the app").click()
        except:
            pass

    def clickGotItWeb(self):
        if self.poco(text="Got It").exists():
            self.poco(text="Got It").click()
        if self.poco(text="Welcome to your new ZSB Series Printer").exists():
            self.poco(text="Welcome to your new ZSB Series Printer").parent().child("android.widget.Button").click()

    def get_current_date(self):
        year = datetime.date.today().year
        date = datetime.date.today().day
        if len(str(date)) == 1:
            date = "0"+str(date)
        month = self.Month[datetime.date.today().month]
        current_date = str(month) + " " + str(date) + ", " + str(year)
        return current_date

    def checkIfElementExists(self, element, text=False):
        if text:
            return self.poco(text=element).exists()
        return self.poco(element).exists()

    def clickNext(self):
        if self.poco("Next").exists():
            self.poco("Next").click()
        elif self.poco(text="Next").exists():
            self.poco(text="Next").click()

    def clickPrevious(self):
        if self.poco("Previous").exists():
            self.poco("Previous").click()
        elif self.poco(text="Previous").exists():
            self.poco(text="Previous").click()

    def clickAddPhoto(self):
        self.poco(text="Add picture").wait_for_appearance(timeout=10)
        self.poco(text="Add picture").click()

    def placePhoto(self):
        touch(Template(Basic_path(r"place_pic.png"), record_pos=(-0.008, 0.287), resolution=(1080, 2280)))

    def selectFileDrive(self, file_name):
        sleep(5)
        curr = []
        prev = []
        while 1:
            for i in range(len(self.poco("android.widget.HorizontalScrollView").child())):
                if self.poco("android.widget.HorizontalScrollView").child()[i].get_name() == file_name:
                    self.poco("android.widget.HorizontalScrollView").child()[i].click()
                    self.clickSelect()
                    return
                curr.append(self.poco("android.widget.HorizontalScrollView").child()[i].get_name())
            if curr == prev:
                break
            prev = curr
            curr = []
            self.poco.scroll()
        error = "File " + file_name + " does not exist."
        raise Exception(error)

    def verifyFilePresentInDrive(self, file_name):
        curr = []
        prev = []
        while 1:
            for i in range(len(self.poco("NAME").parent().child())):
                if self.poco("NAME").parent().child()[1] == "DATE ADDED":
                    if self.poco("NAME").parent().child()[2 * i].get_name() == file_name:
                        return
                    curr.append(self.poco("NAME").parent().child()[2 * i].get_name())
                else:
                    if self.poco("NAME").parent().child()[i].get_name() == file_name:
                        return
                    curr.append(self.poco("NAME").parent().child()[i].get_name())
            if curr == prev:
                break
            prev = curr
            curr = []
            self.poco.scroll()
        scroll_view = self.poco("NAME").parent()
        while not self.poco("NAME").exists():
            scroll_view.swipe("down")
        error = "File " + file_name + " not present."
        raise Exception(error)

    def getFilesShownInDrive(self):
        curr = []
        prev = []
        total = []
        first_loop = 1
        while 1:
            for i in range(first_loop, len(self.poco("NAME").parent().child())):
                if self.poco("NAME").parent().child()[1] == "DATE ADDED":
                    curr.append(self.poco("NAME").parent().child()[2 * i].get_name())
                else:
                    curr.append(self.poco("NAME").parent().child()[i].get_name())
            for i in curr:
                if i in total:
                    break
                total.append(i)
            if curr == prev:
                break
            prev = curr
            curr = []
            first_loop = 0
            self.poco.scroll()
        scroll_view = self.poco("NAME").parent()
        while not self.poco("NAME").exists():
            scroll_view.swipe("down")
        return total

    def checkIfInLoginPage(self):
        try:
            self.poco("Sign In").wait_for_appearance(timeout=20)
        except:
            raise Exception("Not in Login page")

    def checkIfInLoginPageWeb(self):
        try:
            self.poco(text="Sign In With").wait_for_appearance(timeout=20)
        except:
            raise Exception("Not in Login page")

    def checkIfOnHomePage(self):
        try:
            self.poco("Home").wait_for_appearance(timeout=20)
        except:
            raise Exception("Did not reach home page.")

    def checkIfOnHomePageWeb(self):
        try:
            self.poco(text="Home").wait_for_appearance(timeout=20)
        except:
            raise Exception("Did not reach home page.")

    def Login_With_Email_Tab(self):
        sleep(12)
        zebra_login = self.poco(text="Sign In with your email")
        zebra_login.click()
        sleep(4)
        self.poco(text(""))
        self.poco(text("zebra03.swdvt@gmail.com"))
        sleep(1)

    def log_out_of_account(self):
        try:
            self.poco("Home").wait_for_appearance(timeout=15)
            sleep(3)
            self.poco("Open navigation menu").click()
            sleep(3)
            self.poco("android.widget.Button").click()
            count = 5
            while not self.poco("Log Out").exists() and count != 0:
                self.poco.scroll()
                count -= 1
            self.poco("Log Out").click()
        except:
            pass

    def Turn_Off_The_Phone(self):
        sleep(2)
        keyevent("KEYCODE_POWER")

    def Turn_ON_The_Phone(self):
        keyevent("KEYCODE_POWER")
        sleep(2)

    def click_drive_sign_in_if_present(self, username="zebra03.swdvt@gmail.com"):
        sleep(3)
        if self.poco(self.Sign_In_With_Google).exists():
            touch(self.Sign_In_With_Google_Template)
        if self.poco(self.Sign_In_With_Microsoft).exists():
            touch(self.Sign_In_With_Microsoft_Template)
            self.Turn_Off_The_Phone()
            sleep(3)
            self.Turn_ON_The_Phone()
            sleep(3)
            self.Turn_Off_The_Phone()
            sleep(3)
            self.Turn_ON_The_Phone()
            sleep(3)
            try:
                sleep(5)
                self.poco("android.widget.EditText").set_text(username)
                self.poco(text="Next").click()
            except:
                try:
                    self.poco("i0116").set_text(username)
                    self.poco(text="Next").click()
                except:
                    pass
        sleep(3)
