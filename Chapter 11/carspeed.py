
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5 

    def get_speed(self):
        return self.__speed

def main():
    my_car = Car(2014, 'BMW')

    for count in range(5):
        my_car.accelerate()
        print('We should speed up! Speed:', my_car.get_speed())

    for count in range(5):
        my_car.brake()
        print('Now slow down! Speed:', my_car.get_speed())

main()        
        
        
