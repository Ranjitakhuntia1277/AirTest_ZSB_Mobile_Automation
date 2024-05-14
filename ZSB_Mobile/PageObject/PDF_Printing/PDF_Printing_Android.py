import requests
import self
from airtest.core.api import *
from airtest.core.api import sleep
from urllib3.util import url

# from setuptools.config._validate_pyproject.formats import url

from ZSB_Mobile.Common_Method import Common_Method
from poco.exceptions import PocoNoSuchNodeException
from pocoui_lib.android.kotoComponent import poco


class PDF_Printing_Android_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco
        self.Printer_Settings_Btn = "Printer Settings"