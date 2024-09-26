from airtest.core.api import *
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from ...PageObject.Data_Source_Screen.Data_Sources_Screen import Data_Sources_Screen
from ...PageObject.Help_Screen.Help_Screen import Help_Screen
from ...Common_Method import Common_Method
from ...PageObject.Login_Screen.Login_Screen_Android import Login_Screen
from ...PageObject.Others_Screen.Others_Screen import Others
from ...PageObject.Add_A_Printer_Screen.Add_A_Printer_Screen_Android import Add_A_Printer_Screen
from ...PageObject.Printer_Management_Screen.Printer_Management_Screen import Printer_Management_Screen
from ...PageObject.Registration_Screen.Registration_Screen import Registration_Screen
from ...PageObject.Template_Management_Screen_JK.Template_Management_Screen_JK import Template_Management_Screen
from ...PageObject.APP_Settings.APP_Settings_Screen_Android import App_Settings_Screen
import pytest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

# Connect to the device
connect_device("Android:///")


common_method = Common_Method(poco)
login_page = Login_Screen(poco)
help_page = Help_Screen(poco)
printer_management_page = Printer_Management_Screen(poco)
data_sources_page = Data_Sources_Screen(poco)
add_a_printer_page = Add_A_Printer_Screen(poco)
registration_page = Registration_Screen(poco)
others_page = Others(poco)
template_management_page = Template_Management_Screen(poco)
app_settings_page = App_Settings_Screen(poco)

def take_screenshot(step_name):
    """Helper function to take a screenshot with the step name and timestamp."""
    screenshot_name = f"{step_name}_{time.strftime('%Y%m%d_%H%M%S')}.png"
    snapshot(filename=screenshot_name)
    print(f"Screenshot saved: {screenshot_name}")


def testrun_test_case():
    try:
        # Step 1: Perform some action
        touch(Template(r"button1.png"))
        print("Step 1: Button clicked successfully.")

    except Exception as e:
        print(f"Step 1 failed: {e}")
        take_screenshot("step1_button_click")
        raise  # Re-raise the exception to stop further execution if needed

    try:
        # Step 2: Perform another action
        swipe(Template(r"screen.png"), vector=[0.1, -0.3])
        print("Step 2: Swipe action performed successfully.")

    except Exception as e:
        print(f"Step 2 failed: {e}")
        take_screenshot("step2_swipe_action")
        raise  # Re-raise the exception to stop further execution if needed

    try:
        # Step 3: Verify some condition
        assert exists(Template(r"success_image.png")), "Verification failed!"
        print("Step 3: Verification successful.")

    except Exception as e:
        print(f"Step 3 failed: {e}")
        take_screenshot("step3_verification")
        raise  # Re-raise the exception to stop further execution if needed


# if __name__ == "__main__":
#     run_test_case()


def test_Registration_TestcaseID_45859():
    pass
    common_method.tearDown()
    data_sources_page.allowPermissions()
    registration_page.clickSignIn()
    data_sources_page.signInWithEmail()
    registration_page.Enter_Wrong_UserName()
    registration_page.Enter_Wrong_Password()
    login_page.click_SignIn_Button()
    registration_page.Verify_We_Didnot_recognize_Please_Try_Again()
    registration_page.Verify_SignInwith_Page()
    common_method.Stop_The_App()
# except Exception as e:
#     screenshot_path = homepage.capture_screenshot(stepId, test_case_id)
#     insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#     insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#     insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#     upload_case_files(execID, os.path.dirname(screenshot_path))
#     upload_case_files(execID, ADB_LOG_FILE)
#     raise Exception(str(e))
# ------------------------------------------------------

