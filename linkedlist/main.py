class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedlist:

    def __init__(self):
        self.head = node()


    def append(self,data):
        new_node = node(data)

        cur = self.head
        while cur.next != None:
            cur = cur.next

        cur.next = new_node


    def read(self):
        reader = []

        cur = self.head

        while cur.next != None:
            cur = cur.next
            reader.append(cur.data)

        print(reader)

