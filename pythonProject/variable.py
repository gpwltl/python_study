# 기본 사칙 연산 - python3
print(1+1)
print(10-3)
print(33333*4)
print(50 / 8)   # 6.25
print(50 // 8)  # 6
print(50 % 8)   # 2 (나머지)
# 몫과 나머지 한번에 구하는 함수
divmod(50, 8)
print(divmod(50, 8))    # (6,2)

# 변수
a=1
b=2
c="hi"
d=" tom"
print(a+b)  # 3
#print(b+c)  # error - 문자열+숫자하려면, 아래 방식으로
print(str(b)+c) #2hi
print(c+d)  #hi tom

# Q. 다운로드 속도가 초당 800kB이고 다운로드하는 데 걸린 시간이 110초라고 할 때, 다운로드한 파일의 크기는 몇 MB일까요? 단, 로 계산합니다.
r=800
t=110
print(r/1000*t)