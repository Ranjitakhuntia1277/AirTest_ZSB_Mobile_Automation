from time import sleep
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from poco import poco

from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import common_method


class Smoke_Test_iOS:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.SignIn_With_Text = "Sign In With"
        self.Continue_With_Facebook_Option = "Continue with Facebook"
        self.Continue_With_Apple_Option = "Continue with Apple"
        self.home_Text_IS_Present = "Home"
        self.Facebook_UserName = Template(os.path.join(os.path.expanduser('~'),
                                                       "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\PageObject\Images",
                                                       "tpl1707806465367.png"), record_pos=(-0.169, -0.869),
                                          resolution=(1170, 2532))
        self.Continue_With_Password_ForApple_Login = "Continue with Password"
        self.click_On_Password_Text_field = "SecureTextField"
        self.Sign_In_Option = "Sign In"
        self.Apple_UserName = Template(os.path.join(os.path.expanduser('~'),
                                                    "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\PageObject\Images",
                                                    "tpl1707817586300.png"), record_pos=(-0.191, -0.867),
                                       resolution=(1170, 2532))

        self.Google_UserName = Template(os.path.join(os.path.expanduser('~'),
                                                     "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\PageObject\Images",
                                                     "tpl1707818376117.png"), record_pos=(-0.174, -0.867),
                                        resolution=(1170, 2532))

        self.My_Data = "My Data"
        self.Add_File = "android.widget.Button"
        self.Upload_File = "android.widget.Button"
        self.Link_File = "android.widget.Button"
        self.File_Data_Source_Device_Local_File = "Local File"
        self.File_Data_Source_Device_GDrive = "Google Drive"
        self.Select = "Select"
        self.Print_button = "Print"
        self.MyData_Tab = "My Data"
        self.Plus_Icon = ""
        self.LinkFile = ""
        self.SignIn_With_Microsoft = ""
        self.Select_Upload_Files = ""
        self.Uploaded_Files = ""
        self.Delete_File = ""
        self.Print_Button = "Print"
        self.Copies_Field = ""
        self.Delete_Button_On_MyDesign = "Delete"
        self.Cancel_Button_On_Delete_Popup = "Cancel"
        self.Delete_Button_On_Delete_Popup = "Delete"
        self.Deleted_Successfully_Message = ""
        self.Address_Header_And_Description = ""
        self.Barcodes_Header_And_Description = ""
        self.Jewelry_Header_And_Description = ""
        self.Multipurpose_Header_And_Description = ""
        self.Shipping_Header_And_Description = ""
        self.ReturnAddress_Header_And_Description = ""
        self.Postage_Header_And_Description = ""
        self.Round_Header_And_Description = ""
        self.SmallMultipurpose_Header_And_Description = ""
        self.XLShipping_Header_And_Description = ""
        self.XLShipping_Header_And_Description = ""
        self.Back_Icon_On_Address_Screen = ""
        self.Common_Design_Page = ""
        self.Copy_To_My_Design_Text = ""

    ##""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def Verify_SignIn_With_Text_Is_Present(self):
        sleep(10)
        SignIn_With_Text = self.poco(self.SignIn_With_Text)
        SignIn_With_Text.get_text()
        return SignIn_With_Text

    def click_Continue_With_Facebook_Option(self):
        sleep(2)
        Continue_With_Facebook_Option = self.poco(self.Continue_With_Facebook_Option)
        Continue_With_Facebook_Option.click()
        sleep(20)

    def Verify_Facebook_UserName_Is_Displaying(self):
        sleep(3)
        assert_exists(self.Facebook_UserName, "Facebook UserName is displaying")

    def click_Continue_With_Apple_Option(self):
        sleep(2)
        Continue_With_Apple_Option = self.poco(self.Continue_With_Apple_Option)
        Continue_With_Apple_Option.click()
        sleep(20)

    def click_Continue_With_Password_ForApple_Login(self):
        sleep(2)
        Continue_With_Password_ForApple_Login = self.poco(self.Continue_With_Password_ForApple_Login)
        Continue_With_Password_ForApple_Login.click()

    def click_On_Password_Textfield(self):
        enter_apple_id_password = self.poco(self.click_On_Password_Text_field)
        enter_apple_id_password.click()
        sleep(2)

    def Enter_Apple_ID_Password(self):
        self.poco(text("Testing@123"))

    def click_On_Sign_In_Option(self):
        sleep(2)
        Sign_In_Option = self.poco(self.Sign_In_Option)
        Sign_In_Option.click()
        sleep(9)

    def Verify_Apple_UserName_Is_Displaying(self):
        sleep(3)
        assert_exists(self.Apple_UserName, "Apple UserName is displaying")

    def Verify_Google_UserName_Is_Displaying(self):
        sleep(3)
        assert_exists(self.Google_UserName, "Google UserName is displaying")

    def click_My_Data(self):
        my_data = self.poco(self.My_Data)
        my_data.wait_for_appearance(timeout=10)
        my_data.click()

    def click_Add_File(self):
        add_file = self.poco(self.Add_File)
        add_file.wait_for_appearance(timeout=10)
        add_file.click()

    def clickSelect(self):
        select = self.poco(self.Select)
        select.click()

    def click_Upload_File(self):
        upload_file = self.poco(self.Upload_File)
        upload_file.wait_for_appearance(timeout=10)
        upload_file[1].click()

    def click_Link_File(self):
        link_file = self.poco(self.Link_File)
        link_file.wait_for_appearance(timeout=10)
        link_file.click()

    def clickGoogleDrive(self):
        google_drive = self.poco("android.view.View")[3].child()[1]
        google_drive.click()

    def getCurrCount(self, after_scroll=False):
        if after_scroll:
            return (len(self.poco("android.widget.HorizontalScrollView").child()) - 2) // 4
        else:
            if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
                if self.poco("android.widget.HorizontalScrollView").child()[2].get_name() == "DATA SOURCE":
                    return (len(self.poco("android.widget.HorizontalScrollView").child()) - 3) // 3
                return (len(self.poco("android.widget.HorizontalScrollView").child()) - 2) // 2
            else:
                return len(self.poco("android.widget.HorizontalScrollView").child()) - 1

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

    def checkFilesShownAreSupported(self):
        supported_types = ["jpg", "png", "bmp", "txt", "xlsx", "csv"]
        file_list = self.fileListDisplayed()
        for i in file_list:
            if self.substring_after(i, ".") in supported_types:
                return
            else:
                raise Exception(str(i) + " is not of supported format")

    def selectLargeFile(self):
        if self.poco("android.widget.HorizontalScrollView").child()[1].get_name() == "DATE ADDED":
            search_File_Name = self.poco("android.widget.HorizontalScrollView").child()[4].get_name()
            self.poco("android.widget.HorizontalScrollView").child()[4].click()
            self.clickSelect()
        else:
            search_File_Name = self.poco("android.widget.HorizontalScrollView").child()[2].get_name()
            self.poco("android.widget.HorizontalScrollView").child()[2].click()
            self.clickSelect()

    def fileListDisplayed(self, no_of_swipes=False):
        File_List = []
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
            common_method.swipe_screen([0.5, 0.9175213675213675], [0.5, 0.080], 1)
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
                break
            else:
                for i in range(len(temp)):
                    File_List.append(temp[i])
                current_last_child = new_last_child
            temp = []
        common_method.swipe_screen([0.5, 0.080], [0.5, 0.9175213675213675], swipe_count)
        if not no_of_swipes:
            return File_List
        else:
            return File_List, swipe_count

    def check_printer_online_status(self):
        child_names = [child.get_name() for child in
                       self.poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child(
                           "android.view.View").child("android.view.View").child("android.view.View").offspring(
                           "android.widget.ScrollView").child("android.view.View")[0].child("android.view.View").child(
                           "android.view.View")[0].children()]
        modified_list = [item.split('\n') for item in child_names]

        return modified_list[0][0]

    def select_first_label_from_home(self):
        first_label = \
            self.poco("android.widget.ScrollView").child("android.view.View")[1].child("android.view.View").child()[0]
        first_label.click()

    def click_print_button(self):
        print_btn = self.poco(self.Print_button)
        print_btn.click()

    def check_error_print_preview(self):
        a = self.poco("Error\nCould not fetch the Print Preview")
        if a:
            self.poco("Cancel").click()
        else:
            pass

    def click_left_arrow(self):
        self.poco("android.widget.Button").click()

    def click_MyData_Tab(self):
        sleep(2)
        MyData_Tab = self.poco(self.MyData_Tab)
        MyData_Tab.click()
        sleep(4)

    def click_Plus_icon(self):
        sleep(2)
        Plus_icon = self.poco(self.Plus_Icon)
        Plus_icon.click()
        sleep(4)

    def click_LinkFile(self):
        sleep(2)
        LinkFile = self.poco(self.LinkFile)
        LinkFile.click()
        sleep(4)

    def click_SignIn_With_Microsoft(self):
        sleep(2)
        SignIn_With_Microsoft = self.poco(self.SignIn_With_Microsoft)
        SignIn_With_Microsoft.click()
        sleep(4)

    def Upload_Files(self):
        sleep(2)
        Upload_Files = self.poco(self.Select_Upload_Files)
        Upload_Files.click()
        sleep(10)

    def Verify_Uploaded_Files(self):
        sleep(2)
        assert_exists(self.Uploaded_Files, "Upload File is displaying")

    def Click_Delete_File(self):
        sleep(2)
        Delete_File = self.poco(self.Delete_File)
        Delete_File.click()
        sleep(6)

    def enter_user_email_for_registering(self, email):
        self.poco("android.widget.EditText").set_text(email)

    def click_on_next(self):
        self.poco(text="Next").click()

    def wait_for_element_appearance(self, element, time_out=10):
        self.poco(element).wait_for_appearance(timeout=time_out)

    def enter_the_verification_code(self, code):
        self.poco("android.widget.EditText").set_text(code)

    def enter_the_fields(self, firstname, lastname, password):
        temp2 = self.poco("android.widget.EditText")[0]
        temp1 = self.poco(text="signup.zebra.com")
        temp2.drag_to(temp1)
        sleep(3)

        self.poco("android.widget.EditText")[0].set_text(firstname)

        self.poco("android.widget.EditText")[1].set_text(lastname)

        self.poco("android.widget.EditText")[2].set_text(password)

        self.poco("android.widget.EditText")[3].set_text(password)

    def select_the_country(self, country):
        self.poco(text="-- Select --").click()
        scroll_view = self.poco("android.widget.ListView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 26
        for _ in range(max_swipes):
            # Swipe up on the ScrollView
            scroll_view.scroll()

            # Check if the "Accept" element is present and enabled
            search = self.poco(text=country)
            if search.exists():
                self.poco(text=country).click()
                # Accept button is visible and enabled, break out of the loop
                break

    def select_the_check_boxes(self):

        self.poco("android.widget.CheckBox")[0].click()

        self.poco("android.widget.CheckBox")[1].click()

    def click_submit_and_continue(self):
        start_point = [0.5, 0.7]
        end_point = [0.5, 0.4]
        for i in range(1):
            self.poco.swipe(start_point, end_point, duration=0.1)
        self.poco(text="SUBMIT AND CONTINUE").click()

    def check_sign_up_successful(self):
        self.poco("CONTINUE").wait_for_appearance(timeout=30)
        self.poco("CONTINUE").wait_for_appearance(timeout=30)
        self.poco(text="ZSB Printer registration completed.").exists()
        self.poco(text="Success! Click \"continue\" to log into your account.").exists()

    def click_continue_registration_page(self):
        self.poco("CONTINUE").click()

    def wait_for_element_appearance_text(self, element, time_out=15):
        self.poco(text=element).wait_for_appearance(timeout=time_out)

    def signInWithEmail(self):
        try:
            self.poco("android.widget.Button").wait_for_appearance(timeout=10)
            self.poco("android.widget.Button").click()
            self.poco("com.android.chrome:id/coordinator").click()
            print("Successfully clicked Sign In With Email")
        except PocoNoSuchNodeException:
            print("Sign In with Email option not found!\n Test Continues...")
            raise Exception("Sign In with Email option not found!\n Test Failed")

    def complete_sign_in_with_email(self, user_name, password, click_on_sign_in=1, click_back=1, wrong_password=False,
                                    enter_only_password=False):

        if click_back:
            keyevent("back")
        if not enter_only_password:
            self.poco("com.android.chrome:id/coordinator").click()
            self.poco("android.widget.EditText")[0].wait_for_appearance(timeout=10)
            self.poco("android.widget.EditText")[0].set_text(user_name)
        self.poco("android.widget.EditText")[1].wait_for_appearance(timeout=10)
        self.poco("android.widget.EditText")[1].set_text(password)

        # self.poco(text="Sign In").click()
        if click_on_sign_in:
            self.poco("android.widget.Button")[1].click()
        if wrong_password:
            error_message = self.poco("android.widget.TextView").get_text()
            if error_message == "We didn't recognize the username or password you entered. Please try again.":
                print("Successfully displayed Error message for wrong password")
                return
            else:
                print("Error message not displayed for wrong password.")
                raise Exception("Error message not displayed for wrong password.")


    def click_Print_Button(self):
        sleep(3)
        Print_Button = self.poco(self.Print_Button)
        Print_Button.click()
        sleep(2)

    def click_Second_Print_Button(self):
        sleep(4)
        Print_Button = self.poco(self.Print_Button)
        Print_Button.click()
        sleep(8)

    def clear_Copies_Field(self):
        Copies_Field = self.poco(self.Copies_Field)
        Copies_Field.set_text("")

    def click_On_Copies_Filed(self):
        sleep(3)
        Copies_Filed = self.poco(self.Copies_Field)
        Copies_Filed.click()
        sleep(2)

    def Add_Multiple_Copies_Number(self):
        Multiple_Copies_Number = self.poco(self.Copies_Field)
        Multiple_Copies_Number.set_text("3")


    def click_Delete_Button_On_MyDesign(self):
        sleep(3)
        Delete_Button_On_MyDesign = self.poco(self.Delete_Button_On_MyDesign)
        Delete_Button_On_MyDesign.click()
        sleep(2)

    def click_Cancel_Button_On_Delete_Popup(self):
        sleep(3)
        Cancel_Button = self.poco(self.Cancel_Button_On_Delete_Popup)
        Cancel_Button.click()
        sleep(2)

    def Click_Delete_Button_On_Delete_Popup(self):
        sleep(5)
        delete_Button = self.poco(self.Delete_Button_On_Delete_Popup)
        delete_Button.click()

    def Verify_Deleted_Successfully_Message(self):
        assert_exists(self.Deleted_Successfully_Message, "Successfully Deleted Message is displaying")

    def Verify_List_Is_Sorted_From_A_TO_Z(self):
        def is_sorted_a_to_z(input_list):
            sorted_list = sorted(input_list)
            return input_list == sorted_list

        # Example list to test
        example_list = ['Address', 'Barcodes']

        # Verify if the list is sorted from A to Z
        is_sorted = is_sorted_a_to_z(example_list)

        if is_sorted:
            print("The list is sorted from A to Z.")
        else:
            print("The list is not sorted from A to Z.")

    def Verify_Address_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Address_Header_And_Description, "Address Header And Description is displaying")
        # poco.swipe([0.5, 0.8], [0.5, 0.2], duration=1)
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("up", duration=0.5)

    def Verify_Barcodes_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Barcodes_Header_And_Description, "Barcodes Header And Description is displaying")
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("up", duration=0.5)

    def Verify_Jewelry_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Jewelry_Header_And_Description, "Jewelry Header And Description is displaying")
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("up", duration=0.5)

    def Verify_Multipurpose_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Multipurpose_Header_And_Description, "Multipurpose Header And Description is displaying")
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("up", duration=0.5)

    def Verify_Shipping_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Shipping_Header_And_Description, "Shipping Header And Description is displaying")
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("up", duration=0.5)

    def Verify_ReturnAddress_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.ReturnAddress_Header_And_Description, "ReturnAddress Header And Description is displaying")
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("up", duration=0.5)

    def Verify_Postage_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Postage_Header_And_Description, "Postage Header And Description is displaying")
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("up", duration=0.5)

    def Verify_Round_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Round_Header_And_Description, "Round Header And Description is displaying")
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("up", duration=0.5)

    def Verify_SmallMultipurpose_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.SmallMultipurpose_Header_And_Description, "SmallMultipurpose Header And Description is displaying")
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("up", duration=0.5)

    def Verify_XLShipping_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.XLShipping_Header_And_Description,"XLShipping Header And Description is displaying")
        scroll_view = self.poco("ScrollView")
        # Set the maximum number of swipes to avoid an infinite loop
        max_swipes = 2
        for _ in range(max_swipes):
            # Swipe left on the ScrollView
            scroll_view.swipe("up", duration=0.5)

    def click_Back_Icon_On_Address_Screen(self):
        sleep(3)
        Back_Icon = self.poco(self.Back_Icon_On_Address_Screen)
        Back_Icon.click()
        sleep(2)

    def Verify_Common_Design_Page_Is_Displaying(self):
        sleep(2)
        assert_exists(self.Common_Design_Page, "Common Design Page is displaying")

    def Verify_Copy_To_My_Design_Text_Is_Present(self):
        sleep(2)
        assert_exists(self.Copy_To_My_Design_Text, "Copy To My Design Text is displaying")

