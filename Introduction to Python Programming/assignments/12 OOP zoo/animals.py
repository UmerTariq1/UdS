#############################
# UTILITIES                 #
#############################

'''
e.g. a function that reads in the images
'''


#############################
# ANIMALS                   #
#############################

'''
The classes representing animals.
First, define the class hierarchy.
Then think of what the classes have in common,
this functionality goes in the superclass.
Then think of what is special about the subclass,
this goes into the subclass.

Hints: Some methods can be applied to all animals
(e.g., visit(), eat()), some only apply to a particular
animal (e.g., swim()).

Which attributes do the objects have?
--> Design your __init__ methods accordingly.
'''

class Animal:
    def __init__(self, name, image_path=None):
        self.name = name
        self.image_path = image_path
    
    def eat(self):
        print("I am a " + self.name + " and I am ~~~~ EATING!! ~~~~")
    
    def sleep(self):
        print("I am a " + self.name + " and - yawn... ~~~~ ZZZzzzz ~~~~")

    def show_image(self):
        with open(self.image_path, 'r') as f:
            for line in f:            
                print(line.rstrip())

    def visit(self):
        print("Visiting bear ")
        self.show_image()
        print("NAME: " + self.name)
        print("INFORMATION:")
        print("Animal <can eat(), sleep()>")

    def __str__(self) -> str:
        return self.name

class Mammal(Animal):
    def __init__(self, name, image_path=None):
        super().__init__(name, image_path)

    def visit(self):
        super().visit()
        print("\t |")
        print("\t ----- ",end=" ")
        print("Mammal ")
    

class Rodent(Mammal):
    def __init__(self, name, image_path=None):
        super().__init__(name, image_path)

    def gnaw(self):
        print("I am a " + self.name + " and I am *** GNAWING ****")

    def visit(self):
        super().visit()
        print("\t\t |")
        print("\t\t ----- ",end=" ")
        print("Rodent <can gnaw()>")


class Bird(Animal):
    def __init__(self, name, image_path=None):
        super().__init__(name, image_path)

    def fly(self):
        print("I am a " + self.name + " and I am ~~~~ FLYING!! ~~~~")

    def visit(self):
        super().visit()
        print("\t |")
        print("\t ----- ",end=" ")
        print("Bird <can fly()>")
        

class LandBird(Bird):
    def __init__(self, name, image_path=None):
        super().__init__(name, image_path)

    def visit(self):
        super().visit()
        print("\t\t |")
        print("\t\t ----- ",end=" ")
        print("Land Bird")

#water bird is inherited only from bird and not from fish because the output says waterbird can swim. not fish can swim. and also because duck isnt a fish
class WaterBird(Bird):
    def __init__(self, name, image_path=None):
        super().__init__(name, image_path)

    def swim(self):
        print("I am a " + self.name + " and I am ~~~~ SWIMMING!! ~~~~")

    def visit(self):
        super().visit()
        print("\t\t |")
        print("\t\t -----",end=" ")
        print("Water Bird <can swim()>")


class Fish(Animal):
    def __init__(self, name, image_path=None):
        super().__init__(name, image_path)

    def swim(self):
        print("I am a " + self.name + " and I am ~~~~ SWIMMING!! ~~~~")

    def visit(self):
        super().visit()
        print("\t |")
        print("\t ----- ",end=" ")
        print("Fish <can swim()>")
