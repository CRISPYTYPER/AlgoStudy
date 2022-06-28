import datetime as dt

date_string = str(dt.datetime.today().strftime("%Y-%m-%d"))

# print(type(date_string))
print(date_string.strip(), end='')