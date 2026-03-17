# selenium-qa-practice

practicing selenium webdriver with python.
started this after finishing manual testing 
projects on HighScores.ai and SecondBrainLabs.
these are my scripts as i learn automation.

## scripts

| script | what it does | status |
|--------|-------------|--------|
| test_1_open_browser.py | opens browser, reads title | ✅ pass |
| test_2_google_search.py | automates search | ✅ pass |
| test_3_login.py | automates valid login | ✅ pass |
| test_4_negative_login.py | tests wrong credentials | ✅ pass |
| test_5_form_fill.py | fills basic form fields | ✅ pass |
| test_6_form_fill_complete.py | fills complete form with dropdowns | ✅ pass |
| test_7_multiple_assertions.py | multiple checks on login page | ✅ pass |

## things i figured out during practice

- google blocks selenium (bot detection)
  so switched to duckduckgo
- time.sleep() works for practice but
  explicit wait is better for real projects
- screenshots save automatically as proof
- xpath works when id and name dont work
- negative testing is as important as
  positive testing

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

## what i learned

- opening and controlling chrome browser
- finding elements using by.id, by.name,
  by.classname and by.xpath
- typing text with send_keys()
- clicking buttons with .click()
- assertions - verifying actual vs expected
- negative testing with wrong credentials
- taking screenshots as test evidence
- scrolling with execute_script()
- multiple assertions in one test

## next steps

- explicit wait instead of time.sleep()
- page object model
- pytest framework
