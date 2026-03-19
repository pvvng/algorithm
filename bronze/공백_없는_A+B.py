txt = input()

if len(txt) < 3:
  print(int(txt[:1]) + int(txt[1:]))
else:
  ofs = "".join(txt.split("10"))
  if ofs != "":
    ofs = int(ofs)
  else:
    ofs = 0
  print(txt.count("10") * 10 + int(ofs))