s = 0
o = 0

s = str(input("성별은?(m / f) "))
o = int(input("나이는? "))

if s == "f" and o > 5 :
    print("여탕")
elif s == "m" and o > 5 :
    print("남탕")
else :
    print("아무탕")

