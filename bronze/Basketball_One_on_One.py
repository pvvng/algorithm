# 점수가 10-10 동점일 경우, 이전 규칙은 "2승" 규칙으로 대체됩니다. 첫 번째 선수가 최소 2점 이상 앞서면 승리합니다.



game = list(input())
d = {"A": 0, "B": 0}

for i in range(0, len(game) - 1, 2):
  player, score = game[i], game[i+1]
  d[player] += int(score)

if d["A"] > d["B"]:
  print("A")
else:
  print("B")  
