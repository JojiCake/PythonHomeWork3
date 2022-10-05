import random

number_n = int(input("Введите длинну: "))
list_numbers = []
for i in range(number_n):
    new_n = random.randrange(0, 10)
    list_numbers.append(new_n)
print(list_numbers)

sum_n = 0
count = 1

for i in range(1, len(list_numbers), 2):
    sum_n += list_numbers[i]
print(f'Сумма стоящих эллементов в списке нечетных позициях {sum_n}')