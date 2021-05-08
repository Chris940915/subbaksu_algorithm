def solution(record):
    answer = []
    user_dict = dict()
    message = ["님이 들어왔습니다.", "님이 나갔습니다."]
    temp = []

    for r in record:
        enter = r.split()

        if enter[0] == 'Enter':
            user_dict[enter[1]] = enter[2]
            temp.append(enter[1], 0)
        elif enter[1] == 'Leave':
            temp.append(enter[1], 1)
        else:
            user_dict[enter[1]] = enter[2]
    
    for t in temp:
        answer.append(user_dict[t[0]]+message[t[1]])
    
    return answer