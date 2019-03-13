#!/usr/bin/python3
p, k, i  = [], 0, 0
while True:
    try:
        up = input()
        k = int(up)
        break
    except ValueError:
        p.append(up)
while k > 0 and i < len(p):
    for j in range(len(p)-1):
        printbool = True
        for char in range(len(p[j+1]) if len(p[j+1]) <= len(p[i]) else len(p[i])):
            printbool = False if p[j+1][char] == p[i][char] else printbool
        k -=2 if printbool is True else 0
        print(p[i]+"\n"+p[j+1]) if printbool is True else print("",end="")
    i += 1