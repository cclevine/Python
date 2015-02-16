def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    else:
        for div in range(2,num):
            if num % div == 0:
                return False
        return True

for is_prime(number) in range (0,101):
    print(number)
