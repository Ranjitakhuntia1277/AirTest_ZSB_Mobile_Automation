from airtest.core.api import connect_device, auto_setup, start_app
from poco.drivers.ios import iosPoco

uuid = "00008101-00051D400144001E"
Bonding = connect_device("ios:///http+usbmux://"+uuid)
poco = iosPoco(device= Bonding)

auto_setup(logdir="./", compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])
start_app("com.zebra.soho")


