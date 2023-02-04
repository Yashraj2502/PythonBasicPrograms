class person:
    def __init__(self, lName, fName):
        self.firstName = fName
        self.LastName = lName

    def printName(self):
        print(f"\nHello, {self.firstName} {self.LastName}\nHave a great day.")

class student(person):
    def __init__(self, lName, fName, gYear, section):
        super().__init__(lName, fName)
        self.graduationYear = gYear
        self.branch = section

    def welcome(self):
        print(f"Welcome {self.firstName} {self.LastName} to the {self.branch} branch.")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
gradYear = int(input("Enter your graduation year: "))
branchh = input("Enter your branch: ")

obj = student(last_name, first_name, gradYear, branchh)
obj.printName()
obj.welcome()
