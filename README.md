# selenium-qa-practice

i started learning selenium after finishing 
manual testing on HighScores.ai and SecondBrainLabs.
these are my scripts from week 3 onwards.
still learning, still making mistakes, still going.

## how it's organized

```
selenium-qa-practice/
├── conftest.py
├── pages/
│   ├── __init__.py
│   └── login_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_10_pom_login.py
│   ├── test_11_screenshot_on_failure.py
│   ├── test_12_alerts.py
│   ├── test_13_pytest_basics.py
│   ├── test_14_fixtures.py
│   ├── test_15_data_driven.py
│   └── test_16_full_suite.py
├── test_1_open_browser.py
├── test_2_google_search.py
├── test_3_login.py
├── test_4_negative_login.py
├── test_5_form_fill.py
├── test_6_form_fill_complete.py
├── test_7_multiple_assertions.py
├── test_8_explicit_wait.py
└── test_9_xpath_practice.py
```

## what each script does

| script | what it does | status |
|--------|-------------|--------|
| test_1_open_browser.py | first script — just opens browser and reads title | ✅ |
| test_2_google_search.py | search automation — had to switch to duckduckgo (google blocked me) | ✅ |
| test_3_login.py | login form automation — fill and submit | ✅ |
| test_4_negative_login.py | wrong credentials test — checks error message | ✅ |
| test_5_form_fill.py | fills basic form fields | ✅ |
| test_6_form_fill_complete.py | complete form — dropdowns, checkboxes, scroll | ✅ |
| test_7_multiple_assertions.py | checks multiple things on login page | ✅ |
| test_8_explicit_wait.py | replaced time.sleep with proper webdriverwait | ✅ |
| test_9_xpath_practice.py | 5 different ways to find elements using xpath | ✅ |
| pages/login_page.py | page object model — all login page stuff in one place | ✅ |
| tests/test_10_pom_login.py | login test using pom — much cleaner code | ✅ |
| tests/test_11_screenshot_on_failure.py | saves screenshot when test fails | ✅ |
| tests/test_12_alerts.py | handles simple, confirm, and prompt alerts | ✅ |
| tests/test_13_pytest_basics.py | first proper pytest tests with assert | ✅ |
| tests/test_14_fixtures.py | fixtures — chrome opens once for all tests | ✅ |
| tests/test_15_data_driven.py | one test runs with 4 different login combinations | ✅ |
| tests/test_16_full_suite.py | 7 login tests in a class — runs together | ✅ |

## run all 17 tests at once

```
pytest tests/test_13_pytest_basics.py tests/test_14_fixtures.py tests/test_15_data_driven.py tests/test_16_full_suite.py -v --html=reports/report_complete.html
```

## honest things i learned the hard way

- google blocks selenium completely
  switched to duckduckgo — still works fine

- was using time.sleep(3) everywhere
  found out that's lazy — explicit wait is
  the proper way and also faster

- normalize-space() in xpath saved me
  when button text had hidden whitespace
  and nothing else was working

- forgot .clear() in data driven test
  fields were stacking text on top of each other
  took me a while to figure that out 😅

- page object model felt confusing at first
  once it clicked i went back and looked at
  my old scripts thinking "why did i write it like that"

- was reading page title before page loaded
  kept getting empty string
  had to wait for title first

- try/except is how you catch failures properly
  without it the script just crashes with no proof

- conftest.py shares fixtures across files
  without it you repeat the same setup everywhere

## tools

- python 3.13
- selenium 4
- webdriver manager
- pytest 9.0.2
- pytest-html
- pycharm

## practice sites used

- the-internet.herokuapp.com — login tests
- demoqa.com — form fill tests
- duckduckgo.com — search test

## where i started vs where i am now

week 3 start:
just opened a browser and printed the title.
felt like magic at the time.

week 5 end:
17 tests running with one command,
html report generated automatically,
page object model, fixtures, data driven testing.

still a lot to learn but the progress feels real.

## next

- sql for qa (week 6)
- full portfolio cleanup (week 7)
- apply everywhere (week 8)
