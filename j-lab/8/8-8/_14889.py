import sys
input = sys.stdin.readline

def comb(iter, k):
  res = []
  path = []

  def dfs(start):
    if len(path) == k:
      res.append(path[:])
      return 
    
    for i in range(start, len(iter)):
      path.append(iter[i])
      dfs(i + 1)
      path.pop()
  
  dfs(0)
  return res

def get_link_team(n, st):
  visited = [False] * (n+1)
  for s in st:
    visited[s] = True
  lt = [i for i in range(1, n+1) if not visited[i]]

  return lt

def get_score(team, S):
  score = 0
  for i in range(len(team)):
    for j in range(i + 1, len(team)):
      score += S[team[i]-1][team[j]-1] + S[team[j]-1][team[i]-1]
  return score

def sol(n, S):
  # n // 2로 가능한 모든 팀 조합 구하기
  nums = [i for i in range(1, n + 1)]
  teams = comb(nums, n // 2)

  record = set()
  ans = []
  for st in teams:
    # 역순 팀 조합은 고려하지 않음
    if tuple(st) in record:
      continue

    lt = get_link_team(n, st)

    # 조합 기록
    record.add(tuple(st))
    record.add(tuple(lt))

    dff = get_score(st, S) - get_score(lt, S)
    ans.append(abs(dff))
  
  return min(ans)
    
n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]
print(sol(n, S))