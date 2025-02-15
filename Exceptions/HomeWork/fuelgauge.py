while True:
    try:
        xx = input("Enter: ")
        x1, x3 = map(int, xx.split('/'))  # Split input and convert to integers
        if x1 > x3 or x3 == 0:
            raise ValueError
        percentage = round((x1 * 100) / x3)
        if 1 < percentage < 99:
            print(f"{percentage}%")
        elif 99 <= percentage <= 100:
            print("F")
        elif 0 <= percentage <= 1:
            print("E")
        break
    except (ValueError, ZeroDivisionError):
        pass
