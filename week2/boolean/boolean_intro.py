n = int(input())
b = 0
lst = list(map(int, input().split()))
new_lst = []
for i in lst:
    b = i * i
    new_lst.append(b)
print(*(new_lst))