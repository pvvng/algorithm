def sol(S:str):
  if S.startswith('"') and S.endswith('"'):
    ans = S[1:len(S) - 1]
    if ans.strip() == "":
      return "CE"
    return ans
  return "CE"

S = (input())
print(sol(S))