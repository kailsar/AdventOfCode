
import re

data = open("data.txt", "r")
data_list = data.readlines()
data_list.sort()
minute_counter = 0
guard = 0
date = ""
dates = []
results = {}
awake = True

for entry in data_list:
    date = entry[6:11]
    minute = int(entry[15:17])

    if date not in results:
        schedule = []
        for x in range(60):
            schedule.append(0)
        results[date] = schedule

    if 'Guard' in entry:
        guard = (re.search('#(.*) begins', entry).group(1))

    if 'asleep' in entry:
        awake = False
        minute_counter = minute

    if 'wakes' in entry:
        awake = True
        schedule = results[date]
        for x in range(minute_counter, minute):
            schedule[x] = guard

sleeptime = {}
for key, val in results.items():
#   print(val)
    for minute_log in val:
        if minute_log in sleeptime:
            sleeptime[minute_log] += 1
        else:
            sleeptime[minute_log] = 1

sleepiest_guard = 0
sleepiest_time = 0
for key, val in sleeptime.items():
    if (val > sleepiest_time and key != 0):
        sleepiest_guard = key
        sleepiest_time = val

guards_sleepiest_minute = {}
top_sleeps = 0

del sleeptime[0]
for key, val in sleeptime.items():

    list_of_minutes = []
    for x in range(60):
        list_of_minutes.append(0)

    for key2, val2 in results.items():
        for x in range(60):
            if val2[x] == key:
                list_of_minutes[x] += 1

    sleepiest_minute = 0
    most_sleeps = 0
    for x in range(60):
        if list_of_minutes[x] > most_sleeps:
            most_sleeps = list_of_minutes[x]
            sleepiest_minute = x
        if list_of_minutes[x] > top_sleeps:
            top_sleeps = list_of_minutes[x]
            print(key)
    guards_sleepiest_minute[key] = sleepiest_minute


print(guards_sleepiest_minute)