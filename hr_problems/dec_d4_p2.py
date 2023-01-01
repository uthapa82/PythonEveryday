# Calendar module allows us to output calendars and provide
# additional useful functions for them 

import calendar as cal

def main():
    user_input = map(int, (input("Enter date MM DD YY format: ").split()))
    date_list = list(user_input)
    day = cal.weekday(date_list[2], date_list[0], date_list[1])
    days_in_calendar = list(cal.day_name)
    
    print(days_in_calendar[day].upper())

def alternate_sol():
    m, d, y = map(int, input().split())
    day = cal.weekday(y, m, d)
    
    print(cal.day_name[day].upper())
    
if __name__ == '__main__':
    main()