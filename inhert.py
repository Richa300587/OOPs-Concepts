class Animal:
    def __init__(self,name):
        self.name =name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def __init__(self,behaviour):
        super().__init__("Cat")
        self.behaviour=behaviour
    def speak(self):
        super().speak()
        print(f"{self.name} do meow meow")
        print(f"{self.name} is very {self.behaviour}")
cat=Cat("Fast Runner")
cat.speak()