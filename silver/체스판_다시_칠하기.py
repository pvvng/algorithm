# n => h(열), m => w(행)
n, m = map(int, input().split())

board:list[str] = []
for _ in range(n):
  board.append(list(input()))

def rev_color(color) -> str:
  if color == "B":
    return "W"
  return "B"

mx = []

for i in range (n - 7):
  for j in range (m - 7):
    # 시작 범위에 맞게 8X8 체스판 만들기
    chess = [v[j: j + 8] for v in board[i : i + 8]]
    # 시작 지점이 B, W인 경우 모두 확인
    for s in ["B", "W"]:
      cnt = 0
      for l_index in range(len(chess)):
        evens = chess[l_index][0::2]
        odds = chess[l_index][1::2]
        # line_index가 짝수인 경우, 홀수인 경우 나눠서 생각하기
        if l_index % 2 == 0 :
          # 색칠해야할 칸의 개수 세기
          cnt += (evens.count(rev_color(s)) + odds.count(s))
        else:
          cnt += (evens.count(s) + odds.count(rev_color(s)))
      mx.append(cnt)

print(min(mx))