# LoginFunction.py

import datetime
import random
import string
import fnmatch

from airtest.core.api import *
# import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoNoSuchNodeException, PocoTargetTimeout

from ZSB_Mobile.Common_Method import Common_Method

common_method = Common_Method(poco)


class Data_Sources_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Home = "Home"
        self.My_Data = "My Data"
        self.Add_File = "Toggle"
        self.Upload_File = "Upload File"
        self.File_Data_Source_Device_Local_File = "Local File"
        self.File_Data_Source_Device_GDrive = "Google Drive"
        self.File_Data_Source_Device_OneDrive = "OneDrive"
        self.My_Designs = "My Designs"
        self.Print_Btn = "Print"
        self.Camera = "Camera"
        self.Remove_Btn = "Remove"
        self.Cancel_Btn = "Cancel"
        self.HamburgerMenuLocalStorage = "Show roots"
        self.BrowseLocalStorage = "Browse"
        self.Create_New_Design = "Create New Design"
        self.Create_Btn = "Create"
        self.Bar_Code_Location = Template(r"tpl1707978279280.png", record_pos=(-0.055, 0.03), resolution=(1080, 2340))
        self.File_Info_Device = []
        self.File_Info_App = []
        self.Name = "Name"
        self.Month = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
                      7: "Jul", 8: "Aug", 9: "Sept", 10: "Oct", 11: "Nov", 12: "Dec"}
        self.List_Empty = "List is empty"
        self.Date_Added = "DATE ADDED"
        self.Continue = "Continue"
        self.Check_Box = "Switch"
        self.Confirm_Btn = "Confirm"
        self.Label_Range = 0
        self.Use_Local_Contacts = "Use Local Contacts"
        self.Search_Files = Template(r"tpl1705645360605.png", record_pos=(-0.261, -0.571), resolution=(1080, 2340))
        self.expectedSearchList = ["Tes1.jpg", "Test2.png", "Test3.bmp"]
        self.Sign_In_With_Microsoft = "Sign in with Microsoft"
        self.Sign_In_With_Microsoft_Template = Template(r"Microsoft_Icon11.png", record_pos=(0.002, 0.183),
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
        sleep(3)
        my_data = self.poco(self.My_Data)
        my_data.wait_for_appearance(timeout=10)
        my_data.click()

    def click_Add_File(self):
        add_file = self.poco(self.Add_File)
        add_file.wait_for_appearance(timeout=10)
        add_file.click()

    def click_Upload_File(self):
        upload_file = self.poco("Button")[-1]
        upload_file.wait_for_appearance(timeout=10)
        upload_file.click()
        if self.poco("Allow").exists():
            self.poco("Allow").click()

    def click_Upload_File_Web(self):
        upload_file = self.poco(self.Upload_File)
        upload_file.click()
        sleep(2)
        self.poco("Choose File").click()

    def click_Link_File(self):
        link_file = self.poco("Button")[-2]
        link_file.wait_for_appearance(timeout=10)
        link_file.click()

    def chooseAccToLinkFile(self, Acc_Name="swdvt zsb"):
        if self.poco("Continue").exists():
            self.poco("Continue").click()
        self.poco("Choose an account").wait_for_appearance(timeout=10)
        account = self.poco(text=Acc_Name)
        account.click()

    def enterMicrosoftUsername(self, username):
        sleep(3)
        self.poco("Enter your email, phone, or Skype.").wait_for_appearance(timeout=20)
        self.poco("Enter your email, phone, or Skype.").click()
        text(username)
        self.poco("Next").click()
        sleep(3)

    def verify_File_Data(self, file_name, data_source):
        self.verifyFilePresentInList(file_name, data_source, True, True)

    def clickMyDesigns(self):
        sleep(3)
        my_designs = self.poco(self.My_Designs)
        my_designs.wait_for_appearance(timeout=10)
        my_designs.click()

    def selectDesignCreatedAtSetUp(self):
        self.poco(nameMatches="Showing.*").wait_for_appearance(timeout=10)
        set_up_design = self.poco(type="Image")
        set_up_design.click()

    def selectDesignCreatedAtSetUpWeb(self):
        self.poco(textMatches="Showing.*").wait_for_appearance(timeout=10)
        set_up_design = self.poco("Image")
        set_up_design.click()

    def scroll_till_print(self):
        count = 5
        while not self.poco(self.Print_Btn).exists() and count != 0:
            start_point = (0.5, 0.8)
            vector = (0.5, 0.4)
            swipe(start_point, vector)
            count -= 1
        start_point = (0.5, 0.8)
        vector = (0.5, 0.4)
        swipe(start_point, vector)
        sleep(2)

    def clickPrint(self):
        if self.poco(self.Print_Btn).exists():
            print_btn = self.poco(self.Print_Btn)
        else:
            print_btn = self.poco(text=self.Print_Btn)
        print_btn.wait_for_appearance(timeout=10)
        print_btn.click()

    def verifyPhotoOptions(self):
        photo_options = self.poco(nameMatches=".*Picture.*")
        photo_options.exists()

    def expandPhotoOptions(self):
        photo_options = self.poco(nameMatches=".*Picture.*")
        photo_options.click()

    def chooseCameraToClickPhoto(self):
        camera = self.poco(self.Camera)
        camera.wait_for_appearance(timeout=20)
        camera.click()

    def clickRemove(self):
        remove_btn = self.poco(self.Remove_Btn)
        remove_btn.click()

    def clickCancel(self):
        cancel_btn = self.poco(self.Cancel_Btn)
        cancel_btn.wait_for_appearance(timeout=10)
        cancel_btn.click()

    def verifyProgressIndicator(self):
        if self.poco(self.Name).exists():
            print("Progress indicator did not appear")
            return 1 / 0
        else:
            return

    def clickEnter(self):
        keyevent("Enter")

    def click_Menu_HamburgerICNWeb(self):
        sleep(3)
        self.poco("Zebra Small Office Home Office").child("Other").child("Link").click()
        sleep(3)

    def clickCreateDesignBtn(self):
        if self.poco(self.Create_Btn).exists():
            self.poco(self.Create_Btn).focus([0.9,0.9]).click()
        else:
            start_point = (0.5, 0.8)
            vector = (0.5, 0.6)
            swipe(start_point, vector)
            self.poco(self.Create_New_Design).click()

    def selectLabelSize(self):
        self.poco(nameMatches=".*ZSB.*").click()

    def clickContinue(self):
        try:
            self.poco(self.Continue).wait_for_appearance(timeout=20)
            self.poco(self.Continue).click()
        except:
            self.poco("CONTINUE", enabled=True).wait_for_appearance(timeout=20)
            self.poco("CONTINUE").click()

    def clickContinueWeb(self):
        self.poco("Continue").wait_for_appearance(timeout=10)
        self.poco("Continue").focus([0.1,0.1]).click()

    def exitDesigner(self):
        self.poco("Exit Designer").wait_for_appearance(timeout=10)
        self.poco("Exit Designer").focus([0.9,0.9]).click()

    def setLabelName(self, name):
        self.poco("New label").parent().child()[1].click()
        self.poco("TextField").focus([0.9, 0.9]).click()
        text("PullDownToRefresh")
        if self.poco("Done").exists():
            self.poco("Done").click()

    def fileListDisplayed(self, no_of_swipes=False):
        File_List = []
        if self.poco("You don’t have any files").exists():
            return File_List
        for child in self.poco("ScrollView")[1].parent().child():
            if ((".png" in child.get_name()) or (".jpg" in child.get_name()) or (".txt" in child.get_name()) or (
                    ".csv" in child.get_name()) or (".xlsx" in child.get_name()) or (
                    "bnp" in child.get_name())):
                File_List.append(child.get_name())
        return File_List

    def checkIfDesignsLoaded(self):
        sleep(10)
        if self.poco(nameMatches=".*Showing.*").exists():
            pass
        else:
            raise Exception("Designs not loaded.")

    def searchName(self, name):
        try:
            self.poco("Search files").click()
        except:
            self.poco("TextField").click()
        sleep(2)
        text(name)
        sleep(2)

    def checkIfListIsEmpty(self):
        try:
            self.poco(self.List_Empty).wait_for_appearance(timeout=10)
        except:
            raise Exception("List not empty")

    def log_out_for_current_execution_ios(self):
        sleep(8)
        if self.poco("Open navigation menu").exists():
            self.poco("Open navigation menu").click()
            self.poco("Button").click()
            self.poco.scroll()
            self.poco("Log Out").click()
        sleep(2)

    def verifyIfPreviewIsPresent(self):
        if self.poco("Image").exists():
            return
        else:
            raise Exception("Preview not shown")

    def checkPrintIsDisabled(self):
        if self.poco("Print", enabled=False).exists():
            pass
        else:
            raise Exception("Print is Enabled")

    def clickCheckBox(self, checkbox_number=0):
        checkbox = self.poco(self.Check_Box)
        checkbox[checkbox_number].click()

    def clickConfirm(self):
        self.poco(self.Confirm_Btn).click()

    def clickGoogleDrive(self):
        google_drive = self.poco(nameMatches="(?s).*Google Drive.*")
        google_drive.wait_for_appearance(timeout=10)
        google_drive.click()

    def clickMicrosoftOneDrive(self):
        one_drive = self.poco(nameMatches="(?s).*Microsoft OneDrive.*")
        one_drive.wait_for_appearance(timeout=10)
        one_drive.click()

    def verifySignInWithMicrosoft(self):
        try:
            assert_exists(self.Sign_In_With_Microsoft_Template)
            return True
        except:
            return False

    def verifySignInWithGoogle(self):
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
        if click_template:
            touch(self.Sign_In_With_Microsoft_Template)
            sleep(5)
        self.poco("Enter your email, phone, or Skype.").wait_for_appearance(timeout=20)
        self.poco("Enter your email, phone, or Skype.").click()
        text(username)
        self.poco("Next").click()
        sleep(3)
        self.poco("Enter the password for " + username).wait_for_appearance(timeout=10)
        self.poco("Enter the password for " + username).click()
        text(password)

    def wait_for_element_appearance_text(self, element, time_out=15):
        self.poco(text=element).wait_for_appearance(timeout=time_out)

    def checkIfAccPresentLink(self, account):
        if self.poco(label="username").exists():
            self.poco(label="username").click()
            return
        sleep(5)

    def sign_In_With_Google(self, password, username=None, wrong_password=False):
        if username is not None:
            self.poco(type="TextField").click()
            text(username)
            sleep(5)
        self.poco(type="SecureTextField").click()
        text(password)
        sleep(5)
        if wrong_password:
            try:
                self.wait_for_element_appearance_text(
                    "Wrong password. Try again or click ‘Forgot password’ to reset it.")
            except:
                raise Exception(
                    "Error message: \"Wrong password. Try again or click Forgot password to reset it.\" not displayed.")
        swipe([0.5, 0.5], [0.5, 0.1])

        self.poco("Continue").click()


    def signInWithGoogle(self, username, password):
        if self.poco(self.Sign_In_With_Google).exists():
            sign_in_with_google = self.poco(self.Sign_In_With_Google)
            sign_in_with_google.click()
        else:
            touch(self.Sign_In_With_Google_Template)
        sleep(4)
        if self.poco("Continue").exists():
            self.poco("Continue").click()
        self.poco("Choose an account").wait_for_appearance(timeout=10)
        if self.poco(label="username").exists():
            self.poco(label="username").click()
            return
        swipe([0.5, 0.5], [0.5, 0.1])
        if self.poco(label="username").exists():
            self.poco(label="username").click()
            return
        sleep(5)
        self.poco("Use another account").click()
        self.poco(type="TextField").click()
        text(username)
        sleep(5)
        self.poco(type="SecureTextField").click()
        text(password)
        sleep(5)
        swipe([0.5, 0.5], [0.5, 0.1])
        self.poco("Continue").click()

    def signInWithEmail(self):
        try:
            self.poco("Sign In with your email").wait_for_appearance(timeout=20)
            self.poco("Sign In with your email").click()
            print("Successfully clicked Sign In With Email")
        except PocoNoSuchNodeException:
            print("Sign In with Email option not found!\n Test Continues...")
            raise Exception("Sign In with Email option not found!\n Test Failed")
        except Exception as e:
            self.poco(text="Sign In with your email").wait_for_appearance(timeout=20)
            self.poco(text="Sign In with your email").click()
            print("Successfully clicked Sign In With Email")

    def clickBackArrow(self):
        sleep(3)
        back_arrow = self.poco(name="Button")
        back_arrow.wait_for_appearance(timeout=20)
        back_arrow.click()
        sleep(4)

    def checkNoChangeInFileCount(self, initialFileCount):
        file_list = self.fileListDisplayed()
        curr_file_count = len(file_list)
        if initialFileCount == curr_file_count:
            return
        else:
            print("Number of files are not same as before")
            return 1 / 0

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

    def selectExistingFile(self):
        supported_types = ["jpg", "png", "bmp", "txt", "xlsx", "csv"]
        for i in range(len(self.poco("DATE ADDED").parent().child())):
            child = self.poco("DATE ADDED").parent().child()[i].get_name()
            if self.substring_after(child, ".") in supported_types:
                print("del", self.substring_after(child, "."))
                print(child)
            self.clickSelect()
        return child

    def checkIsAlreadyLinkedPopUp(self):
        try:
            self.poco(nameMatches=".*is already linked.*").wait_for_appearance(timeout=20)
        except:
            raise Exception("File already linked pop up not present.")

    def searchFilesInLinkFiles(self, file_name):
        touch(Template(r"search_files_link_files.png", record_pos=(-0.247, -0.567), resolution=(1080, 2340)))
        text(file_name[:4])
        sleep(4)

    def verifyFilePresentInList(self, file_name, datasource=None, data=False, verify_date=True):
        if self.poco(self.List_Empty).exists():
            raise Exception(file_name + "File not present")
        return_value = False
        for i in range(len(self.poco("ScrollView")[0].parent().child())):
            if self.poco("ScrollView")[0].parent().child()[i].get_name() == file_name:
                start_index = i
                return_value = True
        date_added = self.poco("ScrollView")[0].parent().child()[start_index + 1].get_name()
        data_source = self.poco("ScrollView")[0].parent().child()[start_index + 2].get_name()
        if not data:
            return return_value
        else:
            year = datetime.date.today().year
            date = datetime.date.today().day
            month = self.Month[datetime.date.today().month]
            expected_date = str(month) + " " + str(date) + ", " + str(year)
            if return_value:
                if verify_date:
                    if date_added == expected_date:
                        pass
                    else:
                        raise Exception("Date not matching")
                if datasource is not None:
                    if datasource == data_source:
                        return
        raise Exception(file_name + " File not present")

    def clickHome(self):
        home_btn = self.poco(self.Home)
        home_btn.wait_for_appearance(timeout=10)
        home_btn.click()

    def verify_Remove_File_Warning(self, file_type):
        content = self.poco(nameMatches="(?s).*Remove local file.*").get_name()
        if file_type == "Local File":
            if content == "Remove local file\nAre you sure you want to remove the local file? All fields using this data source will need to be reconnected to a data source.":
                return
            else:
                raise Exception("Remove file message not matching.")
        else:
            if content == "Remove linked file\nAre you sure you want to remove the local file? All fields using this data source will need to be reconnected to a data source.":
                return
            else:
                raise Exception("Remove file message not matching.")

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

    def remove_File_Based_On_DataSource(self, datasource, filename=None, cancel=False, verify=False):
        scroll_view = self.poco("DATA SOURCE").parent().child("ScrollView")
        while not self.poco("DATA SOURCE").exists():
            scroll_view.swipe("left")
        for i in range(5):
            scroll_view.swipe("left")

        for i in range(len(self.poco("DATA SOURCE").parent().child())):
            if self.poco("DATA SOURCE").parent().child()[i].get_name() == datasource:
                if filename is not None:
                    if self.poco("DATA SOURCE").parent().child()[i - 2].get_name() == filename:
                        self.poco("DATA SOURCE").parent().child()[i + 1].child("Button").click()
                        self.clickRemove()
                        if verify:
                            self.verify_Remove_File_Warning(datasource)
                        if not cancel:
                            self.clickRemove()
                        else:
                            self.clickCancel()
                        return
                else:
                    self.poco("DATA SOURCE").parent().child()[i + 1].child("Button").click()
                    self.clickRemove()
                    if verify:
                        self.verify_Remove_File_Warning(datasource)
                    if not cancel:
                        self.clickRemove()
                    else:
                        self.clickCancel()
                    return

        raise Exception("No file with datasource " + datasource)

    def remove_File(self, cancel=False):
        common_method.swipe_screen([0.9, 0.3482905982905983], [0.22037037037037038, 0.3482905982905983], 5)
        three_dot = self.poco("Button")
        three_dot.click()
        self.clickRemove()
        try:
            self.verify_Remove_File_Warning("Local File")
        except:
            self.verify_Remove_File_Warning("Google Drive")
        if not cancel:
            self.clickRemove()
        else:
            self.clickCancel()

    def checkDriveEmpty(self):
        if len(self.poco("ScrollView")[0].parent().child()) == 4:
            return
        else:
            raise Exception("Drive Not Empty")

    def searchFileInLocalStorage(self, filename):
        self.poco(self.BrowseLocalStorage).wait_for_appearance(timeout=20)
        self.poco(self.BrowseLocalStorage).click()
        sleep(2)
        self.poco(self.BrowseLocalStorage).click()
        sleep(2)
        self.poco("On My iPhone").click()
        sleep(2)
        self.poco("Search").click()
        sleep(2)
        text(filename)
        sleep(2)
        file = self.poco(type="StaticText",
                         nameMatches=".*" + filename + ".*").parent().parent().child().child().click()

    def selectFileToUploadWeb(self):
        self.poco(self.BrowseLocalStorage).wait_for_appearance(timeout=20)
        self.poco(self.BrowseLocalStorage).click()
        sleep(2)
        self.poco(self.BrowseLocalStorage).click()
        sleep(2)
        self.poco("On My iPhone").click()
        sleep(2)
        selected_file_name = self.poco("Image")[0].parent().parent().child()[1].child().get_name()
        file = self.poco(type="StaticText",
                         nameMatches=".*" + selected_file_name + ".*").parent().parent().child().child().click()
        return selected_file_name

    def selectUnSupportedFile(self):
        """Yet to write"""

    def selectFilesInLocal(self):
        file_list = []
        prev_list = []
        curr_list = []
        start = 1
        scroll_count = 0
        while 1:
            file_count = len(self.poco("File View"))
            print(file_count)
            for i in range(start, file_count + 1):
                print(i)
                filee_name = \
                    self.poco("Image")[i].parent().parent().child()[1].child().get_name()
                print(filee_name)
                curr_list.append(filee_name)
                print("curr:", curr_list)

            for name in curr_list:
                if name not in file_list:
                    print(name)
                    file_list.append(name)
                    print("file", file_list)
                    file = self.poco(type="StaticText",
                                     nameMatches=".*" + name + ".*").parent().parent().child().child().click()
                    file.click()
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

    def searchMyDesigns(self, design_name, enter=True):
        self.poco("Search designs").click()
        sleep(2)
        text(design_name)
        sleep(2)

    def select_All(self, check=True):
        checked_value = common_method.getAttr(self.poco("Switch"), "value")
        if checked_value:
            if not check:
                self.poco("Switch").click()
        else:
            if check:
                self.poco("Switch").click()

    def labelRangeSelection(self, label_range, confirm=True):
        self.scroll_till_print()
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

    def clickUsePhoto(self):
        self.poco("Use Photo").click()

    def allowPermissions(self):
        self.poco(text="While using the app").click()

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

    def selectFileDrive(self, file_name):
        self.searchFilesInLinkFiles(file_name)
        try:
            self.poco(file_name).wait_for_appearance(timeout=20)
            self.poco(file_name).click()
        except PocoTargetTimeout:
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
        sleep(10)
        if self.poco("Continue").exists():
            self.poco("Continue").click()
        try:
            self.poco("Home").wait_for_appearance(timeout=20)
        except:
            raise Exception("Did not reach home page.")

    def checkIfOnHomePageWeb(self):
        try:
            self.poco(text="Home").wait_for_appearance(timeout=20)
        except:
            raise Exception("Did not reach home page.")

    def signIn_if_on_SSO_page_web(self):
        sleep(3)
        if self.poco("pi.zebra.com").exists():
            touch(Template(r"Google_Icon.png", record_pos=(-0.319, -0.173), resolution=(1080, 2340)))
            try:
                self.poco("Sign in with Google").wait_for_appearance(timeout=15)
            except:
                raise Exception("Did not navigate to Sign In with google page")
            account = "zebra02.swdvt@gmail.com"
            self.sign_In_With_Google("Zebra#123456789", account)

    def scroll_till_log_out(self):
        while not self.poco("Log Out").exists():
            self.poco.scroll()
        self.poco.scroll()

    def open_chrome(self):
        sleep(2)
        start_app("com.google.chrome.ios")
        sleep(5)

    def close_chrome(self):
        sleep(2)
        self.poco("kToolbarStackButtonIdentifier").click()
        sleep(2)
        self.poco("Close")[-1].click()
        sleep(2)
        self.poco("TabGridRegularTabsPageButtonIdentifier").click()
        sleep(2)
        stop_app("com.google.chrome.ios")
