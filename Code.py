class Body:
    def __init__(self, age, weight, temp) -> None:
        self.age = age
        self.weight = weight
        self.temp = temp
    
    hands = True
    Face = True
    teeth = True

    def Summarize(self):
        print (F'My age is {self.age}, my weight is {self.weight}, and body temperature is {self.temp}')
    def Dance(self):
        self.temp += 3
        print({f"{self.temp}"})
        return self