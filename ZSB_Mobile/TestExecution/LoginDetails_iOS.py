import subprocess

from airtest.core.api import connect_device, auto_setup, start_app
from poco.drivers.ios import iosPoco

uuid = "00008101-00051D400144001E"
Bonding = connect_device("ios:///http+usbmux://"+uuid)
poco = iosPoco(device= Bonding)

auto_setup(logdir="./", compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])
start_app("com.zebra.soho")
#####------------------------------------------------------------------------------

def test_new_start_app_for_ios_17_and_18(appPackageName="com.zebra.soho"):
    uuid = "00008030-000D68460AD8402E"
    Bonding = connect_device("ios:///http+usbmux://" + uuid)
    poco = iosPoco(device=Bonding)
    auto_setup(logdir="./", compress=3,
               devices=[f"ios:///http+usbmux://{uuid}"])

    # kill_app_command = ['ios', 'kill',appPackageName]
    launch_app_command = ['ios', 'launch',appPackageName]
    # you need to kill the app firstly, and then start the app, otherwith it would fail to open the app after you open the app more than 188 times
    # subprocess.run(kill_app_command, check=True)
    subprocess.run(launch_app_command, check=True)

