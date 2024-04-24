import pytest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

from ZSB_Mobile.PageObject.Login_Screen import *

from ZSB_Mobile.PageObject.Help_Screen.Help_Screen import Help_Screen
from ZSB_Mobile.Common_Method import Common_Method
from ZSB_Mobile.PageObject.Login_Screen.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Registration_Screen.Registration_Screen import Registration_Screen


class Android_App_Help:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
# start_app("com.zebra.soho_app")
sleep(2.0)
wake()
common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
registration_page = Registration_Screen(poco)
errors = []


def test_Help_TestcaseID_45789():
    """""""""test"""""


common_method.Start_The_App()
"""""""""click on the login button"""""""""""
# registration_page.clickSignIn()
# registration_page.click_Google_Icon()
# try:
#     registration_page.wait_for_element_appearance_text("Sign in with Google", 20)
# except:
#     raise Exception("Did not navigate to Sign In with google page")
# while not poco(text="Use another account").exists():
#     poco.scroll()
# login_page.click_GooglemailId()
# while not poco(text="Add account to device").exists():
#     poco.scroll()
# registration_page.addAccountToDevice()
# registration_page.sign_In_With_Google("wrongloginzsb@gmail.com", "wrongloginzsb@123", True)
# registration_page.sign_In_With_Google("wrongloginzsb@1234")
# try:
#     registration_page.wait_for_element_appearance("Home", 20)
# except:
#     common_method.wait_for_element_appearance("Home", 30)
"""Click hamburger icon to expand menu"""
login_page.click_Menu_HamburgerICN()
"""Swipe up"""
poco.scroll()
sleep(2)
"""Check Help icon with '?' is present"""
help_page.checkIfHelpIconIsPresent()
"""Click Help dropdown to expand Help options"""
help_page.click_Help_dropdown_option()
sleep(2)
"""Check Help has Support, FAQs, Contact Us and Live Chat Options"""
help_page.Test_Support_faq_Contactus__Livechat_is_present()
"""Click Support to open support page"""
help_page.click_Support()
"""Check if we are redirected to support page"""
help_page.checkIfLandedOnSupportPage()
sleep(5)
help_page.verify_url("https://zsbsupport.zebra.com/s/")
keyevent("back")
try:
    help_page.checkIfLandedOnSupportPage()
    keyevent("back")
except:
    pass
"""Click FAQs to see FAQ on the web"""
sleep(5)
help_page.click_FAQs()
"""Check if we are redirected to FAQs page"""
help_page.checkIfLandedOnFAQsPage()
sleep(5)
help_page.verify_url("https://zsbsupport.zebra.com/s/faqs")
keyevent("back")
try:
    help_page.checkIfLandedOnFAQsPage()
    keyevent("back")
except:
    pass
"""Click Contact US to view contact options"""
help_page.click_ContactUs()
"""Check if we are redirected to Contact Us page"""
help_page.checkIfLandedOnContactUsPage()
sleep(5)
help_page.verify_url("https://zsbsupport.zebra.com/s/contactsupport")
keyevent("back")
try:
    help_page.checkIfLandedOnContactUsPage()
    keyevent("back")
except:
    pass
"""Click chat to """
help_page.click_Chat()
sleep(5)
"""Verify Chat Page Title"""
help_page.verifyLiveChatWindowTitle()
sleep(2)
"""Verify if Begin Chat button is present"""
help_page.verifyBeginChatBtn()
sleep(2)
common_method.Stop_The_App()


def test_Help_TestcaseID_47788():
    """""""""test"""""


common_method.Start_The_App()
login_page.click_Menu_HamburgerICN()
"""Swipe up"""
poco.scroll()
sleep(2)
"""Click Help dropdown to expand Help options"""
help_page.click_Help_dropdown_option()
"""Click Live Chat"""
help_page.click_Chat()
sleep(2)
"""Check if it displays Available 7am to 7pm ET"""
try:
    help_page.verifyChatHours()
except:
    pass
"""Begin Chat"""
help_page.clickBeginChat()
"""Click Back Arrow"""
help_page.clickBackArrow()
sleep(2)
"""Check if it displays Available 7am to 7pm ET"""
"""Unable to verify due to BUG"""
help_page.verifyChatHours()
common_method.Stop_The_App()


def test_Help_TestcaseID_47919():
    """""""""test"""""


common_method.Start_The_App()
"""Click hamburger icon to expand menu"""
login_page.click_Menu_HamburgerICN()
"""Swipe up"""
poco.scroll()
sleep(2)
"""Check Help icon with '?' is present"""
help_page.checkIfHelpIconIsPresent()
"""Click Help dropdown to expand Help options"""
help_page.click_Help_dropdown_option()
sleep(2)
"""Click Live Chat"""
help_page.click_Chat()
"""Begin Chat"""
help_page.clickBeginChat()
sleep(2)
"""Select Subject from dropdown"""
help_page.selectDropDownForSubject()
sleep(2)
help_page.selectSubjectFromDropDown()
sleep(2)
"""Enter Problem Description"""
help_page.fillDescription()
sleep(2)
"""Select affected printer"""
help_page.selectDropDownForAffectedPrinter()
sleep(2)
help_page.selectAffectedPrinterFromDropDown()
sleep(2)
"""Start chat"""
help_page.startChat()
"""Click Go to chat"""
help_page.goToChat()
"""Check if chat bubble does not appear"""
"""Cannot check since chat bubble does not appear"""
common_method.Stop_The_App()

# common_method.printExceptionIfPresent(errors)
