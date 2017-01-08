import sys
import operator

def GetDistinctLength(input):
    with open(input,mode='rt') as f:
        lines = f.readlines()
        distinctLen = {len(line) for line in lines}    
    print ([x-1 for x in distinctLen])

def WriteToFile(data, file):
    with open(file,mode='wt') as f:
        f.write(str(data))
        
def GetDistinctAndDupesUnsorted(input, numofoccurences = 1, fileName=None, printList=False):
    with open(input, 'rt') as f:
        temp = dict()
        lines = f.readlines() 
        for x in lines:
            if x in temp:
                temp[x] = temp[x] + 1
            else:
                temp[x] = 1
        data = ([x[:-1] + "    " + str(y) for x, y in temp.items() if temp[x] >= numofoccurences])        
        if fileName is not None:
            f = open(fileName,mode='wt')
        if printList and fileName is not None:    
            for x in data:
                print (x)
                f.write(str(x) + "\n")
            f.flush()
            f.close()
        elif printList:
             for x in data:
                print (x)
        elif fileName is not None:
            for x in data:                
                f.write(str(x) + "\n")
            f.flush()
            f.close()
def GetDistinctAndDupes(input, numofoccurences = 1, fileName=None, printList=False):
    with open(input, 'rt') as f:
        temp = dict()
        lines = f.readlines() 
        for x in lines:
            if x in temp:
                temp[x] = temp[x] + 1
            else:
                temp[x] = 1        
        data = (temp.items())
        data = sorted(data, key=operator.itemgetter(1))
        data = ([x[0][:-1] + "    " + str(x[1]) for x in data if x[1] >= numofoccurences])
        if fileName is not None:
            f = open(fileName,mode='wt')
        if printList and fileName is not None:    
            for x in data:
                print (x)
                f.write(str(x) + "\n")
            f.flush()
            f.close()
        elif printList:
             for x in data:
                print (x)
        elif fileName is not None:
            for x in data:                
                f.write(str(x) + "\n")
            f.flush()
            f.close()            

def GetDistinct(input, printList=False):
    with open(input,mode='rt') as f:
        lines = f.readlines()
        distinct = {(line) for line in lines}
        if printList:    
            print ([x[:-1] for x in distinct])
        print ("Distinct lines in file count: " + str(len(distinct)))
        print ("Total lines in file count: " + str(len(lines)))

def GetDupes(input, printList=False):
    with open(input,mode='rt') as f:
        lines = f.readlines()
        distinct = {(line) for line in lines}
        if printList:    
            print ([x[:-1] for x in distinct])
        print ("Distinct lines in file count: " + str(len(distinct)))
        print ("Total lines in file count: " + str(len(lines)))        

def Difference(input1, input2, writeToFile=False):
    with open(input1,mode='rt') as f1:
        lines1 = {line[:-1] for line in f1}
    with open(input2,mode='rt') as f2:
        lines2 = {line[:-1] for line in f2}    
    with open('lines1-lines2.txt', mode='wt') as w:
        print("In 1st not in 2nd")
        for x in lines1.difference(lines2):
            if writeToFile:
                w.write(str(x) + "\n")
            else:
                print (x)
    with open('lines2-lines1.txt', mode='wt') as w2:
        print("In 2nd not in 1st")
        for x in lines2.difference(lines1):
            if writeToFile:
                w2.write(str(x) + "\n")
            else:
                print (x)

def Common(input1, input2, writeToFile=False):
    with open(input1,mode='rt') as f1:
        lines1 = {line[:-1] for line in f1}
    with open(input2,mode='rt') as f2:
        lines2 = {line[:-1] for line in f2}
    print ("Common")
    with open('Common.txt', mode='wt') as w:
        for x in lines1.intersection(lines2):
            if writeToFile:
                w.write(str(x) + "\n")
            else:
                print (x)  

#if __name__ == '__main__':    
    #Difference("1.txt", "2.txt", True)
    #Common("1.txt", "2.txt", True)