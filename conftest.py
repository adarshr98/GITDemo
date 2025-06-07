import os
from selenium import webdriver
from pytest_html import extras


import pytest

def pytest_addoption(parser): #https://docs.pytest.org/en/stable/example/simple.html - url to get parser code
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver
    driver.close()
    
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when in ("call", "setup"):
        xfail = hasattr(report, "wasxfail")
        if (report.failed and not xfail) or (report.skipped and xfail):
            driver = item.funcargs.get("browserInstance")
            if driver is None:
                return

            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            os.makedirs(reports_dir, exist_ok=True)

            file_name = report.nodeid.replace("::", "_").replace("/", "_") + ".png"
            file_path = os.path.join(reports_dir, file_name)

            _capture_screenshot(driver, file_path)

            if hasattr(report, "extra"):
                report.extra.append(extras.image(file_path))
            else:
                report.extra = [extras.image(file_path)]

def _capture_screenshot(driver, file_path):
    driver.get_screenshot_as_file(file_path)
