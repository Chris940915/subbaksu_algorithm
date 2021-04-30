

    # 2)  뒤에서 k번째 원소 구하기:  단방향 연결리스트가 주어졌을 때 뒤에서 k번째 원소를 찾는 알고리즘을 구현하라.

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
    
    class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None
        
        def find_k(self, k):
            curr = self.head

            k_curr = self.head

            for _ in range(k):
                if k_curr == None:
                    return None
                k_curr = k_curr.next
            
            while k_curr is not None:
                k_curr = k_curr.next
                curr = curr.next
            return curr.val