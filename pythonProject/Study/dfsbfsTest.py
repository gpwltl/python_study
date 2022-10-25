# https://www.acmicpc.net/problem/1260 (백준1260)
import sys
input = sys.stdin.readline
from collections import deque

def dfs(graph, start, visited):
    visited[start]=True
    print(start, end=' ')
    for k in graph[start]:
        if not visited[k]:
            dfs(graph, k, visited)

def bfs(graph, start, visited):
    dq=deque([start])
    visited[start]=True #젤 첫번째 true때문에 넣음.
    while dq:
        x=dq.popleft()
        print(x, end=' ')
        for k in graph[x]:
            if not visited[k]:
                dq.append(k)
                visited[k]=True

n,m,v=map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고 >> 조건 존재
for j in range(n+1):
    graph[j].sort()

visited=[False]*(n+1)
dfs(graph, v, visited)
print()

visited2=[False]*(n+1)  # 기존 리스트때문에 한번 초기화 후 진행해야 함.
bfs(graph, v, visited2)