import sys
input = sys.stdin.readline

n = int(input())
X = list(map(int, input().split()))
sorted_X = sorted(list(set(X)))

d = {}
idx = 0
for e in sorted_X:
  d.setdefault(e, idx)
  idx += 1

ans = []
for x in X:
  ans.append(str(d.get(x)))

print(" ".join(ans))