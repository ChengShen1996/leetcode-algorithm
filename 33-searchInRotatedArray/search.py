from math import floor

a = [5,6,7,0,1,2,3,4]
b=[1,2,3,4,5,6,7,8]
target = 9
def findPovit(arr,s,e):
	print(s,e)
	if e==s:
		return s
	mid = floor((s+e)/2)
	if(arr[mid]>arr[e]):
		return findPovit(arr,mid+1,e)
	else:
		return findPovit(arr,s,mid)

def binarySearch(arr,s,e,val):
	print(s,e)
	if e == s:
		if(val!=arr[s]):
			return None
		else:
			return s
	mid = floor((s+e)/2)
	if(arr[mid]>=val):
		return binarySearch(arr,s,mid,val)
	else:
		return binarySearch(arr,mid+1,e,val)
pivot_index = findPovit(b,0,len(a)-1)
print(pivot_index)
if target<=b[-1]:
	print(binarySearch(b,pivot_index,len(b)-1,target))
else:
	print(binarySearch(b,0,pivot_index,target))

# tt = binarySearch(b,0,len(b)-1,4)
