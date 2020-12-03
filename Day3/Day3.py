#%%
#!=== DATA ===!#
grid = []
input = open("input.txt", "r")
for line in input:
    x = list(line)
    x.remove(x[-1])
    grid+=[x]
# %%
#!=== PART 1 ===!#
x = 0
trees = 0
for line in grid:
    if line[x%len(line)]=='#':trees+=1
    x+=3
print(trees)
# %%
#!=== PART 2 ===!#
from math import prod
y = 0
right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]
trees = []
for i in range(len(right)):
    x = 0
    temp = 0
    for y in range(0,len(grid),down[i]):
        if grid[y][x%len(grid[y])]=='#':temp+=1
        x+=right[i]
    trees+=[temp]
print(prod(trees))
# %%
