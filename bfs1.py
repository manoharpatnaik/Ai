from queue import Queue
class BFS:
    def __init__(self,n):
        self.n=n
        self.nodes=range(self.n)
        self.adj_list={node:set() for node in self.nodes}
    def add_edge(self,n1,n2):
        self.adj_list[n1].add(n2)
    def bfs(self,start,target):
        visited=set()
        queue=Queue()
        queue.put(start)
        visited.add(start)
        parent=dict()
        parent[start]=None
        path_found=False
        while not queue.empty():
            current_node=queue.get()
            if current_node==target:
                path_found=True
                break
            for next_node in self.adj_list[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    parent[next_node]=current_node
                    visited.add(next_node)
        path=[]
        if path_found:
            path.append(target)
            while parent[target]is not None:
                path.apppend(parent[target])
                target=parent[target]
            path.reverse()
        return path
n=int(input("enter the no.of nodes:"))
graph=BFS(n)
x=int(input("enter the no.of edges:"))
print("enter the dge one after the other:")
for i in range(x):
    a,b=map(int,input().split())
    graph.add_edge(a,b)
s=int(input("enter the no.of nodes to be searched:"))
while s:
    st,tar=map(int,input("enter the start and end node:").split())
    path=[]
    path=graph.bfs(start,target)
    if len(path)==0:
        print("path not found:")
    else:
        print("path found")
        print("required path is:",path)
    s=s-1
