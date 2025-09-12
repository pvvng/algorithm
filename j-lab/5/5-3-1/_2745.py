def get_nums():
  d = dict()
  for i in range(26):
    d.setdefault(chr(ord("A") + i), i + 10)
  for i in range(10):
    d.setdefault(str(i), i)
  return d

def sol(N, B):
  N = list(N)
  d = get_nums()
  dt = ans = 0
  while len(N) > 0:
    # 기존 ans를 B 배 해주고 마지막 자리에 pop한 요소 집어넣기
    ans =  ans * B + d[N.pop()]
    dt += 1
  return ans

N, B = map(str, input().split())
B = int(B)
print(sol(N, B))
