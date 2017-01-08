from collections import defaultdict
def GroupData(inputFile, delimiterString):
    data = defaultdict(list)
    with open(inputFile, 'rt') as f:
        lines = f.readlines()
        for row in lines:
            content = row.split(delimiterString)
            data[content[0]].append(content[1])
    [print(a,b) for a,b in data.items()]
    