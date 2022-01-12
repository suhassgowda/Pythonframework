[![CircleCI](https://circleci.com/gh/pascal-financial/end-to-end-tests/tree/master.svg?style=shield&circle-token=6d985831cb065b6d8282c29ec6a69605955a7639)](https://circleci.com/gh/pascal-financial/end-to-end-tests/tree/master)
# Selenium Python Framework #

> Automation framework developed using Python + Selenium WebDriver + pytest with Page Object Model which can be used across different web based applications

With this framework in place, whenever we need to automate a web based application, we would not need to start from scratch

---
## Available Sample Scripts

 - Web Application

## Run Tests from Linux/Ubuntu

Install Pre-requisites
1.Python
2.pip
3.pytest

Steps :

1. Run command in root folder 'pip install -r requirements.txt'
2. Set the BROWSER_NAME Constant as CHROME or FIREFOX in ./Config/Config.py file
3. Choose one of the commands . It changes from Ubuntu version to version 
   
	'python3 -m pytest -m pascal --html-report=./Reports/TestReport.html'
	'pytest -m pascal --html-report=./Reports/TestReport.html'
	
Final report can be found in Reports folder

---
## Features

 - Logging
 - Object Repository
 - Reporting
 - Utilities
 - Parallel Execution
 - Rerun
 
 __Details:__

 - _Logging_
    - Logging API is used to include your own messages. Logs file is created in location "Reports\LatestResults"

 - _Reporting_
    - The framework generates default pytest `TestReport.html` report.

 - _Object Repository_
    - Maintained with the help of Page object model.

 - _Utilities_
    - Different Utilities exist (SafeActions, Assertions, customlogger)

---
## Prerequisites
 - __pycharm__
    - Download and install pycharm community from [here](https://www.jetbrains.com/pycharm/download/)
 - __Python__
    - Version: `python-3.9`
	- Website: [link](https://www.python.org/downloads/)
* User can install required ` python libraries` by executing `InstallRequirements.bat`file
    * Clone the framework from repository "https://github.com/VenkataSaiAnnam/pascalWT_Automation.git"
    * Open "..\pascalWT_Automation" from file explorer and double click the "installRequirements.bat" to install the requirements
    * After successfull completion of installation, add the below python paths to Environment Variables
        * C:\Users\<yourname>\AppData\Roaming\Python\Python<>\Scripts
        * C:\Users\<yourname>\AppData\Roaming\Python\Python<>\site-packages
---
## Steps to use the framework

###  Launch the Project  ###

* If you are intended to add new tests or modify the existing tests, open the "pascalWT_Automation" file from pycharm IDE
* In Pycharm `Goto File > Settings > Python interpreter, add python 3.8 interpreter(Location of Python installed)` and Click Ok
* If you see `install requirements` pop-up/alert in Pycharm , Please click on it to install libraries.
* Start using the Project.
        
###  Execution  ###

__To run the tests from pycharm ...__

    * Goto Run > Edit Configurations...
    * Click on + icon on top left to add new configuration and select pytest
    * Input any name, Select root of project as working directory and Click Ok
    * Click on green run icon to run all available tests in the project
    
* To run the tests based on pytest markers,
    * Add pytest marker to testcase as below
    * Refer pytest.ini to add the custom marker description : Avoids Warning
    * To use this marker > Go to Edit Configurations > add `-m regression` as additional arguments to pytest
```
 @pytest.mark.regression
    def test_tc_001_verify_login(self, username, password):
``` 

* If you are intended to just run the existing tests, navigate to "end-to-end-tests" folder and double click "RunTests.bat" file
    * parallel execution and retry: if you are intended to run tests in parallel, change -n and --reruns options count as below: 
        * Open RunTests.bat file in notepad and update count of -n and --reruns option:
    
     `<pytest -v -n 2 --html=./Reports/TestReport.html --reruns 0>`
     
     So, above runs 2 tests at a time and rerun is zero


---
## Who do I talk to?

 - Owner - `Venkata Sai Annam<venkatasai.annam@zenq.com>`
