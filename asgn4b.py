# Assignment - 4b
# To convert string tuple to integer tuple

r = 0
tuplee = (('12', '34'), ('2', '55'))
print("Original Tuple:- ", tuplee)

r = tuple((int(i[0]), int(i[1])) for i in tuplee)

print("Integer Tuple:- ", r)
