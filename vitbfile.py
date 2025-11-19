#!/usr/bin/env python3

# -----------------------------
# ONLINE FOOD ORDERING SYSTEM
# -----------------------------

# VEG MENU 
veg_menu = {
    "Snacks": {
        "Samosa": 10,
        "Pizza": 120,
        "Burger": 60,
        "Pasta": 100
    },
    "Meal": {
        "Veg Thali": 120,
        "Paneer Butter Masala": 150,
        "Veg Biryani": 140,
        "Roti (2)": 20
    },
    "Beverages": {
        "Lassi": 40,
        "Cold Coffee": 70,
        "Tea": 15,
        "Juice": 50
    },
    "Desserts": {
        "Gulab Jamun": 30,
        "Ice Cream": 50,
        "Rasmalai": 60,
        "Kheer": 40
    }
}

# NON-VEG MENU 
nonveg_menu = {
    "Snacks": {
        "Chicken Pakoda": 80,
        "Egg Roll": 50,
        "Chicken Sandwich": 90,
        "Chicken Momos": 100
    },
    "Meal": {
        "Chicken Thali": 180,
        "Butter Chicken": 200,
        "Egg Curry": 120,
        "Chicken Biryani": 160
    },
    "Beverages": {
        "Lassi": 40,
        "Cold Coffee": 70,
        "Tea": 15,
        "Juice": 50
    },
    "Desserts": {
        "Gulab Jamun": 30,
        "Ice Cream": 50,
        "Rasmalai": 60,
        "Kheer": 40
    }
}

# -------------------------------
# ORDER SYSTEM
# -------------------------------
order_list = []
total_bill = 0

print("----- Welcome to Online Food Ordering System -----")

# USER DETAILS
name = input("Enter your Name: ")
address = input("Enter your Address: ")
mobile = input("Enter your Mobile Number: ")

while True:
    print("\nChoose Food Type:")
    print("1. Veg")
    print("2. Non-Veg")
    choice = int(input("Enter choice: "))

    if choice == 1:
        menu = veg_menu
    else:
        menu = nonveg_menu

    print("\nSelect Category:")
    print("1. Snacks")
    print("2. Meal")
    print("3. Beverages")
    print("4. Desserts")

    cat_choice = int(input("Enter choice: "))

    categories = ["Snacks", "Meal", "Beverages", "Desserts"]
    selected_category = categories[cat_choice - 1]

    print(f"\n--- {selected_category} Menu ---")

    items = list(menu[selected_category].keys())
    prices = list(menu[selected_category].values())

    for i in range(len(items)):
        print(f"{i+1}. {items[i]} - ₹{prices[i]}")

    item_choice = int(input("Choose an item: "))
    selected_item = items[item_choice - 1]
    item_price = prices[item_choice - 1]

    order_list.append(selected_item)
    total_bill += item_price

    print(f"{selected_item} added to cart!")

    more = input("Do you want to order more? (yes/no): ").lower()
    if more != "yes":
        break

# -------------------------------
# FINAL SUMMARY
# -------------------------------
print("\n------------------------------")
print("ORDER SUMMARY")
print("------------------------------")
print("Name:", name)
print("Address:", address)
print("Mobile:", mobile)
print("\nItems Ordered:")

for item in order_list:
    print("•", item)

print("\nTotal Bill: ₹", total_bill)
print("\nYour order has been placed successfully!")
print("------------------------------")























    


   
