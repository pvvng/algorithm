def sol():
  for i in range(n):
    for j in range(n):
      x, y = A[i]; p, q = A[j]
      # 자신보다 확실이 큰 사람이 있으면 순위 미루기
      if x < p and y < q: 
        ans[i] += 1

n = int(input())
A = list(tuple(map(int, input().split())) for _ in range(n))
ans = [1] * n
sol()
print(*ans)