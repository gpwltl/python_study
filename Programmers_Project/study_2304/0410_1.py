# 달리기 경주
# 현재 달리는 순서 : players
# 해설진이 부르는 이름 : callings
# ans => 1등부터 등수 순새대로 배열에 담아 return

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
# result = ["mumu", "kai", "mine", "soe", "poe"]
answer = []

player_dict = {player : index for index, player in enumerate(players)}
idx_dict = {index:player for index, player in enumerate(players)}

for calling in callings:
    cur_idx = player_dict[calling]
    front_player = idx_dict[cur_idx-1]

    idx_dict[cur_idx-1], idx_dict[cur_idx] = idx_dict[cur_idx], idx_dict[cur_idx-1]
    player_dict[calling], player_dict[front_player] = player_dict[front_player], player_dict[calling]

answer = sorted(player_dict, key=player_dict.get)
print(answer)