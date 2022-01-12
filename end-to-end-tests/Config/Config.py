import os

import __root__

rootPath = __root__.path()

# Configure the Browser name here as CHROME , FIREFOX , EDGE
CHROME = "CHROME"
FIREFOX = "FIREFOX"
SAFARI = "SAFARI"
BROWSER_NAME = os.environ.get("TEST_BROWSER", CHROME)
# Pipe separated options (e.g. "--headless | --disable-gpu | --window-size=1280,800")
CHROME_OPTIONS = os.environ.get("CHROME_OPTIONS", None)
# Selenium Webdriver executables path
GECKO_PATH = os.path.join(__root__.path(), "Config/drivers/geckodriver")

URL = "https://marksman.staging.pascalfinancial.com/"

# Wait Timeouts
VERY_SHORT_WAIT = 5
SHORT_WAIT = 10
MEDIUM_WAIT = 40
LONG_WAIT = 100
