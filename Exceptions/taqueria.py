def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    print("Enter items one per line. Press Ctrl-D (Ctrl-Z on Windows) to end input.")

    try:
        while True:
            item = input().strip().title()
            if item in menu:
                total_cost += menu[item]
                print(f"${total_cost:.2f}")
            else:
                # Ignore items that are not on the menu
                pass
    except EOFError:
        pass

if __name__ == "__main__":
    main()
