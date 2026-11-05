def ternary (n,fill):
    if n != 0:
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        out = ''.join(nums)
    else:
        out ='0'
    for i in range(fill):
        if i > len(out)-2:
            out += '0'
    return out
    
def calc(oper,func):
    temp = oper[0]
    for i in range(len(func)):
        if func[i] == '+':
            temp = temp+oper[i+1]
        elif func[i] == '*':
            temp = temp*oper[i+1]
    # print(f'{oper}:{func}:{temp}')
    return temp

def calc2(oper,func):
    temp = oper[0]
    temp2 = 0
    for i in range(len(func)):
        if func[i] == '+':
            temp = temp+oper[i+1]
        elif func[i] == '*':
            temp = temp*oper[i+1]
        elif func[i] == '|':
            temp = temp*(10**(len(str(oper[i+1]))))+oper[i+1]
    return temp

# file = open('example.txt','r')
file = open('input.txt','r')

op = []
res = []
for line in file.readlines():
    res.append(int(line.split(':')[0]))
    top = []
    for x in line.split(':')[1].split():
        top.append(int(x))
    op.append(top)

respart1 = 0
respart2 = 0
resok = []
for i in range(len(res)):
    tres = 0
    func = []
    for j in range(len(op[i])-1):
        func.append('+')
    for j in range(2**(len(op[i])-1)):
        for k in range(len(func)):
            if 2**k & j:
                func[k] = '+'
            else:
                func[k] = '*'
        tres = calc(op[i],func)
        if tres == res[i]:
            respart1 += res[i]
            resok.append(i)
            break

for i in range(len(res)):
    if i%100 == 0:
        print(f'at {i} of {len(res)}')
    if i not in resok:
        tres = 0
        func = []
        p2ok = False
        for j in range(len(op[i])-1):
            func.append('+')
        options = ['+','*','|']
        cases = 3**(len(op[i])-1)
        for j in range(cases):
            for k in range(len(func)):
                # print(f'{j}:{ternary(j,len(func))}:{k}:{func}')
                func[k] = options[int(ternary(j,len(func))[k])]
            tres = calc2(op[i],func)
            if tres == res[i]:
                respart2 += res[i]
                # print(f'{res[i]}: {op[i]}:{func}')
                break
                    # print(f'{res[i]}: {op[i]}:{func}')

print(f'{respart1=}') ##1260333054159
print(f'{respart2=}') 
print(f'{respart1+respart2}')