s = ["Soongsil", "Korea", "Hanyang"]
A = list(map(int, input().split()))
if sum(A) >= 100:
  print("OK")
else:
  mn = min(A)
  for i in range(3):
    if A[i] == mn:
      print(s[i])
      break