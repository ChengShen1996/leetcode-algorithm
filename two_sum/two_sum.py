def twoSum(nums,target):
	list_len = len(nums)
	hash_table = {}
	for i in range(list_len):
		hash_table[target-nums[i]] = i
	for i in range(list_len):
		if nums[i] in hash_table:
			if i!= hash_table[nums[i]]:
				return [i,hash_table[nums[i]]]
print(twoSum([3,2,4],6))
