def main():
    grocery_list = {}

    print("Enter items one per line. Press Ctrl-D (Ctrl-Z on Windows) to end input.")

    try:
        while True:
            item = input().strip().lower()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
    except EOFError:
        pass

    sorted_items = sorted(grocery_list.items())

    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
