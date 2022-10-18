list=['a', 'b', 'c']
print(len(list))    # len() 길이
print(list[1])
# 리스트 제거
list.remove('c')
print(list)
# 리스트 추가
list.append('d')
print(list)

# 인터프리터와 컴파일러
# 1. interpret 방식: 동시 통역(한줄 한줄) <- 파이썬
# 2. compile 방식 : 한번에 변환

print('직사각형 그리기\n')
leg = int(input('변의 길이: ')) # input() : 입력받는 부분

for i in range(leg):    # 반복문(leg길이만큼)
    print('* ' * (i+1))

area = (leg ** 2) / 2   # ** : 제곱
print('넓이: ', area)

# Q. 정수 입력 받아, 그 수의 제곱을 계산해 출력하는 파이썬 스크립트 작성하시오.
num = int(input('정수 입력: '))
res = num ** 2
print("result: ", res)