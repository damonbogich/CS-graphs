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
        self.vertices[v1].add(v2)       #self.vertices = dictionary
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
            
            #if dequeued item not in visited:
            if v not in visited:
                #add it to visited
                visited.add(v)
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


    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        #3 rules of recursion: 
            #1. function must call itself
            #2. must have base case
            #3. must move twoards base case
        
        #set for visited vertices
        
        print(starting_vertex)
        #add starting vertex to set
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor)



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
            last_vert = removed_path[len(removed_path) - 1] #'1'

            #if the vertex has not been visited:
            if last_vert not in visited:
                #if it is the destination_index:
                if last_vert == destination_vertex:
                    #return the path
                    return removed_path
                #mark it as visited
                visited.add(last_vert) ### visited = {'1'}

                #then add a path to its neighbors to the back of the queue
                neighbors = self.get_neighbors(last_vert) #returns set of neighbors = {'2','3'}
                print(neighbors)

                #create a list to store the path to all neighbors of current vertex
                neighbor_paths = []
                #loop through and make a list with path to all neighbors
                for i in range(len(neighbors)):
                    neighbor_list = list(neighbors) #['2', '3']

                    neighbor_paths.append(removed_path.copy()) #[['1'], ['1']]
                    neighbor_paths[i].append(neighbor_list[i]) 
                    print('neighbor paths', neighbor_paths)

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
        #create an empty stack
        stack = Stack()
        #create a set for visited vertices
        visited = set()
        #add starting vertex path to stack [['1']]
        stack.push([starting_vertex])

        #while stack is not empty:
        while stack.size() > 0:
            #pop off stack: stack = []
            current_path = stack.pop() # --> ['1'] 
            #store the last item from the popped off stack list: last = '1'
            current_paths_last_vertex = current_path[len(current_path) - 1]
            #if last == destination_vertex:
            if current_paths_last_vertex not in visited: 
                if current_paths_last_vertex == destination_vertex:
                #return popped_off list
                    return current_path
            #add last to visited: visited = {'1'}
                visited.add(current_paths_last_vertex)
                #add path to all of last's ('1') neighbors to queue:  [['1', '2'], ['1', '3']]
                neighbors = self.get_neighbors(current_paths_last_vertex) # --> {'2', '3'}
                #initialize list that can store both neighbor path lists
                neighbor_paths = []

                #loop through neighbors and add them each to list with 1 ---> [['1', '2'], ['1', '3']]
                for i in range(len(neighbors)):
                    neighbor_list = list(neighbors)

                    neighbor_paths.append(current_path.copy()) #[['1'], ['1']]
                    neighbor_paths[i].append(neighbor_list[i]) #[['1', '2'], ['1', '3']]
                    print('neighbor paths', neighbor_paths)
                
                for path in neighbor_paths:
                    stack.push(path)

        return None
                











    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """

        # create a new path that includes the current vertex
        path = path + [starting_vertex]

        # if you have reached the destination return the current path
        if starting_vertex == destination_vertex:
            return path
       
        # loop through each neighbor of the current vertex
        for neighbor in self.get_neighbors(starting_vertex):
            # if you haven't visited the neighbor
            if neighbor not in visited:
                # vadd the neighbor to visited
                visited.add(neighbor)
                # recursively call the function to get a path from the neighbor to the end
                neighborpath = self.dfs_recursive(neighbor, destination_vertex, path.copy())
                # if the call of this function on the current neighbor found a path to the end
                if neighborpath is not None:
                    # return that path
                    return neighborpath
        # if no path to the end was found in any recursive calls we return None
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
