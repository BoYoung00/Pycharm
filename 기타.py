a = {}
with open("test.txt",'r',encoding='UTF-8') as f:
    for line in f:
        for i in range(1):
            k, v1, v2 = line.split()
            ab = v1, v2
        a[k] = ab
print(a)