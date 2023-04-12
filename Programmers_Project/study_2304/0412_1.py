# 덧칠하기
# 페인트가 칠해진 길이 n 미터인 벽 있음.
# m: 벽에 페인트를 칠하는 롤러의 길이
# section: 다시 페인트를 칠하기로 정한 구역들의 번호가 담긴 정수

# 8	4	[2, 3, 6]	2
# 5	4	[1, 3]	1
# 4	1	[1, 2, 3, 4]	4


n=8
m=4
section = [2, 3, 6]
answer = 1
temp = 0
start = section[0]

for i in section:
    if i <= start + (m-1):
        continue
    else:
        start = i
        temp = start + (m-1)
        answer += 1

print(answer)