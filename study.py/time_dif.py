import datetime
import math

# We want to calculate time difference to this date
now = datetime.datetime(2022, 5, 24, 19, 00, 00)

# Uncomment line below for current datetime object
# now = datetime.datetime.now()

# create a list and add all datetime(s)
# all dates that earlier than 'now' object
date_list = [];
date_list.append(datetime.datetime(2022, 5, 29, 10, 59, 24))
date_list.append(datetime.datetime(2021, 5, 29, 10, 12, 12))
date_list.append(datetime.datetime(2021, 5, 24, 17, 24, 54))
date_list.append(datetime.datetime(2020, 5, 14, 8, 43, 5))
date_list.append(datetime.datetime(2019, 5, 13, 19, 20, 20))
date_list.append(datetime.datetime(2012, 5, 8, 19, 20, 20))

print('Time difference to', end = ' ')
print(now.strftime("%B %d, %Y %I:%M:%S %p"))

for d in date_list:

    time_dif = (now - d).total_seconds()

    print(d.strftime("%B %d, %Y %I:%M:%S %p"), ' => ', end = '')

    # calculate for time ago since d
    if time_dif < 60:
        print(math.floor(time_dif), 'secs ago')
    elif time_dif <= 3600:
        print(math.floor(time_dif / 60), 'mins ago')
    elif time_dif <= 86400:
        print(math.floor(time_dif / 3600), 'hours ago')
    elif time_dif <= 86400 * 30:
        print(math.floor(time_dif / 86400), 'days ago')
    elif time_dif <= 86400 * 365.25:
        print(math.floor(time_dif / (86400 * 30)), 'months ago')
    else:
        print(math.floor(time_dif / (86400 * 365.25)), 'years ago')