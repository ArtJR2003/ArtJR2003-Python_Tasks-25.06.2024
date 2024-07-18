str = "reverse me"
reversed_str = ""
for i in range(len(str) - 1, -1, -1):
    reversed_str += str[i]
print(reversed_str)
