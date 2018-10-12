def longstring(s):
	idx_start = 0
	idx_end = 1
	max_len = 1
	cur_str = ''
	str_len = len(s)
	if(str_len ==0):
		return 0
	cur_str = s[idx_start:idx_end]
	while idx_end < str_len:
		print(idx_start,idx_end)
		if s[idx_end] in cur_str:
			idx_repeat = cur_str.find(s[idx_end])
			idx_start = idx_start + idx_repeat +1
			cur_str = s[idx_start:idx_end+1]
			idx_end +=1


		else:
			idx_end +=1
			cur_str = s[idx_start:idx_end]
			if len(cur_str) > max_len :
				max_len = len(cur_str) 

	return max_len

s =input() 
print(longstring(s))
