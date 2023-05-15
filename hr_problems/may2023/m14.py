from collections import defaultdict

# example 
d = defaultdict(list)

# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)

# problem 
n, m = map(int, input().split())
for i in range(n):
    d[input()].append(i+1)

for _ in range(m):
    print(*d.get(input(), [-1]))