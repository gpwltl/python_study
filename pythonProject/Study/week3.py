#1 (defaultdict)
# - 딕셔너리에서 존재하지 않는 키를 조회하면 keyerror exception 발생
# -> defaultdict을 사용하면 키 에러가 안나는 게 아니라 해당 키에 대한 아이템을 딕셔너리에 추가하게 됨.
from collections import defaultdict
dic = defaultdict(int)
dic['죠르디']=10
dic['곰돌이']=3
print(dic)
print(dic['라이언'])
print(dic)
# print result
    # defaultdict(<class 'int'>, {'죠르디': 10, '곰돌이': 3})
    # 0
    # defaultdict(<class 'int'>, {'죠르디': 10, '곰돌이': 3, '라이언': 0})
dic.pop('죠르디')
print(dic)
# print result
    # defaultdict(<class 'int'>, {'곰돌이': 3, '라이언': 0})

dic2=defaultdict(list)
dic2['abc']=['123']
print(dic2)
dic2['abc'].append("456")
print(dic2)
# print result
    # defaultdict(<class 'list'>, {'abc': ['123']})
    # defaultdict(<class 'list'>, {'abc': ['123', '456']})

#2 (for문의 range)
n=14
for i in range(n):
    print(i) # 0~13