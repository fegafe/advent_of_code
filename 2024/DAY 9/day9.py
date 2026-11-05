def print_sort(arr):
    for i in range(len(arr)):
        print(arr[i],end='')

# file = open('example.txt','r')
file = open('input.txt','r')

linein = ''
j=0
for line in file.readlines():
    linein = line.strip()

idd = 0

tosort = []
tosort2 = []
spaces = {}
data = {}
for i in range(len(linein)):
    n = int(linein[i])
    if i%2 == 0:
        ch = str(idd).strip()
        data[idd] = n
        idd += 1
    else:
        ch = '.'
        spaces[idd-1] = n
    for j in range(n):
        tosort.append(ch)
        tosort2.append(ch)

# print(idd)
i = 0
j = len(tosort)-1

while i< j:
    if tosort[i] == '.':
        tosort[i] = tosort[j]
        tosort[j] = '.'
    while tosort[i] != '.':
        i += 1
    while tosort[j] == '.':
        j -= 1
    # print_sort(tosort)
    # print('')

respart1 = 0
for i in range(len(tosort)):
    if tosort[i] == '.':
        continue
    else:
        respart1 += i*int(tosort[i])
print(f'{respart1=}')

idc = idd-1
# print_sort(tosort2)
# print('')

while idc >=0 :
    tofind = data[idc]
    i = 0
    # print(f'{tofind=}:{i=}')
    tofill = 0
    while i < len(tosort2)-1 and tofill < tofind:
        i += tofill
        tofill = 0
        
        while tosort2[i] != '.':
            i += 1
        l = i
        while tosort2[l] == '.':
            tofill += 1
            l += 1
            if l >=len(tosort2)-1:
                i += l
                tofill=0
                break
        # print(f'{tofill=}:{i=}')

    if tofill >= tofind and i < j:
        j = len(tosort2)-1
        while tosort2[j] != str(idc) and i<j:
            j -= 1
        if i<j:
            for k in range(data[idc]):
                tosort2[i+k] = tosort2[j-k]
                tosort2[j-k] = '.'
        # print_sort(tosort2)
        # print('')
    idc -= 1


# test = '00992111777.44.333....5555.6666.....8888..'
# tosort2 = []
# for i in range(len(test)):
    # tosort2.append(test[i])

respart2 = 0
for i in range(len(tosort2)):
    if tosort2[i] == '.':
        continue
    else:
        respart2 += i*int(tosort2[i])
print(f'{respart2=}')