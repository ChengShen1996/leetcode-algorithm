
input_string = input("Please enter the string: ")
# input_string = "vaomxdtiuwqlwhgutkhxxhccsgvyoaccuicgybnqnslogtqhblegfudagpxfvjdacsxgevvepuwthdtybgflsxjdmmfumyqgpxatvdypjmlapccaxwkuxkilqqgpihyepkilhlfkdrbsefinitdcaghqmhylnixidrygdnzmgubeybczjceiybowglkywrpkfcwpsjbkcpnvfbxnpuqzhotzspgebptnhwevbkcueyzecdrjpbpxemagnwmtwikmkpqluwmvyswvxghajknjxfazshsvjkstkezdlbnkwxawlwkqnxghjzyigkvqpapvsntojnxlmtywdrommoltpbvxwqyijpkirvndwpgufgjelqvwffpuycqfwenhzrbzbdtupyutgccdjyvhptnuhxdwbmdcbpfvxvtfryszhaakwshrjseonfvjrrdefyxefqfvadlwmedpvnozobftnnsutegrtxhwitrwdpfienhdbvvykoynrsbpmzjtotjxbvemgoxreiveakmmbbvbmfbbnyfxwrueswdlxvuelbkrdxlutyukppkzjnmfmclqpkwzyylwlzsvriwomchzzqwqglpflaepoxcnnewzstvegyaowwhgvcwjhbbstvzhhvghigoazbjiikglbqlxlccrwqvyqxpbtpoqjliziwmdkzfsrqtqdkeniulsavsfqsjwnvpprvczcujihoqeanobhlsvbzmgflhykndfydbxatskf"
def calculate(index_i,index_j,n):
	return index_i*n + index_j
n = len(input_string)
matrix = [None] * n * n
for i in range(n):
	ind = calculate(i,i,n)
	matrix[ind] = True
for i in range(n-1):
	ind = calculate(i,i+1,n)
	if(input_string[i] == input_string[i+1]):
		matrix[ind] = True
	else:
		matrix[ind] = False

for i in range(n):
	temp = []
	for j in range(n):
		temp.append(matrix[calculate(i,j,n)])
	print(temp)
print(input_string)

def retrive(i,j,n):
	if i<0| j>n-1:
		return False
	else:
		if matrix[calculate(i,j,n)] !=None:
			return matrix[calculate(i,j,n)]
		else:
			temp = retrive(i+1,j-1,n)
			equal = input_string[i] == input_string[j]
			matrix[calculate(i,j,n)] = temp&equal
			return matrix[calculate(i,j,n)]
			# return temp&equal
# for i in range(n):
# 	for j in range(i,n):
# 		if matrix[calculate(i,j,n)] ==None:
# 			matrix[calculate(i,j,n)] = retrive(i,j,n)

for k in range(n):
	print(k)
	i=k
	j=k 
	while i-1>=0 and j+1<n:
		ind_2 = calculate(i-1,j+1,n)
		ind_1 = calculate(i,j,n)
		print(i,j,ind_1,ind_2,n)

		if matrix[ind_2] ==None:
			temp = matrix[ind_1]
			equal = input_string[i-1]==input_string[j+1]
			matrix[ind_2] = temp & equal
		i-=1
		j+=1
	i=k
	j=k+1 
	while i-1>=0 and j+1<n:
		ind_2 = calculate(i-1,j+1,n)
		ind_1 = calculate(i,j,n)
		print(i,j,ind_1,ind_2,n)

		if matrix[ind_2] ==None:
			temp = matrix[ind_1]
			equal = input_string[i-1]==input_string[j+1]
			matrix[ind_2] = temp & equal
		i-=1
		j+=1

for i in range(n):
	temp = []
	for j in range(n):
		temp.append(matrix[calculate(i,j,n)])
	print(temp)

max_len = 0
max_i  = 0
max_j = 0
for i in range(n):
	for j in range(i,n):
		result = matrix[calculate(i,j,n)]
		if(result):
			if j-i>max_len:
				max_i,max_j,max_len = i,j,j-i
print(max_len)
print(max_i)
print(max_j)
print(input_string)
print(input_string[max_i:max_j+1])

# for i in range(n):
# 	temp = []
# 	for j in range(n):
# 		temp.append(matrix[calculate(i,j,n)])
# 	print(temp)
