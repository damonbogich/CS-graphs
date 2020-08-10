class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set() #will hold edges  ## ex: a: (b, c) where b and c are neighbor vertices
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  #theres an edge from v1 --> v2 
        else:
            raise IndexError("nonexistent vert")
    
    def get_neighbors(self, vertex_id):
        return self.vertices(vertex_id)
    
    def bft(self, starting_vertex_id):
        #create an empty queue
        q = Queue()
        #create a set for the visited nodes
        visited = set()
        #Init: enqueue the starting node
        q.enqueue(starting_vertex_id)

        #while queue is not empty:
        while q.size() > 0:
            #dequeue first item
            v = q.dequeue()
            #if it is not visited:
            if v not in visted:
                #add it to visited set and add its neighbors to queue
                for next_vert in self.get_neighbors(v):
                    queue.enqueue(next_vert)


g = Graph()

g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')

g.add_edge('a', 'b') # a --> b
g.add_edge('a', 'c') # a --> c

g.add_edge('b', 'a')
g.add_edge('b', 'b')
g.add_edge('b', 'c')
