import random as r

row = int(input("행 개수 : "))
col = int(input("열 개수 : "))

arr = [i for i in range(row*col)]
print(arr)

arr = r.sample(arr,row*col)
print(arr)


randarr = []
for i in range(0,len(arr),col):
    randarr.append(arr[i:i+col])

print(randarr)