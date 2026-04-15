# SauceDemo Bug Report

## Bug 1 — Same image shown for all products

**Severity:** High
**Module:** Inventory

**Steps to reproduce**

1. Login using `problem_user`
2. Open products page
3. Check product images

**Expected**
Every product should have its own correct image.

**Observed**
All products are showing the same dog image.

**Why this matters**
This can confuse users and they may end up buying the wrong item.

---

## Bug 2 — Add to Cart not working for some products

**Severity:** High
**Module:** Inventory / Cart

**Affected products**

* Sauce Labs Bolt T-Shirt
* Sauce Labs Fleece Jacket
* Test.allTheThings() T-Shirt

**Steps**

1. Login with `problem_user`
2. Click **Add to cart** for the above products

**Expected**
Item should get added and button should change to Remove.

**Observed**
Nothing happens on click.

**Impact**
User cannot add some products to cart.

---

## Bug 3 — Last name field is broken in checkout

**Severity:** Critical
**Module:** Checkout

**Steps**

1. Add any item to cart
2. Go to checkout info page
3. Fill first name
4. Try typing in last name field

**Expected**
Text should appear inside last name field.

**Observed**
Text affects first name field and last name stays empty.

**Impact**
Checkout cannot be completed.

---

## Bug 4 — Wrong product page opens on title click

**Severity:** High
**Module:** Product Navigation

**Steps**

1. Login with `problem_user`
2. Click product titles one by one

**Observed examples**

* Backpack → opens Fleece Jacket
* Bolt T-Shirt → opens Onesie
* Test.allTheThings() → opens Backpack

**Expected**
Clicked product should open its own detail page.

**Impact**
Users may see wrong product details and purchase wrong item.

---

## Bug 5 — Clicking Fleece Jacket logs out the user

**Severity:** Critical
**Module:** Navigation / Session

**Steps**

1. Login with `problem_user`
2. Click **Sauce Labs Fleece Jacket**

**Expected**
Fleece Jacket details page should open.

**Observed**
User gets redirected to login page.

**Impact**
Shopping flow breaks and user session is lost.
