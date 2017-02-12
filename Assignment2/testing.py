
#  


def main(args):
    list1 = [51,10,55,62,63,64,65,10,62,63,64,65,10,62,63,64,65]
    retVal = joiner(list1)    
    test = ''.join(str(chr(x)) for x in retVal) 
    print test
    
def joiner(inVal):
    list2 = [60,45,45,45,45]
    list2.reverse()
    listFull = []
    for i,v in enumerate(inVal):
        if v == 10:
            print(i,v)
            map(lambda x: inVal.insert(i+1,x), list2)    
    return inVal     
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
