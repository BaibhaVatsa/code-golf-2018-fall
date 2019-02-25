p = []
up = raw_input()
while not():    #add type checker
    p.append(up)
t = up
i = 0
s = True
while (i < t) and (i < len(p)):
    for j in range(len(p)-1):
        for k in range(1,len(p[i])):
            if (k < len(p[j+1])) and (p[j][k] is p[i][k]):
                s = False
                break
        if s is True:
            ++i
            print(p[j]+"\n"+p[j+1])