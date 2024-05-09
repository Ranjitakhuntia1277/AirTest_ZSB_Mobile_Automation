from ZSB_Mobile.PageObject.SSO_Token_Renewal_Screen.SSO_Token_Renewal_Screen_Android import SSO_Token_Renewal_Screen
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
import pytest

class SSO_Token_Renewal:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")
wake()
sso_token_renewel_page = SSO_Token_Renewal_Screen(poco)


def test_get_tokens():
    pass
    lines_between_words = sso_token_renewel_page.fetch_lines_between_words()
    print("1", lines_between_words)  # Print the lines, removing leading/trailing whitespace

    # if sso_token_renewel_page.wildcard_search():
    #     print("Wildcard query found in the file")
    # else:
    #     print("Wildcard query not found in the file")
    sso_token_renewel_page.runBatchFileToFetchLogs()

    lines_between_words = sso_token_renewel_page.fetch_lines_between_words()
    print("2", lines_between_words)  # Print the lines, removing leading/trailing whitespace

