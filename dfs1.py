class DFS:
    def __init__(self,n):
        self.n=n
        self.n=range(self.n)
        self.adj_list={node:set() for node in self.n}
    def add_edge(self,n1,n2):
        self.adj_list[n1].add(n2)
    def dfs(self,start,target,path=[],visited=set()):
        path.append(start)
        visited.add(start)
        if(start==target):
            return path
        for adj in self.adj_list[start]:
            if adj not in visited:
                result=self.dfs(adj,target,path,visited)
                if result is not None:
                    return result
        path.pop()
        return None
n=int(input("enter rhe no.of nodes:"))
graph=DFS(n)
x=int(input("enter no.of edges:"))
print("enter the edge one after the other:")
for i in range(x):
    a,b=map(int,input().split())
    graph.add_edge(a,b)
s=int(input("enter the no.of nodes to be searched:"))
while s:
    st,tar=map(int,input("enter the start and target nodes:").split())
    path=[]
    path=graph.dfs(st,tar,path=[],visited=set())
    if path==None:
        print("not found")
    else:
        print("path found")
        print("the required path is:",path)
    s=s-1
