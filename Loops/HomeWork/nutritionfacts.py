fruit_calories={
    "apple":130,
    "avocado":50,
    "banana":110,
    "cantaloupe":50,
    "grapefruit":60,
    "grapes":90,
    "honeydewmelon":50,
    "kiwifruit":90,
    "lemon":15,
    "nectarine":60,
    "lime":20,
    "orange":80,
    "peach":60,
    "pear":100,
    "pineapple":50,
    "plums":70,
    "strawberries":50,
    "sweetcherries":100,
    "tangerine":50,
    "watermelon":80,

}
def main():
    print("item :",end="")
    xx=input()
    xx=xx.lower()

    if xx in fruit_calories:
        print(f"Calories: {fruit_calories[xx]}")

    else:
        print("Invalid")

main()