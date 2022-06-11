# a = 1
# b = 2
# c = 3
# f = []
#
# d = a,b,c
# print(d)
# for i in range(3):
#     f.append(d)
# print(f)


import sys


sys.stdout = open('test.txt', 'w')

for i in range(10):
    print(i)

sys.stdout.close()