# my_list = ['1','2','3']

# last = my_list[len(my_list) - 1]
# print(last)

# print(my_list.copy())

# neighbors = {'2', '3'}


# combined_list = []
# for i in range(len(neighbors)):
#     list_neighbors = list(neighbors)

#     combined_list.append(my_list.copy())
#     combined_list[i].append(list_neighbors[i])

# print(combined_list)



"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  #all of the nodes

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() #initialized new vertex with an empty set
                                         #empty set will then take the connected vertices

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            IndexError('vertex does not exist')       #self.vertices = dictionary
                                        #self.vertices[v1] = set() {v1: {v2}, v2: {}}

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #need an empty queue (next nodes to visit) and an empty set (already visited nodes):
        q = Queue()
        visited = set()

        #enqueue first vertex
        q.enqueue(starting_vertex)

        #loop as long as queue is not empty
        while q.size() > 0:
            #dequeu from queue:
            v = q.dequeue()
            print('v', v)
            
            #if dequeued item not in visited:
            if v not in visited:
                #add it to visited
                visited.add(v)
                print('visited',visited)
                print(v)
                #add it's neighbors to queue
                neighbors = self.get_neighbors(v)

                for neighbor in neighbors:
                    q.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()

        s.push(starting_vertex)

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                neighbors = self.get_neighbors(v)
                for neighbor in neighbors:
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create an empty queue and enqueue the path to the starting vertex
        q = Queue() #empty q

        q.enqueue([starting_vertex]) #[['1']]
        #create set to store visited
        visited = set() #{}
        #while queue is not empty:
        while q.size() > 0:
            #dequeue the first path
            removed_path = q.dequeue() #['1']
            #grab last vertex value from the path
            last_vert_value = removed_path[len(removed_path) - 1] #'1'
            #vertex that was pulled out
            last_vert = self.vertices[last_vert_value] #{} empty set

            #if the vertex has not been visited:
            if last_vert not in visited:
                #if it is the destination_index:
                if last_vert == destination_vertex:
                    #return the path
                    return removed_path
                #mark it as visited
                visited.add(last_vert_value) ###

                #then add a path to its neighbors to the back of the queue
                neighbors = self.get_neighbors(last_vert_value) #returns set of neighbors

                #create a list to store the path to all neighbors of current vertex
                neighbor_paths = []
                #loop through and make a list with path to all neighbors
                for i in range(len(neighbors)):
                    neighbor_list = list(neighbors)

                    neighbor_paths.append(removed_path.copy())
                    neighbor_list[i].append(neighbor_list[i])
                    print(neighbor_paths)

                for path in neighbor_paths:
                    q.enqueue(path)



                #make a copy of the path
                
                #append the neighbor to the back of the path
                #enqueue out new path
            
        return None




    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


my_graph = Graph()

my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_vertex('3')
my_graph.add_vertex('4')
my_graph.add_vertex('4')



print(my_graph.vertices)

my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)

my_graph.add_edge(2, 1)
my_graph.add_edge(3, 7)

my_graph.add_edge(2, 5)
my_graph.add_edge(3, 4)

my_graph.add_edge(5, 2)
my_graph.add_edge(4, 3)

my_graph.add_edge(5, 4)
my_graph.add_edge(4, 5)

print(my_graph.bft('1'))

# print(my_graph.bfs('1', '4'))


    