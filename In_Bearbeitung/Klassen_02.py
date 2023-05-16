class Person:
    def __init__(self, name):
        self.name = name

    def say_i_am(self):
        print(f"I am {self.name}")

class Student(Person):
    def __init__(self, name, cl):
        super().__init__(name)
        self.cl = cl

    def my_class(self):
        super().say_i_am()
        print(f"I am in class {self.cl}")

kerem = Student("Kerem", "2BHEL")

kerem.my_class()