from datetime import datetime, timezone

now_utc = str(datetime.now(timezone.utc))
date = (now_utc.split(" ")[0].split("-"))
for x in date:
  print(x)
