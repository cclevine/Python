#chester levine chapter 12 programming exercise 2

class Employee:

    def __init__(self, employeename, employeenum):
        self.__employeename = employeename
        self.__employeenum = employeenum

    def set_employeename(self, employeename):
        self.__employeename = employeename

    def set_employeenum(self, employeenum):
        self.__employeenum = employeenum

    def get_employeename(self):
        return self.__employeename

    def get_employeenum(self):
        return self.__employeenum

class ShiftSupervisor(Employee):

    def __init__(self, employeename, employeenum, salary, bonus):

        Employee.__init__(self, employeename, employeenum)

        self.__salary = salary

        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus

def main():

    shiftsupervisor1 = ShiftSupervisor('John Smith', "004", 50000, 15000)

    print('Employee Data')
    print('==============')

    print('Employee Name:', shiftsupervisor1.get_employeename())
    print('Employee Number:', shiftsupervisor1.get_employeenum())
    print('Employee Salary:', shiftsupervisor1.get_salary())
    print('Employee Bonus:', shiftsupervisor1.get_bonus())
    
main()
