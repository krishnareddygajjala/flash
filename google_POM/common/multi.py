import pytest
from importlib import import_module
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.parametrize('browser_name', ['firefox', 'chrome', 'ie', 'opera'])
def test_accepts_firefox_options_to_remote_driver(mocker, browser_name):
    options = import_module('selenium.webdriver.{}.options'.format(browser_name))
    caps_name = browser_name.upper() if browser_name != 'ie' else 'INTERNETEXPLORER'
    mock = mocker.patch('selenium.webdriver.remote.webdriver.WebDriver.start_session')
    opts = options.Options()
    opts.add_argument('foo')
    expected_caps = getattr(DesiredCapabilities, caps_name)
    caps = expected_caps.copy()
    expected_caps.update(opts.to_capabilities())

    WebDriver(desired_capabilities=caps, options=opts)
    mock.assert_called_with(expected_caps, None)