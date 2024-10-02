citations = [3, 1, 1]

for i, citation in enumerate(citations):
    print(f"i is {i}")
    print(f"rank is {citation}")
    if citation < i + 1:
        return i+1
    