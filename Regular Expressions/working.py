import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
   
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

  
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()
    
 
    start_minute = start_minute or "00"
    end_minute = end_minute or "00"

    start_hour, start_minute = int(start_hour), int(start_minute)
    end_hour, end_minute = int(end_hour), int(end_minute)

    
    if not (1 <= start_hour <= 12) or not (0 <= start_minute < 60):
        raise ValueError("Invalid start time")
    if not (1 <= end_hour <= 12) or not (0 <= end_minute < 60):
        raise ValueError("Invalid end time")

    
    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0

    
    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    elif end_period == "AM" and end_hour == 12:
        end_hour = 0

   
    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

if __name__ == "__main__":
    main()
