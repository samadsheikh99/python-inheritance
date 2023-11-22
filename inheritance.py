class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
x.printname()
print(x.graduationyear)

#multilevel inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Noble subclass inheriting from Animal
class Mammal(Animal):
    def give_birth(self):
        pass

# Grand subclass inheriting from Mammal
class Dog(Mammal):
    def bark(self):
        print(f"Woof! Woof! I am {self.name}, the loyal dog.")

# Sublime instantiation of the classes
my_dog = Dog("Fluffy")
my_dog.speak()  # Inherits from Animal
my_dog.give_birth()  # Inherits from Mammal
my_dog.bark()  # Specific to Dog class

#hierachical inheratance
# Majestic base class
class LivingBeing:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing.")

# Noble subclasses inheriting from LivingBeing
class Animal(LivingBeing):
    def make_sound(self):
        pass

class Plant(LivingBeing):
    def photosynthesize(self):
        pass

# Sublime subclasses inheriting from Animal
class Mammal(Animal):
    def give_birth(self):
        pass

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is soaring through the skies!")

# Magnificent instantiation of the classes
lion = Mammal("Simba")
eagle = Bird("Zephyr")

lion.breathe()  # Inherits from LivingBeing
lion.give_birth()  # Inherits from Mammal, which inherits from Animal
eagle.breathe()  # Inherits from LivingBeing
eagle.fly()  # Specific to Bird class

#muliple inheritance
# Splendid first base class
class A:
    def speak(self):
        print("Class A speaks.")

# Glorious second base class
class B:
    def jump(self):
        print("Class B jumps.")

# Marvelous third base class
class C:
    def swim(self):
        print("Class C swims.")

# The magnificent union of classes in multiple inheritance
class D(A, B, C):
    def perform_actions(self):
        self.speak()  # Inherits from class A
        self.jump()   # Inherits from class B
        self.swim()   # Inherits from class C
        print(f"{self.__class__.__name__} is a versatile being!")

# Unleashing the power of multiple inheritance
being_d = D()
being_d.perform_actions()


