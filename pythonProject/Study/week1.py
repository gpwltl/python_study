li = list(map(int, input().split()))
print(li)
# 3 2 1 4 2 - input
# [3, 2, 1, 4, 2]

for i in range(0, len(li)):
    print(i)
# 0
# 1
# 2
# 3
# 4

for j in li:
    print(j)
# 3
# 2
# 1
# 4
# 2

# 입력 받는 동시에 문자열 비교하도록! (굳이 input 받아서 list에 append할 필요 없이 바로 확인하고 결과만 카운트!)
n, name = input("input: {num}, {str}").split()
cnt = 0
for i in range(int(n)):
    nameInput = input()
    if name in nameInput:
        cnt += 1
print(cnt)

# 입력값 시간 줄이기 위한 input 설정
import sys
input = sys.stdin.readline

# 에라토스테네스의 체(소수 찾기)
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

print(prime_list(26)) # [2, 3, 5, 7, 11, 13, 17, 19, 23]