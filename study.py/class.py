class Person:

    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

p1 = Person('Tommy')
p2 = Person('Jane')
# Tell p3 to use memory address of p1
p3 = p1

print('Memory address of a: ', id(p1))
print('Memory address of b: ', id(p2))
print('Memory address of c: ', id(p3))

print('p1 name:', p1.getName())
print('p3 name:', p3.getName())

print('Changed p3 name to \'Tom\'')
p3.setName('Tom')
print('p1 name:', p1.getName())
print('p3 name:', p3.getName())

print('p1 is p2:', p1 is p2)
print('p1 is p3:', p1 is p3)