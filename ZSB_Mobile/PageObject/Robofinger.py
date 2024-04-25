import requests
import time


class ServoAPI:
    def __init__(self, driver):
        self.driver = driver


def test_robo_finger():
    url = "http://10.233.194.73/command?action=run&delay=10"
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Robo finger set to 180 degree successful.")
    except requests.exceptions.RequestException as e:
        print("Failed to control robo finger. Exception: {e}")

    print("Robo finger set to 0 degree successful.")


if __name__ == "__main__":
    test_robo_finger()
