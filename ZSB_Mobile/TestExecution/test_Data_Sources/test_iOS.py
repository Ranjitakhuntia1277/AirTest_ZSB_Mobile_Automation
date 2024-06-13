import os

from airtest.core.api import connect_device, auto_setup, start_app, sleep, text, stop_app
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.ios import iosPoco
from self import self
from airtest.core.api import *

import pytest


class iOS:
    pass


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device("Android:///")


import subprocess
import time

def run_adb_command(command):
    """Run an adb command and return the output."""
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr.decode('utf-8'))
    return result.stdout.decode('utf-8')

def start_screen_recording(file_path):
    """Start screen recording on the device."""
    print("Starting screen recording...")
    subprocess.Popen(f"adb shell screenrecord {file_path}", shell=True)

def stop_screen_recording():
    """Stop screen recording on the device."""
    print("Stopping screen recording...")
    # Find the PID of the screenrecord process
    pid = run_adb_command("adb shell pidof screenrecord").strip()
    if pid:
        run_adb_command(f"adb shell kill {pid}")
    else:
        print("Screenrecord process not found.")

def open_chrome():
    """Open the Chrome app on the device."""
    print("Opening Chrome...")
    run_adb_command("adb shell monkey -p com.android.chrome -c android.intent.category.LAUNCHER 1")

def close_chrome():
    """Close the Chrome app on the device."""
    print("Closing Chrome...")
    run_adb_command("adb shell am force-stop com.android.chrome")

def pull_screen_recording(file_path, local_path):
    """Pull the screen recording file from the device to the local machine."""
    print(f"Pulling screen recording from device to {local_path}...")
    run_adb_command(f"adb pull {file_path} {local_path}")

def test_1():
    file_path = "/storage/emulated/0/Download/screenrecord.mp4"
    local_path = "screenrecord.mp4"  # Save to the current directory

    # Start screen recording
    start_screen_recording(file_path)
    time.sleep(2)  # Give some time for the screen recording to start

    # Open Chrome
    open_chrome()
    time.sleep(5)  # Keep Chrome open for 5 seconds

    # Close Chrome
    close_chrome()
    time.sleep(2)  # Give some time for the close command to take effect

    # Stop screen recording
    stop_screen_recording()
    time.sleep(2)  # Wait for the screen recording to be properly saved on the device

    # Pull the screen recording file to the local machine
    pull_screen_recording(file_path, local_path)

    print(f"Screen recording saved to {local_path}")








