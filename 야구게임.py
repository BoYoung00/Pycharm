import random

#변수
strike = 0; ball = 0
tcnt = 0 #시도 횟수
randarr = [] #정답
guessarr = [0, 0, 0] #추측값

#랜덤수 생성
arr=[i for i in range(10)]
randarr = random.sample(arr,3)
print(randarr)

#게임 시작
while True:
    tcnt +=1
    strike = 0; ball = 0

    innum = int(input(">>정수(1~999: esc 00) 입력: "))
    if innum == 0:
        break

    #입력 값에서 100, 10, 1 자리 뽑아냄
    guessarr[0] = innum // 100
    guessarr[1] = (innum % 100) // 10
    guessarr[2] = innum % 10
    print(guessarr)

    #판정
    for i in range(3):
        if guessarr[i] in randarr:
            if guessarr[i] == randarr[i]:
                strike +=1
            else :
                ball +=1


    print("[%d] %d Strike, %d Ball" %(tcnt, strike, ball))

    if strike == 3:
        print("승리!")
