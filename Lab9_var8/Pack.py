class Animal:
    count = 0
    id=0
    weight = 0
    height = 0
    classification = ""


    def __del__(self):
        print('i have deleted animal object')
        Animal.count-=1

    def __init__(self, id=0, weight=0, height=0, classification=""):
        Animal.count+=1
        self.id=id
        self.height = height
        self.weight = weight
        self.classification = classification

    def setWeight(self,weight):
        self.weight=weight

    def getWeight(self):
        return self.weight

    def setHieght(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setClass(self, classification):
        self.classification = classification

    def getClass(self):
        return self.classification

    def input(self):
        self.weight=float(input("Enter weight: \n"))
        self.height = float(input("Enter height: \n"))
        self.classification=str(input("Enter class: \n"))

    def show(self):
        return F'ID:{self.id}, Animal weight:{self.weight}, height:{self.height}, classification:{self.classification}'

class Pet(Animal):
    sound = ""
    food = ""

    def input(self):
        Animal.input(self)
        self.sound = str(input("Enter sound: \n"))
        self.food = str(input("Enter food: \n"))

    def setSound(self, sound):
        self.sound = sound

    def getSound(self):
        return self.sound

    def setFood(self, food):
        self.food = food

    def getFood(self):
        return self.food

    def __init__(self, id=0, weight=0, height=0, classification="",sound="", food=""):
        Animal.__init__(self, id,weight, height, classification)
        self.sound = sound
        self.food = food

    def show(self):
        return Animal.show(self)+F' ,sound:{self.sound}, food:{self.food}'

class Dog(Pet):
    name = ""
    age = 0

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


    def __init__(self, id, weight=0, height=0, classification="", sound="", food="", name="", age=0):
        Pet.__init__(self, id, weight, height, classification,sound,food)
        self.name = name
        self.age = age

    def input(self):
        Pet.input(self)
        self.name = str(input("Enter name \n"))
        self.age = int(input("Enter age \n"))

    def show(self):
        return Pet.show(self) + F' ,name:{self.name}, age:{self.age}'



class Pack:

    dogs = list()


    def addNewDog(self, dog):
        self.dogs.append(dog)

    def removeLastDog(self):
        if len(self.dogs) != 0:
            self.dogs.pop()

    def showPack(self):
        print('show new pack \n')
        for dog in self.dogs:
            print(dog.show())

    def sortPack(self, parametr):

        if parametr == 'weight':
            self.dogs.sort(key=lambda x: x.weight)
        if parametr == 'height':
            self.dogs.sort(key=lambda x: x.height)
        if parametr == 'classification':
            self.dogs.sort(key=lambda x: x.classification)
        if parametr == 'name':
            self.dogs.sort(key=lambda x: x.name)
        if parametr == 'sound':
            self.dogs.sort(key=lambda x: x.sound)
        if parametr == 'food':
            self.dogs.sort(key=lambda x: x.food)
        if parametr == 'age':
            self.dogs.sort(key=lambda x: x.age)