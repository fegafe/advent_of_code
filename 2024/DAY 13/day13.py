def diophantine(a, b, c):
    if c % greatest_common_divisor(a, b) == 0:
        (d, x, y) = extended_gcd(a, b)  # extended_gcd(a,b) function implemented below
        r = c / d
        return (int(r * x), int(r * y))
    else:
        return False
 
def diophantine_all_soln(a, b, c):
    (x0, y0) = diophantine(a, b, c)  # Initial value
    d = greatest_common_divisor(a, b)
    p = a // d
    q = b // d
    i = 0
    if x0 > y0:
        i = -1*(x0//q)
        x0 = x0 + i * q
        y0 = y0 - i * p
    if y0*q < 0:
        i = i +(y0//p)
        x0 = x0 + i * q
        y0 = y0 - i * p
    if x0*q < 0:
        i = -(x0//q)
        x0 = x0 + i * q
        y0 = y0 - i * p
    return(x0, y0,p,q)

def nextnsol(x,n=1):
    return (x[0]+n*x[3],x[1]-n*x[2],x[2],x[3])

def greatest_common_divisor(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

def extended_gcd(a, b):
    assert a >= 0 and b >= 0
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)
    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)


# file = open('example.txt','r')
file = open('input.txt','r')

# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

machines = {}
iid = 0
for line in file.readlines():
    if 'Button A' in line.strip():
        machines[iid] = {}
        machines[iid]['A'] = (int(line.split(':')[1].split(',')[0].strip().split('+')[1]),int(line.split(':')[1].split(',')[1].strip().split('+')[1]))
    elif 'Button B' in line.strip():
        machines[iid]['B'] = (int(line.split(':')[1].split(',')[0].strip().split('+')[1]),int(line.split(':')[1].split(',')[1].strip().split('+')[1]))
    elif 'Prize' in line.strip():
        machines[iid]['P'] = [int(line.split(':')[1].split(',')[0].strip().split('=')[1]),int(line.split(':')[1].split(',')[1].strip().split('=')[1])]
    else:
        iid +=1
# print(machines)

t_tokens1 = 0
for mac in machines:
    if mac >= 0:
        AX = machines[mac]['A'][0]
        AY = machines[mac]['A'][1]
        BX = machines[mac]['B'][0]
        BY = machines[mac]['B'][1]
        PX = machines[mac]['P'][0]
        PY = machines[mac]['P'][1]
        x1 = 0
        y1 = 0
        # print(f'{mac}:x*{AX} + y*{BX} = {PX}:{diophantine_all_soln(AX,BX,PX)}')
        if PX%greatest_common_divisor(AX, BX) == 0 and PY%greatest_common_divisor(AY, BY) == 0:
            found = False
            (x1,y1,p,q) = diophantine_all_soln(AX, BX, PX)
            (x2,y2,r,s) = diophantine_all_soln(AY, BY, PY)
            if PX == x1*AX+y1*BX and PY == x1*AY+y1*BY:
                t_tokens1+=3*x1+y1
                found = True
            elif PX == x2*AX+y2*BX and PY == x2*AY+y2*BY:
                t_tokens1+=3*x2+y2
                found = True
            else:
                tx = x1
                ty = y1
                tx2 = x2
                ty2 = y2
                if (x2-x1)%greatest_common_divisor(q, s) == 0 and (y2-y1)%greatest_common_divisor(p,r) == 0:
                    (a,b,c,d) = diophantine_all_soln(p,r,y2-y1)
                    (i,j,l,m) = diophantine_all_soln(q,s,x2-x1)
                    n1 = -(-i*p*s + i*q*r + r*x1 - r*x2 + s*y1 - s*y2)//(m*q*r - m*p*s)
                    tx = x1 + (i+m*n1)*q
                    ty = y1 - (i+m*n1)*p
                    if (PX == tx*AX + ty*BX and PY == tx*AY + ty*BY):
                        t_tokens1+=3*tx+ty
print(f'{t_tokens1=}')


###PART 2
for mac in machines:
    machines[mac]['P'][0] += 10000000000000
    machines[mac]['P'][1] += 10000000000000


t_tokens2 = 0
for mac in machines:
    if mac >= 0:
        AX = machines[mac]['A'][0]
        AY = machines[mac]['A'][1]
        BX = machines[mac]['B'][0]
        BY = machines[mac]['B'][1]
        PX = machines[mac]['P'][0]
        PY = machines[mac]['P'][1]
        x1 = 0
        y1 = 0
        # print(f'{mac}:x*{AX} + y*{BX} = {PX}:{diophantine_all_soln(AX,BX,PX)}')
        if PX%greatest_common_divisor(AX, BX) == 0 and PY%greatest_common_divisor(AY, BY) == 0:
            found = False
            (x1,y1,p,q) = diophantine_all_soln(AX, BX, PX)
            (x2,y2,r,s) = diophantine_all_soln(AY, BY, PY)
            if PX == x1*AX+y1*BX and PY == x1*AY+y1*BY:
                t_tokens2+=3*x1+y1
                found = True
            elif PX == x2*AX+y2*BX and PY == x2*AY+y2*BY:
                t_tokens2+=3*x2+y2
                found = True
            else:
                tx = x1
                ty = y1
                tx2 = x2
                ty2 = y2
                if (x2-x1)%greatest_common_divisor(q, s) == 0 and (y2-y1)%greatest_common_divisor(p,r) == 0:
                    (a,b,c,d) = diophantine_all_soln(p,r,y2-y1)
                    (i,j,l,m) = diophantine_all_soln(q,s,x2-x1)
                    n1 = -(-i*p*s + i*q*r + r*x1 - r*x2 + s*y1 - s*y2)//(m*q*r - m*p*s)
                    tx = x1 + (i+m*n1)*q
                    ty = y1 - (i+m*n1)*p
                    if (PX == tx*AX + ty*BX and PY == tx*AY + ty*BY):
                        t_tokens2+=3*tx+ty
print(f'{t_tokens2=}')