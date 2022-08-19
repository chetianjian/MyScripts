class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, z):
        self.name = z
        print(self.name,'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

s = PartyAnimal(z = 'Sally')
s.party()

j = PartyAnimal(z = 'Jim') #只有一个字符串变量，可以省略‘z =’，但如果有多个变量需要指定，则需要‘z = 'Jim'' and et cetera.
j.party()
s.party()