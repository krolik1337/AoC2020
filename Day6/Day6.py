#%%
#!=== PART 1 ---!#
input = open("input.txt", "r")
total = 0
data=''
for line in input:
    if len(line)>1:
        data += line.strip()
    else: data+=line
data = data.split('\n')
for record in data:
    total+=len(set(record))
print(total)
# %%
#!=== PART 2 ===!#
input = open("input.txt", "r")
total = 0
data=''
for line in input:
    if len(line)>1:
        data += line.strip()+' '
    else: data+=line
data = data.split('\n')
for record in data:
    record = sorted(record.split(), key=len)
    total+= sum(1 for i in record[0] if all(i in j for j in record))
print(total)
# %%
