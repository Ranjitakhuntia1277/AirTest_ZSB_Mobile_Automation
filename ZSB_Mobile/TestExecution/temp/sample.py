from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from ZSB_Mobile.PageObject.Login_Screen import Login_Screen
from ZSB_Mobile.PageObject.Others.Others import Others



poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


connect_device("Android:///")

a=len(poco("android.widget.HorizontalScrollView").children())

child_names = [child.get_name() for child in poco("android.widget.HorizontalScrollView").children()]
modified_list = [item.split('\n')[0] for item in child_names]

printer_name = 'ZSB-DP13'

test_printer = ''
for i in range(1,a):
    swipe([766, 241],[389, 258])
    if modified_list[i] == printer_name:
        test_printer = child_names[i]


print("before")
poco(test_printer).click()
print("after")





print(child_names)
