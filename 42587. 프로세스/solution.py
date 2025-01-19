class process:
    def __init__(self, priority, index):
        self.priority = priority
        self.index = index

        
def solution(priorities, location):
    queue = []
    for idx in range(len(priorities)):
        queue.append(process(priorities[idx], idx))
        
    order = sorted(queue, key=lambda x : x.priority, reverse=True)
    
    count = 0
    while len(order):
        if order[0].priority == queue[0].priority:
            count += 1
            if queue[0].index == location:
                return count
            order.pop(0)
        temp = queue.pop(0)
        queue.append(temp)