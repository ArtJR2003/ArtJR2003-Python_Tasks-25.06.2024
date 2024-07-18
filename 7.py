str1 = bytearray(b"banana")
target = ord('a')
for i in range(len(str1)):
    if target == str1[i]:
        str1[i] = ord('x')
        
print(str1.decode())
