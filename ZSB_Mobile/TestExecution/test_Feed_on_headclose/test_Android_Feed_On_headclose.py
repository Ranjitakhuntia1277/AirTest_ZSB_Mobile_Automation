from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ...PageObject.Feed_on_Head_Close.Feed_on_HeadClose import Feed_on_HeadClose
from ...PageObject.Smoke_Test.Smoke_Test_Android import Smoke_Test_Android
from ...Common_Method import Common_Method
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
from ...PageObject.APS_Testcases.APS_Notification_Android import APS_Notification
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen


class test_Feed_On_HeadClose():
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
start_app("com.zebra.soho_app")
sleep(3.0)

login_page = Login_Screen(poco)
app_settings_page = App_Settings_Screen(poco)
add_a_printer_screen = Add_A_Printer_Screen(poco)
common_method = Common_Method(poco)
smoke_test_android = Smoke_Test_Android(poco)
registration_page = Registration_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
aps_notification = APS_Notification(poco)


def test_Feed_on_HeadClose_TestcaseID_45790():
    """"Create the object for Login page & Common_Method page to reuse the methods"""""



feed_on_close = Feed_on_HeadClose(poco)

#login_page.click_LoginAllow_Popup()
login_page.click_loginBtn()
sleep(2)
"""""""select the login with google option"""""""""
login_page.click_Loginwith_Google()
sleep(2)

""" Select the existing Google Test Account """
login_page.click_swdvt_account()
time.sleep(10)

""" Click on the Navigation Menu """

login_page.click_Menu_HamburgerICN()
sleep(1)

""" Select the Printer Settings """
feed_on_close.click_Printer_Settings()

""" Select a printer """
feed_on_close.click_selected_printer()
sleep(2)


""" FURTHER CANNOT BE AUTOMATED DUE TO THE BUG ID: SMBM-1684, SMBM-1236"""

""" Click on the icon """

"""Similar methods used"""

feed_on_close.click_icon()
sleep(1)
res = feed_on_close.verify_text()
print(res)

feed_on_close.click_demo_video()
sleep(5)

res = feed_on_close.verify_demo_video()
print(res)


feed_on_close.click_to_exit_demo_video()



# def test_Feed_on_HeadClose_TestcaseID_45791():
#     pass
#
# login_page = Login_Screen(poco)
# feed_on_close = Feed_on_HeadClose(poco)
#
# # login_page.click_LoginAllow_Popup()
# # login_page.click_loginBtn()
# # sleep(2)
# # """""""select the login with google option"""""""""
# # login_page.click_Loginwith_Google()
# # sleep(2)
# #
# # """ Select the existing Google Test Account """
# # login_page.click_swdvt_account()
# # sleep(2)
#
# """ Click on the Navigation Menu """
#
# login_page.click_Menu_HamburgerICN()
# sleep(1)
#
# """ Select the Printer Settings """
# feed_on_close.click_Printer_Settings()
#
# """ Select a printer """
# feed_on_close.click_selected_printer()
# sleep(2)

""" FURTHER CANNOT BE AUTOMATED DUE TO THE BUG ID: SMBM-1684, SMBM-1236"""





# """ check update printer "Feed on Cover Close" value, delete printer but not decomission, restart printer , setting will not set to default"""
#
# def test_Feed_on_HeadClose_TestcaseID_45792():
#     pass


# login_page = Login_Screen(poco)
# feed_on_close = Feed_on_HeadClose(poco)
#
# # login_page.click_LoginAllow_Popup()
# # login_page.click_loginBtn()
# # sleep(2)
# # """""""select the login with google option"""""""""
# # login_page.click_Loginwith_Google()
# # sleep(2)
# #
# # """ Select the existing Google Test Account """
# # login_page.click_swdvt_account()
# # sleep(2)
#
# """ Click on the Navigation Menu """
#
# login_page.click_Menu_HamburgerICN()
# sleep(1)
#
# """ Select the Printer Settings """
# feed_on_close.click_Printer_Settings()
#
# """ Select a printer """
# feed_on_close.click_selected_printer()
# sleep(2)
""" FURTHER CANNOT BE AUTOMATED DUE TO THE BUG ID: SMBM-1684, SMBM-1236"""

# ###""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


