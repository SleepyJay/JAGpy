
#import Looper

import imp; imp.reload(Looper)


# only does 0-1 x 3 (for reference)
def boring():
    boring = []
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0,2):
                boring.append([x,y,z])    

    return boring

# ----

boring = boring()
i=0 
for p in boring:
    i += 1
    print(f"{i}: {p}")

print('----')

# ----

items = Looper.list(0, 2, 3)
i=0
for p in items:
    i += 1
    print(f"{i}: {p}")

# ----

itered = Looper.value_to_list(0,5,87)
print(f"{itered}")
#i=0 
#for p in boring:
#    i += 1
#    print(f"{i}: {p}")

print('----')        


