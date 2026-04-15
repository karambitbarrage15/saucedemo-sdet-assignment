# SauceDemo Test Plan

## Basic Info

**Name:** Aditya Chaturvedi
**Role:** SDET
**Website Tested:** SauceDemo
**URL:** https://www.saucedemo.com

---

## Objective

The purpose of this testing is to validate the main user journey of the SauceDemo website.

I mainly focused on the most important e-commerce workflows:

* login and logout
* inventory page
* product sorting
* cart actions
* checkout form
* session handling
* product navigation
* problem_user specific bug scenarios
* slow response behavior using performance_glitch_user

The main goal is to ensure that a user can log in, browse products, add items to the cart, and complete checkout without issues.

---

## Scope

### Included

* Login and logout
* Invalid login validation
* Locked user validation
* Inventory page
* Product sorting
* Product detail navigation
* Add to Cart / Remove from Cart
* Cart badge updates
* Checkout flow
* Form field validation
* Session checks
* Browser back behavior
* Performance sanity checks

### Not Included

* payment integration
* backend API testing
* database validation
* load testing
* security testing

---

## Testing Types Used

* Functional testing
* Negative testing
* Exploratory testing
* UI validation
* Session testing
* Browser navigation testing
* Basic performance sanity

---

## Environment Used

* Browser: Chrome
* OS: Windows
* Device: Laptop
* Internet: normal Wi-Fi

---

## Test Accounts Used

* `standard_user`
* `locked_out_user`
* `problem_user`
* `performance_glitch_user`

Password used for all:
`secret_sauce`

---
## All Test Scenarios

### Login Scenarios

* Verify login with valid credentials
* Verify login with blank username
* Verify login with wrong password
* Verify locked_out_user cannot log in
* Verify error message visibility on failed login

### Session Scenarios

* Verify session remains active after browser refresh
* Verify logout redirects user to login page
* Verify browser back after logout does not expose inventory page
* Verify direct access to inventory page after logout is blocked

### Inventory Scenarios

* Verify all products are visible after login
* Verify each product image matches the correct item
* Verify product names and prices are displayed
* Verify product detail page opens correctly
* Verify browser back from product detail returns to inventory

### Sorting Scenarios

* Verify Name A-Z sorting
* Verify Name Z-A sorting
* Verify Price low to high sorting
* Verify Price high to low sorting

### Cart Scenarios

* Verify Add to Cart works for every product
* Verify Remove button works correctly
* Verify cart badge updates on add/remove
* Verify correct product is visible in cart
* Verify multiple items can be added

### Checkout Scenarios

* Verify checkout form accepts valid input
* Verify first name field works correctly
* Verify last name field works correctly
* Verify zip code field accepts input
* Verify checkout overview shows correct selected items
* Verify checkout completion flow works

### Exploratory / Problem User Scenarios

* Verify product image mismatch issues
* Verify product title opens correct item
* Verify product click does not log out user
* Verify all Add to Cart buttons respond correctly
* Verify checkout form fields behave correctly

### Performance Scenarios

* Verify inventory loads with acceptable delay for performance_glitch_user
* Verify product detail navigation delay
* Verify back navigation from detail page


## Testing Approach

I first tested the normal user flow using `standard_user` to validate login, session behavior, sorting, and logout.

After the basic flow was stable, I moved to `problem_user` for deeper exploratory testing. Most bugs were found in:

* product image mapping
* Add to Cart functionality
* checkout form fields
* wrong product detail navigation
* unexpected logout on product click

I also used `performance_glitch_user` for a quick sanity check to observe slower navigation and delayed back transitions.

---

## Risk Areas I Focused On

The areas that appeared most risky during testing were:

* product image mapping
* checkout form input fields
* Add to Cart button behavior
* product title navigation
* session stability
* browser back flow
* performance delays

---

## Exit Criteria

Testing is considered complete after:

* all major user flows are covered
* at least 5 bugs are documented
* critical risky areas are validated
* main flows are ready for automation

---

## Final Deliverables

* `test_plan.md`
* `bug_report.md`
* screenshots
* Selenium automation scripts
* `README.md`
* Loom video links
