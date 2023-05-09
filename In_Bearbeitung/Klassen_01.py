class Car:
    def __int__(self, type, power, speed):
        self.type = type
        self.ps = power
        self.speed = speed

    def speed_up(self):
        pass

    def go(self):
        print("Vroom")
        print(f"I drive a {self.type} with {self.ps} PS")


melvin_car = Car("Honda Civic", 200)
muslim_car = Car("BMW M3", 370)


muslim_car.go()
melvin_car.go()