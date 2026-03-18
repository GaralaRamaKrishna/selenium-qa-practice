# selenium-qa-practice

practicing selenium webdriver with python.
started this after finishing manual testing 
projects on HighScores.ai and SecondBrainLabs.
these are my scripts as i learn automation.

## project structure
selenium-qa-practice/
├── pages/
│   └── login_page.py
├── tests/
│   ├── test_10_pom_login.py
│   ├── test_11_screenshot_on_failure.py
│   └── test_12_alerts.py
├── test_1_open_browser.py
├── test_2_google_search.py
├── test_3_login.py
├── test_4_negative_login.py
├── test_5_form_fill.py
├── test_6_form_fill_complete.py
├── test_7_multiple_assertions.py
├── test_8_explicit_wait.py
└── test_9_xpath_practice.py
## all scripts

| script | what it does | status |
|--------|-------------|--------|
| test_1_open_browser.py | opens browser, reads title | ✅ pass |
| test_2_google_search.py | automates search on duckduckgo | ✅ pass |
| test_3_login.py | automates valid login | ✅ pass |
| test_4_negative_login.py | tests wrong credentials | ✅ pass |
| test_5_form_fill.py | fills basic form fields | ✅ pass |
| test_6_form_fill_complete.py | fills complete form with dropdowns | ✅ pass |
| test_7_multiple_assertions.py | multiple checks on login page | ✅ pass |
| test_8_explicit_wait.py | smart waiting with webdriverwait | ✅ pass |
| test_9_xpath_practice.py | 5 xpath methods to find elements | ✅ pass |
| pages/login_page.py | page object model - login page class | ✅ |
| tests/test_10_pom_login.py | pom login test - clean structure | ✅ pass |
| tests/test_11_screenshot_on_failure.py | auto screenshot on fail | ✅ pass |
| tests/test_12_alerts.py | handling alerts and popups | ✅ pass |

## things i figured out

- google blocks selenium (bot detection)
  so switched to duckduckgo
- time.sleep() works for practice but
  explicit wait is better for real projects
- screenshots save automatically as proof
- xpath works when id and name dont work
- normalize-space() in xpath fixes
  whitespace issues with button text
- try/except catches failures and
  saves screenshot automatically
- page object model keeps test code
  clean and easy to maintain
- alert handling needs EC.alert_is_present()
  before reading alert text

## tools used

- python 3.13
- selenium 4
- webdriver manager
- pycharm
- chrome browser

## practice sites

- the-internet.herokuapp.com
- demoqa.com
- duckduckgo.com

## concepts learned

- opening and controlling chrome browser
- finding elements — by.id, by.name,
  by.classname, by.xpath
- explicit wait vs time.sleep()
- page object model (pom)
- try/except for failure handling
- screenshot capture as test evidence
- alert and popup handling

## next steps

- pytest framework
- test reports
- data driven testing
