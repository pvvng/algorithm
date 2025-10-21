import sys
input = sys.stdin.readline

def create_dict(A):
  d = {}
  d.setdefault(" ".join(["-"] * 3), len(A))

  for a in A:
    cur = " ".join(a)
    d.setdefault(cur, 0)
    d[cur] += 1

    for i in range(3):
      slot = ["-"] * 3
      slot[i] = a[i]
      cur = " ".join(slot)

      d.setdefault(cur, 0)
      d[cur] += 1

      for j in range(i+1, 3):
        if i == j:  continue
        slot[j] = a[j]
        cur = " ".join(slot)

        d.setdefault(cur, 0)
        d[cur] += 1

        slot[j] = "-" # backtracking
  return d

def sol(A, B):
  d = create_dict(A)
  ans = []
  for b in B:
    x = d.get(b)
    if x == None:
      ans.append(str(0))
    else:
      ans.append(str(x))
  return ans

n, m = map(int, input().split())
A = [input().split() for _ in range(n)]
B = [input().strip() for _ in range(m)]
print("\n".join(sol(A, B)))