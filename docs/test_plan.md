# SauceDemo Test Plan

I tested the SauceDemo site by just using it like a normal user and trying different things to see what breaks.

---

## What I checked

I mainly went through the basic flow:

* login and logout
* products page
* sorting options
* adding items to cart
* checkout
* clicking on product pages
* refreshing and using back button

Also used different users to see different behavior.

---

## Users I used

* `standard_user` → normal flow
* `locked_out_user` → login error
* `problem_user` → to find bugs
* `performance_glitch_user` → slow loading

Password was same for all:
`secret_sauce`

---

## How I tested

First I logged in using `standard_user` and checked everything step by step:

* login works
* products load
* sorting works
* add to cart works
* checkout works
* logout works

After that I switched to `problem_user` and just started clicking around more randomly.

That’s where most of the bugs showed up.

Then I used `performance_glitch_user` just to see if things load slowly or break.

---

## Things I tried

### Login

* login with correct details
* login with empty fields
* wrong password
* locked user

---

### After login

* refresh page
* logout
* press back after logout
* try opening inventory after logout

---

### Products page

* check all products visible
* check images
* check names and prices
* click products

---

### Sorting

* tried A-Z
* tried Z-A
* tried price sorting

Also checked if anything actually changes on screen.

---

### Cart

* add items
* remove items
* check cart badge
* open cart and verify items

---

### Checkout

* fill first name
* fill last name
* fill zip code
* continue checkout

---

### Extra testing (problem_user)

This is where I found most issues:

* wrong images
* add to cart not working
* wrong product page opening
* sorting not changing anything
* checkout field issue

---

### Performance check

With `performance_glitch_user`:

* pages were slower
* navigation delay
* back button delay

---

## What looked risky

While testing, these parts looked most broken:

* product images
* add to cart
* checkout form
* product navigation
* sorting
* session behavior

---

## When I stopped

I stopped after:

* main flow was tested
* bugs were found
* everything important was covered

---

## Final output

* test plan
* bug report
* screenshots
* Selenium tests
* Loom videos
