import sys
input = sys.stdin.readline

n = int(input())
ans = []
st = set()
all_set = set(range(1, 21))

def checkSet(num: int, st:set)->bool:
  return num in st

for _ in range(n):
  cmd = ""
  x = 0
  cmdx = input()
  if "all" in cmdx:
    st = all_set.copy()
    continue
  elif "empty" in cmdx:
    st.clear()
    continue

  cmd, x = cmdx.split()
  x = int(x)

  if cmd == "add":
    st.add(x)
  elif cmd == "remove":
    if checkSet(x, st):
      st.remove(x)
  elif cmd == "check":
    print(int(checkSet(x, st)))
  elif cmd == "toggle":
    if checkSet(x, st):
      st.remove(x)
    else:
      st.add(x)

