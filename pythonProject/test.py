///1
import sys
input = sys.stdin.readline

def funAvg(li):
    count=0
    avgValue = sum(li)/len(li)
    for i in li:
        if i >= avgValue:
            count += 1
    return count

num=int(input())
for j in range(0, num):
    x=input()
    y=list(map(int, input().split()))
    res=str(funAvg(y))+"/"+str(x)
    print(res, end='')


//////2

import sys
input = sys.stdin.readline

num=int(input())
li=list(str(input()))

count=0

for i in range(0, num-1):
    if li[i] == li[i+1]:
        count += 1

print(num-count)


/////3

import sys
input = sys.stdin.readline
from decimal import *
import operator

x,y = input().split()
di=dict()

for i in range(0, int(x)):
    a, b=input().split()
    di[a]=Decimal(b)

# sorted_dict = sorted(di.items(), key=lambda x:(x[1]))
sorted_dict=sorted(di.items(), key=operator.itemgetter(0))
key, val = sorted_dict[int(y)-1]
print("%s %.2f" % (key, val))

/////4

import sys
input = sys.stdin.readline
n,k=map(int, input().split())
mat=[[0]*(n) for i in range(n)]

x=[0,0,0,-1,1]
y=[-1,1,0,0,0]

count=0

for j in range(0, k):
    a,b = map(int, input().split())
    for i in range(0,5):
        nx=a-1+x[i]
        ny=b-1+y[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:   # n을 기준으로 했어야지!!
            # mat[nx][ny] += 1
            count+=1 # 바로 카운트 세서 결과 내기

print(count)


/// 4. 데크 버전도 테스트 해볼 것!!!! (수)
import sys
input = sys.stdin.readline
from collections import deque
dx = [0 ,0, 1, -1]
dy = [1, -1, 0, 0]
n, k = map(int, input().split())
mat = [[ 0 for _ in range(n)] for _ in range(n)]
q = deque()
for _ in range(k):
    s, e = map(int ,input().split())
    q.append([s-1, e-1])

while q:
    x, y = q.popleft()
    mat[x][y] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0  <= nx < n and 0 <= ny < n:
            #해당 과정 대신에, 조건이 성립하면 1을 더해도 된다.
            mat[nx][ny] += 1
ans = 0
for i in mat:
    ans += sum(i)
print(ans)
