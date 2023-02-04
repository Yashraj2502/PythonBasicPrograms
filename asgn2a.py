# Assignment - 2a
# To accept the cost price of the bike & display the road tax to be paid

a = float(input("Enter the cost price of bike: "))
tax=0

if(a > 100000) :
    tax = 15 / 100 * a

elif (50000 < a <= 100000) :
    tax = 10 / 100 * a

elif (a <= 50000) :
    tax = 5 / 100 * a

print(f"Tax to be paid {tax}")
