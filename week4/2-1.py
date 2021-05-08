

'''
스택 Min : 
기본적인 push 기능과 pop 기능이 구현된 스택에서 최솟값을 반환하는 min 함수를 추가하려고 한다. 
어떻게 설계할 수 있겠는가? push, pop, min 연산은 모두 O(1) 시간에 동작해야 한다.
'''


import sys

class Stack:

    def __init__(self):
        self.list = []
    
    def push(self, data):
        self.list.append(data)
    
    def pop(self):
        if not self.list:
            return False
        
        return self.list.pop()
    
    def peek(self):
        if not self.list:
            return False
        
        return self.list[-1]
    
    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

'''
    Min 값들을 기록하는 스택을 하나 더 두는 방법. 
    만약 스택의 크기가 크긴 하지만 첫 번째 원소가 최솟값이라면 하나의 원소만으로 찾을 수 있다. 
'''
class StackWithMin2(Stack):
    def __init__(self):
        self.s2 = Stack()
    
    def push(self, data):
        if data <= self.min():
            s2.push(data)
        super.push(data)
        
    def min(self):
        if s2.is_empty():
            return sys.maxsize
        else:
            return s2.peek()

    def pop(self):
        value = super.pop()
        if (value == min()):
            s2.pop()
        return value