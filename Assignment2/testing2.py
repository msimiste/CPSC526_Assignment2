


def main(args):
    list1 =  [(['70 3a 2f 2f 77 77 77 2e', '75 6d 61 67 2e 63 61 22'], ['p://www.', 'umag.ca"']), 
 (['3e 55 20 4d 61 67 61 7a', '69 6e 65 3c 2f 61 3e 3c'], ['>U Magaz', 'ine</a><']), 
 (['20 20 20 20 20 20 20 20', '3c 6c 69 3e 3c 61 20 68'], ['        ', '<li><a h']),
  (['72 65 66 3d 22 68 74 74', '70 3a 2f 2f 77 77 77 2e'], ['ref="htt', 'p://www.']), 
  (['75 63 61 6c 67 61 72 79', '2e 63 61 2f 70 75 62 73'], ['ucalgary', '.ca/pubs']),   
  (['2f 63 61 6c 65 6e 64 61', '72 2f 22 3e 55 6e 69 76'], ['/calenda', 'r/">Univ']), 
  (['65 72 73 69 74 79 20 43', '61 6c 65 6e 64 61 72 3c'], ['ersity C', 'alendar<']),
   (['2f 61 3e 3c 2f 6c 69 3e', '20 20 20 20 20 20 3c 2f'], ['/a></li>', '      </'])]
    retVal = joiner(list1)    
    #test = ''.join(str(chr(x)) for x in retVal) 
    #print test
    
def joiner(inVal):
	pre = '<-----'
	line =  map(lambda x: x[0][0] + '  ' + x[0][1] + '  |' + x[1][0] + x[1][1] +'|', inVal)
	out = pre.join(x + '\n' for x in line)
	print(out)      
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
