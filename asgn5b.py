# Built-in functions

listt = [1,56,23,86,34,779]

h = listt.index(23) # Which give index value at specific position
print(f"Index value of 23 is {h}")

listt.insert(0,100) # Here the 100 is inserted at first
print(f"List after the insertion of 100:- \n{listt}")

listt.pop() # Which pop the top most element on the list
print(f"List after performing `pop`:- {listt}")

listt.append(500) # Here 500 number append at the last
print(f"List after appending 500:- {listt}")

listt.reverse()
print(f"Reversal of the list:- {listt}")
