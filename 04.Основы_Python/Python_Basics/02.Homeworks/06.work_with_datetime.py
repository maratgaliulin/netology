from datetime import datetime as dt
from datetime import timedelta

# date_string = '09.05.2018 09:00'
#
# date_datetime = dt.strptime(date_string, '%d.%m.%Y %H:%M')

# print(date_datetime.year, date_datetime.day, date_datetime.hour, date_datetime.weekday())



start_date = '2018-01-01'
end_date = '2019-01-01'

start_date_datetime = dt.strptime(start_date, '%Y-%m-%d')
end_date_datetime = dt.strptime(end_date, '%Y-%m-%d')

start_date_datetime_diff1 = start_date_datetime +timedelta(days=1)

start_date_datetime_diff2 = start_date_datetime +timedelta(days=-7, minutes=-1)

dttime = start_date_datetime
# while dttime < end_date_datetime:
#     print(dttime.strftime('%B %d %Y %I:%M%p'))
#     dttime += timedelta(days=31)

print([(dttime + timedelta(days=30*x)).strftime('%B %d %Y %I:%M%p') for x in range(10)])

# print(start_date_datetime_diff1)
# print(start_date_datetime_diff2)
