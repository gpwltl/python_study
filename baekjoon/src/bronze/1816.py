# 소수 : 양의 약수가(1보다 큰 자연수) 1과 자기 자신만을 약수로 가지는 수
# 자연수를 소수들만의 곱으로 나타내는 것을 소인수 분해

import sys
input=sys.stdin.readline

def is_possible(N):
    d = 2  # 나누는 수
    cnt=0
    while N != 1:
        if N % d != 0:
            d += 1
        else:
            N //= d
            print(d)
            if d > 10**6:
                cnt+=1
            else:
                break
    return cnt

n = int(input())
for i in range(n):
    s = int(input())
    if is_possible(s) > 0:
        print('Yes')
    else:
        print('No')

# 3
# 1000036000099
# 1500035500153
# 20000000000002