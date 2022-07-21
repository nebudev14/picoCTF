flag = "hello"
test = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag)-1, 2)])
print(test)


# flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"
for i in range(0, len(test)):
  print(chr((ord(test[i]) >> 8)))
  print(chr(ord(test[i])-(ord(test[i]) >> 8) >> 8))
  # print(((ord(test[i]))))
  
  # print(chr((ord(test[i]) - (ord(test[i]) >> 8)) >> 8))
  
  # print(chr(ord(flag[i+1]) >> 8))
  # print(flag[i] + ": " + str(i))
  # print(flag[i+1] + ": " + str(i+1))
  # print(chr(ord(flag[i])>>8))
  # print( (chr( ord(flag[i])>>8-(ord(flag[i+1])>>8)  )))
