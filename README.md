# SauceDemo SDET Assignment

This repo contains my work for the SauceDemo testing assignment.

---

## What I did

I tested the SauceDemo site by just using it like a normal user and trying different things to see what works and what breaks.

I mainly checked:

* login and logout
* products page
* sorting
* add to cart
* checkout
* session behavior

I also used `problem_user` to find bugs and `performance_glitch_user` to check slow loading.

---

## What is included

* test plan
* bug report
* Selenium test scripts
* screenshots
* Loom videos

---

## Automation

I wrote 3 Selenium tests:

* login with valid user
* locked user login check
* add to cart and complete checkout

All tests are passing.

---

## How to run

Install dependencies:

```bash
pip install selenium pytest
```

Run tests:

```bash
pytest tests -v
```

---

## Test users

* standard_user
* locked_out_user
* problem_user
* performance_glitch_user

Password:
`secret_sauce`

---

## Note

While running automation, the site was not opening properly on my college Wi-Fi, so I used mobile hotspot to run the tests.

---

That’s it.
