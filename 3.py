import random

number_n = int(input('Введите длину: '))
list_numbers = []
new_n = 0
for i in range(number_n):
    new_n = round(random.uniform(0.00, 10.00), 3)
    list_numbers.append(new_n)
print(list_numbers)
max_number = round(list_numbers[0] % 1, 3)
min_number = round(list_numbers[0] % 1, 3)
list_2 = [num % 1 if num % 1 > 0.0001 else 0 for num in list_numbers]
print(max(list_2))
print(min(list_2))
print(round((max(list_2)-min(list_2)), 3))