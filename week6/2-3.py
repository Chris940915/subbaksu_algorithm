def solution(jobs):
    n = len(jobs)
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))

    # 시작시간, 시간
    start, time = jobs.pop(0)
    # 끝시간
    end = start + time
    answer = time

    while jobs:
        next_idx = 0
        for i in range(1, len(jobs)):
            # 이전 일이 끝난 시간보다 다음 일의 시작 시간이 느릴때, 그냥 넘어감. 
            if jobs[i][0] > end:
                break
            # 이전 일이 끝난 시간보다 빠를 때, next_idx 넘기기. 
            else:
                # next_idx 의 끝나는 시간이 가장 느린 애로 바꾸기. 
                if jobs[next_idx][1] > jobs[i][1]:
                    next_idx = i
        
        next_ = jobs.pop(next_idx)

        if next_[0] > end:
            answer += next_[1]
            end = sum(next_)
        else:
            answer += next_[1]+(end-next_[0])
            end += next_[1]
    answer = answer//n
    return answer