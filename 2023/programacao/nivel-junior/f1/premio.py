P = int(input())
D = int(input())
B = int(input())

x = B*3 + D*2 + P

if x >= 150:
    print('B')
elif x >= 120:
    print('D')
elif x >= 100:
    print('P')
else:
    print('N')
