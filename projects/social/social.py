import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"user {i}")

        #generate all possible friendship combinations
        possible_friendships = []

        #avoid dups by ensuring 1st number < 2nd number
        for user_id in self.users:
            for friend_id in range(user_id + 1,self.last_id + 1): #garuntees 1st friend_id < 2nd friend_id
                possible_friendships.append((user_id, friend_id))
        #shuffle friendships
        random.shuffle(possible_friendships) # keeps everyone friends but randomizes order 

        # create friendships for the first n of pairs 
        # n --> number of users * avg friendships // 2
        number_of_friendships = num_users * avg_friendships // 2 # with input(8,3) = 12 friendships because
        #friendships are 2 way
        
        for i in range(number_of_friendships): #looping to get the first (number_of friendships) friendships
            friendship = possible_friendships[i] # possible friendships is just a list of tuples made up of 
            # random possible friendships
            user_id = friendship[0]
            friend_id = friendship[1]
            self.add_friendship(user_id, friend_id) #adds friendships to graph, now we have a graph
            # we are creating 12 unique friendships, but they are two way friendships, so really it's 24 friendships

    #BFS to find shortest path from every user to every other user
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    # sg = SocialGraph()
    # sg.populate_graph(10, 2)
    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)


    sg = SocialGraph()

    sg.populate_graph(8, 3)

    print('sg.friendships', sg.friendships)
