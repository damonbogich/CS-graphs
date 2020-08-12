
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def get_parents(family, current_node):
    parents = []
    for i in family:
        if i[1] == current_node:
            parents.append(i[0])
    return parents


def earliest_ancestor(ancestors, starting_vertex):
    #create an empty stack
        stack = Stack()
        #create a set for visited vertices
        visited = set()
        #add starting vertex path to stack [['1']]
        stack.push([starting_vertex])

        #while stack is not empty:
        while stack.size() > 0:
            #pop off stack: stack = []
            current_path = stack.pop() # --> ['6'] 
            #store the last item from the popped off stack list: last = '1'
            current_paths_last_vertex = current_path[len(current_path) - 1] #6
            #if last == destination_vertex:
            if current_paths_last_vertex not in visited:
                parents = get_parents(ancestors, current_paths_last_vertex) # [3,5]
                if parents == None:                               ### i think here we check 
                                                                    #for parents current paths last vertex
                                                                    #if it doesn't have any, return it
                #return the node if it has no parents
                    return current_paths_last_vertex
            #add last to visited: visited = {'6'}
                visited.add(current_paths_last_vertex)
                #add path to all of last's ('6') parents to stack:  [['6', '3'], ['6', '5']]

                #deleted this line for now
                ## parents = starting_vertex.get_parents(current_paths_last_vertex) # --> {'2', '3'}

                #initialize list that can store both neighbor path lists
                neighbor_paths = []

                #loop through parents and add them each to list with 1 ---> [['1', '2'], ['1', '3']]
                for i in range(len(parents)):
                    neighbor_list = list(parents)

                    neighbor_paths.append(current_path.copy()) #[['1'], ['1']]
                    neighbor_paths[i].append(neighbor_list[i]) #[['1', '2'], ['1', '3']]
                    print('neighbor paths', neighbor_paths)
                
                for path in neighbor_paths:
                    stack.push(path)

        return None