import math
p, q, s = map(int, input().split())
gcd = math.gcd(p, q)
lcm = p * q // gcd  
print("yes" if s >= lcm else "no")