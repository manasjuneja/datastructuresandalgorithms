class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None


def getlength(node):
    cur = node

    count = 1

    while cur.next != None :
        cur = cur.next
        count += 1

    return count

