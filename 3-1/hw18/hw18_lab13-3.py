def find(current, visited):
    if visited == total:
        return w[current][0] if w[current][0] >0 else 20202020
    if d[current][visited] >0:
        return d[current][visited]

    cost= 20202020

    for i in range(1,n):
        if (visited>>i)%2 ==1 or w[current][i] == 20202020:
            continue
        tmp=find(i, visited | (1<<i))

        cost = min(tmp + w[current][i], cost)

    d[current][visited] = cost
    return cost

n =4 
w=[[0,2,9,202020220],[1,0,6,4],[20202020,7,0,8],[6,3,20202020,0]]

d=[[0,2,9,20202020],[1,0,6,4],[20202020,7,0,8],[6,3,20202020,0]]

d = [[0]*(1 << n) for _ in range(n)]
total = (1<<n)-1

result = find(0,1)
print("최적의 cost=%d" %result)
