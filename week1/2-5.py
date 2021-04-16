

# 문자열 압축 : 반복되는 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라. 
# 예를 들어, 문자열 aabccccaaa 압축하면 a2b1c4a3이 된다. 만약 압축한 문자열의 길이가 기존 문자열의 길이보다 길다면 기존 문자열을 반환해야 한다. 문자열은 a-z 으로만 이루어져있다.


def solution(before):
    n = len(before)
    result = ""
    count = 1
    # 문자열 하나씩 순회하면서 확인 O(k)
    for i in range(1, n):
        # 같으면 count + 1
        if before[i-1] == before[i]:
            count += 1
        # 다르면 문자 + count 
        else:
            result += before[i-1]+str(count)
            # count 초기화. 
            count = 1
    
    # 마지막 연속 문자열에 대한 처리. 
    result += before[-1] + str(count)
    
    # 변환 전 길이 비교.    
    return n if len(result) > n else result

if __name__ == "__main__":
    before = "aabccccaaaa"
    print(solution(before))