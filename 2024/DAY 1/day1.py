

left  = []
right = []

file = open('first_input.txt','r')
# file = open('test.txt','r')
for line in file.readlines():
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))

llist  = list(left)
rlist  = list(right)

# llist.sort(reverse=False)
# rlist.sort(reverse=False)

d = 0
for x in llist:
    c = 0
    for i in range(len(rlist)):
        if x == rlist[i]:
            c += 1
    # td = (llist[i] - rlist[i])
    # if td < 0:
        # td = -td
    d += c * x
print(d)

