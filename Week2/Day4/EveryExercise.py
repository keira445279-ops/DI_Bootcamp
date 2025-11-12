menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def apply_discount(menu, percent):
    for key, value in menu.items():
        multiplier = (1 - percent / 100)
        new_price = value * multiplier
        menu[key] = round (new_price, 2)
        print (f'Happy Day - The price of a drink wist discount is {new_price} NIS')

apply_discount(menu, 10)
        

        






