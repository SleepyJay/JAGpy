
"""Generic looping"""


#
def list(start,stop,size):
    full = []
        
    for x in range(start, stop):
        full.append([x])
    
    nxt = []
    for i in range(0, size-1):
        nxt = []
        for z in range(start, stop):
            for l in full: 
                cur = []   
                for y in l:
                    cur.append(y)
                #print(f"c>{cur}")
                cur.append(z)
                nxt.append(cur)
    
        full = nxt
        #print(f"f>{full}")
    return full


# turn a number in to a list of bits with a given base.    
# options:
    # start, stop, value: the list is normalized up to the range given (# needs better words)
    # stop, value: go from 0 to base in the "bits" 
def value_to_list(start, stop, value):
    list = []
    
    base = stop-start
    iter = value
    while iter > base:
         res = divmod(iter, base)
         iter = res[0]
         list.append(res[1])
    
    list.append(iter)        
    
    return list


