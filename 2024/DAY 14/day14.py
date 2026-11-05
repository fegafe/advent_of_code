def printmap(mapp, show = []):
    for j in range(mxy):
        for i in range(mxx):
            if (i,j) in show:
                print('X',end='')
            else:
                print(mapp[i][j],end='')
        print('')


# file = open('example.txt','r')
file = open('input.txt','r')

mxx = 101
mxy = 103

mapp = []
for i in range(mxx):
    xrow = []
    for j in range(mxy):
        xrow.append(' ')
    mapp.append(xrow)

guard = {}
idd = 0
# # p=0,4 v=3,-3
for line in file.readlines():
    dat = line.strip().split(' ')
    px = int(dat[0].split('=')[1].split(',')[0])
    py = int(dat[0].split('=')[1].split(',')[1])
    vx = int(dat[1].split('=')[1].split(',')[0])
    vy = int(dat[1].split('=')[1].split(',')[1])
    guard[idd] = {'inipos' : (px,py),'vel':(vx,vy)}
    # mapp[px][py] += '1'
    idd += 1
# print(guard)
# printmap(mapp)

sec = 100
c1 = 0
c2 = 0
c3 = 0
c4 = 0
for i in range(100):
    for k in [(7+101*i),(53+103*i)]:
        loca = []
        for g in guard:
            lpx =(guard[g]['inipos'][0]+k*guard[g]['vel'][0])%mxx
            lpy =(guard[g]['inipos'][1]+k*guard[g]['vel'][1])%mxy
            guard[g]['lpos'] = (lpx,lpy)
            if lpx>=0 and lpx < mxx//2:
                if lpy >= 0 and lpy < mxy//2:
                    c1 += 1
                elif lpy > mxy//2 and lpy <= mxy:
                    c2 += 1
            elif lpx > mxx//2 and lpx <= mxx:
                if lpy >= 0 and lpy < mxy//2:
                    c3 += 1
                elif lpy > mxy//2 and lpy <= mxy:
                    c4 += 1
            loca.append((lpx,lpy))
        printmap(mapp,loca)
        print(f'{k=}')
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
# print(f'{c1=}:{c2=}:{c3=}:{c4=}')

printmap(mapp)

respart1 = c1*c2*c3*c4
print(f'{respart1=}')


    



