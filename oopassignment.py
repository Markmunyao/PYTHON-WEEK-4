class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

def Introduce(self):
    raise NotImplementedError("should implement this")

class PersonIntroduce(Person):
    def Introduce(self):
        return f"This is {self.name} he is {self.age} years old, and he is a {self.gender}"

PersonIntroduce_instance=PersonIntroduce("MARK KUSU", 24, "MALE")  

print(PersonIntroduce_instance.Introduce())