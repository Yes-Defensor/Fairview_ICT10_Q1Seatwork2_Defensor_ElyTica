from pyscript import display  # Importing the display function from PyScript to show content on a webpage

# Basic Info
display("Restaurant Name: Shelf Discovery", target="restaurantName")  # string: displays restaurant name
display("Owner: Ely Defensor", target="ownerName")  # string: displays owner's name
display("Established: 2005", target="yearEstablished")  # string (could be int): shows year of establishment
display("Popular Item Price: ₱90.00", target="popularItemPrice")  # string (currency): shows price of popular item
display("Delivery Available: Yes", target="hasDelivery")  # string (boolean-like): indicates delivery availability
display("Business Hours: Open: 11:00 AM - 10:00 PM", target="businessHours")  # string: shows operating hours
display("Tax Rate: 8%", target="taxRate")  # string (percentage): shows applicable tax rate

# Product Names
display("Product Names:", target="productNames")  # string: section header for product names
display("Spaghetti Carbonara", target="productNames")  # string: product name
display("Garlic Bread", target="productNames")  # string: product name
display("Caesar Salad", target="productNames")  # string: product name

# Common Allergens
display("Common Allergens:", target="allergensList")  # string: section header for allergens
display("Peanuts", target="allergensList")  # string: allergen name
display("Gluten", target="allergensList")  # string: allergen name

# Menu Items
display("Menu Items:", target="menuItems")  # string: section header for menu items
display("Spaghetti Carbonara: ₱90.00", target="menuItems")  # string: item name and price
display("Garlic Bread: ₱40.00", target="menuItems")  # string: item name and price
display("Caesar Salad: ₱90.00", target="menuItems")  # string: item name and price
display("Iced Tea: ₱90.00", target="menuItems")  # string: item name and price
display("Sparkling Water: ₱90.00", target="menuItems")  # string: item name and price
