#  1) 중복이 없는가 : 문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘. (자료구조를 추가로 사용하지않고 풀 수 있는 알고리즘도 고민)


def solution_1(s):
    temp = []

    for c in s:
        if c in temp:
            return False
        else:
            temp.append(c)
    return False

def solution_2(s):
    sorted_s = s.sort()

    for i in range(1, len(s)):
        if sorted_s[i-1] == sorted_s[i]:
            return False
    return True

def solution_3(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                return False
    return True

if __name__ == "__main__":
    pass