n = int(input())
a = input().split()
for x in a:
    if len(x)<n and len(x)%2!=0:
        print(x.lower(), sep=',', end=': ')