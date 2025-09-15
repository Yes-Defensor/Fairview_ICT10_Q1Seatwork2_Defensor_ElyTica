from js import document

# 1. Restaurant name (string)
restaurant_name = "Shelf Discovery"  # str

# 2. Owner name (string)
owner_name = "Ely Defensor"  # str

# 3. Year established (integer)
year_established = 2025  # int

# 4. Popular item price (float)
popular_item_price = 80.00  # float

# 5. Delivery availability (boolean)
has_delivery = True  # bool

# 6. Product names (list of strings)
product_names = ["Spaghetti Carbonara", "Garlic Bread", "Caesar Salad"]  # list[str]

# 7. Business hours (string)
business_hours = "Open: 11:00 AM - 10:00 PM"  # str

# 8. Menu prices (list of tuples)
menu_prices = [
    ("Spaghetti Carbonara", 30.00),
    ("Garlic Bread", 10.00),
    ("Caesar Salad", 20.00),
    ("Iced Tea", 10.00),
    ("Sparkling Water", 20.00),
    ("Classic Burger", 20.00),
    ("Fries", 10.00),
    ("Vanilla Milkshake", 30.00),
    ("Grilled Chicken", 80.00),
    ("Mango Smoothie", 30.00)
]  # list[tuple[str, float]]

# 9. Common allergens (list of strings)
common_allergens = ["Peanuts", "Dairy", "Gluten"]  # list[str]

# 10. Tax rate (float)
tax_rate = 0.08  # float

# Display basic info
document.getElementById("restaurantName").innerText = restaurant_name
document.getElementById("ownerName").innerText = f"Owner: {owner_name}"
document.getElementById("yearEstablished").innerText = f"Established: {year_established}"
document.getElementById("popularItemPrice").innerText = f"₱{popular_item_price:.2f}"
document.getElementById("hasDelivery").innerText = "Yes" if has_delivery else "No"
document.getElementById("businessHours").innerText = business_hours

# Display allergens list
allergen_html = "".join(f"<li>{a}</li>" for a in common_allergens)
document.getElementById("allergensList").innerHTML = allergen_html

# Display menu table
table_html = """
<table class='table table-bordered'>
    <thead class='table-primary'>
        <tr><th>Product</th><th>Price (₱)</th></tr>
    </thead>
    <tbody>
"""
for item, price in menu_prices:
    table_html += f"<tr><td>{item}</td><td>₱{price:.2f}</td></tr>"
table_html += "</tbody></table>"

document.getElementById("menuTable").innerHTML = table_html
