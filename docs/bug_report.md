# SauceDemo Bug Report

I tested the website using `problem_user` and just went through the normal user flow like checking products, adding to cart and doing checkout. While doing that I found these issues.

---

## Bug 1 - Same image on all products

When I opened the products page, the first thing I noticed was that every product had the same dog image.

Like backpack, bike light, jacket, everything was showing that same image.

Steps:

1. Login with `problem_user`
2. Open products page
3. Look at product images

What I saw:
All products have same image.

What should happen:
Each product should show its own image.

---

## Bug 2 - Add to cart not working for some items

I tried clicking add to cart for all products.

For Bolt T-Shirt, Fleece Jacket and Test.allTheThings shirt, the button just didn’t work.

I clicked multiple times but nothing happened.

Steps:

1. Login with `problem_user`
2. Click Add to cart on those products

What I saw:
Item is not added at all.

What should happen:
Item should get added to cart.

---

## Bug 3 - Last name field issue in checkout

During checkout I filled the first name and then tried to enter last name.

But the last name field was behaving weird.

It was not taking input properly and it looked like it was affecting the first name field.

Steps:

1. Add any item
2. Go to checkout
3. Enter first name
4. Try entering last name

What I saw:
Last name stays empty and I get error.

What should happen:
Last name should work normally.

---

## Bug 4 - Wrong product page opens

I clicked on product titles to check their pages.

Some of them were opening different product pages.

Like clicking backpack sometimes opened fleece jacket page.

Steps:

1. Login with `problem_user`
2. Click on product titles

What I saw:
Wrong product page opens.

What should happen:
Correct product page should open.

---

## Bug 5 - Sorting not working

I tried using all sorting options like A-Z, Z-A and price options.

But nothing actually changed.

The order of products stayed exactly same.

Steps:

1. Login with `problem_user`
2. Click sort dropdown
3. Select any option

What I saw:
No change in product order.

What should happen:
Products should reorder based on selection.
