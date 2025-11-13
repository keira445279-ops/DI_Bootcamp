menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}
# 3. Discount day:
# Add a function apply_discount(menu_dict, percent) that reduces every price by a percentage.
# Example: apply_discount(menu, 10) makes 10% off happy hour.

def apply_discount(menu, percent):
    for key, value in menu.items():
        multiplier = (1 - percent / 100)
        new_price = value * multiplier
        menu[key] = round (new_price, 2)
        print (f'Happy Day - The price of a {key} with discount is {menu[key]} NIS')

apply_discount(menu, 10)

        

        






