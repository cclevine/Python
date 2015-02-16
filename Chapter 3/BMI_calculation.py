# This program will calculate and display a persons BMI
# In this program, weight is measured in pounds and height is measured in inches

def main():
    # diplay the intro screen
    intro()
    
    # get the users weight
    user_weight=float(input('Enter your weight: '))
    # get the users height
    user_height=float(input('Enter your height: '))

    # perform BMI calculation
    bmi_calculation(user_weight, user_height)
    
    


def intro():
    print('This program calculates your BMI.')
    print('the formula is BMI = weight x 703 / height ^2')
    print('weight is measured in pounds and')
    print('height is measured in inches')
    print()

def bmi_calculation(w, h):
    # perform the BMI formula
    BMI=w*703/h**2
    print('Your Body Mass Index is: ', \
          format(BMI, ',.0f'),\
          sep='')


main()
