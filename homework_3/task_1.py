# Пример обращения
from my_package.functions import Functions

func = Functions()

numbers = [1, 2, 3, 4, 5, 12345]
result = func.calculate_sum(numbers)

print(f"Сумма чисел в списке: {result}")
