#%%
expenses = list(map(int,open("input.txt", "r").read().split()))
#%%
#!===PART 1===!#
for i in expenses:
    for j in expenses:
        if i+j==2020:
            print(i*j)
            raise SystemExit
#%%
#!===PART 2===!#
for i in expenses:
    for j in expenses:
        for k in expenses:
            if i+j+k==2020:
                print(i*j*k)
                raise SystemExit
