# write a program to check the object type to know wheather the method exists in the object or not.

class Dog:
    def talk(self):
        print("Bow wow!")

class Duck:
    def talk(self):
        print("Quack quack!")

class Human:
    def talk(self):
        print("Hello, hi!")


def call_talk(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()
    else:
        print("Wrong object passed")

x = Duck()
call_talk(x)

x = Human()
call_talk(x)

x = Dog()
call_talk(x)