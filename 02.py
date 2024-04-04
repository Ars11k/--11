string=[]
for i in range(3):
    string.append(set(input().split(', ')))
result = string[0] & string[1] & string[2]
print(*result)
print(max(result))

