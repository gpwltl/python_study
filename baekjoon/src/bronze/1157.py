from collections import defaultdict
dic=defaultdict(int)
# inp = input()
inp='zZd'

for i in inp:
    dic[i.upper()] += 1

max_keys = [key for key, value in dic.items() if value == max(dic.values())]

if(len(max_keys) > 1):
    print("?")
else:
    print(max_keys[0])