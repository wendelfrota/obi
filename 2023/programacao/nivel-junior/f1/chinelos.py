N = int(input())
X = [int(input()) for _ in range(N)]
P = int(input())
Pi = [int(input()) for _ in range(P)]

count = 0

for i in Pi:
    if X[i-1] > 0:
        X[i-1] -= 1
        count += 1

print(count)
