class Students():
    def __init__(self,name,age,gender,std):
        self.name=name
        self.age=age
        self.gender=gender
        self.std=std
        
    def enterName(self,name):
        self.name=input("Enter your Name")
        print(self.name)

    def printAge(self):
        print(self.age)

Jeeya=Students("Jeeya",14,"female",9)

print(Jeeya)