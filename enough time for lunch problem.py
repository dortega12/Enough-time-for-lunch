def enough_time_for_lunch(hour1, minute1, hour2, minute2):
    if hour1 > hour2:
        return False
    elif hour2 - hour1 == 1 and minute2 - minute1 == 0:
        return True
    hours = (hour2 - hour1) % 24
    minutes = (minute2 - minute1) % 60
    
    if hours == 0 and minutes >= 45:
        return True
    elif hours > 1:
        return True
    elif hours == 1 and minutes >= 45:
        return True
    else:
        return False

def main():
    a = int(input("first hour"))
    b = int(input("first min"))
    
    x = int(input("second hour"))
    y = int(input("second min"))
    
    print(enough_time_for_lunch(a, b, x, y))
    
main()
    