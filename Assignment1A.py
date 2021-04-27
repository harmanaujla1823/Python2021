menu = {
    "dal": 150,
    "paneer": 300,
    "parantha": 50,
    "tea": 20,
    "donut": 80
}

# VIEW: OUTPUT
print("Please Select Items from Below Menu:")
print(menu)

# price = menu["donut"]
# print(price) # 80

# MODEL:
cart = [] # empty list
choice = "yes"

# VIEW: INPUT
# item1 = input("Enter Food Item1: ")
# cart.append(menu[item1])
#
# item2 = input("Enter Food Item2: ")
# cart.append(menu[item2])
#
# print("Your Pricing for the Items: ")
# print(cart)


# CONTROLLER
while choice == "yes":
    item = input("Enter Food Item: ")
    cart.append(menu[item])

    choice = input("Would you like to add more items(yes/no)")

print("Your Cart[{}]:".format(len(cart)))
print(cart)

total_amount = sum(cart)
print("Total:", total_amount)

promo_code = input("You may Enter Promo Code if you have")

if promo_code == "CRAVINGS":
    print("PROMO CODE APPLIED AND YOU GOT 20%OFF")
    print("Congratulations! You saved ", (0.20 * total_amount), "rupees")
    total_amount = total_amount - (0.20 * total_amount)


print("Amount After Promo Code:", total_amount,"rupees")
print("18% GST APPLIED--->",(0.20*total_amount),"rupees")


total_amount = total_amount + (0.18*total_amount)
print("Final Amount after Promo Code with Taxes is:", total_amount,"rupees")