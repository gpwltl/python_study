res=str(funAvg(y))+"/"+str(x)
print(res, end='')
# 1) end='' : 띄어쓰기 없이 print

print("%s %.2f" % (key, val))
# 2) print할때 %s: str, %f: float, %.2f: 소수점 2자리까지, %d: digit 숫자(정수)

if nx >= 0 and nx < n and ny >= 0 and ny < n:   # n을 기준으로 했어야지!!
    # mat[nx][ny] += 1
    count+=1 # 바로 카운트 세서 결과 내기
# 3) 기준 값 확인 + 해당 그림(2차원 배열)을 출력할 필요 없을땐 count에만 집중하기(쓸데없는 시간 버리지 않기)

#########
# study
## 1) 복잡한 입력과 출력- 함수 없이 for문으로 한 문제에서 테스트케이스 여러가지 동작 가능
n = int(input())
for _ in range(n):

## 2) 출력: 문자열과 상수 한번에
print("%d/%d"%(cnt, n))

## 3) str은 list로 안만들고 바로 리스트처럼 글자간 비교 가능
arr=input()
for a in arr:

## 4) 이차원 배열 만들기
rows = 10
cols = 5
arr = [[0] * cols] * rows
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

## 5) cmp_to_key() : 커스텀한 기준으로 sort()하기.
from functools import cmp_to_key
def cmp(a, b):
    if a[0]==b[0]:	# 같은 값이면 다음 글자가 큰걸로
        return a[1]<b[1]
    else:
        return a[0]<b[0]	#아니면 그냥 정렬 크던게

sorted_arr=sorted(arr, key=cmp_to_key(cmp))