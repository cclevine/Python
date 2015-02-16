# This program gets a series of numbers and
# calculates the average, the total, the highest,
# and the lowest of the numbers entered.

def main():
    # Get the test scores from the user.
    numbers = get_numbers()

    # Get the total of the test scores.
    total = get_total(numbers)

    # Calculate the average. 
    average = total / (len(numbers))

    # Display the average.
    print('The average is:', average)
    # Display the total.
    print('the total of the numbers is', total)
    # Display the lowest number. 
    print('the lowest number is', min(numbers))
    # Display the highest number.
    print('the highest number is', max(numbers))

# The get_numbers function gets a series of numbers
# from the user and stores them in a list.
# A reference to the list is returned.
def get_numbers():
    print('Please enter 20 numbers')
    # Create an empty list.
    num_list = []
    
    # Create a variable to control the loop.
    again = 'y'

    # Get the numbers from the user and add them to
    # the list.
    while again == 'y':
        # Get a number and add it to the list.
        value = float(input('Enter a number: '))
        num_list.append(value)

        # Want to do this again?
        print('Do you want to add another number?')
        again = input('y = yes, anything else = no: ')
        print()
        
    # Return the list.
    return num_list

# The get_total function accepts a list as an
# argument returns the total of the values in
# the list.
def get_total(value_list):
    # Create a variable to use as an accumulator.
    total = 0.0
    
    # Calculate the total of the list elements.
    for num in value_list:
        total += num

    # Return the total.
    return total

# Call the main function.
main()
