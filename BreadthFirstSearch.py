#Author: pl9870
# Feel free to use this code and change as needed
# This code has an implementation of queues and BFS using adjacency matrices as undirected graphs
# sorry for not including a bfs method for adjacency lists...

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.visited = False

class Queue:
    def __init__(self):
        self.size = 0
        self.front = None
        self.back = None

    def enqueue(self, node):
        if self.size == 0:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            pass
        elif self.size == 1:
            self.front = None
            self.back = None
            self.size -= 1
        else:
            temp = self.fronts
            self.front = self.front.next
            temp.next = None
            self.size -= 1

#returns True if root can reach key, else returns False   Time: O(V^2) 
def bfs(graph, nodes, root, key):
    Q = Queue()
    Q.enqueue(root)
    root.visited = True
    node = root
    while not Q.size == 0:   #O(E)
        Q.dequeue()
        for n in neighbors(graph, nodes, node):
            if n.visited == False:
                Q.enqueue(n)
                n.visited = True
            if n == key:
                return True
            node = Q.front
    return False

def neighbors(graph, nodes, node):
    n = []
    for i, x in enumerate(node.data):
        if x == 1:
            n.append(nodes[i])
    return n

def create_nodes(graph):
    list = []
    for i in range(0, len(graph)):
        list.append(Node(graph[i]))
    return list       

#Showing the implementation cuz its weird
graph = [  
          [0,0],   #Node A
          [0,0]    # Node B
        ]

nodes = create_nodes(graph)  
print(bfs(graph, nodes, nodes[0], nodes[1])) 


