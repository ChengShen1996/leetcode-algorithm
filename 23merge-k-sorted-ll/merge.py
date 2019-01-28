from heapq import heapify, heappop, heappush
class ListNode:
	def __init__(self,x):
		self.val 	= x
		self.next 	= None
class MinHeap:
	def __init__(self):
		self.heap = []
		heapify(self.heap)
	def add(self,x):
		heappush(self.heap,x)
	def pop(self):
		return heappop(self.heap)
	def show(self):
		print(self.heap)
	def isEmpty(self):
		return len(self.heap)>0
def Traverse(a):
	temp = []
	i = a
	while(i!=None):
		print(i.val)
		temp.append(i.val)
		i = i.next
heap = MinHeap()
l1 = []
while(True):
	a = input()
	if(a=='end'):
		break
	b = a.split(' ')
	c = [int(x) for x in b]
	nextNode = None
	for i in range(len(c)-1,-1,-1):
		curNode = ListNode(c[i])
		if(nextNode):
			curNode.next = nextNode
		nextNode = curNode
	l1.append(nextNode)	








