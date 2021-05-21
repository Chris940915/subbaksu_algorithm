


def solution(text, bomb):
    n = len(bomb)
    check = list()
    pointer = 0

    while pointer < len(text):
        check.append(text[pointer])
        pointer += 1
        flag = True

        # bomb 에 비해서 check 에 등록된 문자열의 길이가 더 길거나 같을때, 
        if len(check) >= n:
            # 뒤에서부터 확인. 
            for idx in range(-1, -n-1, -1):
                # 같으면 지울건데, 같지 않으면 flag에 False 담기. 
                if not check[idx] == bomb[idx]:
                    flag = False
                    break
            # 같으면 flag == True
            if flag == True:
                # 같으면 check 에서 pop
                for _ in range(n):
                    check.pop()
    if check:
        print(''.join(check))
    else:
        print("FRULA")

if __name__ == "__main__":    
    target = input()
    bomb = input() 
    solution(target, bomb)