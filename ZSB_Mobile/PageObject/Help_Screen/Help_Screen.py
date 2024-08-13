# LoginFunction.py
from platform import platform

# import pytest
from airtest.core.android import Android
from airtest.core.api import exists, sleep
# from pipes import Template
from airtest.core.cv import Template
from poco import poco
from ...Common_Method import Common_Method
from airtest.core.assertions import assert_exists, assert_equal
from airtest.core.api import *
from ...PageObject.Login_Screen import Login_Screen
from airtest.core.api import device as current_device
from ...Common_Method import *
from datetime import datetime, time
import pytest
from poco.exceptions import PocoTargetTimeout
import platform

if platform.system() == "Windows":
    def Basic_path(a):
        return os.path.join("Documents\\New_ZSB_Automation\ZSB_Mobile\\templates", a)

else:
    def Basic_path(a):
        return os.path.join("/Users/symbol/PycharmProjects/AirTest_ZSB_Mobile_Automation/ZSB_Mobile/templates", a)
common_method = Common_Method(poco)


class Help_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Help_btn = "Help"
        self.Support_btn = "Support"
        self.Support_page_title = "Welcome to ZSB Series Support"
        self.Support_page_type = "android.widget.TextView"
        self.FAQs_btn = "FAQs"
        self.FAQ_page_title = "Frequently Asked Questions"
        self.Contact_Us_btn = "Contact Us"
        self.ContactUs_page_title = "Call Us"
        self.Chat_btn = "Live Chat"
        self.Chat_unavailable = "Chat currently unavailable"
        self.BeginChat_btn = "Begin chat"
        self.Chat_subject = "Workspace"
        self.Start_chat = "Start Chatting"
        self.Help_icon = Template(Basic_path("tpl1704698945082.png"), record_pos=(-0.385, 0.553), resolution=(1080, 2340))
        self.Help_text = Template(Basic_path("tpl1704699099813.png"), record_pos=(-0.267, 0.55), resolution=(1080, 2340))
        self.Dropdown_for_help = Template(Basic_path("tpl1704697680422.png"), record_pos=(0.205, 0.552), resolution=(1080, 2340))
        self.Dropdown_for_subject = "Select from dropdown"
        self.Dropdown_for_affected_printer = "Select from dropdown"
        self.browser = {"chrome": "android.chrome", "edge": "microsoft.emmx"}
        self.Desc = "android.widget.EditText"
        self.Account = "swdvt zsb zebra03.swdvt@gmail.com"
        self.Back_Arrow = "android.widget.Button"
        self.Go_To_Chat_Btn = "Go to chat"
        self.Chat_Hours = "Available 7am to 7pm ET"
        self.EnterGooglePassword = "android.widget.EditText"

    def checkIfOnValidChatTime(self):
        eastern_zone = pytz.timezone('US/Eastern')
        eastern_time_now = datetime.now(eastern_zone)
        available_time_interval_start = time(7, 0, 0)
        available_time_interval_end = time(19, 0, 0)
        valid_time_to_chat = available_time_interval_start <= eastern_time_now.time() <= available_time_interval_end
        return valid_time_to_chat

    def click_Help_dropdown_option(self):
        # help_dropdown_btn = self.poco(self.Dropdown_for_help)
        touch(self.Dropdown_for_help)

    def click_Support(self):
        support_btn = self.poco(self.Support_btn)
        support_btn.click()

    def click_FAQs(self):
        faqs_btn = self.poco(self.FAQs_btn)
        faqs_btn.click()

    def click_ContactUs(self):
        contact_us_btn = self.poco(self.Contact_Us_btn)
        contact_us_btn.click()

    def click_Chat(self):
        chat_btn = self.poco(self.Chat_btn)
        chat_btn.wait_for_appearance(timeout=10)
        chat_btn.click()

    def clickBeginChat(self):
        begin_chat = self.poco(self.BeginChat_btn)
        begin_chat.wait_for_appearance(timeout=10)
        begin_chat.click()

    def checkChatCurrentlyUnavailableMessagePresent(self):
        sleep(3)
        try:
            self.poco(self.Chat_unavailable).wait_for_appearance(timeout=15)
        except:
            raise Exception("\"Chat currently unavailable\" Message not present when out of official chat timeline.")

    def checkIfHelpIsPresent(self):
        assert_exists(self.Help_text, "Help option visible")

    def checkIfHelpIconIsPresent(self):
        return assert_exists(self.Help_icon, "Help option is represented by '?'.")

    def checkIfLandedOnSupportPage(self):
        try:
            self.poco(text="Welcome to ZSB Series Support").wait_for_appearance(timeout=20)
        except:
            raise Exception("\"Welcome to ZSB Series Support\" not found on support page.")

    def checkIfLandedOnFAQsPage(self):
        try:
            self.poco(text="Frequently Asked Questions").wait_for_appearance(timeout=20)
        except:
            raise Exception("\"Frequently Asked Questions\" not found on support page.")

    def checkIfLandedOnContactUsPage(self):
        try:
            self.poco(text="Call Us").wait_for_appearance(timeout=20)
        except:
            try:
                self.poco(text="Support Case Submission").wait_for_appearance(timeout=20)
            except:
                raise Exception("\"Call Us\" not found on support page.")

    "--------------------------------------------------------------------------------------------------"
    """ Step 8. Check the logo located on top left is a ZSB Series logo
            (Bug: SMBLDA - 199)."""

    def closeTab(self):
        self.poco(desc="Close tab").click()

    "---------------------------------------------------------------------------------------------------"

    def clickBackArrow(self):
        back_arrow = self.poco(self.Back_Arrow)
        back_arrow.wait_for_appearance(timeout=10)
        back_arrow.click()

    def selectDropDownForSubject(self):
        subject_dropdown_btn = self.poco(self.Dropdown_for_subject)[0]
        subject_dropdown_btn.click()

    def selectSubjectFromDropDown(self):
        subject = self.poco(self.Chat_subject)
        subject.click()

    def fillDescription(self):
        description = self.poco(self.Desc)
        description.click()
        sleep(2)
        description.set_text("Test ping")

    def selectDropDownForAffectedPrinter(self):
        affected_printer_dropdown_btn = self.poco(self.Dropdown_for_affected_printer)
        affected_printer_dropdown_btn.click()

    def selectAffectedPrinterFromDropDown(self):
        self.poco("android.view.View")[6].child()[0].click()

    def Test_Support_faq_Contactus__Livechat_is_present(self):
        support_btn = self.poco(self.Support_btn)
        faq_btn = self.poco(self.FAQs_btn)
        contact_us_btn = self.poco(self.Contact_Us_btn)
        if self.checkIfOnValidChatTime():
            live_chat_btn = self.poco(self.Chat_btn)
        else:
            live_chat_btn = self.poco(self.Chat_unavailable)
        options = [support_btn, faq_btn, contact_us_btn, live_chat_btn]
        for option in options:
            if option.exists():
                # print(f"{option} button is present.")
                assert True

            else:
                # print(f"{option} button is not present.")
                assert False

    def verify_url(self, expected_url):
        sleep(5)
        try:
            self.poco("com.android.chrome:id/security_button").click()
        except:
            self.poco("com.android.chrome:id/location_bar_status_icon").click()
        self.poco("com.android.chrome:id/page_info_truncated_url").click()
        url_on_screen = self.poco("com.android.chrome:id/page_info_url").get_text()
        if expected_url in url_on_screen:
            keyevent("back")
            return True
        else:
            raise Exception("URL not matching")

    def clickContinueWeb(self):
        self.poco(text="Continue").wait_for_appearance(timeout=10)
        self.poco(text="Continue").click()

    def chooseAcc(self, Acc_Name="zebra03.swdvt@gmail.com"):

        account = self.poco(text=Acc_Name)
        count = 0
        while not account.exists() and count <= 2:
            self.poco.scroll()
            count += 1
        account.click()
        sleep(4)
        if self.poco(textMatches=".*By continuing, Google will share your name, email address, language preference, and profile picture with ZSB Series. See ZSB Series’s.*").exists():
            self.clickContinueWeb()
        elif self.poco(text= "Sign in to ZSB Series").exists():
            self.clickContinueWeb()
        sleep(3)

    def swipeLeft(self):
        disp = current_device().display_info
        if disp['orientation'] in (1, 3):
            w, h = [disp['height'], disp['width']]
        else:
            w, h = [disp['width'], disp['height']]
        v1, v2 = 1, 0.1581196581196581
        v11, v22 = 0.22037037037037038, 0.1581196581196581
        w1, h1 = v1 * w, v2 * h
        w2, h2 = v11 * w, v22 * h
        swipe([w1, h1], [w2, h2])

    def startChat(self):
        self.poco(self.Start_chat).click()

    def verifyChatHours(self):
        chat_hours = self.poco("android.view.View")[4].child()[1].get_name()
        if chat_hours == "Available 7am to 7pm ET":
            return
        else:
            error = f"Displaying --{chat_hours} instead of Available 7am to 7pm ET "
            raise Exception(error)

    def goToChat(self):
        self.poco(self.Go_To_Chat_Btn).click()

    def verifyLiveChatWindowTitle(self):
        if self.poco("android.view.View")[4].child().child()[1].get_name() == "Help":
            return
        else:
            raise Exception("Chat window title is not Help")

    def verifyBeginChatBtn(self):
        if self.poco(self.BeginChat_btn).exists():
            return
        else:
            raise Exception("Begin Chat Button not available")

    def addAccountToDevice(self):
        if self.poco(text="Add account to device").exists():
            self.poco(text="Add account to device").click()
        else:
            pass

    def clickNext(self):
        self.poco(text="Next").click()

    def enter_Google_Password(self, password):
        self.poco(self.EnterGooglePassword).set_text(password)

    def Agreement_google_login(self):
        if self.poco(text="I agree").exists():
            self.poco(text="I agree").click()
        if self.poco(text="Accept").exists():
            self.poco(text="Accept").click()

    def checkIfOnSignInPage(self):
        try:
            self.poco("Sign In").wait_for_appearance(timeout=20)
        except:
            raise Exception("Did not reach \"Sign In\" page.")
