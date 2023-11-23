class Person:
    def __init__(self, fname: str, lname: str) -> None:
        self.firstname = fname
        self.lastname = lname


class Student(Person):
    def printname(self) -> None:
        print(self.firstname, self.lastname)


sabbir = Student("Sabbir", "Hossain")
sabbir.printname()

rafi = Student("Raiful", "Islam")
rafi.printname()
