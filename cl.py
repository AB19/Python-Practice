class Node ():
    def __init__(self, data, node = NONE):
        self.data = data
        self.next_node = node
    def get_data (self):
        return self.data
    def get_next (self):
        return self.next_node
    def set_next (self, node):
        self.next_node = node

class LinkedList ():
    def __init__ (self, head = none):
        self.head = head
    def insertNode (self, data):
        n = Node (data)
        n.set_next (self.head)
        self.head = n
    
        
j = Jaffa ()

    
