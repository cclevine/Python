# Chester Levine CSC 119 Chapter 7 Prog Ex 5
# This program reads the values in the numbers.txt
# file and calculates their total.

def main():
    # Open the numbers.txt file for reading.
    numbers_file = open('numbers.txt', 'r')

    # Initialize an accumulator to 0.0.
    total = 0.0

    # Initialize a variable to keep count of the videos.
    count = 0

    print('Here are the numbers in the file:')
    
    # Get the values from the file and total them.
    for line in numbers_file:
        # Convert a line to a float.
        num = float(line)

        # Add 1 to the count variable.
        count += 1
        
        # Display the time.
        print(count, ': ', num, sep='')

        # Add the time to total.
        total += num

    # Close the file.
    numbers_file.close()

    # Display the total of the numbers.
    print('The sum of the numbers is', total,)

# Call the main function.
main()
