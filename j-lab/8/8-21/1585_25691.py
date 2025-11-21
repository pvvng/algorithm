import sys
input = sys.stdin.readline

def init_state(n):
  return "0" * n

def count_state(state):
  return state.count("1")

def update_state(state, idx, goto = 1):
  ls = list(state)
  ls[idx] = str(goto)
  return "".join(ls)

def sol(n, k, tree, cost):
  # visited[i]
  # i에 도달했을때 state 저장
  visited = [set() for _ in range(n)]

  ans = 0

  def dfs(cur, state, apple):
    if count_state(state) == k:
      nonlocal ans
      if ans < apple:
        ans = apple
      return 

    visited[cur].add(state)

    new_apple = apple
    if cost[cur] == 1 and state[cur] == "0":
      new_apple += 1

    ns = update_state(state, cur)

    for nxt in tree[cur]:
      if ns not in visited[nxt]:
        dfs(nxt, ns, new_apple)

  state = init_state(n)
  dfs(0, state, 0)

  return ans

n, k = map(int, input().split())

tree = [[] for _ in range(n)]
for _ in range(n-1):
  p, c = map(int, input().split())
  tree[p].append(c)
  tree[c].append(p)

cost = list(map(int, input().split()))
print(sol(n, k, tree, cost))
