for i in range(input()):
    inp = set()
    for s in raw_input().split():
        inp.add(s)
    inp = sorted(inp)
    print(inp[len(inp)-input()])