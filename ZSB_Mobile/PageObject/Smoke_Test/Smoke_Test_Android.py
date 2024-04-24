# LoginFunction.py
from platform import platform

import pytest
from _pytest.outcomes import skip
from airtest.core.android import Android
from airtest.core.api import exists, sleep
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from pocoui_lib.android.kotoComponent import poco


class Smoke_Test_Android:
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

        self.MyData_Tab = "My Data"
        self.Plus_Icon = "android.widget.Button"
        self.LinkFile = "android.widget.Button"
        self.SignIn_With_Microsoft = "Sign in with Microsoft"
        self.Select_Upload_Files = ""
        self.Uploaded_Files = ""
        self.Delete_File = ""
        self.Print_Button = "Print"
        # self.Copies_Field = ""
        self.Delete_Button_On_MyDesign = "Delete"
        self.Cancel_Button_On_Delete_Popup = "Cancel"
        self.Delete_Button_On_Delete_Popup = "Delete"
        self.Deleted_Successfully_Message = ""
        self.Address_Header_And_Description = (Template(r"tpl1709807557560.png", record_pos=(-0.01, -0.298), resolution=(1080, 2400)))
        self.Barcodes_Header_And_Description = (Template(r"tpl1709807592583.png", record_pos=(0.0, 0.382), resolution=(1080, 2400)))
        self.Jewelry_Header_And_Description = (Template(r"tpl1709807638763.png", record_pos=(-0.004, 0.078), resolution=(1080, 2400)))
        self.Multipurpose_Header_And_Description = (Template(r"tpl1709807672502.png", record_pos=(-0.016, 0.708), resolution=(1080, 2400)))
        self.Postage_Header_And_Description = (Template(r"tpl1709807695114.png", record_pos=(-0.015, 0.524), resolution=(1080, 2400)))
        self.ReturnAddress_Header_And_Description = (Template(r"tpl1709807740614.png", record_pos=(0.005, 0.147), resolution=(1080, 2400)))
        self.Round_Header_And_Description = Template(r"tpl1709807914172.png", record_pos=(-0.006, 0.411), resolution=(1080, 2400))
        self.Shipping_Header_And_Description = Template(r"tpl1709807943476.png", record_pos=(-0.006, -0.21), resolution=(1080, 2400))
        self.SmallMultipurpose_Header_And_Description = (Template(r"tpl1709807971879.png", record_pos=(-0.001, -0.146), resolution=(1080, 2400)))
        self.XLShipping_Header_And_Description = (Template(r"tpl1709807994118.png", record_pos=(0.002, 0.518), resolution=(1080, 2400)))
        self.Back_Icon_On_Address_Screen = "android.widget.Button"
        self.Common_Design_Text = "Common Designs"
        self.Copy_To_My_Design_Text = "Copy to My Designs"
        self.Email_Text_Field = "i0116"
        self.Next_Button = "Next"

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
        poco.scroll()

    def Verify_Barcodes_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Barcodes_Header_And_Description, "Barcodes Header And Description is displaying")
        poco.scroll()

    def Verify_Jewelry_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Jewelry_Header_And_Description, "Jewelry Header And Description is displaying")
        poco.scroll()

    def Verify_Multipurpose_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Multipurpose_Header_And_Description, "Multipurpose Header And Description is displaying")
        poco.scroll()

    def Verify_Shipping_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Shipping_Header_And_Description, "Shipping Header And Description is displaying")
        poco.scroll()

    def Verify_ReturnAddress_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.ReturnAddress_Header_And_Description, "ReturnAddress Header And Description is displaying")
        poco.scroll()

    def Verify_Postage_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Postage_Header_And_Description, "Postage Header And Description is displaying")
        poco.scroll()

    def Verify_Round_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.Round_Header_And_Description, "Round Header And Description is displaying")
        poco.scroll()

    def Verify_SmallMultipurpose_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.SmallMultipurpose_Header_And_Description,
                      "SmallMultipurpose Header And Description is displaying")
        poco.scroll()

    def Verify_XLShipping_Header_And_Description_IS_Present(self):
        sleep(2)
        assert_exists(self.XLShipping_Header_And_Description, "XLShipping Header And Description is displaying")
        poco.scroll()

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
        assert_exists(self.Copy_To_My_Design_Text, "Copy To My Design Text is displaying")

    def click_Email_Text_Field(self):

        sleep(3)
        Email_Text_Field = self.poco(self.Email_Text_Field)
        Email_Text_Field.click()
        sleep(2)
        Email_Text_Field.set_text("soho.swdvt.01@gmail.com")

    def click_Next_Button(self):
        sleep(1)
        Next_Button = self.poco(self.Next_Button)
        Next_Button.click()
        sleep(2)
