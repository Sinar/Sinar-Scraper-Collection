import re
import string


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
        
        elif re.search(r'AUM',output):
            pass
        
        elif re.match(r'^\s+$',output):
            pass
            
        elif re.match(r'^\x0c$',output):
            pass
        
        elif re.search(CLOSE_BLOCK,output):
            BLOCK_START = False
        
        elif re.match(r'^\s+\d+',output):
            pass

        elif re.search('UCAPAN',output):
            if BLOCK_START:
                yield data
            BLOCK_START = False
            
        else:
            if BLOCK_START:
                #write_splitted(fname,output)
                data = data + output
        try:       
            output = finput.next()
        except:
            if BLOCK_START:
                yield data
            break
        
    
        
def driver(filename):
    f = open(filename)
    for i in parse(f):
        if i:
            t = i.split('\n')
            data = {}
            temp = t[1].split('[')
            data['name'] = string.rstrip(string.lstrip(temp[0]))
            temp = temp[1].split(']')
            place = temp[0]
            data['place'] = string.rstrip(string.lstrip(place))

            data['value'] = ' '.join([string.lstrip(j) for j in t[2:]])
            if re.search('minta',temp[1]):
                data['value'] = temp[1] + ' ' + data['value']
            yield data
