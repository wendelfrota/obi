N = int(input())
R = int(input())
P = int(input())

i = 0
total = N

while total < P:
    N *= R
    total += N
    i += 1

print(i)
