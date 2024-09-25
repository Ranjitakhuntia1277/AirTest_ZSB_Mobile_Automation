# LoginFunction.py

import datetime
import random
import string
import fnmatch

from airtest.core.api import *
# import pytest
# from pipes import Template
from poco import poco
from poco.exceptions import PocoNoSuchNodeException, PocoTargetTimeout

from ZSB_Mobile.Common_Method import Common_Method

common_method = Common_Method(poco)


class Printer_Management_Screen:
    pass

    def __init__(self, poco):
        self.poco = poco