my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Зададим начальный индекс
i = 0

while i < len(my_list):
    current_number = my_list[i]
    if current_number > 0:
        print(current_number)
    elif current_number == 0:
        # Пропускаем ноль
        i += 1
        continue
    else:
        break
    # Переходим к следующему элементу
    i += 1
