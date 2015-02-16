


# Global Constants
BASE_HOURS = 40   #base hours per week
OT_MULTIPLIER = 1.5    #the overtime multiplier

def main():
    #get the hours worked and the hourly pay rate
    hours_worked = float(input('Enter the number of hours worked: '))
    pay_rate = float(input('Enter your hourly pay rate: '))

    #calculate and display the gross pay
    if hours_worked > BASE_HOURS:
        calc_pay_with_OT(hours_worked, pay_rate)
    else:
        calc_regular_pay(hours_worked, pay_rate)

#the calcpaywithOT function calculated pay with overtime.
#it accepts the hours worked and pay rate as arguments
#the gross pay is displayed.

def calc_pay_with_OT(hours, rate):
    #calculate the number of OT hours worked.
    overtime_hours = hours - BASE_HOURS

    #calculate the amount of overtime pay
    overtime_pay = overtime_hours * rate * OT_MULTIPLIER

    #calculate the gross pay
    gross_pay = BASE_HOURS * rate + overtime_pay

    print('Your worked overtime, so your gross pay is $ ', format(gross_pay, ',.2f'), sep='')

def calc_regular_pay(hours, rate):
    #calculate the gross pay for work with no OT
    gross_pay = hours * rate

    #display the gross pay
    print('Your gross pay is $ ', format(gross_pay, ',.2f'), sep='')












main()
