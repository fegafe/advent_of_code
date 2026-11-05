import re

def mul_sum(groups):
    total = 0
    for x in groups:
        opers = x.split(',')
        lhs = int(opers[0].replace('mul(',''))
        rhs = int(opers[1].replace(')',''))
        # print(f'{lhs = }:{rhs = }')
        total += lhs*rhs 
    return total

# file = open('example.txt','r')
file = open('input.txt','r')

###PART 1 result = 160672468
dont  = 0
stotal = 0
input_str = ''
for report in file.readlines():
    input_str += report.replace('\r','').replace('\n','')
# print(input_str)
regex ='mul\(\d{1,3},\d{1,3}\)'
test = re.findall(regex,input_str)
total = mul_sum(test)

print(f'{total = }')
input_str = input_str.replace('do()','\r\ndo()')
input_str = input_str.replace('don\'t()','\r\ndon\'t()')
# print(input_str)
lines = input_str.split('\r\n')
for line in lines:
    if 'don\'t' in line[0:5]:
        retest = re.findall(regex,line)
        # print(line)
        dont += mul_sum(retest) 
    else:
        # print(line)
        retest = re.findall(regex,line)
        stotal += mul_sum(retest) 

print(total)
print(dont)
print(stotal) ##new 124717256
print(total-dont) ##112946746
print(stotal+dont) 