


def main(args):
    testSlash = chr(92)
    testTab = chr(9)
    testNewline = chr(10)
    testReturn = chr(13)
    
    testStr = '    a' 
    #=[testSlash,testTab,testNewline,testReturn, chr(15)]
    print ' '.join(hex(ord(x)) for x in (testStr))
    out = map(lambda d: joiner(d), testStr)
    print "line 12: " , ' '.join(out[0:])
   
def joiner(char):
    print("Line 13: " + char)
    tempChar = ord(char)
    if(tempChar < 33) or (tempChar > 127):
        if(tempChar == 9):
            return repr(chr(tempChar))
        elif(tempChar == 10):
            return repr(chr(tempChar))
        elif(tempChar == 13):
            return repr(chr(tempChar))
        else:
            return  '\\' + str(hex(tempChar))
    elif(tempChar == 92):
        return chr(92)
    else:
        return char
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
