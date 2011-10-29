import re


BLOCK_START = False
CLOSE_BLOCK = 'ATURAN URUSAN MESYUARAT DAN USUL-USUL'

def write_splitted(fname,data):
    f = open(fname,'a')
    f.write(data)
    f.close()

def parse(finput):
    BLOCK_START = False
    output = finput.next()
    data = ''
    while output:
        if re.match(r'^\d+\.\s+PR',output):
            yield data
            BLOCK_START = True
            data = output
        
        elif re.match(r'^AUM',output):
            pass
        
        elif re.match(r'^\s+$',output):
            pass
            
        elif re.match(r'^\x0c$',output):
            pass
        
        elif re.search(CLOSE_BLOCK,output):
            BLOCK_START = False
        
        elif re.match(r'^\s+\d+',output):
            pass
            
        else:
            if BLOCK_START:
                #write_splitted(fname,output)
                data = data + output
        try:       
            output = finput.next()
        except:
            yield data
            break
        
    
        
def driver(filename):
    f = open(filename)
    for i in parse(f):
        print i
