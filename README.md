# SauceDemo SDET Assignment

## Overview

This repository contains my submission for the SauceDemo QA/SDET assignment.

The assignment includes:

* Test plan
* Manual bug report
* Selenium automation scripts
* Screenshots
* Exploratory notes
* Loom demo links

---

## Folder Structure

* `docs/` → test plan and bug report
* `screenshots/` → bug and automation screenshots
* `tests/` → Selenium PyTest automation scripts
* `notes/` → exploratory testing observations

---

## Automation Flows Covered

The following critical flows were automated using Selenium WebDriver with PyTest:

1. Valid login with `standard_user`
2. Locked-out user validation with `locked_out_user`
3. Add item to cart and complete checkout flow

---

## Tools Used

* Python 3.12
* Selenium WebDriver
* PyTest
* Google Chrome
* VS Code
* Loom (for demo videos)

---

## How to Run

Install dependencies:

```bash
pip install selenium pytest
```

Run all tests:

```bash
pytest tests -v
```

Run individual tests:

```bash
pytest tests/test_login.py -v
pytest tests/test_locked_user.py -v
pytest tests/test_cart_checkout.py -v
```

---

## Test Accounts Used

* `standard_user`
* `locked_out_user`
* `problem_user`
* `performance_glitch_user`

Password used:
`secret_sauce`

---

## Notes

During automation execution, direct access to SauceDemo was blocked on the college Wi-Fi network in normal browser sessions.

To ensure stable Selenium execution, tests were run using a personal mobile hotspot.

All three required automation flows were executed successfully.

---

## Deliverables Included

* `docs/test_plan.md`
* `docs/bug_report.md`
* Selenium test scripts
* screenshots
* exploratory notes
* Loom video links
