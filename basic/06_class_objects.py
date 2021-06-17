class Person:
    name = ''
    age = 0

    def __init__(self, _name, _age) -> None:
        self.name = _name
        self.age = _age

    def sayHello(self):
        print("My name is {}, I'm {} years old!".format(self.name, self.age))


Peter = Person("Peter", 15)
Peter.sayHello()


# Inheritance
class Student(Person):
    graduateYear = 0

    def __init__(self, _name, _age, _graduateYear) -> None:
        super().__init__(_name, _age)
        self.graduateYear = _graduateYear

    def study(self):
        print("Studying ...")

    def getGraduateYear(self):
        return self.graduateYear


stu1 = Student("John", 20, 2025)
stu1.sayHello()
stu1.study()
print(stu1.getGraduateYear())
