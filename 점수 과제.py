score = int(input("점수를 입력하세요 : "))
rating = ""

if score > 100 or score < 0:
    rating ="값이 범위(0~100)를 초과함!"
elif score >= 95:
    rating = "A+"
elif score >= 90:
    rating = "A"
elif score >= 85:
    rating = "B+"
elif score >= 80:
    rating = "B"
elif score >= 75:
    rating = "C+"
elif score >= 70:
    rating = "C"
elif score >= 65:
    rating = "D+"
elif score >= 60:
    rating = "D"
else:
    rating = "F"

print(rating)