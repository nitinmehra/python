#1.     1
#       22
#       333
#       4444
#       55555
"""
# normal way
for i in range(1,6):
    for j in range(0,i):
        print(i, end="")
    print('')
"""
#lambda
#pattern_1 = lambda number: for i in range(0,number): print(i)
#pattern_1(5)

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