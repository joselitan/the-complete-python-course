for n in range(2, 100):
    #print(f"{n}")
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f'{n} is a prime number.')
