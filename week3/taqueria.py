
def felips_taqueria():
    taqueria_menu={
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    item_p=0
    while True:
        item = input("Item :").title()
        try:
            if item in taqueria_menu:
                item_p += taqueria_menu[item]
                print(f"Total:${item_p:.2f}")
        except EOFError :
            break


felips_taqueria()
