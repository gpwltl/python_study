### 1
import sys
input = sys.stdin.readline

n=int(input())
for _ in range(n):
    x=int(input())
    arr=list(map(int, input().split()))
    cnt=0
    avg=sum(arr)/x
    for i in arr:
        if i >= avg:
            cnt += 1
    print("%d/%d"% (cnt, x))


### 2
import sys
input = sys.stdin.readline

n=int(input())
arr=input()
cnt=1	#마지막 글자는 비교할 필요가 없으니까
for i in range(0, n-1):
    if arr[i] == arr[i+1]:
        continue
    else:
        cnt+=1

print(cnt)

### 3 (근데 틀림,,, 왜지,,)
from functools import cmp_to_key
def cmp(a, b):
    if a[0]==b[0]:	# 같은 값이면 다음 글자가 큰걸로
        return a[1]<b[1]
    else:
        return a[0]<b[0]	#아니면 그냥 정렬 크던게

n, k=input().split()
arr=[]
for _ in range(int(n)):
    li=list(map(str, input().split()))
    arr.append(li)

sorted_arr=sorted(arr, key=cmp_to_key(cmp))
res=sorted_arr[int(k)-1]
print("%s %.2f" % (res[0], float(res[1])))