our_str = "find the letter z"
index = 0
target = 'z'
if 'z' not in our_str:
	print("Character not found")
for i in range(len(our_str)):
	if target == our_str[i]:
		index = i
		print(index)
