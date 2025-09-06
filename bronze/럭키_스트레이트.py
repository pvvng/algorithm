def sol(N, i, j, l, r):
  if i >= j:
    return "LUCKY" if l == r else "READY"
  l += int(N[i])
  r += int(N[j])
  return sol(N, i + 1, j - 1, l, r)
  
N = input()
print(sol(N, 0, len(N)-1, 0, 0))