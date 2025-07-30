def init(A: list):
  d = dict()
  for a in A:
    key, value = map(str, a.split("="))
    d[key.strip()] = value.strip()
  return d

def sol(K:int, S:list, D: dict):
  new_S = []
  for i in range(int(K)):
    c = S[i]
    new_S.append(D[c])
  return " ".join(new_S)

N = int(input())
A = [input() for _ in range(N)]
D = init(A)

for _ in range(int(input())):
  ans = sol(int(input()), input().split(), D)
  print(ans)
