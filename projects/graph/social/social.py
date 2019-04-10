
'''
class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
'''

from collections import deque
from random import randint
import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments.

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        # this creates users up to the number of users input
        for i in range(numUsers):
            self.addUser(i)

        # Create friendships
        poss_users = []

        # for each user, add the user to poss_users
        for key in self.friendships.keys():
            poss_users.append(key)

        # create a random number of friendship for each user. Random
        # number must be between 1 and the avgFriendship input
        # go through the users
        for user in poss_users:
            rand = randint(1, avgFriendships)
            # for each user, add friendships rand number of times
            for i in range(rand):
                user2 = random.choice(poss_users)
                if user < user2:
                    self.addFriendship(user, user2)
    '''
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # self.friendships = {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {
        #     8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = [userID]
        currentPath = []

        visited[userID] = [userID]
        while len(queue) != 0:
            currentUser = queue.pop(0)
            for value in self.friendships[currentUser]:
                if value not in visited:
                    if currentUser not in currentPath:
                        currentPath.append(currentUser)
                    visited[value] = currentPath + [value]
                    queue.append(value)

        return visited
    '''

    def getAllSocialPaths(self, userID):
        visited = {}
        q = deque()
        q.append([userID])
        while len(q) > 0:
            path = q.popleft()
            newUserID = path[-1]
            if newUserID not in visited:
                visited[newUserID] = path
                for friendID in self.friendships[newUserID]:
                    if friendID not in visited:
                        new_path = list(path)
                        new_path.append(friendID)
                        q.append(new_path)
        return visited


graph = SocialGraph()
graph.addUser("Dave")
graph.addUser("John")
graph.addUser("Johnnnnn")
graph.addFriendship(1, 3)
graph.addFriendship(1, 2)
graph.addFriendship(2, 3)
graph.populateGraph(10, 4)
print(graph.getAllSocialPaths(1))
# print(graph.friendships)


# if __name__ == '__main__':
#     sg = SocialGraph()
#     sg.populateGraph(10, 2)
#     print(sg.friendships)
#     connections = sg.getAllSocialPaths(1)
#     print(connections)
