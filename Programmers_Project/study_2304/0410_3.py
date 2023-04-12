# 공원 산책
# park: 공원을 나타내는 문자열 배열
# routes : 공원을 나타내는 문자열 배열

# ["SOO","OOO","OOO"]	["E 2","S 2","W 1"]	[2,1]
# ["SOO","OXX","OOO"]	["E 2","S 2","W 1"]	[0,1]
# ["OSO","OOO","OXO","OOO"]	["E 2","S 3","W 1"]	[0,0]

park = ["SOO","OXX","OOO"]
routes = ["E 2","S 2","W 1"]

start_i = 0
start_j = 0

w=len(park[0])
h=len(park)

for i, val1 in enumerate(park):
    for j, val2 in enumerate(val1):
        if (val2 == 'S'):
            start_i = i
            start_j = j
            break

for route in routes:
    move_i = start_i
    move_j = start_j
    for k in range(int(route[2])):
        if route[0] == 'E' and start_j + (k+1) < w and park[start_i][start_j + (k+1)] != 'X':
            move_j += 1
            if k == int(route[2])-1:
                start_j = move_j
        elif route[0] == 'S' and start_i + (k+1) < h and park[start_i + (k+1)][start_j] != 'X':
            move_i += 1
            if k == int(route[2])-1:
                start_i = move_i
        elif route[0] == 'W' and start_j - (k+1) >= 0 and park[start_i][start_j - (k+1)] != 'X':
            move_j -= 1
            if k == int(route[2])-1:
                start_j = move_j
        elif route[0] == 'N' and start_i - (k+1) >= 0 and park[start_i - (k+1)][start_j] != 'X':
            move_i -= 1
            if k == int(route[2])-1:
                start_i = move_i
        else:
            break

print([start_i, start_j])