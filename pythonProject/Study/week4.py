##1. global 변수
park=[[0 for _ in range(n + 1)] for _ in range(n + 1)]
def isColored():
    global park
# => isColored 함수에서 위에 선언한 park를 그대로 사용 가능

##2. max
## 0보다 작은 값이 나오면 무조건 0으로 판단.
park[i][j]=max(0, park[i][j] - update[i][j])

##3. dq[-1]
from collections import deque
dq=deque()
dq.append(0)
dq.append(2)
dq.append(1)
print(dq[-1])  # 1