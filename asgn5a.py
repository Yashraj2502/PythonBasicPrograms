# User defined functions

def myFunction(fname, lname):
    print(f"\nHello, {fname} {lname} \nHave a great day")

def HEllo(*kids):
    print("\n--------------------------------------\n")
    print("The Youngest child is "+kids[1])

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

myFunction(firstName, lastName)   
HEllo("Vaibhav","Devesh","Subhash")