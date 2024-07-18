str = bytearray(b"capitalize")
target = ord('c')
for i in range(len(str)):
    if target == str[i]:
        str[i] = target - 32
        
print(str.decode())
