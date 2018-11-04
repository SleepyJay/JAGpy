
import Looper
from collections import Counter

#import imp; imp.reload(Looper)




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
fake = [[1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

print("boring-id: {}".format(map(str,boring)))
print("items-id: {}".format(map(str,items)))
print("fake-id: {}".format(map(str,fake)))

c_items = Counter(map(str,items))
print("Counter-items: {}".format(c_items))

c_boring = Counter(map(str,boring))
print("Counter-boring: {}".format(c_boring))

c_fake = Counter(map(str,fake))
print("Counter-fake: {}".format(c_fake))

print("items == boring?")
if c_items == c_boring:
    print("Same")
else:
    print("Different")

print("fake == boring?")
if c_fake == c_boring:
    print("Same")
else:
    print("Different")

itered = Looper.value_to_list(0,5,87)
print(f"{itered}")
#i=0 
#for p in boring:
#    i += 1
#    print(f"{i}: {p}")

print('----')        


