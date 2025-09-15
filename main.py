from pyscript import display  # For the code to work as display (string)

#  Basic Info about the restaurant
display("Restaurant Name: Shelf Discovery", target="restaurantName")  # For the name of restaurant (string)

display("Owner: Ely Defensor", target="ownerName")  # Displaying the owner's name (text) (string)
display("Established: 2005", target="yearEstablished")  # Showing the year it was founded (string)

display("Popular Item Price: ₱90.00", target="popularItemPrice")  # Price of popular item (string)
display("Delivery Available: Yes", target="hasDelivery")  # Telling users if delivery is offered (string)
display("Business Hours: Open: 11:00 AM - 10:00 PM", target="businessHours")  # Showing when the restaurant is open (string)
display("Tax Rate: 8%", target="taxRate")  # Displaying the tax rate (string)

# Product Names #to display menu with items via display and target
display("Product Names:", target="productNames")  # string
display("Spaghetti Carbonara", target="productNames")  # string
display("Garlic Bread", target="productNames")  # string
display("Caesar Salad", target="productNames")  # string

#  Common Allergens #to dislay the menu with items via display and target
display("Common Allergens:", target="allergensList")  # string
display("Peanuts", target="allergensList")  # string
display("Gluten", target="allergensList")  # string

#  Menu Items with Prices #to display the menu with items via display and target
display("Menu Items:", target="menuItems")  # string
display("Spaghetti Carbonara: ₱90.00", target="menuItems")  # string
display("Garlic Bread: ₱40.00", target="menuItems")  # string
display("Caesar Salad: ₱90.00", target="menuItems")  # string
display("Iced Tea: ₱90.00", target="menuItems")  # string
display("Sparkling Water: ₱90.00", target="menuItems")  # string

