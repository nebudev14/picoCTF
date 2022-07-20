with open("data.txt", "r") as f:
  d = f.read()

for i in d.split("\n"):
  print(chr(int(i)), end="")