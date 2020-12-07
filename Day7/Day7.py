#%%
input = open("input.txt", "r")
part1 = 0
part2 = 0
bags = {}
for line in input:
    line = line.strip().split()
    key = line[0]+' '+line[1]
    value = []
    for i in range(2,len(line)):
        if line[i].isdigit():
            value+=[[int(line[i]), line[i+1]+' '+line[i+2]]]
        elif line[i]=='no':
            value+=[[line[i]+' '+line[i+1]]]
    bags[key]=value

def contain(key, check):
    if any('shiny gold' in i for i in bags[key]): return 1
    elif any('no other' in i for i in bags[key]): return 0
    for i in bags[key]:
        check += contain(i[1], check)
    return 1 if check else 0
        
def contain2(key, check):
    if any('no other' in i for i in bags[key]): return 1
    for i in bags[key]:
        check += (i[0] * contain2(i[1], 0))
    return check+1

for key in bags:
    if contain(key, 0):
        part1+=1
    if key == 'shiny gold':
        part2 = contain2(key, 0)-1

print(f'There are {part1} bags that contain shiny gold bag directly (or not)!')
print(f'Shiny gold bag fits {part2} bags inside it!')
# %%

