# 에라토스테네스의 체 알고리즘
ii = int(input())
for _ in range(ii):
    n = int(input())
    a = [True for i in range(n + 1)]
    m = int(n**0.5)

    for i in range(2, m + 1):
        if a[i] == True:
            j = 2
            while i * j <= n:
                a[i * j] = False
                j += 1

    for i in range(2, n + 1):
        cnt = 0
        if a[i] == True and n % i == 0:
            if i <= 10**6:
                print('No')
                break
            print('Yes')
