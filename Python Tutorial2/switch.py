# benefits: cleaner and more readable syntax

def week_name(day):
    match day:
        case 1:
            return "Sat"
        case 2:
            return "Sun"
        case 3:
            return "Mon"
        case 4:
            return "Tue"
        case 5:
            return "Wed"
        case 6:
            return "Thu"
        case 7:
            return "Fri"
        case _:
            return "Invalid"

def is_weekend(wk):
    match wk:
        case "Thu" | "Fri":
            return True
        case "Sat" | "Sun" | "Mon" | "Tue" | "Wed":
            return False
        case _:
            return "Invalid"
        
print(week_name(2))
print(is_weekend(week_name(6)))



# variable scope = where a variable is visible and accessiblt
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in