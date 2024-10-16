# LoginFunction.py
from platform import platform

import pytest
from _pytest.outcomes import skip
from airtest.core.android import Android
from airtest.core.api import exists, sleep
from poco import poco
from ...Common_Method import Common_Method
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
        self.Enter_GoogleID_Field = "SohoApp Testing"
        self.Google_UserID = "android.widget.EditText"
        self.Google_Password = "android.widget.TextView"
        self.Next_LoginBtn = "Next"
        self.Google_MailID = "Use another account"
        self.Google_Email_ID = "android.widget.TextView"
        self.Password_Nextbtn = "passwordNext"
        self.Menu_Hamburger_Icn = "Open navigation menu"
        self.Login_With_Email = "android.widget.Button"
        self.Password_Field = "android.widget.EditText"
        self.Keyboard_back_Icon = "com.android.systemui:id/back"

    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def click_LoginAllow_Popup(self):
        sleep(1)
        loginallow = self.poco(self.LoginAllow_Popup)
        if loginallow.exists():
            loginallow.click()


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
        sleep(20)
        if self.poco(text="Continue with Google").exists():
            self.poco(text="Continue with Google").click()
            sleep(14)
        else:
            self.close_app_reopen_and_click_sign_in()
            self.poco(text="Continue with Google").click()
        print("Successfully clicked Sign In With Google")
        sleep(2)




    def Loginwith_Added_Email_Id(self):
        sleep(9)
        added_email = self.poco(text="SohoApp Testing")
        if added_email.exists():
            added_email.click()
            sleep(15)
        else:
            poco.scroll()
            added_email.click()
            sleep(15)

    def click_GoogleID_Field(self):
        sleep(3)
        enter_googleID_field = self.poco(self.Enter_GoogleID_Field)
        enter_googleID_field.click()

    def Enter_Google_UserID(self):
        sleep(3)
        enter_googleid = self.poco(self.Google_UserID)
        if enter_googleid.exists():
            enter_googleid.click()
            sleep(1)
            enter_googleid.set_text("zebra21.dvt@gmail.com")
            sleep(2)

    def Add_Account_To_Device(self):
        sleep(3)
        add_account_to_device = self.poco(text="Add account to device")
        add_account_to_device.click()

    def click_GooglemailId(self):
        sleep(4)
        poco.scroll()
        google_mailid = self.poco(self.Google_MailID)
        if google_mailid.exists():
            google_mailid.click()
            sleep(9)

    def Enter_Google_Password(self):
        enter_google_password = self.poco(self.Google_Password)
        sleep(2)
        enter_google_password.set_text("Swdvt@#123")

    def click_Next_LoginBtn(self):
        next_login_btn = self.poco(self.Next_LoginBtn)
        next_login_btn.click()

    def click_Emailid_Nextbtn(self):
        sleep(4)
        emailid_nextbtn = self.poco(text="Next")
        if emailid_nextbtn.exists():
            emailid_nextbtn.click()
            sleep(9)
            poco(text("Swdvt@#123"))
        else:
            print("Next button is not present, proceeding with the next part of the code.")

    def click_Password_Nextbtn(self):
        sleep(2)
        password_nextbtn = self.poco(self.Password_Nextbtn)
        if password_nextbtn.exists():
            password_nextbtn.click()
            sleep(8)
        else:
            print("Next button is not present, proceeding with the next part of the code.")

    def click_Menu_HamburgerICN(self):
        sleep(9)
        hamburgerIcn = self.poco(self.Menu_Hamburger_Icn)
        hamburgerIcn.click()

    def click_Allow_ZSB_Series_Popup(self):
        sleep(3)
        Allow_ZSB_Series_Popup = self.poco(self.Allow_ZSB_Series_Popup)
        if Allow_ZSB_Series_Popup.exists():
            Allow_ZSB_Series_Popup.click()


    # def Verify_LoginAllow_Popup_IS_Not_Displaying(self):
    #     if assert_not_exists(self.poco(self.LoginAllow_Popup), "Login Allow pop up is not there"):
    #         print("Pass")
    #     else:
    #         print("Fail")

    def Verify_LoginAllow_Popup_IS_Displaying(self):
        sleep(2)
        if self.poco(self.LoginAllow_Popup).exists():
            print("Pass")
        else:
            print("Login Allow Pop up is not displaying")

    def click_Login_With_Email_Tab(self):
        sleep(12)
        zebra_login = self.poco(name="username")
        if zebra_login.exists():
            zebra_login.click()
            sleep(2)
            poco(text(""))
            poco(text("Zebra01.swdvt@icloud.com"))
            sleep(1)
        else:
            sleep(3)
            self.close_app_reopen_and_click_sign_in()
            sleep(10)
            self.signInWithEmail()
            sleep(12)
            self.poco(name="username").click()
            sleep(2)
            poco(text(""))
            poco(text("Zebra01.swdvt@icloud.com"))
            sleep(1)



    def click_UserName_TextField(self):
        username = self.poco(text="Continue with Google")
        username.click()

    def click_Password_TextField(self):
        sleep(1)
        # poco.scroll()
        # sleep(1)
        self.poco(name="password").click()
        # password = self.poco(self.Password_Field)
        # password.click()

    def Enter_Password(self):
        password = self.poco(name="android.widget.EditText")[1]
        sleep(2)
        password.set_text("Testing@1234")

    def click_SignIn_Button(self):
        sleep(1)
        self.poco(name="submit_id").click()
        sleep(10)

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

    def Enter_Zebra_Password(self):
        password = self.poco(name="password")
        password.set_text("Testing@12345")

    def click_Continue_On_Facebbok_Login_Page(self):
        sleep(10)
        a = self.poco(textMatches="(?s).*Continue.*")
        if a.exists():
            a.click()
            print(a)
    def Verify_ALL_Allow_Popups(self):
        sleep(2)
        loginallow = self.poco(self.LoginAllow_Popup)
        if loginallow.exists():
            loginallow.click()
        sleep(3)
        Allow_ZSB_Series_Popup = self.poco(self.Allow_ZSB_Series_Popup)
        if Allow_ZSB_Series_Popup.exists():
            Allow_ZSB_Series_Popup.click()
            sleep(1)

    def Verify_Login_Option_Is_Present(self):
        sleep(10)
        if self.poco(text="Sign In With").exists():
            return True
        if self.poco(text="Continue with Google").exists():
            return True
        if self.poco(text="Sign In with your email").exists():
            return True

    def click_Cancel_Btn(self):
        sleep(4)
        self.poco(name="Cancel").click()
        sleep(2)

    def Refresh_The_Page(self):
        sleep(1)
        start_x, start_y = 540, 400
        end_x, end_y = 540, 1200
        swipe((start_x, start_y), (end_x, end_y), duration=0.5)
        poco.swipe((500, 200), (500, 1000))
        sleep(4)

    def click_LogIn_with_popup(self):
        sleep(2)
        signInBtn = self.poco("Sign In")
        signInBtn.click()
        if self.poco("Allow").exists():
            self.poco("Allow").click()
        elif self.poco(text="Allow").exists():
            self.poco(text="Allow").click()
        sleep(4)

    def Dismiss_Keyboard(self):
        sleep(1)
        if self.poco("com.android.chrome:id/coordinator").exists():
            self.poco("com.android.chrome:id/coordinator").click()
        keyevent("Enter")
        sleep(2)

    def Handle_Refresh_And_Login(self):
        sleep(3)
        stop_app("com.zebra.soho_app")
        sleep(3)
        start_app("com.zebra.soho_app")
        sleep(3)
        if self.poco(self.LoginAllow_Popup).exists():
            self.poco(self.LoginAllow_Popup).click()
        if self.poco(self.Allow_ZSB_Series_Popup).exists():
            self.poco(self.Allow_ZSB_Series_Popup).click()
            sleep(2)
        if self.poco(self.loginBtn).exists():
            self.poco(self.loginBtn).click()
            sleep(12)
        zebra_login = self.poco(text="Sign In with your email")
        if zebra_login.exists():
            zebra_login.click()
            sleep(2)
            poco(text(""))
            poco(text("Zebra01.swdvt@icloud.com"))
            sleep(1)

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
        self.Verify_ALL_Allow_Popups()
        self.clickSignIn()

    def signInWithEmail(self):
        sleep(10)
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



    def allowPermissions(self):
        try:
            self.poco(text="While using the app").wait_for_appearance(timeout=15)
            self.poco(text="While using the app").click()
        except:
            pass



    def BugFix_For_Google(self):
        sleep(10)
        login_btn = self.poco(self.loginBtn)
        if login_btn.exists():
            login_btn.click()
            sleep(1)
            self.Verify_ALL_Allow_Popups()
            sleep(20)
            self.click_Loginwith_Google()
            sleep(9)
            self.Loginwith_Added_Email_Id()
        else:
            pass

    def BugFix_For_ZebraEmail(self):
        sleep(10)
        login_btn = self.poco(self.loginBtn)
        if login_btn.exists():
            login_btn.click()
            sleep(1)
            self.Verify_ALL_Allow_Popups()
            sleep(20)
            self.signInWithEmail()
            sleep(10)
            self.click_Login_With_Email_Tab()
            self.click_Password_TextField()
            self.Enter_Zebra_Password()
            self.click_SignIn_Button()
            sleep(2)

        else:
              pass