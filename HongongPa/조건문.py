score = 4.3

# 방법 1 
if score == 4.5: 
    print("A+") 
elif 4.0 <= score < 4.5: 
    print("A0")
elif 3.5 <= score < 4.0:
    print("B+")
else:
    print("B0")

# 방법 2 
if score == 4.5: 
    print("A+") 
elif 4.0 <= score: 
    print("A0")
elif 3.5 <= score:
    print("B+")
else:
    print("B0")

# 방법 2가 효율적인 코드 -> 상위 값은 이미 검사하였으니, 검사 생략 