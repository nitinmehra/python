#1.     1
#       22
#       333
#       4444
#       55555

# normal way
for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print('')
#lambda

pattern_1 = lambda number: [print(str(i)*i) for i in range(1, number)][0]
pattern_1(5)