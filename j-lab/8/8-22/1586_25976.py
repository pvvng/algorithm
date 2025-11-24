import sys
input = sys.stdin.readline

def init_state(n):
  return "0" * n

def update_state(n, state, idx):
  new_state = ""
  for i in range(n):
    if i == idx:
      new_state += "1"
      continue
    new_state += state[i]
  return new_state

def count_state(state):
  return state.count("1")

def sol(n, k, tree, cost):
  visited = [set() for _ in range(n)]
  state = init_state(n)
  ans = (-1, 0, 0)

  def dfs(cur, state, apple, peer):
    if count_state(state) == k:
      nonlocal ans
      mul = apple * peer
      cand = (mul, apple, peer)
      
      # 갱신 조건:
      # 1) 곱이 더 크면 갱신
      # 2) 곱이 같으면 사과(apple)가 더 많으면 갱신
      # 3) 사과도 같으면 배(peer)가 더 많으면 갱신
      # 튜플 비교
      if cand > ans:
        ans = cand
      return 

    new_state = update_state(n, state, cur)
    visited[cur].add(new_state)

    prev = cost[cur]
    cost[cur] = 0
    # 사과, 배 추가
    if prev == 1:
      apple += 1
    elif prev == 2:
      peer += 1

    for nxt in tree[cur]:
      if new_state not in visited[nxt]:
        dfs(nxt, new_state, apple, peer)

    cost[cur] = prev # 백트래킹

  dfs(0, state, 0, 0)

  return f"{ans[1]} {ans[2]}"

n, k = map(int, input().split())

tree = [[] for _ in range(n)]
for _ in range(n-1):
  p, c = map(int, input().split())
  tree[p].append(c)
  tree[c].append(p)

cost = list(map(int, input().split()))
print(sol(n, k, tree, cost))