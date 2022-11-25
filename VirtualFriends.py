class DisjointSet:
    # Initialized disjoint sets have themselves as their parent (i.e., they are alone in the set)
    def __init__(self):
        self.parent = self
        self.size = 1

    # Find the root of the disjoint set
    def find(self):
        # If the node points to itself, it is the root
        if self.parent == self:
            return self
        # Otherwise, reiterate through this function with this node's parent
        # This compresses the path, such that all nodes in the path end up pointing directly to the root
        else:
            self.parent = DisjointSet.find(self.parent)
            return self.parent

    # Merge the two sets passed to it (self and second_set)
    def union(self, other):
        p1 = DisjointSet.find(self)
        p2 = DisjointSet.find(other)
        # If these two sets have the same root, they are already in the same disjoint set
        if p1 == p2:
            return p1.size

        # Otherwise, we compare the sizes of our sets, and connect the root of the smaller set to the other root
        elif p1.size > p2.size:
            p2.parent = p1
            p1.size += p2.size
            return p1.size
        else:
            p1.parent = p2
            p2.size += p1.size
            return p2.size


# Take in user input to see how many cases to test
cases = input()
for __ in range(int(cases)):
    pairs = input()

    # Take in as many inputs of friends as requested by the user
    for friends_to_test in range(int(pairs)):
        friends_added = input()
        p1, p2 = friends_added.split(" ")

        # If either name is not already in our disjointFriendsDict (i.e., the user hasn't passed that name
        # to us yet), add it to the dictionary with a new DisjointSet class assigned to it
        if p1 not in disjoint_friends_dict:
            disjoint_friends_dict[p1] = DisjointSet()
        if p2 not in disjoint_friends_dict:
            disjoint_friends_dict[p2] = DisjointSet()

        # Then, take the union of the two DisjointSet classes and print its size
        union_size = disjoint_friends_dict[p1].union(disjoint_friends_dict[p2])
        print(union_size)

    # After running through all of the friendships formed in the test case, reset our disjoint_friends_dict
    disjoint_friends_dict = {}