"""
model

color

speed limit

company


"""


class CarSelect():
    def __init__(self ):
        self.model = ""
        self.color = ""
        self.speedLimit = ""
        self.company = ""
        self.chooseModel()

    def chooseModel(self):
        model = input("Choose your car model: ")

        self.model = model

        print("Model " , model , " chosen.")

        self.chooseColor()
    
    def chooseColor(self):

        color = input("Choose your car color: ")

        self.color = color

        print("Color " , color ," chosen.")

        self.chooseCompany()

    def chooseCompany(self):

        company = input("Choose your Company: ")

        self.company = company

        print("Company " , company , " chosen" )

        self.End()

    def End(self):
        print("Good choice! Your car will be delivered soon.")

    



select = CarSelect()

 