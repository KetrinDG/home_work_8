from datetime import date, datetime, timedelta

users = [{'name': 'Bill', 'birthday': '2000-01-14'},
         {'name': 'Jill', 'birthday': '2001-01-15'},
         {'name': 'Kim', 'birthday': '1995-01-17'},
         {'name': 'Jan', 'birthday': '2002-01-18'},
         {'name': 'Max', 'birthday': '2001-01-24'}
         ]

# функция диапазона: определяем дату вывода
def generate_range_dates(start_date, end_date) -> list:
    date_1 = min(start_date, end_date)
    date_2 = max(start_date, end_date)
    # Сразу добавляем стартовую дату
    items = [date_1]
    while date_1 < date_2:
        date_1 += timedelta(days=1)
        items.append(date_1)
    return items


def get_birthdays_per_week(users):
    # текущая дата
    current_date = datetime.now().date()
    year_ = current_date.year
    days_dict = {}

    # данные для функции диапазона
    start_date = date.today() + timedelta(days=7)
    end_date = date.today() + timedelta(days=14)
    date_range = generate_range_dates(start_date, end_date)

    # пользователи
    for i in users:
        bd = datetime.strptime(i['birthday'], '%Y-%m-%d')
        cur_bd = bd.replace(year=year_).date()

        # если выпадает на выходные и понедельник
        get_monday = [d for d in date_range if d.weekday() == 0][0]
        if cur_bd in date_range:
            if cur_bd.weekday() in (5, 6):
                cur_bd = get_monday
        # другой любой день
            if days_dict.get(cur_bd):
                days_dict[cur_bd].append(i['name'])
            else:
                days_dict[cur_bd] = [i['name']]

    return days_dict


birthday_dict = get_birthdays_per_week(users)


if __name__ == '__main__':
    for dt, user in get_birthdays_per_week(users).items():
        print(f'{dt.strftime("%A")} : {",".join(user)}')