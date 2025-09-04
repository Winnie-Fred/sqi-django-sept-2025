# Django Template Language (DTL) Assignment – Library System

In a new project in a folder called `library_dashboard`, create a view called `dashboard` that passes this context into a template called `dtl/dashboard.html`:

```python
    context = {
        "librarian": "Kemi Adebayo",
        "books": [
            {
                "title": "Things Fall Apart",
                "author": "Chinua Achebe",
                "isbn": "978-0-385-47454-2",
                "category": "Literature",
                "available_copies": 3,
                "total_copies": 5,
                "publication_year": 1958,
                "is_featured": True,
                "price": 2500.00
            },
            {
                "title": "Purple Hibiscus",
                "author": "Chimamanda Ngozi Adichie",
                "isbn": "978-1-4000-7694-4",
                "category": "Literature",
                "available_copies": 0,
                "total_copies": 2,
                "publication_year": 2003,
                "is_featured": False,
                "price": 3200.00
            },
            {
                "title": "Half of a Yellow Sun",
                "author": "Chimamanda Ngozi Adichie",
                "isbn": "978-1-4000-4418-9",
                "category": "Historical Fiction",
                "available_copies": 1,
                "total_copies": 3,
                "publication_year": 2006,
                "is_featured": True,
                "price": 3800.00
            },
            {
                "title": "The Beautiful Ones Are Not Yet Born",
                "author": "Ayi Kwei Armah",
                "isbn": "978-0-435-90516-8",
                "category": "Literature",
                "available_copies": 2,
                "total_copies": 2,
                "publication_year": 1968,
                "is_featured": False,
                "price": 2800.00
            }
        ],
        "library_stats": {
            "total_members": 1247,
            "books_borrowed_today": 23,
            "overdue_books": 8,
            "new_arrivals_this_month": 15
        },
        "current_date": timezone.now(),
        "library_name": "Ibadan Central Library",
        "is_weekend": timezone.now().weekday() >= 5,
        "featured_message": "Discover African Literature Classics!"
    }
```

## Your Task

Create a Django template (`dtl/dashboard.html`) that displays this library information using DTL features. Your template should include:

### Required Features:

1. **Basic Variable Display:**
   - Show the librarian's name and library name
   - Display the current date and featured message

2. **Conditional Logic:**
   - Display different greetings based on whether it's a weekend or weekday
   - Show availability status for each book (Available/Out of Stock)
   - Highlight featured books with "FEATURED"

3. **Loop Through Data:**
   - List all books with their details
   - Display library statistics

4. **Filters:**
   - Format the book prices as currency (₦)
   - Format the current date nicely like in the sample output
   - Convert book titles to uppercase for headers


Starter Template (dtl/dashboard.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Library Dashboard</title>
</head>
<body>
    <!-- 1. Basic Variables -->
    <h1><!-- TODO: Show library name --></h1>
    <p>Librarian: <!-- TODO: Show librarian's name --></p>
    <p>Today's Date: <!-- TODO: Format and display current_date --></p>
    <h3><!-- TODO: Show featured_message --></h3>

    <!-- 2. Conditional Greeting -->
    <p><!-- TODO: If is_weekend is true, show weekend greeting, else show weekday greeting --></p>

    <!-- 3. Books List -->
    <h2>Books Collection</h2>
    <ul>
        <!-- TODO: Loop through books -->
        <li>
            <!-- TODO: Show book title in uppercase -->
            <!-- TODO: Show author, publication year, and category -->
            <!-- TODO: Show ISBN -->
            <!-- TODO: Show price formatted as currency -->
            <!-- TODO: If available_copies > 0, show availability, else "Out of Stock" -->
            <!-- TODO: If book is_featured, show "FEATURED" -->
        </li>
    </ul>

    <!-- 4. Library Statistics -->
    <h2>Library Statistics</h2>
    <ul>
        <!-- TODO: Show total_members -->
        <!-- TODO: Show books_borrowed_today -->
        <!-- TODO: Show overdue_books -->
        <!-- TODO: Show new_arrivals_this_month -->
    </ul>
</body>
</html>
```


## Sample Expected Output
```
Ibadan Central Library
Librarian: Kemi Adebayo
Today's Date: Thursday, 04 September 2025
Discover African Literature Classics!

Welcome to a new weekday at the library!

Books Collection
--------------------------------------------------
THINGS FALL APART by Chinua Achebe (1958)
ISBN: 978-0-385-47454-2
Category: Literature
Price: ₦2500.0
Available (3 copies)
FEATURED
--------------------------------------------------
PURPLE HIBISCUS by Chimamanda Ngozi Adichie (2003)
ISBN: 978-1-4000-7694-4
Category: Literature
Price: ₦3200.0
Out of Stock
--------------------------------------------------
HALF OF A YELLOW SUN by Chimamanda Ngozi Adichie (2006)
ISBN: 978-1-4000-4418-9
Category: Historical Fiction
Price: ₦3800.0
Available (1 copies)
FEATURED
--------------------------------------------------
THE BEAUTIFUL ONES ARE NOT YET BORN by Ayi Kwei Armah (1968)
ISBN: 978-0-435-90516-8
Category: Literature
Price: ₦2800.0
Available (2 copies)

Library Statistics
- Total Members: 1247
- Books Borrowed Today: 23
- Overdue Books: 8
- New Arrivals This Month: 15
```