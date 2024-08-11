def prime_generator(end):
    for n in range(2, end + 1):
        if n == 2 or n == 3 or n > 3 and n % 2 != 0 and all(n % i for i in range(3, n // 2 + 1)):
            yield n


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
