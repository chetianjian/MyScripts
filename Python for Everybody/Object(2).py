#Construct a class
#Example 1.
class PartyAnimal:
    x = 0 #x is an attribute (some data) of the class PartyAnimal, and all PartyAnimals will have a variable x in them.
    def party(self): #This is a method (ability),
        self.x = self.x + 1
        print('So far: ',self.x)
#为什么用self.x？
#哪个对象调用了party()，self就是那个对象，但是对于不同的对象，其attribute (data) 不一样，所以self.x指定或唤醒self的x。做一个类比，a、b
#是两个list，而两个list肯定拥有不一样的attribute。


an = PartyAnimal()
#This syntax basically says that, make me a PartyAnimal, just like the 'x = list()' we used before, it constructs a
#new list for me, list() is a template of list, and gives me that empty list back to variable x. Using a PartyAnimal
#Template, to make a PartyAnimal Object, which ends up in the variable an.


an.party()
#We make a call by taking the name of the object (an), and then .party is a method defined above.
#Abbrev. of PartyAnimal.party(an)

an.party()
#Calls again

an.party()
#And again



#Constructor and Destructor

class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')
    def party(self):
        self.x = self.x + 1
    def __del__(self):
        print('I am destructed', self.x)


an = PartyAnimal()
an.party()
an.party()