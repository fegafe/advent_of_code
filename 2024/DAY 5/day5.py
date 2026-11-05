def check_rules_order(orderi, rules):
    correct = True
    for e in range(len(orderi)):
        for j in range(len(rules)):
            if orderi[e] == rules[j][0]:
                for l in range(e):
                    if orderi[l] == rules[j][1]:
                        correct = False
                        # print(f'{order[i][l]} before: {order[i][e]} in {order[i]}')
    return correct

def correc_pair(orderi,rules):
    for e in range(len(orderi)):
        for j in range(len(rules)):
            if orderi[e] == rules[j][0]:
                for l in range(e):
                    if orderi[l] == rules[j][1]:
                        # print(f'{orderi[l]} before: {orderi[e]} in {orderi}')
                        orderi[l] = rules[j][0]
                        orderi[e] = rules[j][1]
    return orderi

# file = open('example.txt','r')
file = open('input.txt','r')

rules = []
order = []
donerules = False
for line in file.readlines():
    if line == '\n':
        donerules = True
    elif donerules:
        torder = []
        for x in line.strip().split(','):
            torder.append(int(x))
        order.append(torder)
    else: 
        rules.append((int(line.split('|')[0]),int(line.split('|',)[1])))

# print(rules)
# print(order)
orderok =[]
ordernotok = []
for i in range(len(order)):
    correct = check_rules_order(order[i],rules)
    if correct:
        orderok.append(i)
    else:
        ordernotok.append(i)
        # print(f'{order[i]}:{correct}')
respart1 = 0
for i in orderok:
    if len(order[i])%2 != 1:
        print(f'{order[i]}:Not odd')
    else:
        index = len(order[i])//2
        respart1 += order[i][index]
print(f'{respart1=}')

outorder = []
for i in ordernotok:
    status = False
    while not status:
        torder = correc_pair(order[i],rules)
        order[i]=torder
        if check_rules_order(torder, rules):
            status = True
            outorder.append(order[i])
    if not status:
        print(f'error in i:{i} -> {order[i]}')
        i -= 1

respart2 = 0
for i in ordernotok:
    if len(order[i])%2 != 1:
        print(f'{order[i]}:Not odd')
    else:
        index = len(order[i])//2
        respart2 += order[i][index]
print(f'{respart2=}')