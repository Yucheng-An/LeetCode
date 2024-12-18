def convert(s, numRows):
    if numRows == 1:
        return s
    rows = [''] * numRows 
    current_row = 0
    going_down = False
    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == numRows - 1:
            going_down = True
        if going_down:
            


s = "PAYPALISHIRING"
numRows = 4
res = convert (s,numRows)
print(res)
rows = [''] * numRows
print(rows)