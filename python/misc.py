from collections import Counter

def CountWords(inputFile):
    with open(inputFile, 'rt', encoding='utf-8') as f:
        lines = f.readlines()
    c = Counter([line[:-1] for line in lines])
    print(c.most_common())

def GetDistinctAndDupes(input, numofoccurences = 1, fileName=None, printList=False):
    with open(input, 'rt', encoding='utf-8') as f:        
        lines = f.readlines() 
        c = Counter([line[:-1] for line in lines])
        if fileName is not None:
            f = open(fileName,mode='wt')
        if printList and fileName is not None:    
            for i,j in c.most_common():
                if j >= numofoccurences:
                    temp = [i + "    " + str(j)]
                    print (temp)
                    f.write(str(temp) + "\n")                    
            f.flush()
            f.close()
        elif printList:
             for i,j in c.most_common():
                 if j >= numofoccurences:
                    temp = [i + "    " + str(j)]
                    print (temp)
        elif fileName is not None:
            for i,j in c.most_common():
                if j >= numofoccurences:                    
                    temp = [i + "    " + str(j)]               
                    f.write(str(temp) + "\n")                    
            f.flush()
            f.close()

if __name__ == "__main__":
    GetDistinctAndDupes('1.txt',2,'rss.txt',True)