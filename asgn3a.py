# Assignment - 3a
# Toprint the following pattern.
# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5

print("Number pattern\n")
row=6
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(j,end='\t')
    print("\n")
