def worker(p):
    z = 8
    a = True
    b = p >= 10
    c = b or (p > 6)
    if b:
        if c and (p < z + 5):
            return 'One'
        return 'Two'
    else:
        if a and (p - 1 < z):
            return 'Three'
        else:
            return 'Four'

y = int(input('Please enter an integer value '))
print(worker(y))

worker()
