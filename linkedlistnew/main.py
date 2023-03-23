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


def findindex(node, value):
    cur = node

    ind = 0

    while cur.next != None :
        cur = cur.next
        ind += 1
        if cur.val == value:
            break

    return ind


def deletenode(node, index):
    cur = node

    ind = 0

    while cur.next != None :
        temp = cur
        cur = cur.next
        ind += 1
        if ind == index :
            temp.next = cur.next



def update(node, value, newvalue):
    cur = node

    while cur.next != None :
        cur = cur.next
        if cur.val == value :
            cur.val == newvalue

