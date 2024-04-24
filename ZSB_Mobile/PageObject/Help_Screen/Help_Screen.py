# LoginFunction.py
from platform import platform

# import pytest
from airtest.core.android import Android
from airtest.core.api import exists, sleep
# from pipes import Template
from airtest.core.cv import Template
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method
from airtest.core.assertions import assert_exists, assert_equal
from airtest.core.api import *
from ZSB_Mobile.PageObject.Login_Screen import Login_Screen
from airtest.core.api import device as current_device


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
        self.BeginChat_btn = "Begin chat"
        self.Chat_subject = "Workspace"
        self.Start_chat = "Start Chatting"
        self.Help_icon = Template(r"tpl1704698945082.png", record_pos=(-0.385, 0.553), resolution=(1080, 2340))
        self.Help_text = Template(r"tpl1704699099813.png", record_pos=(-0.267, 0.55), resolution=(1080, 2340))
        self.Dropdown_for_help = Template(r"tpl1704697680422.png", record_pos=(0.205, 0.552), resolution=(1080, 2340))
        self.Dropdown_for_subject = "Select from dropdown"
        self.Dropdown_for_affected_printer = "Select from dropdown"
        self.browser = {"chrome": "android.chrome", "edge": "microsoft.emmx"}
        self.Desc = "android.widget.EditText"
        self.Account = "swdvt zsb zsbswdvt@gmail.com"
        self.Back_Arrow = "android.widget.Button"
        self.Go_To_Chat_Btn = "Go to chat"
        self.Chat_Hours = "Available 7am to 7pm ET"
        self.EnterGooglePassword = "android.widget.EditText"

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

    def checkIfHelpIsPresent(self):
        assert_exists(self.Help_text, "Help option visible")

    def checkIfHelpIconIsPresent(self):
        return assert_exists(self.Help_icon, "Help option is represented by '?'.")

    def checkIfLandedOnSupportPage(self):
        support = self.poco(text="Welcome to ZSB Series Support")
        support_title = support.get_text()
        assert_equal(support_title, "Welcome to ZSB Series Support", "Title of the page is matching")

    def checkIfLandedOnFAQsPage(self):
        faq = self.poco(text="Frequently Asked Questions")
        faq_title = faq.get_text()
        assert_equal(faq_title, "Frequently Asked Questions", "Title of the page is matching")

    def checkIfLandedOnContactUsPage(self):
        contact_us = self.poco(text="Call Us")
        contact_us_title = contact_us.get_text()
        assert_equal(contact_us_title, "Call Us", "Title of the page is matching")

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
        live_chat_btn = self.poco(self.Chat_btn)
        options = [support_btn, faq_btn, contact_us_btn, live_chat_btn]
        for option in options:
            if option.exists():
                print(f"{option} button is present.")
                assert True

            else:
                print(f"{option} button is not present.")
                assert False

    def verify_url(self, expected_url):
        self.poco("com.android.chrome:id/security_button").click()
        self.poco("com.android.chrome:id/page_info_truncated_url").click()
        url_on_screen = self.poco("com.android.chrome:id/page_info_url").get_text()
        if url_on_screen == expected_url:
            return
        else:
            raise Exception("URL not matching")

    def chooseAcc(self):
        account = self.poco(self.Account)
        account.click()

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
            print("Chat window title is not Help")
            return 1 / 0

    def verifyBeginChatBtn(self):
        if self.poco(self.BeginChat_btn).exists():
            return
        else:
            print("Begin Chat Button not available")
            return 1 / 0

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