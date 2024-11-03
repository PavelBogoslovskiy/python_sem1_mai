from datetime import datetime

# Текущая дата
current_datetime = datetime.now()
print("Текущая дата и время:", current_datetime)

# Разница между датами
date1 = datetime(2023, 1, 1)
date2 = current_datetime
difference = date2 - date1
print("Разница между датами:", difference.days, "дней")
print("Разница между датами:", difference.seconds, "секунд")
# second выдает разницу в секундах, глядя только на время
# total_seconds выдает разницу, учитывая день, год и месяц
print("Разница между датами:", difference.total_seconds(), "секунд")

# Преобразование строки в datetime
date_str = "2024-11-01 20:30:00"
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(f"Преобразованная дата и время: {date_obj}, тип {type(date_obj)}")

