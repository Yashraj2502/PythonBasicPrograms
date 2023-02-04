# Assignment - 3c
# To reverse the given number/string

t = int(input("Enter the numberical string: "))
rev=0
while (t != 0):
    rem = t%10    # 123 % 10 = 3
    rev = rev*10 + rem  #  0 = 0*10 + 3 = 3
    t = t//10     # n = 123//10 = 12
    
print(rev)