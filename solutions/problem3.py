#!/usr/bin/python3
i = []
for j in range(int(input())):
    [i.append(s) if s not in i else 0 for s in input().split()]
    print(sorted(i)[-int(input())])