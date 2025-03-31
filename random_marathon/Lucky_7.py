# Print 0 if the number does not contain 7 and is not divisible by 7.
# Print 1 if the number does not contain 7 but is divisible by 7.
# Print 2 if the number does contain 7 but is not divisible by 7.
# Print 3 if the number does contain 7 and is divisible by 7.

def isLucky(num):
  divisible = isDivisible(num)
  contain = isContain(num)

  return divisible + contain

def isDivisible(num) :
  if(num % 7 == 0):
    return 1
  else:
    return 0

def isContain(num) :
  if("7" in str(num)):
    return 2
  else:
    return 0
  
num = int(input())
print(isLucky(num))