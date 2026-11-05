##sort input ranges
sranges = sorted(ranges, key=lambda x:x[0],reverse =  False)

nranges = []
for r in sranges:
    nt = r
    for nr in nranges:
        if r[0] <= nr[1]:
            nt = (nr[0],max(r[1],nsr[1]))
            nranges.remove(nr)
            break
    nranges.append(nt)

##nranges sorted full new ranges (joined if necesary)