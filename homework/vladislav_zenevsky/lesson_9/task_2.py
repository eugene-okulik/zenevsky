temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

hot_days_temperatures = list(filter(lambda x: x > 28, temperatures))
avg = int(sum(hot_days_temperatures) / len(hot_days_temperatures))

print(f'Maximum is: {max(hot_days_temperatures)}, minimum is: {min(hot_days_temperatures)}, average is: {avg}')
