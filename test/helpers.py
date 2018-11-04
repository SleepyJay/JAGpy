

# only does 0-1 x 3 (for reference)
def list_01_by_3():
    boring = []
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                boring.append([x, y, z])

    return boring


