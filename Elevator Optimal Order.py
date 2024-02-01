from math import inf
weight = [1,2,4,5,2,3,2,1,2,3,4,2,3,4,2,3,4,6,7,5]
limit = 10
n = len(weight)
best = [[inf,inf]]*(1<<n)
best[0] = [1,0]
for s in range(1, 1 << n):
    # initial value: n+1 rides are needed
    best[s] = [n + 1, 0]
    for p in range(n):
        if s & (1 << p):
            option = list(best[s^(1 << p)])
            if option[1] + weight[p] <= limit:
                # add p to an existing ride
                option[1] += weight[p]
            else:
                # reserve a new ride for p
                option[0] += 1
                option[1] = weight[p]
            best[s] = min(best[s], option)
