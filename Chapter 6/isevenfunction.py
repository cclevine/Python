def is_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False
    

number=int(input('enter a number'))
if is_even(number):
    print('the number is even')
else:
    print('the number is odd')
