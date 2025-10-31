n = 5
A = [3, 5, 1, 2, 8]

# 누적합
B = [0] * n
for i in range(n):
  B[i] = B[i-1] + A[i]

# 구간합 
r = (2, 4)
# print(B[r[1]] - B[r[0] - 1])

# 구간 업데이트
# (start, end, d)
r1 = (1, 3, 2)
r2 = (0, 2, 3)
r3 = (1, 4, 1)

# 누적합 사용 x
CA = (A)
for i in range(r1[0], r1[1] + 1):
  CA[i] = CA[i] + r1[2]
# print(CA)

for i in range(r2[0], r2[1] + 1):
  CA[i] = CA[i] + r2[2]
# print(CA)

for i in range(r3[0], r3[1] + 1):
  CA[i] = CA[i] + r3[2]
# print(CA)

# 누적합 
CB = [0] * n
CB[r1[0]] += r1[2]
CB[r1[1] + 1] -= r1[2]
print(CB)

CB[r2[0]] += r2[2]
CB[r2[1] + 1] -= r2[2]
print(CB)

CB[r3[0]] += r3[2]
# CB[5] 는 존재하지 않으므로 안빼도 됨
# CB[r3[1] + 1] -= r3[2]
print(CB)

A = [3, 5, 1, 2, 8]
for i in range(1, n):
  CB[i] = CB[i-1] + CB[i]
for i in range(n):
  A[i] += CB[i]
print(A)