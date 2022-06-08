import random as r

innum = 0
rnum = r.randint(1, 20)
i=0

while i != 5 :
    innum = int(input("숫자 입력(1~20) : "))

    if innum == rnum :
        i += 1
        print("[%d] 정답" %i)
        print("당신이 이겼습니다.")
        re = str(input("게임을 다시 하시겠습니까?(Y/N) "))
        if re == 'Y':
            rnum = r.randint(1, 20)
            i = 0
            continue
        elif re == 'N':
            break

    elif rnum > innum :
        i += 1
        print("[%d] Up" %i)
        if i == 5 :
            print("당신이 졌습니다.")
            re = str(input("게임을 다시 하시겠습니까?(Y/N) "))
            if re == 'Y':
                rnum = r.randint(1, 20)
                i = 0
                continue
            elif re == 'N':
                break

    elif rnum < innum :
        i += 1
        print("[%d] Down" %i)
        if i == 5 :
            print("당신이 졌습니다.")
            re = str(input("게임을 다시 하시겠습니까?(Y/N) "))
            if re == 'Y':
                rnum = r.randint(1, 20)
                i = 0
                continue
            elif re == 'N':
                break