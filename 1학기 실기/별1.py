for i in range(1, 6, 1):
    print("*"*i)

print("-------")

for j in range(5, 0, -1):
    print(" "*j, end= '')
    print("*****")

print("-------")

for a in range(5):
    print("%d " %a * 5)

print("-------")

for b in range(0,5,1):
    print("%d " %b * (b+1))
print()

print("-------")

for d in range(5):
    for c in range(5-d-1,-1,-1):
        print("%d" %c, end=' ')
    print()

print("-------")

num1 = int(input("몇단(2~9)? "))
for e in range(1, 10,1):
    print("%d X %d = %d" %(num1, e, num1*e))

print("-------")

for f in range(2, 10, 1):
    print("   <%d단>" %f)
    for g in range(1, 10, 1):
        print("%d X %d = %d" %(f, g, f*g))
    print()

print("-------")

for h in range(2, 10, 1):
    print("  <%d단>  " %h, end='\t')
print()

for n in range(1, 10, 1):
    for k in range(2, 10, 1):
        print("%d X %d = %d" %(k, n, n*k), end='\t')
    print()