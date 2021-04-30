

'''
중간 노드 삭제 :  단방향 연결리스트가 주어졌을 때, 중간(처음과 끝 노드 제외)노드 하나를 삭제하는 알고리즘을 구현하라.
        입력 : 연결리스트드 a->b->c->d->e 에서 노드 c
        결과 :  a->b->d->e

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def deleteAtIndex(self, index):

        if index < 0 or index >= self.size:
            return
        
        curr = self.head

        for _ in range(index-1):
            curr = curr.next
        curr.next = curr.next.next