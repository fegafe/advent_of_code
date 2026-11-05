import sys

# Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0

def runcode(opc, ope):
    global IP,out,regis
    if  opc == 0:
        if ope>3:
            regis[0] = regis[0] // 2**regis[ope-4]
        else:
            regis[0] = regis[0] // 2**ope
        IP += 1
    elif opc == 1:
        regis[1] = regis[1] ^ ope
        IP += 1
    elif opc == 2:
        if ope > 3:
            regis[1] = regis[ope-4]%8
        else:
            regis[1] = ope%8
        IP += 1
    elif opc == 3:
        if regis[0] != 0:
            IP = ope
        else:
            IP += 1
    elif opc == 4:
        regis[1] = regis[1] ^ regis[2]
        IP += 1
    elif opc == 5:
        if ope>3:
            out += str(regis[ope-4]%8)+','
        else:
            out += str(ope%8)+','
        IP += 1
    elif opc == 6:
        if ope>3:
            regis[1] = regis[0] // 2**regis[ope-4]
        else:
            regis[1] = regis[0] // 2**ope
        IP += 1
    elif opc == 7:
        if ope>3:
            regis[2] = regis[0] // 2**regis[ope-4]
        else:
            regis[2] = regis[0] // 2**ope
        IP += 1

# file = open('example.txt','r')
# # file = open('input.txt','r')

sys.setrecursionlimit(1000000)

RA = 28422061
# 164278473950527
# RA = 8193
RB = 0
RC = 0
instr = [2,4,1,1,7,5,1,5,4,2,5,5,0,3,3,0]

linstr = []
for l in instr:
    linstr.append(str(l))
print(linstr)
regis = [RA,RB,RC]
IP = 0
out = ''
opcode = []
operan = []
for i in range(len(instr)):
    if i%2==0:
        opcode.append(instr[i])
    else:
        operan.append(instr[i])

print(opcode)
print(operan)

i=0
##PART1
while IP < len(opcode):
    # print(f'{i=}{IP=}::{opcode[IP]}::{operan[IP]}::{out=}::{regis=}')
    runcode(opcode[IP], operan[IP])
    i += 1
respart1 = out[:-1]
print(f'{respart1=}') ##'3,6,7,0,5,7,3,1,4'


##PART2
 # 35184384000014

outprog = []
i = 0

# B = 8*k+3
# B xor C =      =xx
            # xxx011
# tra =  35186304000014
       # 35184372088832
# # tra = 281474000000014
      # 281474976710656
# linstr = []
# for l in instr:
    # linstr.append(str(l))

dig = {}
tra = 1
while outprog != linstr and i < 1025:
    out = ''
    regis=[tra,0,0]

    IP = 0
    while IP < len(opcode):
        runcode(opcode[IP], operan[IP])
    outprog = out[:-1].split(',')
    if int(out[0]) not in dig:
        dig[int(out[0])] = []
    dig[int(out[0])].append(tra)
    tra = tra + 1
    i += 1

for i in range(8):
    print(f'{i}:{dig[i]}')

def runprog(ra):
    global IP,regis,out
    regis=[ra,0,0]
    IP = 0
    out = ''
    while IP < len(opcode):
        runcode(opcode[IP], operan[IP])
    outstr = out[:-1].split(',')
    return outstr

i = -1
out = ''
tra = 0
stra =''
while outprog != linstr and i >= -16:
    found = False
    print(f'looking for {instr[i]}::{instr[16+i:]}')
    for j in dig[instr[i]]:
        if 0 <= j - (8*tra)%1024 <= 1024:
            outprog = runprog(8*tra + j - (8*tra)%1024)
            # print(f'{8*tra + j - (8*tra)%1024}::{outprog}')
            if len(outprog) == len(instr[16+i:]):
                if outprog == linstr[16+i:]:
                    print(f'{i}::dig={instr[i]}::{j}::{(8*tra)%1024}')
                    stra = f'8*({stra})+{j - (8*tra)%1024}'
                    print(stra)
                    tra = 8*tra + j - (8*tra)%1024
                    # print(tra)
                    found = True
                    break
    i -=1
print(f'{tra}::{outprog=}')



# ########################################
# td = 17
# i = td-1
# out = ''
# tra = 4
# stra =f'{tra}'
# while outprog != linstr and i >= 1:
    # found = False
    # regis=[tra,0,0]
    # IP = 0
    # out = ''
    # while IP < len(opcode):
        # runcode(opcode[IP], operan[IP])
    # outprog = out[:-1].split(',')
    # i -=1
    # if i < 1:
        # break
    # for j in dig[instr[i-td]]:
        # if 0 <= j - (8*tra)%1024 <= 1024:
            # print(f'{i}::dig={instr[i-td]}::{j}::{(8*tra)%1024}')
            # stra = f'8*({stra})+{j - (8*tra)%1024}'
            # print(stra)
            # tra = 8*tra + j - (8*tra)%1024
            # found = True
            # break
    # if not found:
        
        # print(f'in {td - i} dig={instr[i-td-1]} for {(8*tra)%1024}')
        # print(f'{tra}::{outprog=}')
# print(f'{tra}::{outprog=}')
# ###############################

# print(f'{a}::{tra}::{outprog=}::len={len(outprog)}')
# print(tra)
# respart2 = tra
# print(f'{respart2=}')

# print((164278496489122//8//8))
# print(2566851507642%1024)
# print(164278496489088%1024)
# # nra = 2566851507642*8*8
# nra = 164278496489088+61

# regis=[nra,0,0]
# IP = 0
# out = ''
# print(f'                 {linstr}')
# while IP < len(opcode):
    # runcode(opcode[IP], operan[IP])
# outprog = out[:-1].split(',')
# print(f'{nra}::{outprog}') ##164278496489149
