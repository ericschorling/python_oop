menu = {
    "Brunch" : {
        "Steak and Eggs": 16.99, 
        "Three Egg Breakfast": 8.99, 
        "Egg Benedict": 11.99, "Biscuit and Gravy": 7.99, 
        "Chicken Fingers": 10.99, "Chicken Wrap": 8.99, 
        "Steak Salad" : 1.99
    },
    "Drinks": {
        "Soft Drink": 1.99, 
        "Coffee": 1.99, 
        "Orange Juice": 0.99, 
        "Milk": 0.55, 
        "Water": 0.00
    } 
}

menu['Brunch']['Steak Salad'] = 15.99
menu['Specials'] = {
    "Soup of the Day": 8.99,
    "Catch of the Day": 14.99,
    "Chef Special": 15.99
}
menu['Brunch']['Three Egg Breakfast'] = {
    'Without Bacon': 8.99,
    'With Bacon': 9.99,
}

order_1 =['Egg Benedict', "Coffee", 'Biscuit and Gravy', 'Coffee', 'Steak and Eggs', 'Soft Drink']
order_2 = ['Steak Salad', 'Soft Drink', 'Soup of the Day',]
order_total = 0
order_tax = 0.07

def print_it_all(the_menu, the_order):
    order_total = 0
    for items in range(len(the_order)):
        for sections in the_menu:
            if the_order[items] in the_menu[sections]:
                order_total += print_menu(the_menu, the_order[items], sections)
            #else:
                #print("Not an item")
    return order_total

def print_menu(menu_dict, the_order_item, menu_sect):
    item_price = menu_dict[menu_sect][the_order_item]
    print('{:<20}{:>20}{:>6}'.format(the_order_item,'$', f'{(item_price):.2f}'))
    #print(menu_dict[menu_sect][the_order_item])
    return menu_dict[menu_sect][the_order_item]


def order_total_func(order_dict, the_order):
    order_total_value = 0
    for orders in the_order:
        order_total_value += order_dict[orders]
    return order_total_value


def print_tips(order_total, tax_rate):
    print("")
    print('{:>38}{:>2}{:>6}'.format("Price: ","$", f'{(order_total):.2f}'))
    #print('{:<30}{:<40}'.format('Price:', f'$ {(order_total):.2f}' ))
    #print("Taxes: $ %.2f" % (order_total * tax_rate))
    print('{:>38}{:>2}{:>6}'.format("Taxes: ","$", f'{(order_total*tax_rate):.2f}'))
    #print("Total: $ %.2f" % (order_total * (1 + tax_rate)))
    print('{:>38}{:>2}{:>6}'.format("Total: ","$", f'{(order_total*(1+tax_rate)):.2f}'))
    
    print("**Suggested Tip**")
    
    x = 25
    while x >= 15:
        print(f"Tip {x}%:" , end='')
        print('{:>12}{:>6}'.format('$',f'{((x/100)* order_total):.2f}'))
        x -= 5



order_total = print_it_all(menu, order_1)
#print(order_total)
print_tips(order_total, order_tax)
