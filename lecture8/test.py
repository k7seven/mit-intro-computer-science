class Animal:
    def __init__(self, mouth: int, legs: int):
        self.__mouth = mouth
        self.__legs = legs

    def __str__(self):
        return f"Animal has {self.mouth} mouth and {self.legs} legs."

    @property
    def mouth(self):
        return self.__mouth

    @property
    def legs(self):
        return self.__legs



animal1 = Animal(1, 4)
print(animal1)
