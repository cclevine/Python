def main():
    number=int(input('Enter a number: '))

    sum = totalsum(number)

    print('The sum of 1 to the number you entered is: ', sum)

def totalsum(num):
    if num == 0:
        return 0
    else:
        return num + totalsum(num-1)

main()
