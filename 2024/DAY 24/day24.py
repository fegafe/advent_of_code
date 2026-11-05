import sys
import time
import itertools

# file = open('example.txt','r')
file = open('input.txt','r')

def calc(x,y,f):
    if   f == 'AND':
        return x&y
    elif f == 'OR':
        return x|y
    elif f == 'XOR':
        return x^y
    print(f)

def intvalof(fval,toper):
    alout = toper[fval[0]]
    for i in fval[1:]:
        alout = (alout<<1) | toper[i]
    return alout

def outval(tout):
    valout = 0
    for i in range(len(tout)-1,0,-1):
        valout = valout | tout[f'z{i:02}']
        valout = valout << 1
    return valout

def calcz(tfunc,toper,tout):
    sumout = -1
    while sumout < 0:
        for r in tfunc:
            if toper[r] == -1:
                function = tfunc[r].split(' ')[1].strip()
                op1      = tfunc[r].split(' ')[0].strip()
                op2      = tfunc[r].split(' ')[2].strip()
                if toper[op1] >= 0 and toper[op2] >= 0:
                    toper[r] = calc(toper[op1],toper[op2],function)
                    if r in tout:
                        tout[r] = toper[r]
        sumout = 0
        for r in tout:
            sumout += tout[r]

sys.setrecursionlimit(1000000)
stime = time.time()

init = {}
oper = {}
func = {}
out  = {}

getoper = True
for line in file.readlines():
    line = line.strip()
    if line == '':
        getoper = False
        continue
    elif getoper:
        op,val = line.split(':')
        init[op] = int(val)
    else:
        ops,res = line.split('->')
        res = res.strip()
        func[res.strip()] = ops.strip()
        top = ops.split(' ')
        if top[0] in init:
            oper[top[0]] = init[top[0]]
        else:
            oper[top[0]] = -1
        if top[2] in init:
            oper[top[2]] = init[top[2]]
        else:
            oper[top[2]] = -1
        if res.startswith('z'):
            oper[res] = -1
            out[res] = -1000

##PART2

# Zn          = Xn XOR Yn XOR CARRY(Zn)<- Check if this is ok, of not, look where it is the correct or check the operands**
#               XOR[n]        CARRY[n]
# CARRY (Zn)  = (Xn-1 AND Yn-1)  OR  SCARRY (Zn)
#                AND[n-1] OR SCARRY[n]
# SCARRY (Zn) = ((Xn-1 XOR Yn-1) AND CARRY(Zn-1))
#               XOR[n-1]             CARRY[n-1]

func['fgc'],func['z12'] = func['z12'],func['fgc']
func['z29'],func['mtj'] = func['mtj'],func['z29']
func['vvm'],func['dgr'] = func['dgr'],func['vvm']
func['dtv'],func['z37'] = func['z37'],func['dtv']

part2 = ['fgc','z12','z29','mtj','vvm','dgr','dtv','z37']
part2.sort()
print(','.join(part2))

p1func = func.copy()
p1oper = oper.copy()
p1out  = out.copy()
calcz(p1func,p1oper,p1out)
z = outval(p1out)
print(f'respart1 = {z}') ##65635066541798
print(f'{time.time()-stime} seconds')

xval = []
yval = []



for op in p1oper:
    if op.startswith('x'):
        xval.append(op)
    if op.startswith('y'):
        yval.append(op)

xval.sort(reverse=True)
yval.sort(reverse=True)

x = intvalof(xval,p1oper)
y = intvalof(yval,p1oper)

exres = x+y
dif   = exres^z
print(f'{z:b}')
print(f'{exres:b}')
print(f'{dif:0{len(out)}b}')


i = 0
tochk = set()
zok   = set()
while dif:
    if dif&1 == 1:
        tochk.add(f'z{i:02}')
    else:
        zok.add(f'z{i:02}')
    dif = dif>>1
    i += 1

CARRY = {}
SCARRY = {}
XOR = {}
AND = {}

CARRY['00']  = ''
SCARRY['00'] = ''

CARRY['01']  = 'njb'
SCARRY['01'] = ''

