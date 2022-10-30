from collections import deque

# DFS
visited=[False]*8   # 방문 정보를 기록하기 위한 리스트
                    # 1부터 파악할 수 있게 0을 포함한 F 개수만큼!! (0을 안쓰더라도)
graph=[
    [],         # 0
    [2, 3],     # 1
    [1, 4, 5],  # 2
    [1, 6],     # 3
    [2],        # 4
    [2],        # 5
    [3, 7],     # 6
    [6]         # 7
]

def DFS(v):
    visited[v]=True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

DFS(1)  # 1 2 4 5 3 6 7

##############
# BFS
visited2=[False]*8
graph2=[
    [],         # 0
    [2, 3],     # 1
    [1, 4, 5],  # 2
    [1, 6],     # 3
    [2],        # 4
    [2],        # 5
    [3, 7],     # 6
    [6]         # 7
]

def BFS(v):
    q=deque()
    q.append(v)
    while q:
        x=q.popleft()
        print(x, end=' ')
        for i in graph2[x]:
            if not visited2[i]:
                q.append(i)
                visited2[i]=True
BFS(1)  # 1 2 3 4 5 6 7

#######
# deque
#from collections import deque
dq=deque('love')
print(dq)   # deque(['l', 'o', 'v', 'e'])
dq.append('x')
dq.appendleft('y')
print(dq)   # deque(['y', 'l', 'o', 'v', 'e', 'x'])
print(dq.pop()) # x
print(dq.popleft()) # y


### 스터디
# 1번 노드는 2번, 3번 노드와 양방향 연결되어 있다.
# 2번 노드는 1번, 3번 노드와 양방향 연결되어 있다.
# 3번 노드는 1번, 2번 노드와 양방향 연결되어 있다.
