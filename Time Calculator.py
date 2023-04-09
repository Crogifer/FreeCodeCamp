def add_time(start_time_ampm, difference, day = False):

    def get_key(my_dict, val):
        for key, value in my_dict.items():
            if val == value:
                return key
 
        return "key doesn't exist"

    #initialise
    dayslater_output = ""
    dayweek_output = ""

    #split current time into hours, minutes, ampm
    start_time = start_time_ampm.split()[0]
    ampm = start_time_ampm.split()[1]
    hours = int(start_time.split(":")[0])
    minutes = int(start_time.split(":")[1])

    #split time difference into hours, minutes
    hours_diff = int(difference.split(":")[0])
    minutes_diff = int(difference.split(":")[1])

    #initiaise day, dictionary
    days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 0:"Sunday"}

    #get index of entered week day
    if(day != False):
        day = day.lower()
        day = day.capitalize()
        day_number = get_key(days, day)

    #calculate time from start of day in minutes
    globaltime_minutes = hours*60 + minutes
    if ampm == "PM":
        globaltime_minutes += 12*60

    #calculate total time diff in minutes and in days
    day_diff = 0
    globaltime_diff_minutes = hours_diff*60 + minutes_diff
    globaltime_diff_minutes_temp = globaltime_diff_minutes
    while globaltime_diff_minutes_temp > (60*24 - globaltime_minutes):
        day_diff += 1
        globaltime_diff_minutes_temp -= (60*24)

    #find days later output
    if day_diff == 1:
        dayslater_output += "next day"
    elif day_diff > 1:
        dayslater_output += str(int(day_diff)) + " days later"
    else:
        dayslater_output = None

    #find week day output
    if day == False:
        dayweek_output = None
    else:
        day_number_new = day_number + day_diff
        dayweek_output = days[(day_number_new % 7)]

    #find new time, hours, minutes
    time_new = globaltime_minutes + globaltime_diff_minutes
    while time_new > 24 * 60:
        time_new -= (24 * 60)
    time_new_hours = int(time_new / 60)
    if time_new_hours >= 12:
        time_new_hours -= 12
        ampm_new = "PM"
    else:
        ampm_new = "AM"
    time_new_minutes = str(time_new % 60)
    if len(time_new_minutes) < 2:
        time_new_minutes = "0" + time_new_minutes

    #when 12 pm, display 12, not 0
    if time_new_hours == 0:
        time_new_hours += 12

    #12:03 AM, Thursday (2 days later)
    if (dayweek_output != None) and (dayslater_output != None):
        return f"{time_new_hours}:{time_new_minutes} {ampm_new}, {dayweek_output} ({dayslater_output})"
    elif (dayweek_output == None) and (dayslater_output != None):
        return f"{time_new_hours}:{time_new_minutes} {ampm_new} ({dayslater_output})"
    elif (dayweek_output == None) and (dayslater_output == None):
        return f"{time_new_hours}:{time_new_minutes} {ampm_new}"
    else:
        return f"{time_new_hours}:{time_new_minutes} {ampm_new}, {dayweek_output}"


print("1", add_time("3:30 PM", "2:12"))
print("2", add_time("11:55 AM", "3:12"))
print("3", add_time("9:15 PM", "5:30"))
print("4", add_time("11:40 AM", "0:25"))
print("5", add_time("2:59 AM", "24:00"))
print("6", add_time("11:59 PM", "24:05")) ####
print("7", add_time("8:16 PM", "466:02"))
print("8", add_time("5:01 AM", "0:00"))
print("9", add_time("3:30 PM", "2:12", "Monday"))
print("10", add_time("2:59 AM", "24:00", "saturDay"))
print("11", add_time("11:59 PM", "24:05", "Wednesday")) #######
print("12", add_time("6:30 PM", "205:12"))