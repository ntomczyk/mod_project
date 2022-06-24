# mod_project
# Project requirements:

- Step 1: Install/upgrade Python version to:

- Python 3.10.5

- Step 2: Install pip for Python 3, there was issue with pip for python 3.10 on ubuntu 20.04 

```
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
```

- Step 3: Install virtualenv, for linux:

```
sudo apt install -y python3-venv
```

- Step 4: Launch your Python 3 virtual environment, add name of the virtual environment e.g. project_venv - in project directory:

```
python3 -m venv mod_project_venv
```

- Step 5: Activate your new Python 3 environment - in project directory
 
```
source mod_project_venv/bin/activate 
```

- you can make sure you are now working with Python 3.10.5, if you use Pycharm set given Python interpreter:
- Settings->Project->Python Interpreter and choose from the list or Add Interpreter

```
python --version
```
- this command will show you what is going on: the python executable you are using is now located inside your 
virtualenv repository

```
which python 
```

- Step 6: Install all requirements plugins and libraries in chosen version,
if you add new one use pip freeze > requirements.txt

```
pip install -r requirements.txt
```
- or install the newest stable version one by one e.g. pip install Selenium

- Step 7: Leave the virtual environment

```
deactivate
```


# Set pytest as runner
- Before running tests set Pytest as test runner
- If you use Pycharm you can set in Settings->Tools->Python integrated tools->Default test runner. 
- After setting runner restart Pycharm.

# Load environment variables from .env
- In **.default.env** there are all the variables needed to run the tests. 
- **It is required to set all variables in your own .env and add them to 
.gitignore before running the tests**
- You can specify the ENV credentials on the command line, it will override existing one:

```
pytest --envfile .dev1.env
```

# Running tests:

- Run all tests

```
pytest
```

- Run tests in a directory

```
pytest tests/
```

- Run specific test

```
pytest tests/test_order_process.py
```

- Run test in specific browser, default browser is chrome in headless mode

```
pytest tests/test_order_process.py --browser=chrome
```

- Run marked tests (rest of tests will be skipped):
*in test add mark e.g. @mark.smoke* 

```
pytest -m smoke
```

- Run test few times e.g. 2 times

```
pytest tests/test_order_process.py --count=2
```

- Display printed things in the tests results

```
pytest tests/test_order_process.py -s
```

- Display a better view of the test results in the terminal

```
pytest tests/test_order_process.py -vv
```

# Reports

- Xml report is generated automatically - command from pytest.ini

# Allure report 

- Run test and store results in report dir (using allure-pytest)

```
pytest --alluredir=reports/allure_reports
```
- Allure required Java

```curl -o allure-2.7.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/allure-2.7.0.tgz
sudo tar -zxvf allure-2.7.0.tgz -C /opt/   
sudo ln -s /opt/allure-2.7.0/bin/allure /usr/bin/allure  
allure --version 
```

- open in local machine in default browser e.g. allure serve -h 127.0.0.1 -p 8085 allure-reports


```
allure serve report
```

- rerun failed tests e.g. 2 times set in pytest.ini 

```
--reruns 2
```





