# 3) 회문 수열 : 주어진 문자열이 회문(palindrome)의 순열인지 아닌지 확인하는 함수를 작성하라. 회문이란 앞으로 읽으나 뒤로 읽으나 같은 단어 혹은 구절을 의미하며, 순열이란 문자열을 재배치하는 것을 뜻한다.
#            입력 : Tact Coa
#            출력 : True   (순열 : “taco cat”, “acto cta” 등 )

def solution(s):
    s_dict = {}

    # create hashtable
    for c in s:
        if c not in s_dict:
            s_dict[c] = 1
        else:
            s_dict[c] += 1

    temp = 0
    for v in s_dict.values():
        if v % 2 != 0:
            temp += 1
            if temp > 1:
                return False
    return True


if __name__ == "__main__":
    pass