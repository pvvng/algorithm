import sys
input = sys.stdin.readline

def sol(A):
  stats = [[0] * 5 for _ in range(3)]
  for a in A:
    f1, f2, f3 = a
    stats[0][f1] += 1
    stats[1][f2] += 1
    stats[2][f3] += 1

  scores = []
  for i in range(3):
    cnt = stats[i]
    score = cnt[1] + cnt[2]*2 + cnt[3]*3
    stats[i][0] = score
    stats[i][4] = i + 1
    scores.append(score)

  max_score = max(scores)
  cands = []
  for i in range(3):
    cnt = stats[i]
    if max_score == cnt[0]:
      cands.append(cnt)

  if len(cands) == 1:
    return f"{cands[0][4]} {max_score}"
  
  cands.sort(key=lambda x : (-x[3], -x[2]))
  if cands[0][3] > cands[1][3]:
    return f"{cands[0][4]} {max_score}"
  if cands[0][2] > cands[1][2]:
    return f"{cands[0][4]} {max_score}"
  return f"0 {max_score}"
  
n = int(input())
A = [tuple(map(int, input().split())) for _ in range(n)]
print(sol(A))