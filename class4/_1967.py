import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 원과 비슷하다. 원 내부의 임의의 점에서 가장 먼 점을 하나 찾고
# 해당 점에서 원 위의 가장 먼 점을 찾으면 두 점을 연결했을 때 원의 지름이 되듯
# 트리 또한 임의의 한 노드에서 가장 먼 노드를 찾고 해당 노드에서 
# 다시 가장 먼 노드를 찾아주면 해당 노드까지의 거리가 트리의 지름이 된다.
# 문제에서 제시해 준 원의 그림 자체가 일종의 힌트였던 것
def dfs(n, start, nodes):
  visited = [False] * (n+1)

  def recur(cur, nodes, total):
    ret = (cur, total)
    
    for nxt, w in nodes[cur]:
      if visited[nxt]:
        continue
      visited[nxt] = True
      res = recur(nxt, nodes, total + w)
      if res[1] > ret[1]:
        ret = res

    return ret
  
  visited[start] = True
  return recur(start, nodes, 0)

# 루트에서 가장 먼 노드 A를 구한다
# A에서 가장 먼 노드 B를 구한다
def sol(n: int, nodes: list):
  A = dfs(n, 1, nodes)
  B = dfs(n, A[0], nodes)
  return B[1]

n = int(input())
nodes = [[] for _ in range(n + 1)]
for _ in range(n-1):
  p, c, w = map(int, input().split())
  nodes[p].append((c, w))
  nodes[c].append((p, w))

print(sol(n, nodes))