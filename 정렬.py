al = [4, 3, 2, 6, 1, 0, 8, 3, 6, 6, 9, 7]
print(al)

for i in range(len(al)):
    # min : 가장 작은 값을 찾기 위해 다른 인덱스에 있는 값들과 비교해야하는 값을 넣는 방 (빈 방)
    min = i

    # 0번 인덱스를 나머지 인덱스와 비교해서 제일 작은 값이 0번째 값에 저장 되어야 함
    for j in range(i+1, len(al)):
        if al[j] < al[min]:
            min = j # 제일 작은 값을 min에 저장 되면

    # 다른 수 들과 비교하고 있는 (고정)값(i)을 비교를 반복해서 가장 작은 값으로 저장된 min값을 넣어줌
    # 2개의 꽉찬 물컵을 1개의 빈컵을 가지고 교환하는거 생각하면 됨
    al[i], al[min] = al[min], al[i]

print(al)

for i in range(len(al)):
    min = i

    for j in range(i+1, len(al)):
        if al[j] > al[min]:
            min = j

    al[i], al[min] = al[min], al[i]

print(al)