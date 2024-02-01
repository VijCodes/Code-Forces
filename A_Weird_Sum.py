from collections import defaultdict, Counter
from sys import stdin
input = lambda: stdin.buffer.readline().decode().strip()

rows, cols = map(int, input().split())
grid = []
for _ in range(rows):
    grid.append(list(map(int, input().split())))
result = 0

#Scan rowwise
color_to_last = defaultdict(lambda : [0, 0, -1]) # count,cost,last row
for row in range(rows):
    counts = Counter(grid[row])
    for val, count in counts.items():
        count_old, cost, last_row = color_to_last[val]
        result += ((row-last_row)*count_old+cost)*count
        color_to_last[val] = count+count_old, (row-last_row)*count_old+cost, row 
            
#Scan columnwise
color_to_last = defaultdict(lambda:[0, 0, -1]) # count,cost,last col
for col in range(cols):
    counts = Counter([grid[row][col] for row in range(rows)])
    for val, count in counts.items():
        count_old, cost, last_col = color_to_last[val]
        result += ((col-last_col)*count_old+cost)*count
        color_to_last[val] = count+count_old, (col-last_col)*count_old+cost, col
print(result)      