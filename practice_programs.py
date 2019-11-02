#1.     1
#       22
#       333
#       4444
#       55555
"""
# normal way
for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print('')
"""
#lambda
#pattern_1 = lambda number: for i in range(0,number): print(i)
#pattern_1(5)

<<<<<<< HEAD
#2.
"""
*******
 *****
  ***
   *
"""
count = 7
for i in range(7,0,-1):
    for k in range(count - i):
        print(' ', end='')
    for j in range(0,i):
        print('*', end='')
    print('')
=======
pattern_1 = lambda number: [print(str(i)*i) for i in range(1, number)][0]
pattern_1(5)
>>>>>>> c074a6fa8a6f162f26375484578bd0c98180217a
