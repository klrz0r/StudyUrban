numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
new_list = []

for i in numbers:
    if i == 1:
        continue
    is_prime = True
    new_list.append(i)
    for n in new_list:
        if i % n == 0 and i != n:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)