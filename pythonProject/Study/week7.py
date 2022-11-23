##1 정렬
from collections import defaultdict
arr = [4, 10, 100, 1000, 100000]
event = defaultdict(int)
for i in arr:
    event[i] += 1
print(event)
# 딕셔너리의 Value 기준으로 큰 값부터 작은 값부터 정렬, Value가 같다면 Key순으로 정렬
res = sorted(event.items(), key=lambda x: (x[1], x[0]), reverse=True)
print(res, end = ' ')

