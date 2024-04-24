import datetime
import logging
import os
import re
import shutil
import subprocess
import ipaddress
import random
import time
from pipes import Template
from platform import platform
from time import sleep

import package_name
from airtest.core.api import swipe, exists, touch, keyevent, shell, start_app, stop_app, uninstall, install
from airtest.core.assertions import assert_true
from airtest.report.report import LogToHtml
from poco.exceptions import PocoNoSuchNodeException
# from pocoui_lib.android.kotoComponent import poco
# from shell import Shell
from smb.SMBConnection import SMBConnection
# from airtest.report.report import LogToHtml
# from common.baseValue import *
# from common.filepath import *

from airtest.core.android.android import ADB
import tidevice
from airtest.core.api import *
from airtest.core.api import device as current_device
from poco import poco

# from test.body import poco


class Common_Method():
    pass

    def __init__(self, poco):
        self.poco = poco

        # longSleep = 60

    shortSleep = 15

    def getElementNum(self, pocoElemnt):
        e = 0
        for i in pocoElemnt:
            e = e + 1
        return e

    def run_the_command(self, command):
        cmd = command

        os.system(cmd)

    def getAttr(self, pocoElemnt, attr, shortSleep=shortSleep):
        """_summary_
        Args:
            pocoElemnt (_type_): _description_
            attr (_type_):
            For Android:
            	type
	            name
	            desc
	            enabled
	            visible
	            resourceId
	            zOrders
	            package
	            anchorPoint
	            dismissable
	            checkable
	            scale
	            boundsInParent
	            focusable
	            touchable
	            longClickable
	            size
	            pos
	            focused
	            checked
	            editalbe
	            selected
	            scrollable

            For iOS:
            	type
	            name
	            visible
	            label
	            rawIdentifier
	            value
	            isEnabled
	            isVisible
	            isAccessible
	            rect
	            pos
	            size
	            zOrders
	            anchorPoint

        Returns:
            _type_: _description_
        """
        pocoElemnt.refresh()
        self.waitElementShortTime(pocoElemnt, timeSleep=shortSleep)
        return pocoElemnt.attr(attr)

    def identify_poco_nametext_exist(self, pocoElemnt, type, keyword, timeSleep=shortSleep):
        # global text
        global text
        self.waitElementShortTime(pocoElemnt, timeSleep)
        if type == 'text':
            text = pocoElemnt.attr('text')
        elif type == 'name':
            text = pocoElemnt.attr('name')
        pattern = re.escape(keyword)
        match = re.search(pattern, text)
        return match

    def wait_for_element_appearance(self,element, time_out=10):
        self.poco(element).wait_for_appearance(timeout=time_out)

    def wait_for_element_disappearance(self,element, time_out=20):
        self.poco(element).wait_for_disappearance(timeout=time_out)

    def wait_for_element_appearance_enabled(self,element, time_out=10):
        self.poco(element,enabled=True).wait_for_appearance(timeout=time_out)

    def wait_for_element_appearance_namematches(self,element, time_out=15):
        self.poco(nameMatches=".*"+element+".*").wait_for_appearance(timeout=time_out)


    def wait_for_element_appearance_textmatches(self,element, time_out=10):
        self.poco(textMatches=".*"+element+".*").wait_for_appearance(timeout=time_out)

    def swipe_by_positions(self,start_point,end_point):
        self.poco.swipe(start_point, end_point, duration=0.5)

    def swipe_screen(self, point1, point2, number_of_swipes):
        disp = current_device().display_info
        w, h = [disp['width'], disp['height']]
        x1, y1 = point1
        x2, y2 = point2
        w1, h1 = x1 * w, y1 * h
        w2, h2 = x2 * w, y2 * h
        for i in range(number_of_swipes):
            swipe([w1, h1], [w2, h2])

    def wait_for_element_appearance_text(self,element, time_out=15):
        self.poco(text=element).wait_for_appearance(timeout=time_out)

    def Click(self, pocoElemnt, timeSleep=shortSleep, pos=[0.5, 0.5], needfresh=True):
        try:
            if needfresh:
                pocoElemnt.refresh()
            pocoElemnt.wait_for_appearance(timeSleep)
            pocoElemnt.click(pos)
        except Exception as e:
            self.triggerError("click action failure", str(e))
            # snapshot(msg="click action failure \n"+str(e))
            # log(Exception("click action failure \n"+str(e)))
            # raise Exception("click action failure")

    def click(self):
        pocoElemnt = self.poco(self.pocoElemnt)
        pocoElemnt.click()

    def longClick(self, pocoElemnt, timeSleep=3, pos=[0.5, 0.5]):
        try:
            pocoElemnt.refresh()
            pocoElemnt.wait_for_appearance(timeSleep)
            pocoElemnt.focus(pos).long_click(timeSleep)
        except Exception as e:
            self.triggerError("long click action failure", str(e))
            # snapshot(msg="long click action failure \n"+str(e))
            # log(Exception("long click action failure \n"+str(e)))
            # raise Exception("long click action failure")

    def identifyPocoExist(self, pocoElement, timeSleep=3):
        try:
            pocoElement.refresh()
        except:
            return False

        if pocoElement.wait(timeSleep).exists():
            x, y = pocoElement.get_position()
            return y > 0
        else:
            return False

    def input(self, pocoElemnt, value, enter=False, timeSleep=60, pos=[0.5, 0.5], settext=True):
        # longSleep
        try:
            pocoElemnt.refresh()
            pocoElemnt.wait_for_appearance(timeSleep)
            if platform == "Android":
                pocoElemnt.click(pos)
                if settext:
                    pocoElemnt.refresh()
                    pocoElemnt.set_text(value)
                    if enter == False:
                        print('do not hit enter key')
                    else:
                        keyevent("ENTER")
                else:
                    text(value)
                    if enter == False:
                        print('do not hit enter key')
                    else:
                        keyevent("ENTER")
            else:
                pocoElemnt.click(pos)
                text(value, enter=enter)
        except Exception as e:
            self.triggerError("input action failure", str(e))
            # snapshot(msg="input action failure \n"+str(e))
            # log(Exception("input action failure \n"+str(e)))
            # raise Exception("input action failure")

    def swipe_down(self, width, height, proportion=0.4, height_proportion=0.5, duration=1, width_proportion=0.5):
        start_pt = (width * width_proportion, height * height_proportion)
        end_pt = (width * width_proportion, height * proportion)
        swipe(end_pt, start_pt, duration=duration)

    def swipe_up(self, width, height, proportion=0.4, height_proportion=0.5, width_proportion=0.5):
        start_pt = (width * width_proportion, height * height_proportion)
        end_pt = (width * width_proportion, height * proportion)
        swipe(start_pt, end_pt)

    def swipeUpDown(self, width, height, height_proportion1=0.4, height_proportion0=0.5, duration=None,
                    width_proportion=0.5, type="up"):
        start_pt = (width * width_proportion, height * height_proportion0)
        end_pt = (width * width_proportion, height * height_proportion1)
        if type == "up":
            if duration:
                swipe(start_pt, end_pt, duration=duration)
            else:
                swipe(start_pt, end_pt)
        else:
            if duration:
                swipe(end_pt, start_pt, duration=duration)
            else:
                swipe(end_pt, start_pt)

    def swipe_Transverse(self, width, height, proportion_left=0.5, proportion_right=0.4, duration=2):
        left_pt = (width * proportion_left, height * 0.5)
        right_pt = (width * proportion_right, height * 0.5)
        swipe(left_pt, right_pt, duration=duration)

    def swipeUpByUseElement(self, pocoElemnt):
        try:
            pocoElemnt.refresh()
            pocoElemnt.swipe('up')
        except Exception as e:
            self.triggerError(str(e))

    def swipeDownByUseElement(self, pocoElemnt):
        try:
            pocoElemnt.refresh()
            pocoElemnt.swipe('down')
        except Exception as e:
            self.triggerError(str(e))

    def get_current_test(self):
        full_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
        test_file = full_name.split("::")[0].split('/')[-1].split('.py')[0]
        test_class = full_name.split("::")[-2]
        test_name = full_name.split("::")[-1]
        return full_name, test_file, test_class, test_name

    def waitElementLongTime(self, pocoElemnt, timeSleep=60):
        try:
            pocoElemnt.refresh()
            pocoElemnt.wait_for_appearance(timeSleep)
        except Exception as e:
            self.triggerError("wait element appears for " + str(timeSleep) + " failure", str(e))
            # snapshot(msg="wait element appears for "+str(timeSleep)+" failure \n" +str(e))
            # log(Exception("wait element appears for "+str(timeSleep)+" failure \n" +str(e)))
            # raise Exception("wait element appears for "+str(timeSleep)+" failure")

    def waitElementShortTime(self, pocoElemnt, timeSleep=shortSleep, is_error=True):
        try:
            pocoElemnt.refresh()
            pocoElemnt.wait_for_appearance(timeSleep)
        except Exception as e:
            if is_error:
                self.triggerError("wait element appears for " + str(timeSleep) + " failure", str(e))
            # snapshot(msg="wait element appears for "+str(timeSleep)+" failure \n"+str(e))
            # log(Exception("wait element appears for "+str(timeSleep)+" failure \n"+str(e)))
            # raise Exception("wait element appears for "+str(timeSleep)+" failure")

    def waitElementDismiss(self, pocoElemnt, timeSleep=shortSleep):
        try:
            pocoElemnt.refresh()
            pocoElemnt.wait_for_disappearance(timeSleep)
        except Exception as e:
            self.triggerError("wait element disappears for " + str(timeSleep) + " failure", str(e))
            # snapshot(msg="wait element disappears for "+str(timeSleep)+" failure \n"+str(e))
            # log(Exception("wait element disappears for "+str(timeSleep)+" failure \n"+str(e)))
            # raise Exception("wait element disappears for "+str(timeSleep)+" failure")

    def checkUiElementExistBySwipe(self, pocoElement, width, height, Maxcount=5, height_proportion1=0.4,
                                   timeSleep=shortSleep, is_error=True, width_proportion=0.5):
        try:
            count = 0
            while (count < Maxcount) and not self.identifyPocoExist(pocoElement):
                count = count + 1
                self.swipeUpDown(width, height, height_proportion1=height_proportion1,
                                 width_proportion=width_proportion)
            self.waitElementShortTime(pocoElement, timeSleep, is_error=is_error)
            self.displayTheShadedElement(pocoElement, width, height)
            # There might be fast scrolling, subsequent operational errors, waiting for 1 second
            sleep(1)
        except Exception as e:
            if is_error:
                self.triggerError("swipe and wait for the element appears failure: " + str(e))

    def checkUiElementExistBySwipeDown(self, pocoElement, width, height, Maxcount=5, height_proportion1=0.5,
                                       timeSleep=shortSleep, is_error=True, height_proportion0=0.9,
                                       width_proportion=0.1):
        try:
            count = 0
            while (count < Maxcount) and not self.identifyPocoExist(pocoElement):
                count = count + 1
                self.swipeUpDown(width, height, height_proportion1=height_proportion1,
                                 height_proportion0=height_proportion0, width_proportion=width_proportion, type="down")
            self.waitElementShortTime(pocoElement, timeSleep, is_error=is_error)
            self.displayTheShadedElement(pocoElement, width, height)
        except Exception as e:
            if is_error:
                self.triggerError("swipe and wait for the element appears failure", str(e))

    def displayTheShadedElement(self, pocoElement, width, height):
        pocoElement.refresh()
        x, y = pocoElement.get_position()
        count = 0
        while y <= 0 and count < 4:
            count = count + 1
            self.swipeUpDown(width, height)
            pocoElement.refresh()
            x, y = pocoElement.get_position()
        if y >= 0.85:
            self.swipeUpDown(width, height, height_proportion1=0.2)

    def checkUiElementExistBySwipeTransverse(self, pocoElement, width, height, Maxcount=5, proportion_left=0.5,
                                             proportion_right=0.4, duration=2):
        try:
            count = 0
            while (count < Maxcount) and not self.identifyPocoExist(pocoElement):
                count = count + 1
                self.swipe_Transverse(width, height, proportion_left=proportion_left, proportion_right=proportion_right,
                                      duration=duration)
            pocoElement.wait_for_appearance(1)
        except Exception as e:
            self.triggerError("swipe and wait for the element appears failure", str(e))

    def identifyCurrentFocusApp(self, dev, partOfAppPackageName):
        if platform == "Android":
            allActivityApp = shell("dumpsys window")
            allActivityApp.split(r"\r\n")
            eachLine = allActivityApp.splitlines()
            for app in eachLine:
                if bool(re.search('.*mCurrentFocus.*', app)):
                    result = partOfAppPackageName in app
                    return result
        else:
            currentAppName = dev.app_current()
            result = partOfAppPackageName in str(currentAppName)
            return result

    def goToTheApp(self, dev, appPackageName, width=None, height=None, smartlift=False, tidevice=False,
                   kill_iOS_app_real=True):
        if smartlift == True:
            self.stopAppCache(dev, appPackageName, width, height, kill_iOS_app_real=kill_iOS_app_real)
        result = self.identifyCurrentFocusApp(dev, appPackageName)
        starttime = self.startRecordTime()
        duringTime = 0
        while result == False and duringTime < 32:
            try:
                if tidevice:
                    self.start_app_tidevice(appPackageName)
                else:
                    start_app(appPackageName)
                sleep(5)
                result = self.identifyCurrentFocusApp(dev, appPackageName)
                endtime = self.StopRecordTime()
                duringTime = self.CalculateTimeSpend(starttime, endtime)
                if result == False and duringTime > 28:
                    self.triggerError("the " + appPackageName + " app can't be opened more than 28s")
            except Exception as e:
                self.triggerError("the " + appPackageName + " app can't be opened more than 28s", str(e))
        else:
            print("the " + appPackageName + "app was opened successfully")
            sleep(8)

    def goBacktoApp(self, dev, appPackageName, appName=None):
        if platform == "Android":
            self.goToTheApp(dev, appPackageName)
        else:
            self.openSwitcher(dev)
            sleep(4)
            self.click(appName)

    def clickCirclePoint(self, dev, iOSAirtestPic_path=None):
        try:
            if dev.device_info['model'] == "iPad":
                picList = [
                    Template(os.path.join(iOSAirtestPic_path, "iPad_assistiveTouch00.png"), record_pos=(-0.461, 0.181),
                             resolution=(2360, 1640)),
                    Template(os.path.join(iOSAirtestPic_path, "iPad_assistiveTouch01.png"), record_pos=(-0.46, 0.182),
                             resolution=(2360, 1640)),
                    Template(os.path.join(iOSAirtestPic_path, "iPad_assistiveTouch02.png"), record_pos=(0.447, 0.381),
                             resolution=(1536, 2048)),
                    Template(os.path.join(iOSAirtestPic_path, "iPad_assistiveTouch03.png"), record_pos=(-0.444, 0.343),
                             resolution=(1640, 2360))]
                for pic in picList:
                    pos = exists(pic)
                    if pos:
                        touch(pos)
                        break
            else:
                touch(Template(os.path.join(iOSAirtestPic_path, "iPhone_assistiveTouch00.png"), record_pos=(0.4, 0.619),
                               resolution=(1170, 2532)))
        except Exception as e:
            self.triggerError("click Circle point failure", str(e))

    def openSwitcher(self, dev, iOSAirtestPic_path=None):
        try:
            self.clickCirclePoint(dev)
            sleep(3)
            if dev.device_info['model'] == "iPad":
                touch(Template(os.path.join(iOSAirtestPic_path, "iPad_appSwitcher.png"), record_pos=(0.1, 0.109),
                               resolution=(2360, 1640)))
            else:
                touch(Template(os.path.join(iOSAirtestPic_path, "iPhone_appSwitcher.png"), record_pos=(0.1, 0.109),
                               resolution=(2360, 1640)))
        except Exception as e:
            self.triggerError("open A ppSwitcher failure", str(e))

    def stopAppCache(self, dev, appPackageName, width=None, height=None, kill_iOS_app_real=False, tidevice=False):
        try:
            if platform == "Android":
                stop_app(appPackageName)
            else:
                if kill_iOS_app_real == False:
                    self.stop_app_tidevice(appPackageName)
                else:
                    self.goToTheApp(dev, appPackageName, tidevice=tidevice)
                    self.openSwitcher(dev)
                    if dev.device_info['model'] == "iPad":
                        sleep(4)
                        x = width
                        y = height
                        swipe((x * 0.81, y * 0.33), (x * 0.81, 0))
                    else:
                        sleep(1)
                        x = width
                        y = height
                        swipe((x + 30000, y * 0.8), (x + 30000, 0))
        except Exception as e:
            self.triggerError("stop app cache failure", str(e))

    def del_file(self, path_data):
        for i in os.listdir(path_data):
            file_data = path_data + "\\" + i
            if os.path.isfile(file_data) == True:
                os.remove(file_data)
            else:
                self.del_file(file_data)

    def startRecordTime(self):
        starttime = datetime.datetime.now()
        return starttime

    def StopRecordTime(self):
        endtime = datetime.datetime.now()
        return endtime

    def CalculateTimeSpend(self, starttime, endtime):
        duringTime = (endtime - starttime).seconds
        return duringTime

    def openControlCenter(self, width=None, height=None):
        if platform == "Android":
            # Drop down to display the status bar.
            # shell("service call statusbar 1")
            shell("cmd statusbar expand-notifications")
        else:
            x = width + 30000000
            y = height
            swipe((x, 0), (x, y * 0.5))
            sleep(3)

    def triggerError(self, message, error=" "):
        assert_true(False, message)

    def drag_to(self, pocoElemnt, target, duration=2.0, timeSleep=shortSleep):
        try:
            pocoElemnt.refresh()
            pocoElemnt.wait_for_appearance(timeSleep)
            pocoElemnt.drag_to(target, duration=duration)
        except Exception as e:
            self.triggerError("Drag failure", str(e))

    def checkSwitchIsEnable(self, element) -> bool:
        if platform == "Android":
            if self.getAttr(element, "checked"):
                return True
            else:
                return False
        else:
            if self.getAttr(element, "value") == "1":
                return True
            else:
                return False

    def clear_input_box(self, pocoElemnt, selectAll, hitEnter=False):
        if self.get_text(pocoElemnt) == None:
            return
        self.longClick(pocoElemnt, 3, pos=[0.9, 0.5])
        if platform == "iOS":
            sleep(4)
        self.click(selectAll)
        if platform == "Android":
            keyevent("KEYCODE_DEL")
        else:
            sleep(4)
            text("\b", enter=False)
        if hitEnter:
            if platform == "Android":
                keyevent("ENTER")
            else:
                text("\b", enter=True)

    def set_attribute(self, pocoElement, attribute, value, timeSleep=shortSleep):
        try:
            pocoElement.refresh()
            pocoElement.wait_for_appearance(timeSleep)
            pocoElement.setattr(attribute, value)
        except Exception as e:
            self.triggerError("set attribute faile", str(e))

    def get_text(self, pocoElemnt, shortSleep=shortSleep):
        if platform == "Android":
            text = self.getAttr(pocoElemnt, "text", shortSleep=shortSleep)
        else:
            text = self.getAttr(pocoElemnt, "value", shortSleep=shortSleep)
        return text

    def back(self):
        if platform == "Android":
            keyevent("BACK")
        else:
            pass

    def click_mid(self, width, height):
        touch([0.5 * width, 0.5 * height])

    def is_valid_ip(self, address):
        try:
            ipaddress.IPv4Address(address)
            return True
        except ipaddress.AddressValueError:
            return False

    def common_assert(self, text, message=None):
        try:
            assert text
        except Exception as e:
            if message == None:
                self.triggerError("Expected result:%s" % text, str(e))
            else:
                self.triggerError(message, str(e))

    def get_random_element(self, my_list):
        return random.choice(my_list)

    def uninstall_App(self, zsbPackageName=None, uiud=None):
        if platform == 'Android':
            try:
                uninstall(zsbPackageName)
            except:
                pass
        else:
            count = 0
            while count < 3:
                count += 1
                sleep(1)
                if Common_Method().check_App_if_Install():
                    try:
                        device = tidevice.Device(uiud)
                        device.app_uninstall(zsbPackageName)
                    except Exception as e:
                        print("delete zsb app fail by tidevice" + str(e))
                else:
                    break
                if count == 3:
                    assert_true(False, "the app wasn't uninstall by tidevice")

    def install_App(self, packageName, shared_folder_appPackage_path=None, uiud=None):
        target_apk_path = os.path.join(shared_folder_appPackage_path, packageName)
        self.smb_authenticate()
        try:
            if platform == 'Android':
                install(target_apk_path)
            else:
                device = tidevice.Device(uiud)
                device.app_install(target_apk_path)
        except:
            self.triggerError('install app fail')
        finally:
            if os.path.exists(target_apk_path):
                try:
                    shutil.rmtree(target_apk_path)
                except Exception as e:
                    """"""

    def smb_authenticate(self, shared_folder_appPackage_path=None, shared_folder_username=None,
                         shared_folder_password=None):
        match = re.match(r'\\\\(.*?)\\(.*?)\\', shared_folder_appPackage_path)
        server_ip = match.group(1)
        server_name = match.group(2)
        conn = SMBConnection(shared_folder_username, shared_folder_password, 'client_name', server_name,
                             use_ntlm_v2=True)
        conn.connect(server_ip)

        conn.close()

    def check_App_Version(self, zsbPackageName=None, uiud=None):
        if platform == 'Android':
            return ADB(serialno=uiud).get_package_version(zsbPackageName)
        else:
            command = f'tidevice -u {uiud} applist'
            output = subprocess.check_output(command, shell=True).decode('utf-8', 'ignore')
            lines = output.split('\n')
            for line in lines:
                if zsbPackageName in line:
                    version_match = re.search(r'\d+\.\d+\.\d+', line)
                    if version_match:
                        return version_match.group(0)

    def check_App_if_Install(self, zsbPackageName=None, uiud=None):
        if platform == 'Android':
            try:
                result = ADB(serialno=uiud).check_app(zsbPackageName)
                return result
            except:
                return False
        else:
            command = f'tidevice -u {uiud} applist'
            output = subprocess.check_output(command, shell=True).decode('utf-8', 'ignore')
            lines = output.split('\n')
            for line in lines:
                if zsbPackageName in line:
                    return True
            return False

    def swipe_for_my_data(self, element1_pos, element2_pos, width, height):
        pos1 = [element1_pos[0] * width, element1_pos[1] * height]
        pos2 = [element2_pos[0] * width, element2_pos[1] * height]
        swipe(pos1, pos2)

    def swipe_coord_to_coord(self, element_pos1, element_pos2, width, height):
        swipe([element_pos2[0] * width, element_pos2[1] * height], [element_pos1[0] * width, element_pos1[1] * height])

    def checkUiElementExistBySwipe_coord_to_coord(self, pocoElement, element_pos1, element_pos2, width, height,
                                                  Maxcount=5):
        try:
            count = 0
            while (count < Maxcount) and not self.identifyPocoExist(pocoElement):
                count = count + 1
                self.swipe_coord_to_coord(element_pos1, element_pos2, width, height)
            self.waitElementShortTime(pocoElement)
            pocoElement.refresh()
            x, y = pocoElement.get_position()
            count = 0
            while y <= 0 and x <= 0 and count < 2:
                count = count + 1
                self.swipe_coord_to_coord(element_pos1, element_pos2, width, height)
            if y >= 0.85 or x >= 0.85:
                self.swipe_coord_to_coord(element_pos1, element_pos2, width, height)
        except Exception as e:
            self.triggerError("swipe and wait for the element appears failure", str(e))

    # def update_file_content_in_sharedfolder(self, file_path, file_name, content, type='a'):
    #     os.system(f'net use {shared_folder_path}{file_path} /user:{shared_folder_username} {shared_folder_password}')
    #     with open(f'{shared_folder_path}{file_path}\{file_name}', type) as f:
    #         f.write(content)
    #         if type == 'a':
    #             f.write('\n')

    # def read_file_content_in_sharedfolder(self, file_path, file_name):
    #     os.system(f'net use {shared_folder_path}{file_path} /user:{shared_folder_username} {shared_folder_password}')
    #     with open(f'{shared_folder_path}{file_path}\{file_name}', 'r') as f:
    #         content = f.read()
    #     return content

    def clear_adblog(self):
        cmd = "logcat -c"
        shell(cmd)

    def get_adblog(self, dev, path, uiud=None):
        u'''  获取app adb日志
        :param  adb_log_path  adb日志存储的绝对路径
        :return  None
        :example get_adblog(adb_log_path)
        '''
        adbPath = dev.adb.cmd_options[0]
        with open(path, 'a') as f:
            poplog = subprocess.Popen([adbPath, '-s', uiud, 'logcat'], stdout=f)
        return poplog

    def recoverAirtestProcessAndGenerateAirtestReport(self, Bonding, logdir,
                                                      caseFail, caseErrorLog, test_name,
                                                      test_class, test_file, ScriptFileName,
                                                      export_dir, poplog, generateReport=True, uiud=None):
        reports_item = ""
        try:
            # actually the android and iPhone can use the same api to generate the video,
            # but it would appears android can't save the video if it fail, ios didn't have this
            # issue. So android use the android best way, ios use the ios best way
            if platform == "Android":
                Bonding.stop_recording(logdir + "\\" + test_name + ".mp4")
            else:
                Bonding.stop_recording()
        except Exception as e:
            logging.info('Error recoverAirtestProcessAndGenerateAirtestReport stop_recording: ' + str(e))
        finally:
            try:
                if caseFail:
                    print(str(Exception(caseErrorLog)))
                    logging.log(Exception(caseErrorLog))
            except Exception as e:
                logging.info('Error recoverAirtestProcessAndGenerateAirtestReport caseFail area' + str(e))
            try:
                if generateReport:
                    reports_item = self.generateAirtestReport(test_name, test_class, test_file, ScriptFileName, logdir,
                                                              export_dir, logdir)
            except Exception as e:
                logging.info('Error recoverAirtestProcessAndGenerateAirtestReport generateAirtestReport: ' + str(e))
            finally:
                try:
                    if platform == "Android":
                        uninstall('com.netease.open.pocoservice')
                    else:
                        Common_Method().removeWebDriverAgent(uiud)
                except Exception as e:
                    logging.info('Error recoverAirtestProcessAndGenerateAirtestReport remove poco server: ' + str(e))
                finally:
                    try:
                        poplog.terminate()
                        poplog.kill()
                    except Exception as e:
                        logging.info(
                            'Error recoverAirtestProcessAndGenerateAirtestReport poplog terminate' + str(e))
                    finally:
                        return reports_item

    def generateAirtestReport(self, test_name, test_class, test_file, script_root, log_root, export_dir, logfile,
                              uiud=None):
        try:
            one_report_dict = {
                "script": test_name,
                "tests": {
                    uiud: {
                        "status": 0,
                        "path": ""
                    }
                }
            }
            r = LogToHtml(script_root=script_root, log_root=log_root,
                          export_dir=export_dir, logfile=logfile + '\log.txt', lang='en',
                          plugins=["poco.utils.airtest.report"])
            try:
                r.report()
            except:
                sleep(30)
                r.report()
            data = r.report_data()
            one_report_dict['tests'][uiud]['status'] = 0 if data['test_result'] == True else 1
            one_report_dict['tests'][uiud][
                'path'] = test_class + "\\" + test_name + "\\" + 'Report_' + test_file + ".log/log.html"

            return one_report_dict
        except Exception as e:
            raise Exception("report generation failure " + str(e))

    def wait_notification_disappear(self, pocoElement, wait_time=15):
        if self.identifyPocoExist(pocoElement, wait_time):
            self.waitElementDismiss(pocoElement, wait_time)

    def clickEnabledButton(self, pocoElement):
        if platform == "Android":

            timeout = 0
            while timeout < 5:
                pocoElement.refresh()
                if self.getAttr(pocoElement, "enabled") == True:
                    self.click(pocoElement)
                    break
                timeout += 1
        else:
            timeout = 0
            while timeout < 5:
                self.click(pocoElement)
                if not self.identifyPocoExist(pocoElement):
                    break
                timeout += 1

    def get_phone_brand(self):
        if platform == "Android":
            cmd = "getprop ro.product.brand"
            result = shell(cmd)
            return result.strip()
        else:
            return "Apple"

    def get_phoneOS_version(self):
        if platform == 'Android':
            cmd = "getprop ro.build.version.release"
            result = shell(cmd)
            return result.strip()
        else:
            return self.get_iOS_info('ProductVersion').strip()

    def get_phone_model(self):
        if platform == 'Android':
            cmd = "getprop ro.product.model"
            result = shell(cmd)
            return result.strip()
        else:
            MarketName = self.get_iOS_device_market_name()
            if MarketName != "None":
                return MarketName
            else:
                return self.get_iOS_info('ProductType')

    def get_iOS_device_market_name(self):
        command = f'tidevice info'
        text = subprocess.check_output(command, shell=True).decode('utf-8', 'ignore')
        patterns = {
            "MarketName": r"MarketName:\s+(.*)",
            "DeviceName": r"DeviceName:\s+(.*)",
            "ProductVersion": r"ProductVersion:\s+(.*)"
        }
        device_info = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, text)
            if match:
                device_info[key] = match.group(1)
            else:
                device_info[key] = None
        return device_info["MarketName"].strip()

    def get_iOS_info(self, key, uiud=None):
        """
        key option:
        ['ActivationState', 'ActivationStateAcknowledged', 'BasebandStatus', 'BluetoothAddress', 'BoardId', 'BrickState', 'BuildVersion', 'CPUArchitecture', 'ChipID', 'DeviceClass', 'DeviceColor', 'DeviceName',
'DieID', 'EthernetAddress', 'FirmwareVersion', 'HardwareModel', 'HardwarePlatform', 'HasSiDP', 'HostAttached', 'MLBSerialNumber', 'ModelNumber', 'NonVolatileRAM', 'PartitionType', 'PasswordProtected', 'ProductName', 'ProductType', 'ProductVersion', 'ProductionSOC', 'ProtocolVersion', 'RegionInfo', 'SerialNumber', 'SoftwareBehavior', 'SoftwareBundleVersion', 'SupportedDeviceFamilies', 'TelephonyCapability', 'TimeIntervalSince1970', 'TimeZone', 'TimeZoneOffsetFromUTC', 'TrustedHostAttached', 'UniqueChipID', 'UniqueDeviceID', 'UntrustedHostBUID', 'UseRaptorCerts', 'Uses24HourClock', 'WiFiAddress', 'WirelessBoardSerialNumber']
        """
        device = tidevice.Device(uiud)
        allValue = device.get_value()
        value = allValue[key]
        return value

    # def startWebDriverAgent(self, device_id):
    #     webDriverAgentPath = os.path.join(resource_path, 'wda-vxxx.ipa')
    #     subprocess.run(['tidevice', '-u', device_id, 'install', str(webDriverAgentPath)], check=True)
    #     # subprocess.run(['cmd', '/c', 'start', 'tidevice', '-u', device_id, 'xctest', '-B',
    #     #                 'com.zebra.WebDriverAgentLib.xctrunner'], check=True)
    #     subprocess.run(['tidevice', '-u', device_id, 'launch', 'com.zebra.WebDriverAgentRunner.xctrunner'], check=True)
    #     # os.system(r'tidevice -u %s install '%device_id + webDriverAgentPath)
    #     # os.system(r'cmd/c start tidevice -u %s xctest -B com.zebra.WebDriverAgentLib.xctrunner'%device_id)
    #     time.sleep(6)

    def removeWebDriverAgent(self, device_id):
        try:
            os.system(r'tidevice -u %s uninstall com.zebra.WebDriverAgentRunner.xctrunner' % device_id)
            time.sleep(6)
        except Exception as e:
            print(e)

    def reinstall_tidevice(self):
        os.system('pip uninstall -y tidevice')
        os.system('cmd/c start pip uninstall -y tidevice')
        os.system('pip install tidevice')

    def resetiPhone(self, device_id):
        os.system(r'tidevice -u %s reboot' % device_id)

    def getTideviceSyslog(self, device_id, path):
        with open(path, 'a') as f:
            poplog = subprocess.Popen(['tidevice', '-u', device_id, 'syslog'], stdout=f)
        return poplog

    # def env_not_production(self):
    #     if not app_environment == "Production":
    #         return True
    #     else:
    #         return False
    #
    # def env_production(self):
    #     if app_environment == "Production":
    #         return True
    #     return False

    def start_app_tidevice(self, appPackageName):
        tidevice.Device().app_start(bundle_id=appPackageName)
        # subprocess.run(['tidevice', '-u', device_id, 'launch', appPackageName], check=True)

    def stop_app_tidevice(self, appPackageName):
        tidevice.Device().app_kill(appPackageName)
        # subprocess.run(['tidevice', '-u', device_id, 'kill', appPackageName], check=True)

    def modify_file_content(self, file_path, key, value):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        if key is not None:
            for i in range(len(lines)):
                if lines[i].startswith(key):
                    lines[i] = key + f" = {value}\n"
                    break
        with open(file_path, 'w') as file:
            file.writelines(lines)

    # ///////////////////////
    # try:
    #     # Your Poco operation here
    #    poco("your_poco_query").click()
    # except PocoNoSuchNodeException as e:
    #  print(f"PocoNoSuchNodeException: {e}")
    #     # Add additional logging or error handling as needed
    #     # You might want to capture a screenshot or print the current screen state for debugging

    # def check_text_presence(text_to_check):
    #     # Search for the text on the screen
    #     text_element = poco(text=text_to_check)
    #
    #     if text_element.exists():
    #         print(f"Text '{text_to_check}' is present on the screen.")
    #         return True
    #     else:
    #         print(f"Text '{text_to_check}' is not present on the screen.")
    #         return False

    # Example usage
    # text_present = check_text_presence("YourTextToCheck")
    #
    # if text_present:
    #     # Perform actions when the text is present
    #     pass
    # else:
    #     # Perform actions when the text is not present
    #     pass

    def drag_bar(element, direction='right', duration=1.0):
        # Get the position of the element
        global start_point, end_point
        element_pos = element.get_position()

        if direction == 'right':
            start_point = element_pos[0]
            end_point = element_pos[0] + 200  # Adjust the distance as needed
        elif direction == 'left':
            start_point = element_pos[0] + 200
            end_point = element_pos[0]

        # Perform the drag
        poco.swipe([start_point, element_pos[1]], [end_point, element_pos[1]], duration=duration)

    def Stop_The_App(self):
        sleep(2)
        stop_app("com.zebra.soho_app")

    def Start_The_App(self):
        start_app("com.zebra.soho_app")
        sleep(4)


    def relaunch_app(self):
        app_package = "com.zebra.soho_app"
        stop_app(app_package)
        sleep(2)
        start_app(app_package)
        sleep(2)

    # def Open_Google_Search_for_ZSBApp(self):
    #
    #     start_app("com.android.chrome")
    # sleep(5)
    # touch(Template(r"tpl1706523292994.png", record_pos=(0.028, 0.918), resolution=(1080, 2400)))
    # sleep(4)
    # touch(Template(r"tpl1706523705888.png", record_pos=(0.006, -0.894), resolution=(1080, 2400)))
    # text("https://zsbportal.zebra.com/")
    # sleep(5)
    def Start_The_iOSApp(self):
        start_app("com.zebra.soho")
        sleep(4)

    def Stop_The_iOSApp(self):
        sleep(2)
        start_app("com.zebra.soho")
        sleep(4)

    def relaunch_iOSapp(self):
        app_package = "com.zebra.soho"
        stop_app(app_package)
        sleep(2)
        start_app(app_package)
        sleep(2)
