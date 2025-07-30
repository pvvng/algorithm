def sol(txt:str):
  ans = ""
  for char in txt:
    ans += char.upper() if char.islower() else char.lower()
  return ans

# print(sol(input()))

# 별 메서드가 다있네;
print(input().swapcase())