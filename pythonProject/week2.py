res=str(funAvg(y))+"/"+str(x)
print(res, end='')
# 1) end='' : 띄어쓰기 없이 print

print("%s %.2f" % (key, val))
# 2) print할때 %s: str, %f: float, %.2f: 소수점 2자리까지, %d: digit 숫자(정수)

if nx >= 0 and nx < n and ny >= 0 and ny < n:   # n을 기준으로 했어야지!!
    # mat[nx][ny] += 1
    count+=1 # 바로 카운트 세서 결과 내기
# 3) 기준 값 확인 + 해당 그림(2차원 배열)을 출력할 필요 없을땐 count에만 집중하기(쓸데없는 시간 버리지 않기)