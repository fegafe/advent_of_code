stones = []
# stones.append([125,17])
stones =[0]
i = 0
n = 75
lrun = []
seen = {}
for y in stones:
    lrun.append([y])
    i = 0
    while i < n:
        k = 0
        run = []
        for x in lrun[0]:
            if x in seen:
                run.append(seen[x][0])
                if seen[x][1] != -1:
                    run.append(seen[x][1])
            else:
                nx2 = -1
                if x == 0:
                    nx = 1
                elif len(str(x))%2 == 0:
                    s = len(str(x))//2
                    nx = int(str(x)[:-1*s])
                    nx2 = int(str(x)[s:])
                else:
                    nx = x*2024
                k += 1
                run.append(nx)
                seen[x] = (nx,-1)
                if nx2 != -1:
                    run.append(nx2)
                    seen[x] = (nx,nx2)
        lrun = []
        lrun.append(run)
        if i%5 == 0:
            print(f'{i}:{len(lrun[0])}')
        i += 1
    respart1 += len(lrun[0])
print(f'{respart1=}')