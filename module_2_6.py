first = int(input('Введите числа:'))
second = int(input())
third = int(input())
if first == second == third:
    print(3)
if first == second or second == third or first == third:
    print(2)
else:
    print(0)
#В данной задаче, следуя из условий, оператор elif не понадобился