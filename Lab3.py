from collections import defaultdict

class Graph:
	def __init__(self,vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def DLS(self,src,target,maxDepth):

		if src == target : return True

		if maxDepth <= 0 : return False

		for i in self.graph[src]:
				if(self.DLS(i,target,maxDepth-1)):
					return True
		return False

	
	def IDDFS(self,src, target, maxDepth):
		
		for i in range(maxDepth):
			if (self.DLS(src, target, i)):
				return True
		return False


n = int(input("Enter a number: "))
g = Graph(n)

choice = input("add edge? (y/n)")
while choice == 'y':
    src = int(input("Enter source node: "))
    dest = int(input("Enter destination node: "))
    g.addEdge(src, dest)
    choice = input("add edge? (y/n)")
    

target = int(input("Enter Target: "))
maxDepth = int(input("Enter Max Depth: "))
src = int(input("Enter source: "))

if g.IDDFS(src, target, maxDepth) == True:
	print ("Target is reachable from source " +
		"within max depth")
else :
	print ("Target is NOT reachable from source " +
		"within max depth")
