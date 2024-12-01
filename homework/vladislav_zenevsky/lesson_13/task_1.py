import os
import datetime

base_path = os.path.dirname(__file__)

homework_path = os.path.dirname(os.path.dirname(base_path))

eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

actions = []


def read_file():
    with open(eugene_file_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    number_date, action = data_line.split(' - ')
    _, date = number_date.split(maxsplit=1)
    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    actions.append((date, action))

for date, action in actions:
    if "распечатать эту дату, но на неделю позже" in action:
        print(date + datetime.timedelta(weeks=1))
    elif "распечатать какой это будет день недели" in action:
        print(date.strftime("%A"))
    elif "распечатать сколько дней назад была эта дата" in action:
        print((datetime.datetime.now() - date).days)
