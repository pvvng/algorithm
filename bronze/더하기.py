import sys
input = sys.stdin.readline
ans = []
for _ in range(int(input())):
  n = int(input())
  ans.append(str(sum(list(map(int, input().split())))))
print("\n".join(ans))