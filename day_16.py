from datetime import datetime
d = datetime.now()
print('current day', d.day)
print('current month', d.month)
print('current hour', d.hour)
print('current minute', d.minute)
print('current timestamp', d.timestamp())
dm = d.strftime("%m/%d/%Y, %H:%M:%S")
print(dm)
today = "5 December, 2019"
time = datetime.strptime(today, "%d %B, %Y")
print(time)
new_year = datetime(2026, 1, 1, 0, 0, 0) 
diff = d - new_year
print(diff)
qst6 = d.timestamp()
diffj = datetime(1970, 1, 1, 0, 0, 0)
qsst6 = d - diffj 
print(qst6)
print(qsst6)