def sol(S: str):
  S_len = len(S)
  st = set()
  for i in range(S_len):
    for j in range(S_len - i):
      st.add(S[j:(i + j + 1)])
  return len(st)

S = input()
print(sol(S))
