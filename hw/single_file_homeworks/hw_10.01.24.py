class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def set_age(self, new_age):
        self._age = new_age

    def say_hi(self):
        print(f"Hi from {self._name}")


class Student(Person):

    def __init__(self, name, age, stage):
        super().__init__(name, age)
        self._stage = stage

    def say_hi(self):
        print(f"Hi from student {self._name}")

    def __add__(self, other):
        return f"{self._name}, {self._age}, {self._stage + other._stage}"


class Employee(Person):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary

    def say_hi(self):
        print(f"Hi from employee {self._name}")

    def __add__(self, add_salary):
        self._salary = self._salary + add_salary

    def get_salary(self):
        return self._salary


era = Student('Era', 19, 2)
nurtay = Student('Nurtay', 20, 1)
roma = Employee('Roma', 40, 100000)

print(era + nurtay)  # exercise 1
roma + 50000
print(roma.get_salary())  # exercise 2
