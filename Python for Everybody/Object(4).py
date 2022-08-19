#Inheritance
#我们可以在已经存在的class的基础上，添加我们自己的细节，继承原有class所有的capability，以建立一个新的class。

#Subclass
#'Subclasses' are more specialized version of a class, which inherit attributes and behaviors from their parent classes,
#and can introduce their own.

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

class FootballFan(PartyAnimal):
    #It is like an extension, FootballFan is everything that PartyAnimal is, plus what ever we define down here.
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal(nam = 'Sally')
s.party()

j = FootballFan(nam = 'Jim')
j.party()
j.touchdown()



#Definitions:
#Class - A template
#Attribute - A variable within a class
#Method - A function within a class
#Object - A particular instance of a class
#Constructor - Code that runs when an object is created
#Inheritance - The ability to extend a class to make a new class
