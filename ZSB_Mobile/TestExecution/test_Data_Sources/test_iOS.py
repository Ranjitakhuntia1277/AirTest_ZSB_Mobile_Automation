from airtest.core.api import connect_device, auto_setup, start_app, sleep, text, stop_app
from poco.drivers.ios import iosPoco
from self import self
from airtest.core.api import *

import pytest


class iOS:
    pass


uuid = "00008101-00051D400144001E"
Bonding = connect_device("ios:///http+usbmux://" + uuid)
poco = iosPoco(device=Bonding)
auto_setup(logdir="./", compress=3,
           devices=[f"ios:///http+usbmux://{uuid}"])


def test_DataSources_TestcaseID_45729():
    pass

    packagename = "com.zebra.soho"
    try:
        pass
    finally:
        stop_app(packagename)
        sleep(1)
        start_app(packagename)
        sleep(1)
