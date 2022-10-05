def multiply_list(number_list):
    even_len = 0
    new_list = []
    if not len(number_list) % 2 == 0:
        even_len = int((len(number_list) + 1) / 2)
    else:
        even_len = int(len(number_list) / 2)
    for i in range(0, even_len):
        new_list.append(number_list[i] * (number_list[len(number_list)- i - 1]))
    return new_list


list_1 = [4, 5, 6, 7, 8]
list_2 = [4, 5, 7, 8]
mult_list = multiply_list(list_1)
print(f'{list_1} => {mult_list}')
  