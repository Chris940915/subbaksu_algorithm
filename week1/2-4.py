#  4) 하나 빼기 : 문자열을 편집하는 방법 세 가지 1) 문자 삽입, 2) 문자 삭제, 3) 문자 교체. 문자열 두 개가 주어졌을 때, 문자열을 같게 만들기 위한 편집 횟수가 1회 이내인지 확인하는 함수를 작성하라,
#             ex)    pale, ple -> true
#                      pales, pale -> true
#                      pale, bale -> true
#                      pale, bake -> false


# 길이 : s1 > s2 
def insert(s1, s2):
    # s1, s2 각각의 순회 Index
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        # index 같지 않을 때, 
        if s1[i] != s2[j]:
            # 두 문자열의 index가 다르면 두 번째 다른 상황. 
            if (i!=j):
                return False
            # 길이가 긴 s1 의 index 만 +1 
            i += 1
        else:
            i += 1
            j += 1
    return True


# 2개 이상 다르면, return false
def replace(s1, s2):
    flag = True
    for c1, c2 in zip(s1, s2):
        # 문자열이 다를 때, 
        if c1 != c2 :
            # 이미 한번 달랐으면 return false
            if not flag:
                return False
            # 처음 다른 것으로 false로 변경. 
            flag = False
    return True


def solution(s1, s2):
    n_a = len(s1)
    n_b = len(s2)

    if n_a == n_b:
        return replace(s1, s2)
    elif n_a - n_b == 1:
        return insert(s1, s2)
    elif n_a - n_b == -1:
        return insert(s2, s1)
    return False


if __name__ == "__main__":
    print(solution("bale", "pale"))