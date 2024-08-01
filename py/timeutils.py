import string
from datetime import datetime

def iso_date_to_unix(isodate): 

    return 0

def increment_date_day(current_time, num_days):
    return current_time + (86400 * num_days)

def increment_date_hr(current_time, num_hours):
    return current_time + (3600 * num_hours)

def increment_date_wk(current_time, num_weeks):
    return current_time + ((7 * 86400) * num_weeks)

def increment_date_yr(current_time, num_years):
    return current_time + ((7 * 86400) * num_years)

def get_formatted_unix(mode):
    """
        Gets a formatted unix timestamp for use on Discord
    """
    unix_time = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
    unix_time = increment_date_hr(unix_time, 4)    
    discord_time = "<t:" + str(unix_time).split('.', 1)[0]

    if mode == 't':
        discord_time += ":t>"
    elif mode == 'T':
        discord_time += ":T>"
    elif mode == 'd':
        discord_time += ":d>"
    elif mode == 'D':
        discord_time += ":D>"
    elif mode == 'f':
        discord_time += ":f>"
    elif mode == 'F':
        discord_time += ":F>"
    elif mode == 'R':
        discord_time += ":R>"
    else:
        discord_time += ">"
    return discord_time

if __name__ == "__main__":
    print(get_formatted_unix('t'))
    print(get_formatted_unix('T'))
    print(get_formatted_unix('d'))
    print(get_formatted_unix('D'))
    print(get_formatted_unix('f'))
    print(get_formatted_unix('F'))
    print(get_formatted_unix('R'))
    print(get_formatted_unix('0'))
