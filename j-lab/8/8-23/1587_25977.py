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

def sol(n, k, tree, cost):
  ans = 0
  # 특정 노드를 방문할 때 현재 상태를 저장
  visited = [set() for _ in range(n)]

  def dfs(cur, state, apple, peer):
    nonlocal ans
    if apple > k:
      return 

    if ans < peer:
      ans = peer
    
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
    
    cost[cur] = prev
  
  state = init_state(n)
  dfs(0, state, 0, 0)
  return ans

n, k = map(int, input().split())

tree = [[] for _ in range(n)]
for _ in range(n-1):
  p, c = map(int, input().split())
  tree[p].append(c)
  tree[c].append(p)

cost = list(map(int, input().split()))

print(sol(n, k, tree, cost))