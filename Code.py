class Body:
    def __init__(self, age, weight, temp, hands=True) -> None:
        self.age = age
        self.weight = weight
        self.temp = temp
        self.hands = hands
        Face = True
        teeth = False

    def Summarize(self):
        print (F'My age is {self.age}, my weight is {self.weight}, and body temperature is {self.temp}')
    def Dance(self):
        self.temp += 3
        print({F"{self.temp}"})
        return self
    def CuttParts(self):
        self.hands != self.hands
        print(F"{self.hands}")
        return self

