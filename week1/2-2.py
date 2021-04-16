#     2)  순열 확인 : 문자열 두 개가 주어졌을 때 이 둘이 서로 순열 관계에 있는지 확인하는 메서드를 작성하라.


# 정렬을 이용한 비교.
def solution_1(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2) 

# 문자열 출현 횟수 확인.
def solution_2(s1, s2):
    if len(s1) != len(s2):
        return False

    c_dict = {}

    for c1 in s1:
        if c1 not in c_dict:
            c_dict[c1] = 1
        else:
            c_dict[c1] += 1
    
    for c2 in s2:
        if c2 not in c_dict:
            return False
        else:
            c_dict[c2] -= 1

    return True if not any(c_dict.values()) else False

if __name__ == "__main__":
    print(solution_2("dog", "goa"))