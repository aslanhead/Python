denominations = [1, 5, 10, 21, 25]
changelist = list()
def MakeChage(input):
    for x in range(1,100):
        if x in denominations:
            changelist.append(x)
            continue
        x.append(1, MakeChage(x-1))
            