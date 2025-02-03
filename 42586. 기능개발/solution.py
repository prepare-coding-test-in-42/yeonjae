def solution(progresses, speeds):
    remains = []

    for i in  range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            remains.append((100 - progresses[i]) // speeds[i])
        else:
            remains.append((100 - progresses[i]) // speeds[i] + 1)
        
    answer = []
    finish = 0
    # Iterate through the remaining days of tasks and get the number of days until the moment of reversed order
    for j in range(len(remains)):
        if (remains[j] > finish):
            # Update finish with the largest number so far
            finish = remains[j]
            # Once the element larger than the current element is found, track down the number of elements until this continues
            counts = 0
            for k in range(j, len(remains)):
                if (remains[k] <= finish):
                    counts += 1
                # Once the continuation ends, break
                else:
                    break
            # Add the number of tasks that can be deployed together
            answer.append(counts)

    return answer