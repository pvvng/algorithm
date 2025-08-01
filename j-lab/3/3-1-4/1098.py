def sol(A:list, B:list) -> list:
  ans = []
  for b in B:
    i, j = b[1], b[2]
    if b[0] == 1:
      k = b[3]
      for i in range(i, j+1):
        A[i] += k
    elif b[0] == 2:
      cnt = 0
      for i in range(i, j+1):
        cnt += A[i]
      ans.append(cnt)
  return ans

def get_splited_map(type) :
  return map(type, input().split())

n, m = get_splited_map(int)
A = list(get_splited_map(int))
B = [tuple(get_splited_map(int)) for _ in range(m)]

for e in sol(A, B):
  print(e)