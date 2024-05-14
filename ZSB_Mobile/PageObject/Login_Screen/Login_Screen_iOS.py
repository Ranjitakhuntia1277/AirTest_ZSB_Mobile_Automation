from time import sleep
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from poco import poco
# from ZSB_Mobile.TestExecution.temp.sample import poco
from poco.drivers.ios import iosPoco
# from pocoui_lib.ios.kotoComponent import poco
class Login_Screen_iOS:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.loginBtn = "Sign In"
        self.Continue_popup_to_login = "Continue"
        self.Enter_GoogleID_Field = "SohoApp Testing"
        self.Google_Login = "Continue with Google"
        self.Bluetooth_Allow = "android:id/button1"
        self.Google_MailID = "Use another account"
        self.Password_Nextbtn = "Next "
        self.Menu_Hamburger_Icn = "Open navigation menu"
        self.Google_UserID = "identifierId"
        self.Emailid_Nextbtn = "identifierNext"
        self.Google_Password = "Enter your password"
        self.Next_LoginBtn = "Next"
        self.LoginAllow_Popup = "Continue"
        self.Allow_ZSB_Series_Popup = ""
        self.Use_Another_Account = "Use another account"
        self.Google_MailID = "Use another account"
        self.Password_Nextbtn = "passwordNext "
        self.UserName = "TextField"
        self.Password_Field = "SecureTextField"
        self.SignIn_Button = "Sign In"
        self.Login_With_ZebraEmail = "Sign In with your email"
        self.Keyboard_back_Icon=""



    def clcik_Login_Btn(self):
        login_btn = self.poco(self.loginBtn)
        login_btn.click()

    def click_Continue_Btn_To_Login(self):
        sleep(2)
        Continue_btn = self.poco(self.Continue_popup_to_login)
        Continue_btn.click()

    def click_loginBtn(self):
        sleep(3)
        login_btn = self.poco(self.loginBtn)
        login_btn.click()
        login_btn.click()


    def click_GoogleID_Field(self):
        enter_googleID_field = self.poco(self.Enter_GoogleID_Field)
        enter_googleID_field.click()

    def click_Loginwith_Google(self):
        google_login = self.poco(self.Google_Login)
        google_login.click()
        sleep(10)

    def click_Bluetooth_Allow(self):
        bluetooth_allow = self.poco(self.Bluetooth_Allow)
        bluetooth_allow.click()

    def click_Loginwith_Google(self):
        sleep(3)
        google_login = self.poco(self.Google_Login)
        if google_login.exists():
           google_login.click()
           sleep(15)
        else:
           print("Google login option is not present, , proceeding with the next part of the code.")

    def Loginwith_Added_Email_Id(self):
        sleep(4)
        poco.scroll()
        added_email= self.poco(text="SohoApp Testing")
        if added_email.exists():
            added_email.click()
            sleep(9)
        else:
            print("Added Email is not present")

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
        sleep(7)
        hamburgerIcn = self.poco(self.Menu_Hamburger_Icn)
        hamburgerIcn.click()

    def click_Allow_Login_Popup(self):
        sleep(3)
        Allow_ZSB_Series_Popup = self.poco(self.LoginAllow_Popup)
        if Allow_ZSB_Series_Popup.exists():
            Allow_ZSB_Series_Popup.click()
        else:
            # pytest.skip("Allow ZSB Series Popup does not exist, skipping test.")
            print("Element not found, proceeding with the next part of the code.")

    def Verify_LoginAllow_Popup_IS_Not_Displaying(self):
        if assert_not_exists(self.poco(self.LoginAllow_Popup), "Login Allow pop up is not there"):
            print("Pass")
        else:
            print("Fail")

    def Verify_LoginAllow_Popup_IS_Displaying(self):
        sleep(2)
        if self.poco(self.LoginAllow_Popup).exists():
            print("Pass")
        else:
            print("Login Allow Pop up is not displaying")

    def click_Login_With_Email_Tab(self):
        sleep(9)
        self.poco(name="Sign In with your email").click()
        sleep(4)
        self.poco(name="TextField").click()
        sleep(2)
        self.poco(text("Zebra01.swdvt@icloud.com"))
        sleep(1)



    def click_Password_TextField(self):
        sleep(2)
        sleep(2)
        start_point = (0.57, 0.47)  # Example coordinates (x, y)
        # Specify the vector for swiping up
        vector = (0.297, 0.211)  # Example vector (delta_x, delta_y)
        # Perform the swipe action
        swipe(start_point, vector)
        password = self.poco(self.Password_Field)
        password.click()

    def Enter_Password(self):
        password = self.poco(self.Password_Field)
        sleep(2)
        password.set_text("Testing@1234")

    def click_SignIn_Button(self):
        sleep(1)
        self.poco("Sign In").click()
        sleep(9)

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
        sleep(1)
        self.poco(text("Testing@12345"))
