from platform import platform

import pytest
from airtest.core.android import Android
from airtest.core.api import *
from airtest.core.cv import Template
from poco import poco
from ZSB_Mobile.Common_Method import Common_Method
from airtest.core.api import device as current_device
import os
from ZSB_Mobile.PageObject.Login_Screen import Login_Screen



def Basic_path(a):
    return os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates",a)
class Others:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.search_text = "https://zsbportal.zebra.com/"
        self.Google_Login = "Continue with Google"
        self.swdvt_test_account = "SWDVT IDC test account soho.swdvt.01@gmail.com"
        self.test_print = "Test Print"
        self.ZSB_DP12 = "ZSB-DP12\nTab 3 of 3"
        self.ZSB_DP12_1 = "ZSB-DP12 (1)\nTab 2 of 5"
        self.Printer_Settings_Btn = "Printer Settings"
        self.Label_alignment_demo = "Label Alignment Demo"
        self.android_widget_button = "android.widget.Button"
        # self.three_dots = Template(r"tpl1704949114184.png", record_pos=(0.398, -0.695), resolution=(1080, 2340))
        # self.three_dots = Template(r"C:\Users\tr5927\Desktop\ZSB_Automation\ZSB_Mobile\templates\tpl1704949114184.png", record_pos=(0.398, -0.695), resolution=(1080, 2340))
        self.three_dots = Template(os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates",
                                                "tpl1704949114184.png"), record_pos=(0.398, -0.695),
                                   resolution=(1080, 2340))
        self.delete_button = "Delete"
        self.delete_printer_text = "Delete Printer\nPlease acknowledge the following to continue:\nThis action cannot be undone. Deleting your printer will: \n•  Permanently remove it from your workspace\n•  Factory reset your printer\nAfter deleting your printer, proceed to the Bluetooth settings on your device to remove the existing Bluetooth bond."
        self.cancel_delete_printer_btn = "Cancel"
        self.click_Home_btn = "Home"
        self.Google_ZSB_DP12_1 = "zsbdp12"
        self.google_search_feild = "com.google.android.googlequicksearchbox:id/googleapp_hint_text"
        self.google_text_field = "com.google.android.googlequicksearchbox:id/googleapp_search_box"
        self.google_hamburger_menu = Template(Basic_path("tpl1704994282096.png"), record_pos=(-0.418, -0.921),
                                              resolution=(1080, 2340))
        self.notifications_button = "Notifications"
        self.seekbar_path = "android.widget.SeekBar"
        #self.down_arrow_button = Template(r"tpl1705053444096.png", record_pos=(0.407, -0.425), resolution=(1080, 2340))
        self.down_arrow_button = Template(os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates","tpl1705053444096.png"), record_pos=(0.407, -0.425), resolution=(1080, 2340))

        self.dismiss_button = "Dismiss"
        self.photo_upload = "Upload Photo"
        self.photo_gallery = "Photo Gallery"
        self.upload_via_gallery_dir = "com.google.android.documentsui:id/dir_list"
        self.remove_image_button = "Remove Image"
        #self.default_image_avtar = Template(r"tpl1705409483217.png", record_pos=(-0.358, -0.654),resolution=(1080, 2340))
        self.default_image_avtar = Template(os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile"
                                                                                  "\\templates",
                                                         "tpl1705409483217.png"), record_pos=(-0.358, -0.654),
                                            resolution = (1080, 2340))
        self.profile_edit = "android.widget.Button"
        self.camera_button = "Camera"
        self.check_permission_text_for_camera = "com.android.permissioncontroller:id/permission_message"
        self.click_allow_permission = "com.android.permissioncontroller:id/permission_allow_button"
        self.capture_image_button = "com.android.camera:id/shutter_button"
        self.retake_image_button = "com.android.camera:id/intent_done_retry"
        self.use_image_button = "com.android.camera:id/done_button"
        self.edit_printer_name_text = "android.widget.EditText"
        self.click_deny_permission = "com.android.permissioncontroller:id/permission_deny_button"
        self.log_out_button = "Log Out"
        self.Home_button = "Home"
        self.Print_button = "Print"
        self.wi_fi_button = "Wi-Fi\nTab 2 of 2"
        self.manage_network_button = "Manage Networks"
        self.continue_button = "Continue"
        self.add_network_button = "Add Network"
        self.common_designs_button = "Common Designs"
        self.my_designs_button = "My Designs"
        self.copy_to_my_designs = "Copy to My Designs"
        self.zsb_app_icon = Template(
            os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates",
                         "tpl1706000380672.png"), record_pos=(-0.36, -0.59), resolution=(720, 1280))
        self.my_data_button = "My Data"
    def start_google(self):
        start_app("com.google.android.googlequicksearchbox")

    def click_Printer_Settings(self):
        # self.poco("My Designs").scroll()

        printer_settings = self.poco(self.Printer_Settings_Btn)
        printer_settings.click()

    def click_Printer_Settings_in_google(self):
        left_scroll_position = self.poco("My Designs").get_position()

        # Define the target position on the left side where you want to scroll
        target_position = [left_scroll_position[0], left_scroll_position[1] - 0.2]  # Adjust the Y coordinate as needed

        # Perform the swipe or scroll action
        self.poco.swipe(left_scroll_position, target_position, duration=1)

        printer_settings = self.poco(self.Printer_Settings_Btn)
        printer_settings.click()

    def check_text_history(self):
        return self.poco(text="History").exists()


    def click_selected_printer(self):
        zsb_printer = self.poco(self.ZSB_DP12_1)
        zsb_printer.click()

    def click_home_button(self):
        home_btn = self.poco(self.click_Home_btn)
        home_btn.click()

    def swipe_left(self):
        disp = current_device().display_info
        if disp['orientation'] in (1, 3):
            w, h = [disp['height'], disp['width']]
        else:
            w, h = [disp['width'], disp['height']]
        v1, v2 = 0.9120370370370371, 0.13333333333333333
        v11, v22 = 0.22037037037037038, 0.13333333333333333

        w1, h1 = v1 * w, v2 * h
        w2, h2 = v11 * w, v22 * h
        print("---->")
        print([w1, h1])
        print([w2, h2])
        swipe([w1, h1], [w2, h2])

    def click_test_print(self):
        test_prin = self.poco(self.test_print)
        test_prin.click()

    def click_icon(self):
        icon = self.poco(self.android_widget_button)
        icon.click()

    def click_demo_video(self):
        alignment_demo = self.poco(self.Label_alignment_demo)
        alignment_demo.click()

    def close_demo_video(self):
        # close_video = self.poco(self.Close_demo_video)
        # close_video.click()
        keyevent("back")

    def click_three_dots(self):

        touch(self.three_dots)
        # click_three_dots_btn = self.poco(self.three_dots)
        # click_three_dots_btn.click()

    def click_delete_button(self):
        del_button = self.poco(self.delete_button)
        del_button.click()

    def click_cancel_delete_printer(self):
        cancel_btn = self.poco(self.cancel_delete_printer_btn)
        cancel_btn.click()

    def verify_delete_printer_text(self):
        res = assert_equal(self.delete_printer_text,
                           "Delete Printer\nPlease acknowledge the following to continue:\nThis action cannot be undone. Deleting your printer will: \n•  Permanently remove it from your workspace\n•  Factory reset your printer\nAfter deleting your printer, proceed to the Bluetooth settings on your device to remove the existing Bluetooth bond.",
                           "Matched")
        print(res)

    def check_cancel_and_delete_button(self):

        child_names = [child.get_name() for child in self.poco(
            "Delete Printer\nPlease acknowledge the following to continue:\nThis action cannot be undone. Deleting your printer will: \n•  Permanently remove it from your workspace\n•  Factory reset your printer\nAfter deleting your printer, proceed to the Bluetooth settings on your device to remove the existing Bluetooth bond.").children()]
        if "Cancel" in child_names and "Delete" in child_names:
            print("OK")
        else:
            print("Error")

    def get_no_of_left_cartridge(self):
        child_names = [child.get_name() for child in
                       self.poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child(
                           "android.view.View").child("android.view.View").child("android.view.View").offspring(
                           "android.widget.ScrollView").child("android.view.View")[0].child("android.view.View").child(
                           "android.view.View")[0].children()]

        modified_list = [item.split('\n') for item in child_names]
        modified_list = modified_list[0][4].split(" ")

        return int(modified_list[0])

    def check_auto_update_cartridge(self, previous, current, count):

        return 1 if previous - count == current else 0

    def click_google_search_bar(self):

        google_search_bar = self.poco(self.google_search_feild)
        google_search_bar.click()

    def enter_the_text_in_goole(self, String):

        self.poco(self.google_text_field).set_text(String)

    def click_enter(self):
        keyevent("enter")

    def select_photo_gallery(self):
        photo_gallery_btn = self.poco(self.photo_gallery)
        photo_gallery_btn.click()

    def click_upload_photo(self):
        upload_photo_btn = self.poco(self.photo_upload)
        upload_photo_btn.click()

    def click_hamburger_button_in_Google(self):
        # hamburger_icon = self.poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.FrameLayout").offspring("com.android.chrome:id/compositor_view_holder").offspring("root")[1].child("android.view.View")[0].child("android.view.View").click()
        # hamburger_icon.click()

        touch(self.google_hamburger_menu)

    def google_scroll_down(self):
        self.poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child(
            "android.widget.FrameLayout").scroll()

    def scroll_down_till_printer_test_label_in_google(self):
        count = 0
        while (not self.poco(name="android.widget.Button", text="Print Test Label").exists()) and count < 3:
            self.poco.scroll()
            count += 1

        self.poco.swipe([0.5, 0.9], [0.5, 0.7], duration=0.1)

    def click_google_print_test_button(self):

        self.poco(text="Print Test Label").click()

    def click_selected_printer_in_google(self):
        self.poco(text=self.Google_ZSB_DP12_1).click()

    def change_Darkness_level_in_google(self, new_value):
        seekbar = self.poco(self.seekbar_path)
        percentage = new_value / 100.0

        seekbar_size = seekbar.get_size()
        click_x = seekbar_size[0] * percentage

        seekbar.click([click_x, seekbar_size[1] / 2])

    def click_notifications_button_in_google(self):
        notification_btn = self.poco(self.notifications_button)
        notification_btn.click()

    def click_notifications_button(self):
        notification_btn = self.poco(self.notifications_button)
        notification_btn.click()

    def get_notification_text_in_google(self):
        temp = []

        elem_count = len(self.poco("android.widget.TextView"))

        for i in range(6,elem_count,2):
            store = self.poco("android.widget.TextView")[i]
            temp.append(store.get_text())

        return temp

    def scroll_up(self,count):
        start_point = [0.5, 0.2]
        end_point = [0.5, 0.8]

        # Perform the scroll-up action

        for i in range(count):
            self.poco.swipe(start_point, end_point, duration=0.1)

    def get_notification_text_in_Android(self):
        temp = []

        # t = len(self.poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child(
        #     "android.widget.FrameLayout").offspring("com.android.chrome:id/compositor_view_holder").offspring(
        #     "root").child("android.view.View")[1].children())
        # for i in range(t - 3):
        #     store = self.poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child(
        #         "android.widget.FrameLayout").offspring("com.android.chrome:id/compositor_view_holder").offspring(
        #         "root").child("android.view.View")[1].child("android.view.View")[i + 1].child(
        #         "android.view.View").child("android.widget.TextView")[0]
        #     temp.append(store.get_text())

        t = len(self.poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child(
            "android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child(
            "android.view.View")[1].offspring(
            "Below is the historical view of the notifications you have received.").child("android.view.View").child(
            "android.view.View").children())
        for i in range(t):
            store = [self.poco("Below is the historical view of the notifications you have received.").child(
                "android.view.View").child("android.view.View").child("android.view.View")[i].children().get_name()]
            store_1 = [item.split('\n') for item in store]
            temp.append(store_1[0][0])

        return temp

    """Function Should be updated again once the bug is resolved"""

    def verify_notifications(self, google, android):
        txt = "Print complete"
        a = google.count(txt)
        b = android.count(txt)

        if a == b:
            return True
        else:
            return False

    def click_down_arrow_button(self):
        touch(self.down_arrow_button)

    def click_dismiss_printer_notification(self):
        dismiss_btn = self.poco(self.dismiss_button)
        dismiss_btn.click()

    def add_id_to_child_elem(self, arr):
        for i in range(len(arr)):
            arr[i] = arr[i] + 'i'

        return arr

    def check_remove_image_button_exists(self):

        a = self.poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child(
            "android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child(
            "android.view.View")[1].offspring("Remove Image").exists()
        return a

    def select_first_image_from_gallery(self):

        click_first_img = self.poco(self.upload_via_gallery_dir).child()[0]
        click_first_img.click()

    def click_remove_image_button(self):
            click_remove_btn = self.poco(self.remove_image_button)
            click_remove_btn.click()


    def verify_default_image(self):
        #res = self.get_avatar_image()
        try:
            res = assert_exists(self.default_image_avtar, "existes")
            return res

        except:
            return 0

    def get_avatar_image(self):
        f_n = self.get_first_name()
        l_n = self.get_last_name()
        temp = f_n[0].upper()+l_n[0].upper()
        res = "Avatar"+temp
        return res


    def click_on_profile_edit(self):

        self.poco(self.profile_edit).click()

    def select_camera(self):
        click_camera = self.poco(self.camera_button)
        click_camera.click()

    def verify_text_camera_permission(self):
        try:
            temp = self.poco(self.check_permission_text_for_camera).get_text()
            a = assert_equal(temp, "ZSB Series Would like to Access the Camera", "equal")
            return a
        except:
            return False

    def click_allow(self):

        try:
            self.poco(self.click_allow_permission).click()
        except:
            self.poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()

    def capture_the_image_button(self):
        try:
            take_img_btn = self.poco(self.capture_image_button)
            take_img_btn.click()
        except:
            pass
        try:
            self.poco("org.codeaurora.snapcam:id/shutter_button").click()
        except:
            self.run_the_command("adb shell input keyevent KEYCODE_CAMERA")

    def retake_the_image_button(self):
        try:
            retake_btn = self.poco(self.retake_image_button)
            retake_btn.click()
        except:
            self.poco("org.codeaurora.snapcam:id/preview_btn_retake").click()

    def use_the_image_button(self):
        try:
            ok_image = self.poco(self.use_image_button)
            ok_image.click()
        except:
            self.poco("org.codeaurora.snapcam:id/done_button").click()


    def get_the_version_no(self):
        version_name = self.poco("android.view.View").child("android.view.View").child("android.view.View").child(
            "android.view.View").child("android.view.View").child().get_name()
        temp = version_name.split()
        return temp[1]

    def get_printer_names(self):
        child_names = [child.get_name() for child in self.poco("android.widget.HorizontalScrollView").children()]

        modified_list = [item.split('\n')[0] for item in child_names]
        return modified_list, child_names

    def rename_printer(self, printer1, printer2_name):
        printer1_rename = self.poco(self.edit_printer_name_text)
        printer1_rename.click()
        printer1_rename.set_text(printer2_name)

    def verify_text_update_printer_name(self):
        a = [self.poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child(
            "android.view.View").child("android.view.View").child("android.view.View").child(
            "android.view.View").offspring()[1].get_name()]
        a = a[0].split('\n')
        a = " ".join(a)
        try:
            res = assert_equal(a[0], "this name is duplicated with another printer, update fail", "Ok")
            return res
        except:
            return False

    def select_printer_1(self, printer1):
        res,printer = self.get_printer_names()
        self.poco(printer[0]).click()

    def go_back(self):
        keyevent("back")

    def click_deny(self):
        self.poco(self.click_deny_permission).click()

    def get_null_name_error_and_space_for_printer_name(self):

        a = self.poco("android.widget.EditText").child().get_name()

        try:
            res = assert_equal(a, "Name must be at least 1 character", "ok")
            return res
        except:
            return 0

    def click_edit_profile_in_google(self):

        self.poco("root").child("android.view.View")[2].child("android.view.View")[0].offspring(
            "android.widget.Image").click()

    def verify_default_image_in_google(self, param):
        res = self.poco(text=param).exists()
        return res

    def click_log_out_button(self):
        log_out_btn = self.poco(self.log_out_button)
        log_out_btn.click()

    def scroll_down(self):
        self.poco.scroll()

    def edit_first_name(self, new_name):
        first_name = self.poco("android.widget.EditText")[0]
        first_name.click()
        first_name.set_text(new_name)
        keyevent("enter")

    def edit_last_name(self, new_name):
        last_name = self.poco("android.widget.EditText")[1]
        last_name.click()
        last_name.set_text(new_name)
        keyevent("enter")

    def get_first_name(self):
        first_name = self.poco("android.widget.EditText")[0]
        return first_name.get_text()

    def get_last_name(self):
        last_name = self.poco("android.widget.EditText")[1]
        return last_name.get_text()

    def check_printer_online_status(self):
        child_names = [child.get_name() for child in
                       self.poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child(
                           "android.view.View").child("android.view.View").child("android.view.View").offspring(
                           "android.widget.ScrollView").child("android.view.View")[0].child("android.view.View").child(
                           "android.view.View")[0].children()]
        modified_list = [item.split('\n') for item in child_names]

        return modified_list[0][0]

    def get_printers(self):

        try:
            child_names = [child.get_name() for child in self.poco("android.widget.HorizontalScrollView").children()]

            modified_list = [item.split('\n')[0] for item in child_names]

            res = dict(zip(modified_list, child_names))
            return res

        except:
            child_names = [child.get_name() for child in
                 self.poco("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child(
                     "android.view.View").child("android.view.View").child("android.view.View")[1].children()]

            modified_list = [item.split('\n')[0] for item in child_names]

            res = dict(zip(modified_list, child_names))
            return res

    def click_printer(self, printer_name):
        selected = self.poco(printer_name)
        selected.click()

    def click_Home_button(self):
        home_btn = self.poco(self.Home_button)
        home_btn.click()

    def click_print_button(self):
        print_btn = self.poco(self.Print_button)
        print_btn.click()

    def check_error_print_preview(self):
        a = self.poco("Error\nCould not fetch the Print Preview")
        if a:
            self.poco("Cancel").click()
        else:
            pass

    def select_first_label_from_home(self):
        first_label = \
            self.poco("android.widget.ScrollView").child("android.view.View")[1].child("android.view.View").child()[0]
        first_label.click()

    def click_left_arrow(self):
        self.poco("android.widget.Button").click()

    def click_wifi_button(self):
        wifi_btn = self.poco(self.wi_fi_button)
        wifi_btn.click()

    def click_manage_network_button(self):
        m_n_btn = self.poco(self.manage_network_button)
        m_n_btn.click()

    def check_bluetooth_connection_required_diloge(self):
        print(self.poco("android.view.View").child("android.view.View").child("android.view.View").child(
            "android.view.View").child("android.view.View").child("android.view.View").get_text())
        a = self.poco("android.view.View").child("android.view.View").child("android.view.View").child(
            "android.view.View").child("android.view.View").child("android.view.View").get_text()
        return a

    def click_continue_in_bluetooth_connection_required(self):
        self.poco(self.continue_button).click()

    def click_add_network_button(self):
        add_network = self.poco(self.add_network_button)
        add_network.click()

    def click_on_sign_in_with_email(self):
        self.poco("android.widget.Button").click()

    def enter_user_name_in_sign_with_email(self, user_name):
        try:
            self.poco("myForm").child("android.view.View")[0].click()
            self.poco("username").set_text(user_name)
            keyevent("back")
        except:
            self.poco("android.widget.EditText")[0].set_text(user_name)

    def enter_password_in_sign_with_email(self, password):
        try:
            self.poco("myForm").child("android.view.View")[1].click()
            self.poco("password").set_text(password)
            keyevent("back")
        except:
            self.poco("android.widget.EditText")[1].set_text(password)

    def click_on_sign_in(self):
        try:
            self.poco("submit_id").click()
        except:
            self.poco("android.widget.Button")[1].click()

    def click_enter_network_manually(self):
        self.poco("Enter Network Manually...").click()

    def enter_network_name(self, network_name):
        self.poco("android.widget.EditText").click()
        self.poco("android.widget.EditText").set_text(network_name)
        keyevent("enter")

    def click_join_network(self):
        self.poco("Join").click()

    def get_network_names(self):
        a = len(self.poco("android.widget.ScrollView").child().child().child().child().child().child().child())
        temp = []
        original_names = []
        for i in range(a):
            name = self.poco("android.widget.ScrollView").child().child().child().child().child().child().child()[
                i].get_name()
            original_names.append(name)
            name = name.split(" ")[1]
            temp.append(name)

        res = dict(zip(temp, original_names))

        return res

    def swap_two_networks(self, nw_1, nw_2):

        temp2 = self.poco(nw_2)

        temp1 = self.poco(nw_1).focus('center')
        temp2.drag_to(temp1)

    def delete_one_network(self,network_name):

        #self.poco(nameMatches=".*"+network_name).focus([1, 0.5]).click()
        self.poco(network_name).focus([0.95, 0.4]).click()

    def check_apply_changes_button_clickable(self):
        a = self.poco("Apply Changes", enabled=True).exists()
        return a

    def click_apply_changes_button(self):
        self.poco("Apply Changes").click()

    def click_common_designs_button(self):
        self.poco(self.common_designs_button).click()

    def search_designs(self, str):
        design = self.poco("android.widget.EditText")
        design.click()
        design.set_text(str)
        keyevent("enter")

    def select_first_design(self):
        first_design = self.poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child(
            "android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child(
            "android.view.View")[1].child("android.view.View").child("android.view.View")[0]
        first_design.click()

    def click_on_copy_to_my_designs(self):
        self.poco(self.copy_to_my_designs).click()

    def click_on_my_designs(self):
        self.poco(self.my_designs_button).click()

    def click_enter_data_for_design(self):
        self.poco("android.widget.EditText")[0].click()

    def click_enter_text_for_design(self):
        self.poco("android.widget.EditText")[1].click()

    def check_the_swift_keyboard(self):
        a = self.poco("com.touchtype.swiftkey:id/keyboard_frame").exists()
        return a

    def enter_data_for_design(self, str):

        a = self.poco("android.widget.EditText")[0]
        a.set_text(str)

    def enter_text_for_design(self, str):
        a = self.poco("android.widget.EditText")[1]
        a.set_text(str)

    def install_zsb_series_on_google_play(self):
        start_app("com.android.vending")

        self.poco("Search Google Play").click()
        self.poco("android.widget.EditText").set_text("zsb series")
        keyevent("enter")
        self.poco("ZSB Series\nZebra Technologies\n").click()
        self.poco("Install").click()

    def uninstall_zsb_series_on_google_play(self):
        stop_app("com.android.vending")

        start_app("com.android.vending")

        self.poco("Search Google Play").click()
        self.poco("android.widget.EditText").set_text("zsb series")
        keyevent("enter")
        self.poco("ZSB Series\nInstalled\n").click()
        self.poco("Uninstall").click()
        self.poco("Uninstall").click()

    def uninstall_and_install_zsb_series_on_google_play(self):
        stop_app("com.android.vending")

        start_app("com.android.vending")

        self.poco("Search Google Play").click()
        self.poco("android.widget.EditText").set_text("zsb series")
        keyevent("enter")
        self.poco("ZSB Series\nInstalled\n").click()
        self.poco("Uninstall").click()
        self.poco("Uninstall").click()
        self.poco("Install").wait_for_appearance(timeout=10)
        self.poco("Install").click()

    def wait_for_element_appearance(self,element, time_out):
        self.poco(element).wait_for_appearance(timeout=time_out)

    def wait_for_element_appearance_text(self,element, time_out):
        self.poco(text=element).wait_for_appearance(timeout=time_out)



    def update_zsb_series_on_google_play(self):
        stop_app("com.android.vending")

        start_app("com.android.vending")

        self.poco("Search Google Play").click()
        self.poco("android.widget.EditText").set_text("zsb series")
        keyevent("enter")
        self.poco("ZSB Series\nInstalled\n").click()
        self.poco("Update").click()

    def click_zsb_app_icon(self):
        try:
            touch(self.zsb_app_icon)
        except:
            self.zsb_app_icon = Template(
                os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates",
                             "tpl1706012780496.png"), record_pos=(-0.36, -0.59), resolution=(720, 1280))
            touch(self.zsb_app_icon)

    def check_allow_permission_for_location(self):
        a = self.poco("com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        if a:
            a.click()
        else:
            pass

    def open_the_zsb_series_app_in_play_store(self):

        start_app("com.android.vending")
        self.poco("Open").click()

    def click_Open_in_playstore(self):
        self.poco("Open").click()


    def check_home_page(self):
        a = self.poco("Home").exists()
        return a

    def run_the_command(self, path):
        cmd = path

        # Using os.system() method
        a = os.system(cmd)
        return a

    def check_zsb_app_icon(self):
        try:
            try:
                assert_exists(self.zsb_app_icon)
                return 1
            except:
                self.zsb_app_icon = Template(
                    os.path.join(os.path.expanduser('~'), "Desktop\ZSB_Automation\ZSB_Mobile\\templates",
                                 "tpl1706012780496.png"), record_pos=(-0.36, -0.59), resolution=(720, 1280))
                assert_exists(self.zsb_app_icon)
                return 1

        except:
            return 0

    def install_the_zsb_apk_in_files_android_8(self):
        self.poco(text="ZsbMobile-stage 4619.apk").click()
        try:
            self.poco("android:id/button1").click()
        except:
            pass
        self.poco("com.android.packageinstaller:id/ok_button").click()
        sleep(5)

    def check_app_is_installed_on_android_8(self):
        a = self.poco(text="App installed.").exists()
        return a

    def open_wifi_settings_in_android(self):
        cmd = "adb shell am start -n com.android.settings/.wifi.WifiSettings"
        self.run_the_command(cmd)

    def turn_on_wifi(self):
        cmd = "adb shell svc wifi enable"
        self.run_the_command(cmd)

    def check_no_notifications(self):
        a = self.poco("Below is the historical view of the notifications you have received.\nNo notifications").exists()
        return a

    def change_password_for_user_account(self):
        try:
            self.poco("Change")[1].click()
        except:
            self.poco("Change").click()

    def enter_user_name_for_change_password(self,user_name):
        self.poco("android.widget.EditText").set_text(user_name)

    def click_on_submit(self):
        self.poco(text="SUBMIT").click()

    def change_old_password_to_new_password(self, old_password, new_password):

        self.poco("android.widget.EditText")[0].set_text(old_password)
        self.poco("android.widget.EditText")[1].set_text(new_password)
        self.poco("android.widget.EditText")[2].set_text(new_password)

    def check_password_changed_successfully(self):
        a = self.poco(text="Password changed successfully.").exists()
        return a

    def click_here_to_login_after_changing_password(self):
        self.poco("Click here ").click()

    def get_my_data_all(self):
        child_names = [child.get_name() for child in self.poco("android.widget.HorizontalScrollView").children()]
        return child_names

    def get_designs_visible_designs(self):

        child_names = [child.get_name() for child in
                       self.poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android"
                                                                                                             ".view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.view.View").child().children()]
        return child_names

    def select_wifi(self,ssid, password):

        #self.poco(text="Internet").click()
        self.run_the_command("adb shell svc wifi enable")
        self.poco(text=ssid).wait_for_appearance(timeout=20)

        self.poco(text=ssid).click()
        try:
            self.poco(type="android.widget.EditText").set_text(password)
            keyevent("enter")

        except:
            sleep(1)

    def open_wifi_settings(self):
        cmd = "adb shell am start -a android.settings.SETTINGS"
        self.run_the_command(cmd)
        try:
            self.poco(text="Search settings").click()
            text("wifi")
            keyevent("enter")
            sleep(1)
            self.poco(text="Wi-Fi").click()

        except:
            pass


    def get_recently_printed_labels(self):
        child_names = [child.get_name() for child in self.poco("android.widget.ScrollView").child("android.view.View")[1].child(
            "android.view.View").child().children()]

        return child_names

    def check_same_after_switching_network(self,arr1, arr2):
        for i in range(len(arr1)):
            if arr1[i]!=arr2[i]:
                return 0
        return 1

    def click_on_my_data(self):
        self.poco(self.my_data_button).click()

    def check_network_present(self, str1):
        #a = self.poco(nameMatches=".*"+str1).exists()
        a = self.poco(str1).exists()
        return a

    def check_two_arrays_same(self,arr1,arr2):
        if len(arr1)!=len(arr2):
            return 0
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return 0
        return 1

    def check_google_pop_up_for_printer_drivers(self):
        a=self.poco(text="Got It").exists()
        if a:
            self.poco(text="Got It").click()
        else:
            pass

    def check_google_pop_up_zsb_series_printer(self):
        try:
            self.poco("android.widget.Button").click()
        except:
            pass




















