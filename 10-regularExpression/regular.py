string = input("Enter your string: ")
pattern = input("Enter your pattern: ")

n = len(string)-1
stack_string = []
stack_pattern = []
while(n>=0):
	i = n
	while(string[i] == string[n]):
		i-=1
	stack_string.append(string[i+1:n+1])
	n=i
# Tokenize the input string

print(stack_string)

n = len(pattern)-1
while(n>=0):
	if pattern[n] == '.':
		stack_pattern.append(pattern[n:n+1])
		n-=1
	elif pattern[n] =='*':
		print(n)
		stack_pattern.append(pattern[n-1:n+1])
		n-=2
	else:
		i = n
		while(pattern[i]==pattern[n]):
			i-=1
		stack_pattern.append(pattern[i+1:n+1])
		n=i
print(stack_pattern)