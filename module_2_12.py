#Данные
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

#Сам цикл
for num in numbers:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

#Удаляем 1 - т.к. не считается ни простым, ни составным числом
if 1 in primes:
    primes.remove(1)
if 1 in not_primes:
    not_primes.remove(1)

print(primes)
print(not_primes)