import sys
from collections import defaultdict

# Increase recursion limit for deep trees
sys.setrecursionlimit(10**6)

def dfs(x, fa):
    global res
    f[x][1] = max(f[x][1], a[x])
    for i in v[x]:
        if i != fa:
            dfs(i, x)
            t1 = max(f[i][3] + a[i], f[i][2] + a[i], f[i][1], a[i])
            f[x][3] = max(f[x][3], f[x][3] + t1, f[x][2] + t1)
            f[x][2] = max(f[x][2], f[x][1] + t1)
            f[x][1] = max(f[x][1], t1)
    res = max(res, f[x][3] + a[x], f[x][2], f[x][1] + a[x])

# Placeholder for input() to avoid redefinition
input_data = input

# Read number of test cases
t = int(input_data())
for _ in range(t):
    n = int(input_data())
    res = 0
    a = [0] + list(map(int, input_data().split()))
    f = [[-float('inf')] * 4 for _ in range(n + 1)]
    v = defaultdict(list)

    # Read tree edges
    for _ in range(n - 1):
        j, k = map(int, input_data().split())
        v[j].append(k)
        v[k].append(j)

    # Perform DFS traversal
    dfs(1, 0)
    
    # Output the result for the current test case
    print(res)
    
    # Cleanup for the next test case
    v.clear()
