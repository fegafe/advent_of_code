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
 
def nextnsol(x,n=1):
    return (x[0]+n*x[3],x[1]-n*x[2],x[2],x[3])

if __name__ == "__main__":
    AX = 62
    AY = 48
    BX = 21
    BY = 74
    PX = 10000000003946
    PY = 10000000006404
    # PX = 3946
    # PY = 6404
    (x1,y1,p,q) = diophantine_all_soln(AX,BX,PX)
    (x2,y2,r,s) = diophantine_all_soln(AY,BY,PY)
    (a,b,c,d)   = diophantine_all_soln(p,r,y2-y1)
    (i,j,l,m)   = diophantine_all_soln(q,s,x2-x1)
    
    (i1,j1,l1,m1) = nextnsol((i,j,l,m),0)
    (a1,b1,c1,d1) = nextnsol((a,b,c,d),0)
    tx = x1 + i1*q
    ty = y1 - i1*p
    tx2 = x2 - a1*s
    ty2 = y2 + a1*r
    print(f'{(tx,ty)}:{tx*AX + ty*BX} : {PX} || {tx*AY + ty*BY} : {PY}')
    print(f'{(tx2,ty2)}:{tx2*AX + ty2*BX} : {PX} || {tx2*AY + ty2*BY} : {PY}')
    (i1,j1,l1,m1) = nextnsol((i,j,l,m),1)
    (a1,b1,c1,d1) = nextnsol((a,b,c,d),-1)
    ## tx1 = x1 + (i+m*n1)*q
    ## tx2 = x2 - (a-d*n2)*s
    ## x2-x1 = i*q +m*n1*q + a*s-d*n2*s
    ## x2 - x1 - i*q - a*s = m*q*n1 - d*s*n2
    
    ##ty1 = y1 - (i+m*n1)*p
    ##ty2 = y2 + (a-d*n2)*r
    ## y2 -y1 = -i*p -m*n1*p - a*r +d*n2*r
    ## y2 - y1 + i*p + a*r = -m*p*n1 + d*r*n2
    ## x2 - x1 - i*q - a*s =  m*q*n1 - d*s*n2
    
    ## (y2 - y1 + i*p + a*r + m*p*n1) / (d*r)= n2
    ## (x2 - x1 - i*q - a*s)*r = m*q*n1*r - s*(y2 - y1 + i*p + a*r) - s*m*p*n1
    ##(x2 - x1 - i*q - a*s)*r + s*(y2 - y1 + i*p + a*r) = n1 * (m*q*r - s*m*p)
    n1 = (x2 - x1 - i*q - a*s)*r + s*(y2 - y1 + i*p + a*r) // (m*q*r - s*m*p)
    n1 = -(-i*p*s + i*q*r + r*x1 - r*x2 + s*y1 - s*y2)//(m*q*r - m*p*s)
    print(n1)
    # (n1,n2,f,g) = diophantine_all_soln(m*p,d*r,y2 - y1 + i*p + a*r)
    # print((n1,n2,f,g))
    # (n1,n2,f,g) = diophantine_all_soln(m*q,d*s,x2 - x1 - i*q - a*s)
    # print((n1,n2,f,g))
    tx = x1 + (i+m*n1)*q
    ty = y1 - (i+m*n1)*p
    tx2 = x2 - a1*s
    ty2 = y2 + a1*r
    print(f'{(tx,ty)}:{tx*AX + ty*BX} : {PX} || {tx*AY + ty*BY} : {PY}')
    # print(f'{(tx2,ty2)}:{tx2*AX + ty2*BX} : {PX} || {tx2*AY + ty2*BY} : {PY}')
    # print(diophantine_all_soln(66,21,12176))