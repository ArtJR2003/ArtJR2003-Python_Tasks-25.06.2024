str = "find the letter z"
index = 0
for i in range(len(str)):
    if 'z' in str:
        index = i
    else:
        print("Character not found")
print("index of z is:", index)
