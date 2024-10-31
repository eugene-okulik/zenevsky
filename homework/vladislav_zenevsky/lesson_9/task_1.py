import datetime

date_to_format = 'Jan 15, 2023 - 12:05:33'

formatted_date = datetime.datetime.strptime(date_to_format, '%b %d, %Y - %H:%M:%S')

print(formatted_date.strftime('%B'))
print(formatted_date.strftime('%d.%m.%Y, %H:%M'))
