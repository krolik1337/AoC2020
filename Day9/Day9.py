#%%
data = list(map(int,open("input.txt", "r").read().split()))

index = 25
myNumber = 0

while index < len(data):
    slice = data[index-25:index]
    broken = False
    for i in slice:
        for j in slice:
            if i+j==data[index]:
                index+=1
                broken = True
                break
        if broken: break
    else:
        myNumber = data[index]
        print('My number is', myNumber)
        break

for i in range(len(data)):
    numbers = []
    index = i
    broken = False
    while True:
        numbers += [data[index]]
        if sum(numbers) == myNumber:
            print(f'Smallest: {min(numbers)}, Largest: {max(numbers)}, Result: {min(numbers) + max(numbers)}')
            broken = True
            break
        elif sum(numbers) > myNumber:
            break
        else:
            index += 1
    if broken:
        break

# %%
