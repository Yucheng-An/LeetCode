citations = [3, 1, 1]


def hindex(citations):
    if len(citations) == 1:
        if citations[0] == 0:
            return 0
        else:
            return 1
    citations.sort(reverse=True)
    ranklist = [1]
    rank = 1
    p = 1
    while p < len(citations):
        if citations[p] != citations[p - 1]:
            rank += 1
        ranklist.append(rank)
        p += 1
    print(citations)
    print(ranklist)
    for i in range(len(citations)):
        if ranklist[i] == 


hindex(citations)
