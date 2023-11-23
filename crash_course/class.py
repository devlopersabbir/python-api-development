class Animal:
    name = "dog"
    color = "black"


obj1 = Animal()


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def about(self) -> str:
        return f"Name is: {self.name} and age is: {self.age}"


obj = Person("Sabbir", 19)
print(obj.about())
