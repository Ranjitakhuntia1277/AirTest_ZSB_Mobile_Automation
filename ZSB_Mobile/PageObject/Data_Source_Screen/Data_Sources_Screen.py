# LoginFunction.py

import datetime
import random
import string

from airtest.core.api import *
# import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoNoSuchNodeException

from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen

common_method = Common_Method(poco)


class Data_Sources_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Acc_Name = "swdvt zsb"
        self.Home = "Home"
        self.My_Data = "My Data"
        self.Add_File = "android.widget.Button"
        self.Upload_File = "android.widget.Button"
        self.Link_File = "android.widget.Button"
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
        self.Bar_Code_Location = Template(r"tpl1707978279280.png", record_pos=(-0.055, 0.03), resolution=(1080, 2340))
        self.File_Info_Device = []
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
        self.Search_Files = Template(r"tpl1705645360605.png", record_pos=(-0.261, -0.571), resolution=(1080, 2340))
        self.expectedSearchList = ["Tes1.jpg", "Test2.png", "Test3.bmp"]
        self.Sign_In_With_Microsoft = "Sign in with Microsoft"
        self.Sign_In_With_Microsoft_Template = Template(r"tpl1706511322813.png", record_pos=(0.002, 0.183),
                                                        resolution=(1080, 2340))
        self.test_45738 = Template(r"tpl1706683702494.png", record_pos=(0.0, -0.264), resolution=(1080, 2340))
        self.Sign_In_With_Google = "Sign in with Google"
        self.Sign_In_With_Google_Template = Template(r"Google_Icon.png", record_pos=(-0.006, 0.017),
                                                     resolution=(1080, 2340))
        self.Select = "Select"
        self.File_Name_Web = ""
        # self.search_File_Name = ""
        self.is_already_linked = Template(r"tpl1706012736859.png", record_pos=(-0.139, 0.898), resolution=(1080, 2340))
        self.Use_Your_Password_Instead = "idA_PWD_SwitchToPassword"
        self.Enter_Password = Template(r"Password.png", record_pos=(-0.063, -0.556), resolution=(1080, 2340))
        self.search_Files_In_Link_Files = Template(r"search_files_link_files.png", record_pos=(-0.247, -0.567),
                                                   resolution=(1080, 2340))

    def click_My_Data(self):
        my_data = self.poco(self.My_Data)
        my_data.wait_for_appearance(timeout=10)
        my_data.click()

    def click_Add_File(self):
        add_file = self.poco(self.Add_File)
        add_file.wait_for_appearance(timeout=10)
        add_file.click()

    def click_Upload_File(self):
        upload_file = self.poco(self.Upload_File)
        upload_file.wait_for_appearance(timeout=10)
        upload_file[1].click()

    def click_Upload_File_Web(self):
        upload_file = self.poco(self.Upload_File)
        upload_file[3].click()

    def click_Media_Picker_Web(self):
        media_picker = self.poco("android.widget.LinearLayout")[5]
        media_picker.click()

    def click_Link_File(self):
        link_file = self.poco(self.Link_File)
        link_file.wait_for_appearance(timeout=10)
        link_file.click()

    def chooseAccToLinkFile(self):
        account = self.poco(self.Acc_Name)
        account.click()

    def select_File_To_Upload(self, return_name=False):
        name_on_device = self.poco("com.google.android.documentsui:id/item_root")[0].child(
            "androidx.cardview.widget.CardView").offspring("com.google.android.documentsui:id/nameplate").child(
            "android.widget.RelativeLayout").child()[0].get_text()
        self.File_Info_Device.append(name_on_device)

        file = self.poco("com.google.android.documentsui:id/item_root")[0].child(
            "androidx.cardview.widget.CardView").offspring("com.google.android.documentsui:id/nameplate").child(
            "android.widget.RelativeLayout")[0]
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

    def verify_File_Data(self):

        assert_exists(Template(r"tpl1705388526509.png", record_pos=(-0.436, -0.259), resolution=(1080, 2340)),
                      "File icon matches.")
        name_app = self.poco("android.widget.HorizontalScrollView").child()[-4].get_name()
        self.File_Info_App.append(name_app)
        year = datetime.date.today().year
        date = datetime.date.today().day
        month = self.Month[datetime.date.today().month]
        date_app = self.poco("android.widget.HorizontalScrollView").child()[-3].get_name()
        self.File_Info_App.append(date_app)
        data_source_app = self.poco("android.widget.HorizontalScrollView").child()[-2].get_name()
        self.File_Info_App.append(data_source_app)
        expected_date = str(month) + " " + str(date) + ", " + str(year)
        self.File_Info_Device.append(expected_date)
        self.File_Info_Device.append(self.File_Data_Source_Device_Local_File)
        print("---------------")
        print(self.File_Info_App)
        print(self.File_Info_Device)
        for i in range(len(self.File_Info_App)):
            if self.File_Info_App[i] == self.File_Info_Device[i]:
                return
            else:
                print("---------------")
                print("file info on app:\n" + self.File_Info_App)
                print("Expected fileinfo:\n" + self.File_Info_Device)
                raise Exception("File data does not match")

    def clickMyDesigns(self):
        my_designs = self.poco(self.My_Designs)
        my_designs.click()

    def selectDesignCreatedAtSetUp(self):
        self.poco(nameMatches="Showing.*").wait_for_appearance(timeout=10)
        set_up_design = self.poco("android.view.View")[5]
        set_up_design.click()

    def clickPrint(self):
        if self.poco(self.Print_Btn).exists():
            print_btn = self.poco(self.Print_Btn)
        else:
            print_btn = self.poco(text = self.Print_Btn)
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
        three_dots = self.poco("android.widget.HorizontalScrollView").child()[-1].child()
        three_dots.click()

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
        self.poco("android.widget.Image").click()

    def clickCreateDesignBtn(self):
        if self.poco(text=self.Create_Btn).exists():
            self.poco(text=self.Create_Btn).click()
        else:
            self.poco.scroll()
            self.poco(self.Create_New_Design).click()

    def selectLabelSize(self):
        self.poco("android.view.View")[16].click()

    def clickContinue(self):
        self.poco(self.Continue).wait_for_appearance(timeout=10)
        self.poco(self.Continue).click()

    def clickContinueWeb(self):
        self.poco(text="Continue").wait_for_appearance(timeout=10)
        self.poco(text="Continue").click()

    def clickAddBarcode(self):
        self.poco(text="Add barcode").wait_for_appearance(timeout=10)
        self.poco(text="Add barcode").click()

    def placeBarcode(self):
        touch(self.Bar_Code_Location)
        # sleep(2)
        # self.poco("android.webkit.WebView").focus([0.1, 0.3]).click()

    def exitDesigner(self):
        self.poco("android.widget.Button").wait_for_appearance(timeout=10)
        self.poco("android.widget.Button").click()

    def uploadFileWeb(self):
        self.poco("android.widget.Button")[1].click()

    def selectFileToUploadWeb(self):
        self.poco("android.widget.LinearLayout")[7].click()

    def setLabelName(self, name):
        self.poco("android.widget.Image")[1].click()
        self.poco("android.widget.TextView")[1].click()
        self.poco("android.widget.EditText").set_text(name)

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
        temp = []
        swipe_count = 0
        if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
            if self.poco("android.widget.HorizontalScrollView").child()[2].get_name() == "DATA SOURCE":
                if self.poco("android.widget.HorizontalScrollView").child()[-1].get_name() == "android.view.View":
                    current_last_child = self.poco("android.widget.HorizontalScrollView").child()[-4].get_name()
                else:
                    current_last_child = self.poco("android.widget.HorizontalScrollView").child()[-3].get_name()
            else:
                current_last_child = self.poco("android.widget.HorizontalScrollView").child()[-2].get_name()
        else:
            current_last_child = self.poco("android.widget.HorizontalScrollView").child()[-1].get_name()
        for i in range(1, self.getCurrCount() + 1):
            if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
                if self.poco("android.widget.HorizontalScrollView").child()[2].get_name() == "DATA SOURCE":
                    File_List.append(self.poco("android.widget.HorizontalScrollView").child()[3 * i].get_name())
                else:
                    File_List.append(self.poco("android.widget.HorizontalScrollView").child()[2 * i].get_name())
            else:
                File_List.append(self.poco("android.widget.HorizontalScrollView").child()[i].get_name())
        while True:
            self.poco.scroll()
            swipe_count += 1
            for i in range(1, self.getCurrCount() + 1):
                if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
                    if self.poco("android.widget.HorizontalScrollView").child()[2].get_name() == "DATA SOURCE":
                        temp.append(self.poco("android.widget.HorizontalScrollView").child()[3 * i].get_name())
                    else:
                        temp.append(self.poco("android.widget.HorizontalScrollView").child()[2 * i].get_name())
                else:
                    temp.append(self.poco("android.widget.HorizontalScrollView").child()[i].get_name())
            if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
                if self.poco("android.widget.HorizontalScrollView").child()[2].get_name() == "DATA SOURCE":
                    if self.poco("android.widget.HorizontalScrollView").child()[-1].get_name() == "android.view.View":
                        new_last_child = self.poco("android.widget.HorizontalScrollView").child()[-4].get_name()
                    else:
                        new_last_child = self.poco("android.widget.HorizontalScrollView").child()[-3].get_name()
                else:
                    new_last_child = self.poco("android.widget.HorizontalScrollView").child()[-2].get_name()
            else:
                new_last_child = self.poco("android.widget.HorizontalScrollView").child()[-1].get_name()
            if current_last_child in temp:
                index_from = temp.index(current_last_child) + 1
                for i in range(index_from, len(temp)):
                    File_List.append(temp[i])
                if temp[-1] == current_last_child:
                    break
            else:
                for i in range(len(temp)):
                    File_List.append(temp[i])
                current_last_child = new_last_child
            temp = []
        while not self.poco("NAME").exists():
            scroll_view = self.poco("android.view.View")
            scroll_view.swipe("down")
        if not no_of_swipes:
            return File_List
        else:
            return File_List, swipe_count

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
        if len(poco("android.view.View")[5].child()) == 1:
            return
        else:
            print("Label created not found")
            return 1 / 0
        # design_name = poco("android.view.View")[5].child().get_name()
        # if design_name[:label_name_len] == LabelName:
        #     return
        # else:
        #

    def searchName(self, name):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(name)
        sleep(2)
        self.clickEnter()

    def searchExistingName(self):
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

    def generateRandomWord(self, length):
        return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))

    def checkIfListIsEmpty(self):
        if self.poco(self.List_Empty).exists():
            return True
        else:
            # print("Files are not filtered")
            # return 1 / 0
            raise Exception("List not empty")
    def searchRandomWord(self):
        random_word = self.generateRandomWord(64)
        self.searchName(random_word)
        sleep(7)
        self.checkIfListIsEmpty()

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
        data_sources_page = Data_Sources_Screen(poco)
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text("")
        count_after_clearing_text = data_sources_page.countNumberOfFiles()
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

    def selectLabelRange(self, label_range):
        self.Label_Range = label_range
        checkbox = self.poco(self.Check_Box)
        self.poco("android.widget.ScrollView").child()[5].click()
        checkbox[0].click()
        checkbox[0].click()
        for i in range(label_range):
            checkbox[3 + i].click()

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

    def signInWithMicrosoft(self, username, password):
        if self.poco(self.Sign_In_With_Microsoft).exists():
            sign_in_with_microsoft = self.poco(self.Sign_In_With_Microsoft)
            sign_in_with_microsoft.click()
        else:
            touch(self.Sign_In_With_Microsoft_Template)
        self.poco("i0116").wait_for_appearance(timeout=10)
        self.poco("i0116").click()
        # username = "zsbswdvt@gmail.com"
        self.poco("i0116").set_text(username)
        self.poco("idSIButton9").click()
        sleep(3)
        if self.poco(self.Use_Your_Password_Instead).exists():
            self.poco(self.Use_Your_Password_Instead).click()
            sleep(2)
        touch(self.Enter_Password)
        sleep(2)
        self.poco("i0118").set_text(password)
        # password = "hmWepX4AUMLa!9E"
        # self.poco(text(password))
        self.poco("idSIButton9").click()

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
        self.poco("identifierId").set_text(username)
        sleep(3)
        self.poco(text="Next").click()
        sleep(3)
        self.poco("android.widget.EditText").set_text(password)
        sleep(3)
        self.poco(text="Next").click()
        self.poco.scroll()
        if self.poco(text="I agree").exists():
            self.poco(text="I agree").click()
        self.poco.scroll()
        if self.poco(text="Accept").exists():
            self.poco(text="Accept").click()

    def signInWithEmail(self):
        try:
            self.poco("android.widget.Button").wait_for_appearance(timeout=10)
            self.poco("android.widget.Button").click()
            self.poco("com.android.chrome:id/coordinator").click()
            print("Successfully clicked Sign In With Email")
        except PocoNoSuchNodeException:
            print("Sign In with Email option not found!\n Test Continues...")
            raise Exception("Sign In with Email option not found!\n Test Failed")

    def clickBackArrow(self):
        back_arrow = self.poco("android.widget.Button")
        back_arrow.wait_for_appearance(timeout=10)
        back_arrow.click()

    def checkNoChangeInFileCount(self, initialFileCount):
        file_list = self.fileListDisplayed()
        curr_file_count = len(file_list)
        if initialFileCount == curr_file_count:
            return
        else:
            print("Number of files are not same as before")
            return 1 / 0

    def checkFilesShownAreSupported(self):
        supported_types = ["jpg", "png", "bmp", "txt", "xlsx", "csv"]
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
            search_File_Name = self.poco("android.widget.HorizontalScrollView").child()[2].get_name()
            self.poco("android.widget.HorizontalScrollView").child()[2].click()
            self.clickSelect()
        else:
            search_File_Name = self.poco("android.widget.HorizontalScrollView").child()[1].get_name()
            self.poco("android.widget.HorizontalScrollView").child()[1].click()
            self.clickSelect()

        return search_File_Name

    def checkIsAlreadyLinkedPopUp(self):
        if assert_exists(self.is_already_linked, "File already present."):
            return
        else:
            raise Exception("File already linked pop up not present.")

    def searchFilesInLinkFiles(self, file_name):
        touch(self.search_Files_In_Link_Files)
        self.poco(text(file_name))

    def verifyFilePresentInList(self, file_name, datasource=None, data=False, verify_date=True):
        if self.poco(self.List_Empty).exists():
            raise Exception(file_name + "File not present")
        file_list = self.fileListDisplayed()
        scroll_view = self.poco("android.widget.HorizontalScrollView")
        while not self.poco("DATA SOURCE").exists():
            scroll_view.swipe("left")
        for j in range(5):
            scroll_view.swipe("left")
        """Change on mac"""
        for i in range(len(file_list)):
            if not data:
                if file_list[i] == file_name:
                    return
            else:
                year = datetime.date.today().year
                date = datetime.date.today().day
                month = self.Month[datetime.date.today().month]
                date_app = self.poco("android.widget.HorizontalScrollView").child()[3 + 4 * i].get_name()
                data_source_app = self.poco("android.widget.HorizontalScrollView").child()[4 + 4 * i].get_name()
                expected_date = str(month) + " " + str(date) + ", " + str(year)
                name_app = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
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
                            if i == len(file_list)-1:
                                raise Exception("Date not matching")
        raise Exception(file_name + "File not present")



    def clickHome(self):
        home_btn = self.poco(self.Home)
        home_btn.click()

    def verify_Remove_File_Warning(self):
        content = self.poco("android.view.View")[4].child().get_name()
        if content[7:12] == "local":
            return
        else:
            if content == "Remove linked file\nAre you sure you want to remove the local file? All fields using this data source will need to be reconnected to a data source.":
                return

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

    def remove_File_Based_On_DataSource(self, datasource, filename=None, cancel=False, verify=False):
        scroll_view = self.poco("android.widget.HorizontalScrollView")
        curr_child_count = self.getCurrCount(False)
        scrolled = False
        while not self.poco("DATA SOURCE").exists():
            scroll_view.swipe("left")
        for i in range(5):
            scroll_view.swipe("left")
        prev_arr = []
        while True:
            curr_arr = []
            for i in range(curr_child_count):
                if not scrolled:
                    name_app = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
                    curr_arr.append(name_app)
                else:
                    name_app = self.poco("android.widget.HorizontalScrollView").child()[4 * i].get_name()
                    curr_arr.append(name_app)
            if prev_arr == curr_arr:
                break
            prev_arr = curr_arr
            self.poco.scroll()
            scrolled = True

        while not self.poco("DATA SOURCE").exists():
            for i in range(curr_child_count):
                if not scrolled:
                    data_source = self.poco("android.widget.HorizontalScrollView").child()[4 + 4 * i].get_name()
                    name_app = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
                else:
                    data_source = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
                    name_app = self.poco("android.widget.HorizontalScrollView").child()[4 * i].get_name()
                if data_source == datasource:
                    if filename is not None:
                        if name_app == filename:
                            three_dot = self.poco("android.widget.Button")[i]
                            three_dot.click()
                            self.clickRemove()
                            if verify:
                                self.verify_Remove_File_Warning()
                            if not cancel:
                                self.clickRemove()
                            else:
                                self.clickCancel()
                            return
                    else:
                        three_dot = self.poco("android.widget.Button")[i]
                        three_dot.click()
                        self.clickRemove()
                        if verify:
                            self.verify_Remove_File_Warning()
                        if not cancel:
                            self.clickRemove()
                        else:
                            self.clickCancel()
                        return name_app
            scroll_view.swipe("down")
            curr_child_count = self.getCurrCount(True)
        scrolled = False
        for i in range(curr_child_count):
            if not scrolled:
                data_source = self.poco("android.widget.HorizontalScrollView").child()[4 + 4 * i].get_name()
                name_app = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
            else:
                data_source = self.poco("android.widget.HorizontalScrollView").child()[2 + 4 * i].get_name()
                name_app = self.poco("android.widget.HorizontalScrollView").child()[4 * i].get_name()
            if data_source == datasource:
                if filename is not None:
                    if name_app == filename:
                        three_dot = self.poco("android.widget.Button")[i]
                        three_dot.click()
                        self.clickRemove()
                        if verify:
                            self.verify_Remove_File_Warning()
                        if not cancel:
                            self.clickRemove()
                        else:
                            self.clickCancel()
                        return
                else:
                    three_dot = self.poco("android.widget.Button")[i]
                    three_dot.click()
                    self.clickRemove()
                    if verify:
                        self.verify_Remove_File_Warning()
                    if not cancel:
                        self.clickRemove()
                    else:
                        self.clickCancel()
                    return name_app
        raise Exception("No file with datasource " + datasource)

    def remove_File(self, cancel=False):
        common_method.swipe_screen([0.9, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 3)
        three_dot = self.poco("android.widget.Button")
        three_dot.click()
        self.clickRemove()
        self.verify_Remove_File_Warning()
        if not cancel:
            self.clickRemove()
        else:
            self.clickCancel()

    def checkDriveEmpty(self):
        if len(self.poco("android.view.View")[1].child()) == 3:
            return
        else:
            raise Exception("Drive Not Empty")

    def searchFileInLinkFilesAndUpload(self, filename):
        self.searchFilesInLinkFiles(filename)
        return "Yet to write"

    def searchFileInLocalStorage(self, filename, location):
        self.poco(self.HamburgerMenuLocalStorage).click()
        sleep(2)
        self.poco(text="Recent").click()
        sleep(2)
        self.poco(self.HamburgerMenuLocalStorage).click()
        sleep(2)
        if location == "Downloads":
            self.poco(text="Downloads").click()
        if location == "Documents":
            self.poco(text="Documents").click()
        sleep(2)
        self.poco(desc="Search").click()
        sleep(2)
        self.poco("com.google.android.documentsui:id/search_src_text").set_text(filename)
        sleep(2)
        self.clickEnter()
        file = self.poco("com.google.android.documentsui:id/item_root")[0]
        file.click()

    def selectFileInLocalStorage(self):
        file_1 = self.poco("com.google.android.documentsui:id/preview_icon")[0].parent()
        file_1.click()
    def selectFilesInLocal(self):
        """Change this on mac"""
        file_range = len(self.poco("com.google.android.documentsui:id/dir_list").child())
        file_list = []
        if self.poco("com.google.android.documentsui:id/item_root")[file_range - 1].child().child()[
            0].get_name() != "android.widget.LinearLayout":
            current_last_child = \
            self.poco("com.google.android.documentsui:id/item_root")[file_range - 2].child().child()[
                0].child().child().get_text()
            file_count = file_range - 1
            pass
        else:
            current_last_child = \
            self.poco("com.google.android.documentsui:id/item_root")[file_range - 1].child().child()[
                0].child().child().get_text()
            file_count = file_range
        for i in range(file_count):
            file_name = self.poco("com.google.android.documentsui:id/item_root")[i].child().child()[
                0].child().child().get_text()
            file_list.append(file_name)
        file_1 = self.poco("com.google.android.documentsui:id/item_root")[0]
        file_1.click()
        sleep(2)

        for i in range(1, file_count):
            sleep(5)
            self.click_Add_File()
            sleep(2)
            self.click_Upload_File()
            sleep(2)
            file_i = self.poco("com.google.android.documentsui:id/item_root")[i]
            file_i.click()
        enter_while = True
        scroll_count = 0
        while True:
            sleep(5)
            self.click_Add_File()
            sleep(2)
            self.click_Upload_File()
            sleep(2)
            temp = []
            scroll_count += 1
            for i in range(scroll_count):
                self.poco.scroll()
            file_range = len(self.poco("com.google.android.documentsui:id/dir_list").child())
            if self.poco("com.google.android.documentsui:id/item_root")[file_range - 1].child().child()[
                0].get_name() != "android.widget.LinearLayout":
                new_last_child = \
                self.poco("com.google.android.documentsui:id/item_root")[file_range - 2].child().child()[
                    0].child().child().get_text()
                file_count = file_range - 2
                pass
            else:
                new_last_child = \
                self.poco("com.google.android.documentsui:id/item_root")[file_range - 1].child().child()[
                    0].child().child().get_text()
                file_count = file_range - 1
            if new_last_child == current_last_child:
                print("breakingggg...")
                return file_list
            for i in range(file_count):
                file_name = self.poco("com.google.android.documentsui:id/item_root")[i].child().child()[
                    0].child().child().get_text()
                temp.append(file_name)
            if current_last_child in temp:
                index_from = temp.index(current_last_child) + 1
            else:
                index_from = 0
            for i in range(index_from, len(temp)):
                sleep(3)
                file_list.append(temp[i])
                print(file_list)
                if not enter_while:
                    sleep(5)
                    self.click_Add_File()
                    sleep(2)
                    self.click_Upload_File()
                    sleep(2)
                    for j in range(scroll_count):
                        self.poco.scroll()
                file_i = self.poco("com.google.android.documentsui:id/item_root")[i]
                print(file_i.child().child()[0].child().child().get_text())
                file_i.click()
                enter_while = False
            current_last_child = new_last_child

    def searchMyDesigns(self, design_name, enter=True):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(design_name)
        if enter:
            self.clickEnter()

    def verifyPreviewShownIsCorrect(self):
        assert_exists(self.test_45738, "Preview shown is correct.")

    def labelRangeSelection(self, label_range, confirm=True):
        checkbox = self.poco(self.Check_Box)
        self.poco("All").click()
        checkbox[0].click()
        checkbox[0].click()
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
        os.system('adb shell input keyevent 26')

    def clickGotItWeb(self):
        if self.poco(text="Got It").exists():
            self.poco(text="Got It").click()

    def get_current_date(self):
        year = datetime.date.today().year
        date = datetime.date.today().day
        month = self.Month[datetime.date.today().month]
        current_date = str(month) + " " + str(date) + ", " + str(year)
        return current_date
