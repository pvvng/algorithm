def dp(a, k):
  D = [0] * (k + 1) # D[i]: a를 i로 변환하는 최소 연산 횟수
  # 출발점 a = 0, a+1 = 1
  for i in range(a+1, k+1):
    # 기본 전이: i를 만들려면 (i-1)에서 +1 연산을 한 번 더하면 되므로, 일단 D[i-1] + 1로 초기값을 둠
    D[i] = D[i-1] + 1 
    # i가 짝수이고, 그 절반(i//2)이 출발점 a 이상이면 i//2에서 *2로 올 수 있으니 그 경로도 고려하겠다는 조건
    if i % 2 == 0 and (i // 2) >= a: 
      D[i] = min(D[i], D[i//2] + 1)
  return D[k]

# 역방향 dp
def dp2(a, k):
  cnt = 0
  while a != k:
    cnt += 1
    if k % 2 == 0 and k // 2 >= a:
      k //= 2
    else:
      k -= 1 
  return cnt

# 최소 연산경로
def min_path(a, k):
  path = [k]
  while a < k:
    if k % 2 == 0 and k // 2 >= a:
      k //= 2
      path.append(k)
    else:
      k -= 1 
      path.append(k)
  path.reverse()
  return path

# a를 a보다 큰 가장 작은 소수로 변환하는 최소 연산 횟수
def sol(a):
  k = a + 1 # k가 주어지지 않고 직접 만듬
  while not is_prime(k):
    k += 1
  # dp 테이블 생성
  D = [0] * (k + 1)
  for i in range(a+1, k+1):
    D[i] = D[i-1] + 1
    if i % 2 == 0 and i // 2 >= a:
      D[i] = min(D[i], D[i//2] + 1)
  return D[k]

def is_prime(n):
  if n < 2:
    return False
  
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


# BFS
def bfs(a, k):
  q = [(a, 0)]
  idx = 0
  visited = set([a])
  dt = ["+", "*"]

  while idx < len(q):
    cur, dist = q[idx]
    idx += 1

    if cur == k:
      return dist

    for d in dt:
      if d == "+":
        nxt = cur + 1
        if nxt not in visited and nxt <= k:
          q.append((nxt, dist + 1))
          visited.add(nxt)
      elif d == "*":
        nxt = cur * 2
        if nxt not in visited and nxt <= k:
          q.append((nxt, dist + 1))
          visited.add(nxt)

a, k = map(int, input().split())
print(sol(a))