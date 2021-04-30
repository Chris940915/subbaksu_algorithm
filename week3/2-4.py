'''
4) 리스트의 합 : 연결리스트로 숫자를 표현할 때 각 노드가 자릿수 하나를 가리키는 방식으로 표현할 수 있다. 
        각 숫자는 역순으로 배열되어 있는데, 첫 번째 자리수가 리스트의 맨 앞에 위치하도록 배열된다는 뜻이다. 
        이와 같은 방식으로 표현된 숫자 두 개가 있을 때, 이 두 수를 더하여 그 합을 연결리스트로 반환하는 함수를 작성하라.
        입력 : (7->1->6) + (5->9->2). 즉, 617+295
        결과 : 2->1->9 즉, 912.
'''

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
    
    def set_next(self, node):
        curr = self.head
        next_node = Node()
    
        while curr.next is not None:
            curr = curr.next
        next_node = curr.next

        next_node.val = node.val
        next_node.next = curr.next.next

    def sum_list(self, node_1, node_2, next_v):
        if node_1 is None and node_1 is None and next_v is None:    
            return None
        
        result = Node()
        value = next_v

        if node_1 != None:
            value += node_1.val
        
        if node_2 != None:
            value += node_2.val
        
        result.val = value%10

        if node_1 is not None or node_2 is not None:
            new_node = sum_list(node_1.next if node_1 is not None else None, node_2.next if node_2 is not None else None, 1 if value > 9: else 0)
            result.set_next(new_node)
        return result