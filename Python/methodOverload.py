class maths:
   def addition( self, *args):
       sum = 0
       for x in args:
           sum += x
       print(sum)

h = maths()
h.addition(4, 5)
h.addition(4, 5, 6)
