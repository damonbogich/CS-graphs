
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
 
        stack = Stack()

        visited = set()
   
        stack.push([starting_vertex])


        while stack.size() > 0:
            
            current_path = stack.pop() 
            
            current_paths_last_vertex = current_path[len(current_path) - 1] #6

            # this array was not necessary for this project, but it ensures
            # that parent with smallest value is returned, not just the last
            # parent in a path to be popped off of stacks
            current_paths_last_vertex_neighbors = []
            if current_paths_last_vertex not in visited:
                parents = get_parents(ancestors, current_paths_last_vertex) # [3,5]

                current_paths_last_vertex_neighbors.append(current_paths_last_vertex)
                if parents == [] and len(current_path) == 1: 
                    return -1 
                if parents == [] and stack.size() == 0:
                                                   
                    return min(current_paths_last_vertex_neighbors)
                
                    


                visited.add(current_paths_last_vertex)
                
                neighbor_paths = []
                for i in range(len(parents)):
                    neighbor_list = list(parents)

                    neighbor_paths.append(current_path.copy()) 
                    neighbor_paths[i].append(neighbor_list[i]) 
                    print('neighbor paths', neighbor_paths)
                
                for path in neighbor_paths:
                    stack.push(path)

        return None