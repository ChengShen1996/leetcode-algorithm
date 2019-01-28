string = input("Enter your string: ")
n = input("Enter the # of rows: ")
n = int(n)
index = []
for i in range(n):
	index.append(i)
for i in range(n-2,0,-1):
	index.append(i)
print(index)
round_len = 2*n-2
string_len = len(string)
map_list = [None]* string_len
for i in range(string_len):
	temp = i % round_len
	map_list[i] = index[temp]
print(map_list)
result = ''
for i in range(round_len):
	for j in range(string_len):
		if map_list[j] ==i:
			result+=string[j]
print(result)

