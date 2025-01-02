def isValidSudoku(self, board: List[List[str]]) -> bool:
    rowset = [set() for _ in range(9)]
    columnset = [set() for _ in range(9)]
    subgridset = [[set() for _ in range(3)] for _ in range(3)]
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue
            if num in rowset[r]:
                return False
            if num in columnset[c]:
                return False
            if num in subgridset[r//3][c//3]:
                return False
            rowset[r].add(num)
            columnset[c].add(num)
            subgridset[r//3][c//3].add(num)
    return True
