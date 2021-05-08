
'''
스택 정렬 : 
가장 작은 값이 위로 오도록 스택을 정렬하는 프로그램을 작성하라.
추가적으로 하나 정도의 스택은 사용해도 괜찮지만, 스택에 보관된 요소를 배열 등의 다른 자료구조로 복사할 수는 없다. 
스택은 push, pop, peek, isEmpty의 네 가지 연산을 제공해야 한다.
'''

class Stack:
    def __init__(self):
        self.list = []
    
    def push(self, data):
        self.list.append(data)
    
    def pop(self):
        return self.list.pop()
    
    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)
    
    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

def sort_stack(stack_o):
    stack_n = Stack()

    while not stack_o.is_empty():
        tmp = stack_o.pop()

        if not stack_n.is_empty() and tmp >= stack_n.peek():
            stack_n.push(tmp)
        else:
            while not stack_n.is_empty() and stack_n.peek() > tmp:
                stack_o.push(stack_n.pop())
            stack_n.push(tmp)
        