class Car():
    def __init__(self):
        self.owner=""
        self.company=""
        self.model=""
        self.colour=""
    def enterOwner(self):
        self.owner=input("Write your Name")
    def enterCompany(self):
        self.company=input("Write your Company Name")
    def enterModel(self):
        self.model=input("Write your Model Name")
    def enterColor(self):
        self.colour=input("Write your ColorName")
    def print(self):
        print("Your car Info")
        print(self.owner)
        print(self.company)
        print(self.model)
        print(self.colour)
Car1=Car()
Car1.enterOwner()
Car1.enterCompany()
Car1.enterModel()
Car1.enterColor()
Car1.print()

       
        
