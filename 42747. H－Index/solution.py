def solution(citations):
    # H-index can only be as large as the number of publications
    answer = len(citations)

    # Rank the publications in descending order by the number of times they have been cited
    citations.sort(reverse=True)
    
    # Loop through to find the entry where the rank is greater than the number of citations
    for h in range(len(citations)):
        if citations[h] <= h:
            answer = h
            break
    return answer