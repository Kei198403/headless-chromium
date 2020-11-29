import os
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DictBunch(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, **kwargs):
        self.update(kwargs)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, dict):
        self.__dict__ = dict


class Chrome:
    driver = None
    options = webdriver.ChromeOptions()
    binary_location: str = ""
    executable_path: str = ""
    wh = DictBunch()

    def __init__(self):
        self.configure_aws_labmda()

    def __del__(self):
        self.close_driver()

    def open_driver(self):
        if self.binary_location:
            self.options.binary_location = self.binary_location
        self.driver = webdriver.Chrome(
            executable_path=self.executable_path,
            chrome_options=self.options
        )

    def configure_aws_labmda(self):
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--single-process")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--window-size=1280x1696")
        self.options.add_argument("--disable-application-cache")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--hide-scrollbars")
        self.options.add_argument("--enable-logging")
        self.options.add_argument("--log-level=0")
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--homedir=/tmp")

        if "USER_AGENT" in os.environ:
            self.options.add_argument("--user-agent=%s" %
                                      os.environ["USER_AGENT"])

        self.executable_path = "/usr/local/bin/chromedriver"
        self.binary_location = "/usr/local/bin/headless-chromium"

    def save_window_handles(self):
        self.wh.window_handles = self.driver.window_handles

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))

        wh_now = self.driver.window_handles
        wh_then = self.wh.window_handles

        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()
        else:
            raise Exception("window取得失敗")

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None


def main():
    chrome = Chrome()
    wait = WebDriverWait(chrome.driver, 10)

    chrome.open_driver()
    chrome.driver.get("http://taruo.net/e/")
    wait.until(EC.presence_of_all_elements_located)
    chrome.driver.save_screenshot("~/taruo.net.png")
    chrome.close_driver()


if __name__ == "__main__":
    main()
