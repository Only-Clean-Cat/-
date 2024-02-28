def test(*args,**kwargs):
    print(args)
    print(kwargs)

test('Семен', 25.6, True, a='Иван', b=10, c=False)

def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n - 1)
    return n * factorial_n_minus_1
print(factorial(15))



