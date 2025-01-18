# Import counter class from collections module
from collections import Counter

def solution(participant, completion):
    # Counter class objects using the provided lists as an iterable data container
    diff = Counter(participant) - Counter(completion)
    
    return list(diff.elements())[0]