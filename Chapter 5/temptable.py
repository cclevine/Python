#Chester Levine CSC 119 Prog Ex 6
#This program will display a table of Celcius Temperatures
#0-20 and their Fahrenheit equivalents.  The formula for converting
#Fahrenheit to Celcius is F=(9/5)*C+32

def main():
    #print the table headings
    print('Celcius\t| Fahrenheit')
    print('____________________')
    print('')

    #print the temperatures
    for celcius in range(0,21):
        fahrenheit=(9/5)*celcius+32
        print(celcius, '\t|',format(fahrenheit, '.1f'))

#call the main function

main()
