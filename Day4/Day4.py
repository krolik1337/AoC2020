#%%
#!=== PART 1 ===!#
input = open("input.txt", "r")
total = 0
current=''
data=''
for line in input:
    if len(line)>1:
        data += line.strip()+' '
    else: data+=line
data = data.split('\n')
for record in data:
    record = record.split()
    if len(record)==8 or (len(record)==7 and all('cid' not in i for i in record)):
        total+=1
print(total)
# %%
#!=== PART 2 ===!#
input = open("input.txt", "r")
total = 0
data=''
data2=[]
for line in input:
    if len(line)>1:
        data += line.strip()+' '
    else: data+=line
data = data.split('\n')
for record in data:
    current = {}
    record = record.split()
    for i in record:
        key, value = i.split(':')
        current[key] = value
    data2+=[current]

for record in data2:
    tests = 0
    if 'byr' in record and len(record['byr'])==4 and 1920<=int(record['byr'])<=2002:tests+=1
    if 'iyr' in record and len(record['iyr'])==4 and 2010<=int(record['iyr'])<=2020:tests+=1
    if 'eyr' in record and len(record['eyr'])==4 and 2020<=int(record['eyr'])<=2030:tests+=1
    if 'hgt' in record:
        if 'cm' in record['hgt'] and 150 <= int(record['hgt'][:-2]) <=193: tests+=1
        if 'in' in record['hgt'] and 59 <= int(record['hgt'][:-2]) <=76: tests+=1
    if 'hcl' in record and len(record['hcl'])==7 and all(i in '#abcdef1234567890' for i in record['hcl']):tests+=1
    if 'ecl' in record and record['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:tests+=1
    if 'pid' in record and len(record['pid']) == 9 and all(i.isdigit() for i in record['pid']):tests+=1
    if tests==7: total+=1
print(total)
# %%
