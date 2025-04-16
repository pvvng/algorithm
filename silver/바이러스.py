import sys
input = sys.stdin.readline

x = int(input())
n = int(input())

nodes = {}

for i in range(1, x+1):
  nodes.setdefault(i, [])

for _ in range(n):
  num, nxt = map(int, input().split())
  nodes[num].append(nxt)
  # 재귀 호출의 깊이를 줄이기 위해선 양방향 연결을 시켜야한다
  nodes[nxt].append(num)

infected_nodes = set()
start_node_idx = 1

def dfs(nums:int, nodes:dict, infected_nodes:set):
  nxt_nodes = nodes[nums]
  infected_nodes.add(nums)
  for nxt in nxt_nodes:
    if nxt not in infected_nodes:
      dfs(nxt, nodes, infected_nodes)

dfs(start_node_idx, nodes, infected_nodes)
infected_nodes.remove(start_node_idx)
print(len(infected_nodes))