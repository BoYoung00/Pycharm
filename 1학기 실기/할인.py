a = str(input("지역주민/국가유공자/현역군인 인가요?(y/n) "))

if a == "y" :
    print("무료")
elif a == "n":
    b = str(input("65세 이상 연령인가요?(y/n) "))
    if b == "y" :
        print("50% 할인")
    else :
        print("할인없음")