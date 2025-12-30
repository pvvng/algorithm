def sol(n, fruits):
  ans = 1

  Fdict = {}
  start = 0

  Fdict[fruits[start]] = 1
  # 길이를 길게 만들기 위해 back을 늘린다.
  for back in range(1, n):
    b = fruits[back]
    Fdict.setdefault(b, 0)
    Fdict[b] += 1
    # 만약 조건(과일 갯수는 2 이하)이 깨진다면 start를 움직여 회복시킨다.
    while len(Fdict) > 2:
      s = fruits[start]
      Fdict[s] -= 1
      if Fdict[s] <= 0:
        del Fdict[s]
      
      start += 1
    ans = max(ans, back - start + 1)

  return ans

n = int(input())
fruits = list(map(int, input().split()))
print(sol(n, fruits))