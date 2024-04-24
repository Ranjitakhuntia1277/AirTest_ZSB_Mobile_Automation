from platform import platform

import pytest
from airtest.core.android import Android
from airtest.core.api import *
from poco import poco
# from ZSB_Mobile.Common_Method import*

from ZSB_Mobile.PageObject.Login_Screen import Login_Screen


class App_Settings_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Printer_Settings_Btn = "Printer Settings"
        self.PrinterName_In_Printer_Settings = Template(r"tpl1704389359227.png", record_pos=(0.1, -0.774),
                                                        resolution=(1080, 2400))

        self.WiFi_Tab = "Wi-Fi"
        self.Current_Network_Txt = "Current Network"
        self.Network_Name_Txt = "NESTWIFI"
        self.Network_Status_Txt = "Network Status"
        self.Network_Status_Result_Txt = "Connected"
        self.IPAddress_Txt = "IP Address"
        self.IPAddress_Result_Txt = "192.168.86.155"
        self.Manage_Network = "Manage Networks"
        self.Save_Network_Message_Txt = "You can save up to 5 network profiles to your Saved Networks. If no saved networks are available, you will have to add a new one."
        self.Threedot_On_Workspace = " "





    def click_Printer_Settings(self):
        printer_settings = self.poco(self.Printer_Settings_Btn)
        printer_settings.click()

    # def Enter_Google_Password(self):
    #     enter_google_password = self.poco(self.Google_Password)
    #     sleep(2)
    #     enter_google_password.set_text("Swdvt@#123")

    def click_PrinterName_On_Printersettings(self):
        # printerName = self.poco(self.PrinterName_In_Printer_Settings)
        touch(self.PrinterName_In_Printer_Settings)

    def click_wifi_tab(self):
        wifi_tab = self.poco(self.WiFi_Tab)
        wifi_tab.click()

    def get_text_CurrentNetwork_Txt(self):
        current_network_txt = self.poco(self.Current_Network_Txt)
        current_network_txt.get_text()
        # Print the text
        print(f"Current Network Text: {current_network_txt}")

        # Return the text if needed
        return current_network_txt

    def get_text_Network_Name_Txt(self):
        network_name_txt = self.poco(self.Network_Name_Txt)
        network_name_txt.get_text()

    def get_text_Network_Status_Txt(self):
        network_status_txt = self.poco(self.Network_Status_Txt)
        network_status_txt.get_text()

    def get_text_Network_Status_Result_Txt(self):
        network_status_result_txt = self.poco(self.Network_Status_Result_Txt)
        network_status_result_txt.get_text()

    def get_text_IPAddress_Txt(self):
        IPaddress_txt = self.poco(self.IPAddress_Txt)
        IPaddress_txt.get_text()

    def get_text_IPAddress_Result_Txt(self):
        IPaddress_result_txt = self.poco(self.IPAddress_Result_Txt)
        IPaddress_result_txt.get_text()

    def click_Manage_Networks_Btn(self):
        manage_network = self.poco(self.Manage_Network)
        manage_network.get_text()

    def IS_Present_Save_Network_Message_Txt(self):
        save_network_message = self.poco(self.Save_Network_Message_Txt)
        save_network_message.get_text()

    def click_Threedot_On_Workspace(self):
        threedot_On_Workspace = self.poco(self.Threedot_On_Workspace)
        threedot_On_Workspace.click()
