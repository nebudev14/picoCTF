# decode_msg = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag)-1, 2)])

encoded = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"
flag = ""
for i in range(0, len(encoded)):
  char1 = ord(encoded[i]) >> 8
  flag += chr(char1)
  flag += chr(ord(encoded[i]) - (char1 << 8))

print(flag)