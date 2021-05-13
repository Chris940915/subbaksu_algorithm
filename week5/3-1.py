

def solution(N, stages):
    answer = []
    user_dict = dict()
    user_n = len(stages)

    for idx in range(1, N+1):
        count_user = stages.count(idx)

        if count_user == 0:
            user_dict[idx] = 0
            continue
        user_dict[idx] = count_user/user_n
        user_n -= count_user
    answer = sorted(user_dict, key=lambda x: user_dict[x], reverse=True)
    
    return answer