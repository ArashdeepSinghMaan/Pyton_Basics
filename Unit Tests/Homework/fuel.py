def main():
    fraction = input("Enter: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except ValueError:
        print("ValueError: Invalid fraction")
    except ZeroDivisionError:
        print("ZeroDivisionError: Denominator cannot be zero")

def convert(fraction):
    try:
        numerator, denominator = map(int, fraction.split('/'))
        if denominator == 0:
            raise ZeroDivisionError
        if numerator > denominator:
            raise ValueError
        percentage = int(round((numerator * 100) / denominator))
        return percentage
    except ValueError:
        raise ValueError

def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage}%"
    elif 99 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"
    else:
        return "error"

if __name__ == "__main__":
    main()
