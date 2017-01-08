with open(r'raw\CIPInvoices.txt',mode='rt', encoding='utf-8') as f:
    lines = f.readlines()
    for l in lines:
        print (l)
