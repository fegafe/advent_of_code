
###09:42//10:06

# file = open('example.txt','r')
# # file = open('input.txt','r')

def stones_after(x):
    if x in solved:
        if len(solved[x])>1:
            return solved[x][0],solved[x][1]
        else:
            return solved[x][0],-1
    elif x == 0:
        solved[x] = [1]
        return 1,-1
    elif len(str(x))%2 == 0:
        s = len(str(x))//2
        solved[x] = [int(str(x)[:-s]),int(str(x)[s:])]
        return int(str(x)[:-s]),int(str(x)[s:])
    else:
        solved[x] = [x*2024]
        return x*2024,-1


def stones_af_nsteps(x,steps):
    if steps == 0:
        return 1
    elif (x,steps) in cache:
        return cache[(x,steps)]
    else:
        res = 0
        nx,ny = stones_after(x)
        res += stones_af_nsteps(nx,steps-1)
        if ny >=0:
            res += stones_af_nsteps(ny,steps-1)
    cache[(x,steps)] = res
    return res

def fill25(s):
    # print(s)
    k = 1
    sh[s] = {}
    nns = [s]
    while k <= 25:
        rs = []
        for x in nns:
            rs.extend(stones_after(x))
        sh[s][k] = rs
        nns = rs
        k += 1

solved = {}
cache =  {}
stones = []
stones = [125,17]
stones =[2,72,8949,0,981038,86311,246,7636740]

# stones =[2]
n = 75
respart1 = 0
for s in stones:
    respart1 += stones_af_nsteps(s,n)
print(f'{respart1=}')

# sh = {}
# ns = {}
# psol = {}
# for i in range(-1,n+1):
    # psol[i]=[]
# i = 1
# ns[0] = stones
# maxns = 0
# stop = ''
# while i <= n:
    # for ts in ns[i-1]:
        # if ts not in psol[i-1]:
            # if ts not in sh:
                # fill25(ts)
            # for j in sh[ts]:
                # if i+j-1 in ns:
                    # ns[i+j-1].extend(sh[ts][j])
                    # psol[i+j-1].extend(sh[ts][j])
                # else:
                    # ns[i+j-1] = []
                    # psol[i+j-1] = []
                    # ns[i+j-1].extend(sh[ts][j])
                    # psol[i+j-1].extend(sh[ts][j])
        # else:
            # if ts in sh:
                # for j in sh[ts]:
                    # if i+j-1 in ns and (i+j-1)>25:
                        # ns[i+j-1].extend(sh[ts][j])
                        # psol[i+j-1].extend(sh[ts][j])
                    # elif (i+j-1)>25:
                        # ns[i+j-1] = []
                        # psol[i+j-1] = []
                        # ns[i+j-1].extend(sh[ts][j])
                        # psol[i+j-1].extend(sh[ts][j])
            # psol[i-1].remove(ts)
    # i +=1
# print(f'{len(ns[n])}')


# lrun = []C
# for y in stones:
    # lrun.append([y])
    # i = 0
    # while i < n:
    
        # k = 0
        # run = []
        # for x in lrun[0]:
            # nx2 = -1
            # if x == 0:
                # nx = 1
            # elif len(str(x))%2 == 0:
                # s = len(str(x))//2
                # nx = int(str(x)[:-1*s])
                # nx2 = int(str(x)[s:])
            # else:
                # nx = x*2024
            # k += 1
            # run.append(nx)
            # if nx2 != -1:
                # run.append(nx2)
        # lrun = []
        # lrun.append(run)
        # # if i == 25:
            # # print(i)
        # i += 1
    # respart1 += len(lrun[0])
# print(f'{respart1=}')