for i in range(0,len(out)):
    cur  = f'{i:02}'
    prev = f'{i-1:02}'
    xind = f'x{i:02}'
    yind = f'y{i:02}'
    for c in func:
        if func[c] == f'{xind} XOR {yind}' or func[c] == f'{yind} XOR {xind}':
            XOR[f'{i:02}'] = c
        elif func[c] == f'{xind} AND {yind}' or func[c] == f'{yind} AND {xind}':
            AND[f'{i:02}'] = c

CARRY2 = {}
for j in range(1,len(out)-1):
    curz  = f'z{j:02}'
    function = func[curz].split(' ')[1].strip()
    op1      = func[curz].split(' ')[0].strip()
    op2      = func[curz].split(' ')[2].strip()
    if op1 == XOR[f'{j:02}']:
        CARRY2[f'{j:02}'] = op2
    elif op2 == XOR[f'{j:02}']:
        CARRY2[f'{j:02}'] = op1
    else:
        print(j)

exz = {}
exz2 = {}
for i in range(2,len(out)-1):
    cur  = f'{i:02}'
    prev = f'{i-1:02}'
    for c in func:
        if func[c] == f'{XOR[prev]} AND {CARRY[prev]}' or func[c] == f'{CARRY[prev]} AND {XOR[prev]}':
            SCARRY[cur] = c
    for c in func:
        if func[c] == f'{AND[prev]} OR {SCARRY[cur]}' or func[c] == f'{SCARRY[cur]} OR {AND[prev]}':
            CARRY[cur] = c
    exz[cur] = f'{XOR[cur]} XOR {CARRY[cur]}'
    exz2[cur] = f'{CARRY[cur]} XOR {XOR[cur]}'
    if exz[cur] != func[f'z{cur}']:
        if exz2[cur] != func[f'z{cur}']:
            print(f'{exz[cur]}::{func[f"z{cur}"]} check operands')
            for c1 in func:
                if exz[cur] == func[c1]:
                    print(f'{c1}::{func[c1]} z{cur}::{func[f"z{cur}"]} change {c1} with {f"z{cur}"}')
                elif exz2[cur] == func[c1]:
                    print(f'{c1}::{func[c1]} z{cur}::{func[f"z{cur}"]} change {c1} with {f"z{cur}"}')



# ttch = set()
# ttch = tochk.copy()
# while ttch:
    # top = ttch.pop()
    # if top in func:
        # op1 = func[top].split(' ')[0].strip()
        # op2 = func[top].split(' ')[2].strip()
        # tochk.add(op1)
        # tochk.add(op2)
        # ttch.add(op1)
        # ttch.add(op2)

# tzok = set()
# tzok = zok.copy()
# while tzok:
    # top = tzok.pop()
    # if top in func:
        # op1 = func[top].split(' ')[0].strip()
        # op2 = func[top].split(' ')[2].strip()
        # tzok.add(op1)
        # tzok.add(op2)
        # zok.add(op1)
        # zok.add(op2)

# for zo in zok:
    # if zo in tochk:
        # tochk.remove(zo)

# checkthis = []
# for tc in tochk:
    # if tc in func:
        # checkthis.append(tc)

# for c in checkthis:
    # if c.startswith('z'):
        # print(f'{c}:{p1oper[c]}:{func[c]}')
        # op1 = func[c].split(' ')[0].strip()
        # op2 = func[c].split(' ')[2].strip()
        # if op1 not in checkthis:
            # print(f'{op1} not in {c}')
        # if op2 not in checkthis:
            # print(f'{op2} not in {c}')




# comb = itertools.combinations(checkthis, 8)
# i = 0
# for c in comb:
    # print(c)
    # comb2 = itertools.combinations(c, 2)
    # for c2 in comb2:
        # print(c2)
    # if i> 1:
        # break
    # i += 1
    

# i = 0
# for c in comb2:
    # print(c)
    # i += 1
    # if i > 3:
        # break
# print(sum(1 for ignore in comb2))

# # ###LONG WAY###
# # comb = combinations(loper, 2)
# # poss = []
# # for c in comb:
    # # poss.append(c)
# # comb2 = combinations(loper, 4)
# # # print(sum(1 for ignore in comb2))

