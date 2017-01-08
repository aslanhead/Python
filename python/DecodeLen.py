def DecodeLength(input):
    prev = -1    
    total = 0
    for c in input:        
        k = int(c)        
        if k < 1 or k > 9:
            print ("bad input: should contain digits ranging from 1 and 9")
            return -1
        total = total + 1
        if prev != -1:
            value = prev*10 + k
            if value <= 26:
                total = total + 1
        prev = k
    return total

if __name__ == '__main__':    
    print(DecodeLength('123'))