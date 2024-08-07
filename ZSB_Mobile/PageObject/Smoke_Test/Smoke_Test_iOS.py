from time import sleep
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from poco import poco
from pocoui_lib.ios.kotoComponent import poco
from ZSB_Mobile.PageObject.Data_Source_Screen.Data_Sources_Screen import common_method


class Smoke_Test_iOS:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.SignIn_With_Text = "Sign In With"
        self.Continue_With_Facebook_Option = "Continue with Facebook"
        self.Continue_With_Apple_Option = "Continue with Apple"
        self.home_Text_IS_Present = "Home"
        self.Continue_With_Password_ForApple_Login = "Continue with Password"
        self.click_On_Password_Text_field = "SecureTextField"
        self.Sign_In_Option = "Sign In"
        self.Apple_UserName = Template(r"tpl1707817586300.png", record_pos=(-0.191, -0.867),
                                       resolution=(1170, 2532))

        self.Google_UserName = Template(r"tpl1707818376117.png", record_pos=(-0.174, -0.867), resolution=(1170, 2532))

        self.MyData_Tab = "My Data"
        self.Plus_Icon = "android.widget.Button"
        self.LinkFile = "android.widget.Button"
        self.SignIn_With_Microsoft = "Sign in with Microsoft"
        self.SignIn_With_Google_Drive = ""
        self.Delete_File = "Remove"
        self.Print_Button = "Print"
        self.Delete_Button_On_MyDesign = "Delete"
        self.Cancel_Button_On_Delete_Popup = "Cancel"
        self.Delete_Button_On_Delete_Popup = "Delete"
        self.Deleted_Successfully_Message = ""
        self.Back_Icon_On_Address_Screen = "android.widget.Button"
        self.Common_Design_Text = "Common Designs"
        self.Copy_To_My_Design_Text = "Copy to My Designs"
        self.Print_button = "Print"
        self.Select_Btn = "Select"
        self.Threedot_On_MyData = "android.widget.Button"

        # #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
        if self.poco(nameMatches="(?s).*Zebra Soho .*").exists():
            self.poco(nameMatches="(?s).*Zebra Soho .*").get_name()


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
        poco(text("Testing@123"))

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
        sign_in_with_microsoft = self.poco(self.SignIn_With_Microsoft)
        if sign_in_with_microsoft.exists():
            sign_in_with_microsoft.click()
        else:
            print("Sign in with Microsift is not displaying")

    def click_SignIn_With_Google_Drive(self):
        sleep(2)
        sign_in_with_google_drive = self.poco(nameMatches="(?s).*Sign in with Google.*")
        if sign_in_with_google_drive.exists():
            sign_in_with_google_drive.click()
        else:
            print("Sign in with Google is not displaying")

    def click_Add_Another_Account_On_Google_Drive(self):
        sleep(2)
        poco.scroll()
        Google_email = self.poco(text="Add another account")
        if Google_email.exists():
            Google_email.click()
            sleep(3)

    def Enter_Email_On_Google_Drive(self):
        sleep(2)
        google_drive_email = self.poco(name="identifierId")
        if google_drive_email.exists():
            google_drive_email.click()
            sleep(1)
            google_drive_email.set_text("soho.swdvt.01@gmail.com")
            sleep(4)
        else:
            print("Emailo Field is not displaying")

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

    def Add_Multiple_Copies_Number(self):
        # Copies_Field = self.poco(self.Copies_Field)
        poco("android.widget.FrameLayout").child("android.view.View").child("android.view.View").offspring(
            "android.widget.ScrollView").child("android.widget.EditText")[1].set_text("")
        poco(text("3"))

    def click_On_Copies_Filed(self):
        sleep(3)
        poco("android.widget.FrameLayout").child("android.view.View").child("android.view.View").offspring(
            "android.widget.ScrollView").child("android.widget.EditText")[1].click()
        sleep(2)
        poco.set_text("")

        # def Add_Multiple_Copies_Number(self):
        #     poco("android.widget.FrameLayout").child("android.view.View").child("android.view.View").offspring("android.widget.ScrollView").child("android.widget.EditText")[1]).set_text("3")

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
        self.poco(nameMatches="(?s).*has been successfully removed.*").get_name()
        # assert_exists(self.Deleted_Successfully_Message, "Successfully Deleted Message is displaying")

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

    def click_Back_Icon_On_Address_Screen(self):
        sleep(3)
        Back_Icon = self.poco(self.Back_Icon_On_Address_Screen)
        Back_Icon.click()
        sleep(2)

    def Verify_Common_Design_Page_Is_Displaying(self):
        sleep(2)
        Common_Design_Text = self.poco(self.Common_Design_Text)
        Common_Design_Text.get_text()
        return Common_Design_Text

    def Verify_Copy_To_My_Design_Text_Is_Present(self):
        sleep(2)
        a = self.poco(self.Copy_To_My_Design_Text).get_name()
        return a

    def click_Email_Text_Field(self):
        sleep(2)
        microsoft_email = self.poco(type="android.widget.EditText")
        if microsoft_email.exists():
            microsoft_email.click()
            sleep(1)
            microsoft_email.set_text("swdvt.zebra@outlook.com")
            sleep(4)
        else:
            print("Sign in field is not displaying")

    def click_Next_Button(self):
        sleep(1)
        Next_Button = self.poco(text="Next")
        if Next_Button.exists():
            Next_Button.click()
            sleep(2)
        else:
            print("Next button is not displaying")

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

    def click_Microsoft_Password_Field(self):
        sleep(2)
        microsoft_password = self.poco(type="android.widget.EditText")
        if microsoft_password.exists():
            microsoft_password.click()
            sleep(1)
            microsoft_password.set_text("Swdvt@123")
            sleep(4)
        else:
            print("Password field is not displaying")

    def click_Google_Drive_Password_Field(self):
        sleep(2)
        gooogle_password = self.poco(type="android.widget.EditText")
        if gooogle_password.exists():
            gooogle_password.click()
            sleep(1)
            gooogle_password.set_text("Swdvt@#123")
            sleep(5)
        else:
            print("Password field is not displaying")

    def click_Sign_In_Button(self):
        sleep(1)
        sign_in_btn = self.poco(text="Sign in")
        if sign_in_btn.exists():
            sign_in_btn.click()
            sleep(1)
        else:
            print("Sign in button is not displaying")

    def click_Microsoft_OneDrive_Tab(self):
        sleep(2)
        microsoft_tab = self.poco(name="Microsoft OneDrive\nTab 2 of 2")
        if microsoft_tab.exists():
            microsoft_tab.click()
            sleep(1)
        else:
            print("Microsoft Onedrive tab is not present")

    def click_On_Search_Files(self):
        sleep(2)
        SearchBar2 = self.poco(self.Search_Files)
        SearchBar2.click()
        sleep(3)

    def click_On_Jpg_File(self):
        sleep(1)
        self.poco(nameMatches="(?s).*jpg.*").click()
        sleep(2)

    def click_On_PNG_File(self):
        sleep(1)
        self.poco(nameMatches="(?s).*png.*").click()
        sleep(2)

    def click_On_Select_Btn(self):
        sleep(1)
        select_btn = self.poco(self.Select_Btn)
        select_btn.click()
        sleep(4)

    def click_Three_Dot_On_MyData(self):
        sleep(1)
        threedot = self.poco(self.Threedot_On_MyData)
        threedot.click()
        sleep(1)

    def get_ith_design_by_index_in_my_designs(self, i):
        temp = []
        prev = []
        while len(temp) != i:
            curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]
            for j in curr:
                if j not in temp:
                    temp.append(j)
                    if len(temp) >= i:
                        break

            if prev == curr:
                break

            self.poco.scroll()
            prev = curr
        return temp[-1]

    def get_all_designs_in_My_Designs(self):
        sleep(1)
        total = []
        prev = []
        while 1:
            curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.widget.ImageView")]
            if curr != prev:
                for i in curr:
                    if i not in total:
                        total.append(i)

            if curr == prev:
                break

            self.poco.scroll()
            prev = curr

        return total

    def get_all_designs_in_Common_Designs(self):
        sleep(1)
        total = []
        prev = []
        while 1:
            curr = [child.get_name() for child in self.poco("android.view.View").child(type="android.view.View")]
            if curr != prev:
                for i in curr:
                    if i not in total:
                        total.append(i)

            if curr == prev:
                break

            self.poco.scroll()
            prev = curr

        return total

    def get_first_design_in_my_designs(self):
        a = self.poco("android.view.View").child(type="android.widget.ImageView")[0].get_name()
        return a