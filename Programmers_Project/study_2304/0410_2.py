# 추억 점수
# name: 그리워하는 사람의 이름을 담은 문자열 배열
# yearning: 각 사람별 그리움 점수를 담은 정수 배열
# photo: 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열

# ["kali", "mari", "don"]	[11, 1, 55]	[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]	[67, 0, 55]
# ["may", "kein", "kain", "radi"]	[5, 10, 1, 3]	[["may"],["kein", "deny", "may"], ["kon", "coni"]]	[5, 15, 0]

name=["kali", "mari", "don"]
yearning=[11, 1, 55]
photo=[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
# answer = 	[67, 0, 55]

answer = []
d = dict()

for i in range(len(name)):
    d[name[i]] = yearning[i]

# dictionary = dict(zip(name, yearning))
# print(dictionary)

for j in photo:
    ans = 0
    for k in j:
        if k in d:
            ans+=d[k]
    answer.append(ans)
print(answer)