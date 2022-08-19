#Object Oriented
#A program is made up of many cooperating objects, instead of being
# the 'whole program', each object is a little 'island' within the
#program and cooperatively working with other programs. A prgram is
#made up of one or more objects working together, objects make use of
#each other's capabilities.

#Example 1.
#Just like the difference between the floor counting conventions in US
#and Europe, we may write a python program as following:

Floor_in_Europe = input('Enter a floor number-')
try:
    if int(Floor_in_Europe) < 0:
        print('Enter a correct number')
    else:
        Floor_in_US = int(Floor_in_Europe) + 1
        print(Floor_in_US)
except:
    print('Enter a correct number')

#The above program provides consumers with an application or a program
#to convert the number of floors in the Europe to the US. The users don't
#actually care about the stuffs inside the program, but the program developers do.
#The object is kind of like a program but smaller, it's a little thing we can draw boundary around.

#From the outside looking in, you ignore the detail, from inside looking out, you ignore the outer detail.

#Terminology
#Class: A template
#Class defines the abstract characteristics of a thing(object), including things's characteristics (its attributes,
#fields or properties) and the thing's behaviors (the things it can do, or methods, operations or features).
#For example, the CLASS dog would consist of traits shared by dogs, such as breed and fur color (characteristics),
#and the ability to bark and sit(behaviors). However, if you grab a specific dog, its an object.


#Method or Message: A defined capability of a class
#Methods are an object's abilities. In language, methods are verbs. A dog named Lassie has the ability to bark, so
#bark() is one of Lassie's methods. She may have other methods as well, such as sit(), eat() and walk(). Within the
#program, using a method usually affects only one particular object, all dogs can bark, but you need only one
#particular dog to do the barking.


#Field or attribute: A bit of data in a class

#Object or Instance: A particular instance of a class
#The object or instance is the real specific thing.


#Example 2.
x = 'abc'
print(type(x))

#The type of x is 'string', it basically says that x is an object of type class, the class string.

dir(x) #What are the capabilities(method) of x?