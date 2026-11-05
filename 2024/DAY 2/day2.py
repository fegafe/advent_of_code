
def abs_dif(x,y):
    if (x-y) < 0:
        return y-x
    else:
        return x-y


def test_arr(levels):
    typ = 0
    rep = True
    i = 0
    fail = -1
    while i < len(levels)-1:
        if levels[i] > levels[i+1]:
            typ -= 1
        elif levels[i] < levels[i+1]:
            typ += 1
        if abs_dif(levels[i+1],levels[i]) > 3 or abs_dif(levels[i+1],levels[i]) == 0 or abs_dif(typ,0) < i:
            # # PART 1
            rep = False
            fail = i
            return rep
        i += 1
    return rep

# file = open('example.txt','r')
file = open('input.txt','r')
safe = 0

for report in file.readlines():
    rlevels = []
    levels_str = report.split()
    for i in range(len(levels_str)):
        rlevels.append(int(levels_str[i]))

    if test_arr(rlevels):
        safe += 1
    else:
        for i in range(len(rlevels)):
            nlevels = []
            for j in range(len(rlevels)):
                if i!= j:
                    nlevels.append(rlevels[j])
            if test_arr(nlevels):
                safe += 1
                break
print(safe)

