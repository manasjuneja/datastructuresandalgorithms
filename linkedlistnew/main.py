class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None


def getlength(node):
    count = 1
    cur = node

    while cur.next != None :
        cur = cur.next
        count += 1

    return count 

node_1 = Node(32)
node_2 = Node(89)
node_1.next = node_2
print(getlength(node_1))



# def findindex(node, value):
