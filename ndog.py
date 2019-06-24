class Dog():
    age = 0
    name = ""
    weight = 0
    
    def bark(self):
        #self.name - обращение к имени текущего объекта - собаки!
        print(self.name, "говорит гав!")
        print("Возраст моей собаки",self.age, "год.")

myDog = Dog()
myDog.name = "Лайка"
myDog.weight = 20
myDog.age = 1

myDog.bark()
