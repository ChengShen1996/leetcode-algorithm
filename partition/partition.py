import numpy as np
def swap(lis,left_idx,right_idx):
	temp = lis[left_idx]
	lis[left_idx] = lis[right_idx]
	lis[right_idx] = temp
def swap_seg(lis,left_idx,right_idx,small_idx,equal_idx):
	temp = lis[small_idx:equal_idx+1]

	lis[small_idx:small_idx+right_idx -equal_idx] = lis[equal_idx+1:right_idx+1]

	lis[small_idx+right_idx-equal_idx:right_idx+1] = temp
def partition(lis, left, right,pivot_idx):
	pivot_val = lis[pivot_idx]
	swap(lis,pivot_idx,right)
	store_idx = left
	equal_idx = right -1
	i = 0
	while(i<=equal_idx):
		print(i,store_idx,equal_idx)
		if lis[i]< pivot_val:
			swap(lis, store_idx, i)
			store_idx+=1
			i+=1
		elif lis[i] == pivot_val:
			swap(lis, equal_idx,i)
			equal_idx -=1
		else:
			i+=1
	swap_seg(lis,left,right,store_idx,equal_idx)
#	swap(lis,right,store_idx)
a= np.random.randint(low = 1, high = 100, size = 15)
tar_list = a.tolist()
#tar_list = [2,5,7,9,3,4,3,1,2,6,7] 
print(tar_list)
partition(tar_list,0,len(tar_list)-1,4)
print(tar_list)

