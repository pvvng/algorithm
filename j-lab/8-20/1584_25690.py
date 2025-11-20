import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 이웃한 두 정점을 white, black 또는 white, white로 색칠해야 한다
def sol(n, tree, weight):
  # white -> 0, black -> 1
  dp = [[-1, -1] for _ in range(n)]

  # dp[cur][color]에 도달할 때 가중치 최소합을 반환한다.
  def dfs(state: tuple, tree: list, weight: list, dp: list):
    cur, color = state

    # 이미 해당 위치의 값이 등록되어 있으면 해당 값을 사용한다.
    if dp[cur][color] != -1:
      return dp[cur][color]

    # 기본값을 더한다.
    dp[cur][color] = weight[cur][color]

    # 자식 노드를 찾는다.
    children = tree[cur]
    for child in children:
      # color가 white(0)
      # 자식은 black. white 둘 다 가능함
      if color == 0:
        dp[cur][color] += min(dfs((child, 0), tree, weight, dp), dfs((child, 1), tree, weight, dp))
      # color가 black(1)
      # 자식은 white만 가능함
      else:
        dp[cur][color] += dfs((child, 0), tree, weight, dp)

    # 해당 자리의 색칠이 완료되면 값 반환
    return dp[cur][color]
  
  return min(dfs((0, 0), tree, weight, dp), dfs((0, 1), tree, weight, dp))

n = int(input())

tree = [[] for _ in range(n)]
for _ in range(n-1):
  p, c = map(int, input().split())
  tree[p].append(c)

weight = [(0, 0) for _ in range(n)]
for i in range(n):
  weight[i] = tuple(map(int, input().split()))

print(sol(n, tree, weight))