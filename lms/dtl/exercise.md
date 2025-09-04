# Django Template Language (DTL) Exercise – Shop Cart

You are given a view called `shopping_cart` that passes this context into a template called `dtl/cart.html`:

```python
from django.shortcuts import render
from django.utils import timezone

def shopping_cart(request):
    context = {
        "customer": "Chinedu",
        "cart_items": [
            {"name": "Laptop", "price": 250000, "quantity": 1},
            {"name": "Headphones", "price": 15000, "quantity": 2},
            {"name": "USB Cable", "price": 2000, "quantity": 3},
        ],
        "has_discount": True,
        "store": {
            "name": "Tech World",
            "city": "Abuja",
        },
        "today": timezone.now(),
    }
    return render(request, "dtl/cart.html", context)
```

Tasks

Greeting

Show the customer’s name in uppercase.

Example: Hello, CHINEDU!

Loop (Cart Items)

Loop through all cart_items and display:

Item name

Price

Quantity

Display them in a table.

Conditional

If has_discount is True, show:
You have a discount available!

Otherwise show:
No discounts at this time.

Dictionary Lookup

Show the store name and city.

Example: Shopping at Tech World, Abuja.

Filters

Show today’s date in this format: Thursday, 04 September 2025.

Show how many items are in the cart (using length filter).

Starter Template (cart.html)
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Shopping Cart</title>
</head>
<body>
    <!-- 1. Greeting -->
    <h2><!-- TODO: Greet customer with uppercase name --></h2>

    <!-- 2. Cart Items -->
    <h3>Your Cart</h3>
    <table border="1" cellpadding="5">
        <thead>
            <tr>
                <th>Item</th>
                <th>Price</th>
                <th>Quantity</th>
            </tr>
        </thead>
        <tbody>
            <!-- TODO: Loop through cart_items -->
        </tbody>
    </table>

    <!-- 3. Conditional -->
    <p><!-- TODO: Show discount message if has_discount is true --></p>

    <!-- 4. Store Info -->
    <p><!-- TODO: Show store name and city --></p>

    <!-- 5. Filters -->
    <p>Today is: <!-- TODO: Show formatted date --></p>
    <p>Total different items in cart: <!-- TODO: Show length of cart_items --></p>
</body>
</html>
```

## Sample Expected Output

```
Hello, CHINEDU!

Your Cart:
+-------------+---------+----------+
| Item        | Price   | Quantity |
+-------------+---------+----------+
| Laptop      | 250000  |    1     |
| Headphones  | 15000   |    2     |
| USB Cable   | 2000    |    3     |
+-------------+---------+----------+

You have a discount available!

Shopping at Tech World, Abuja.

Today is: Thursday, 04 September 2025
Total different items in cart: 3
```