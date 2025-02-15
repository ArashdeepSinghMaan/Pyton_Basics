import sys
import time
import cowsay

def main():
    option = input("Enter 1 for HH:MM:SS, Enter 2 for MM:SS, Enter 3 for SS: ")
    user_input = input("Enter Time: ")
    hours, minutes, seconds = convert_time(option, user_input)
    total_time = calculate_total_seconds(hours, minutes, seconds)
    countdown(total_time)

def convert_time(option, user_input):
    try:
        if option == "1":
            hours, minutes, seconds = map(int, user_input.split(":"))
        elif option == "2":
            hours = 0
            minutes, seconds = map(int, user_input.split(":"))
        elif option == "3":
            hours = 0
            minutes = 0
            seconds = int(user_input)
        else:
            raise ValueError("Invalid option")
        
        if seconds >= 60:
            minutes += seconds // 60
            seconds = seconds % 60
        
        if minutes >= 60:
            hours += minutes // 60
            minutes = minutes % 60
        
        return hours, minutes, seconds
    except ValueError:
        print("Invalid format")
        sys.exit(1)

def calculate_total_seconds(hours, minutes, seconds):
    total_time = hours * 3600 + minutes * 60 + seconds
    return total_time

def countdown(total_time):
    while total_time > 0:
        print(f"{total_time} seconds")
        time.sleep(1)
        total_time -= 1
    
    cowsay.cow("Time Out")

if __name__ == "__main__":
    main()
