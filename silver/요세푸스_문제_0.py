n ,k = map(int, input().split())
table = list(range(1, n+1))

ans = []
base = 0
while(len(table) > 0):
  # base를 기준으로 k-1 만큼 떨어진 곳은 pop_index다
  # 다만, pop_index는 table의 length보다 클 수 있으므로 
  # % 을 통해 최대 크기를 table로 한정한다
  # 이전 pop_index는 다음 시행의 base가 된다
  pop_index = (base + k-1) % len(table)
  ans.append(table.pop(pop_index))
  base = pop_index

print(f"<{", ".join((map(str, ans)))}>")