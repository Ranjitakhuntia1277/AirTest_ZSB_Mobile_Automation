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


class Login_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco

        self.LoginAllow_Popup = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
        self.Allow_ZSB_Series_Popup = "com.android.permissioncontroller:id/permission_allow_button"
        self.loginBtn = "Sign In"
        self.Use_Another_Account = "Use another account"
        self.Bluetooth_Allow = "android:id/button1"
        self.Google_Login = "Continue with Google"
        self.Enter_GoogleID_Field = "SWDVT IDC test account"
        self.Google_UserID = "identifierId"
        self.Emailid_Nextbtn = "identifierNext"
        self.Google_Password = "android.widget.TextView"
        self.Next_LoginBtn = "Next"
        self.Google_MailID = "Use another account"
        self.Google_Email_ID = "android.widget.TextView"
        self.Password_Nextbtn = "passwordNext "
        self.Menu_Hamburger_Icn = "Open navigation menu"
        self.Login_With_Email = "android.widget.Button"
        self.UserName = "username"
        self.Password_Field = "password"
        self.SignIn_Button = "submit_id"
        self.Login_With_ZebraEmail = Template(os.path.join(os.path.expanduser('~'),
                                                           "Pictures\Automation_Backup\ZSB_Automation\ZSB_Mobile\Images",
                                                           "tpl1707302769907.png"), record_pos=(-0.018, 0.215),
                                              resolution=(1080, 2400))

    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def click_LoginAllow_Popup(self):
        sleep(1)
        loginallow = self.poco(self.LoginAllow_Popup)
        if loginallow.exists():
            loginallow.click()
        else:
            # pytest.skip("Login allow popup does not exist, skipping test.")
            print("Element not found, proceeding with the next part of the code.")

    def click_Bluetooth_Allow(self):
        bluetooth_allow = self.poco(self.Bluetooth_Allow)
        bluetooth_allow.click()
        sleep(2)

    def click_loginBtn(self):
        sleep(3)
        login_btn = self.poco(self.loginBtn)
        if login_btn.exists():
          login_btn.click()
        else:
            print("Login button is not present, , proceeding with the next part of the code.")

    def click_Loginwith_Google(self):
        sleep(3)
        google_login = self.poco(self.Google_Login)
        if google_login.exists():
           google_login.click()
           sleep(15)
        else:
           print("Google login option is not present, , proceeding with the next part of the code.")



    def click_GoogleID_Field(self):
        sleep(3)
        enter_googleID_field = self.poco(self.Enter_GoogleID_Field)
        enter_googleID_field.click()

    def Enter_Google_UserID(self):
        sleep(3)

        enter_googleid = self.poco(self.Google_UserID)
        if enter_googleid.exists():
            enter_googleid.click()
            enter_googleid.set_text("soho.swdvt.01@gmail.com")
        else:
            print("field is not present to enter the email id, , proceeding with the next part of the code.")

    def click_GooglemailId(self):
        sleep(3)
        google_mailid = self.poco(self.Google_MailID)
        if google_mailid.exists():
            google_mailid.click()
        else:
            google_emailid = self.poco(self.Google_Email_ID)
            google_emailid.click()
            sleep(2)

    def Enter_Google_Password(self):
        enter_google_password = self.poco(self.Google_Password)
        sleep(2)
        enter_google_password.set_text("Swdvt@#123")

    def click_Next_LoginBtn(self):
        next_login_btn = self.poco(self.Next_LoginBtn)
        next_login_btn.click()

    def click_Emailid_Nextbtn(self):
        sleep(2)
        emailid_nextbtn = self.poco(self.Emailid_Nextbtn)
        if emailid_nextbtn.exists():
            emailid_nextbtn.click()
        else:
           print("Next button is not present, proceeding with the next part of the code.")

    def Enter_Password_To_Login(self):
         sleep(1)
         poco(text("Swdvt@#123"))

    def click_Password_Nextbtn(self):
        sleep(2)
        password_nextbtn = self.poco(self.Password_Nextbtn)
        if password_nextbtn.exists():
           password_nextbtn.click()
           sleep(8)
        else:
            print("Next button is not present, proceeding with the next part of the code.")

    def click_Menu_HamburgerICN(self):
        sleep(2)
        hamburgerIcn = self.poco(self.Menu_Hamburger_Icn)
        hamburgerIcn.click()

    def click_Allow_ZSB_Series_Popup(self):
        sleep(3)
        Allow_ZSB_Series_Popup = self.poco(self.Allow_ZSB_Series_Popup)
        if Allow_ZSB_Series_Popup.exists():
            Allow_ZSB_Series_Popup.click()
        else:
            # pytest.skip("Allow ZSB Series Popup does not exist, skipping test.")
            print("Element not found, proceeding with the next part of the code.")

    # def Verify_LoginAllow_Popup_IS_Not_Displaying(self):
    #     if assert_not_exists(self.poco(self.LoginAllow_Popup), "Login Allow pop up is not there"):
    #         print("Pass")
    #     else:
    #         print("Fail")

    def Verify_LoginAllow_Popup_IS_Not_Displaying(self):
        sleep(2)
        if self.poco(self.LoginAllow_Popup).exists():
            print("Fail")
        else:
            print("Pass")

    def click_Login_With_Email_Tab(self):
        sleep(7)
        touch(self.Login_With_ZebraEmail)
        # login_with_email = self.poco(self.Login_With_Email)
        # # login_with_email.click()
        # if login_with_email.exists():
        # login_with_email.click()
        # else:
        #     print("Login with email element not found.")

    def click_UserName_TextField(self):
        username = self.poco(self.UserName)
        username.click()

    def Enter_UserName(self):
        username = self.poco(self.UserName)
        username.set_text("soho.swdvt.01@gmail.com")

    def click_Password_TextField(self):
        password = self.poco(self.Password_Field)
        password.click()

    def Enter_Password(self):
        password = self.poco(self.Password_Field)
        sleep(2)
        password.set_text("Swdvt@#123")

    def click_SignIn_Button(self):
        signin = self.poco(self.SignIn_Button)
        signin.click()
        sleep(7)

    def Check_loginBtn_IS_Present(self):
        sleep(5)
        login_btn = self.poco(self.loginBtn)
        if login_btn.exists():
            # Click on the "OK" or "Allow" button
            login_btn.click()
            print("Login Button is enabled.")
            return True
        else:
            print("Login Button is not enabled.")
            return False

    def Enter_Zebra_UserName(self):
        sleep(2)
        username = self.poco(self.UserName)
        username.set_text("Zebra01.swdvt@icloud.com")

    def Enter_Zebra_Password(self):
        password = self.poco(self.Password_Field)
        password.set_text("Testing@1234")
