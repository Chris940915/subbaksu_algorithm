# Linked List 구현


class Node(object):

    def __init__(self, val):
        self.vall = val
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index : int) -> int:
        if index < 0 or index > self.size:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        
        return curr.val
    
    def addAtHead(self, val: int)-> None:

        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int)-> None:
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)
        self.size += 1

    def addAtIndex(self, index : int):

        if index > self.size:
            return
        
        node = Node(val)

        if index <= 0:
            node.next = self.head
            self.head = node
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
        self.size += 1
    
    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:
            return
        
        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1