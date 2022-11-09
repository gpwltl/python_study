##1. 문제 풀이의 역발상
# 주변에 2가 없을 때 0을 만들 수 있어서, 남은 1(0을 만들지 못한) 의 개수는? => 2를 발견했을 때 1은 그대로 1이기에 그때 바로 cnt
# for i in range(n):
#     for j in range(n):
#         if graph[i][j]==1:
#             res+=1

for i in range(2, -1, -1):
    print(i)

##2.

##3. 순열과 조합
import itertools

chars = ['A', 'B', 'C']
p = itertools.permutations(chars, 2)  # 순열
c = itertools.combinations(chars, 2)  # 조합

print("순열", list(p))
print("조합", list(c))

# for p in per:
#     front=p[0]
#     for j in range(1, n):
#         if front%10==p[j]//10:
#             front = front * 10 + p[j]%10
#         else:
#             front = front*100 + p[j]
#     ans = min(ans, front)