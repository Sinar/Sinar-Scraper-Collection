import re
import sqlite3

START = False
LINE_START = 'JAWAPAN-JAWAPAN LISAN BAGI PERTANYAAN-PERTANYAAN'
PAGE_END = '^\x0c$'
PAGE_START = '^\B+\d+$'
QUESTION_START = '\[ (\w\B*)+ \]'

TEXT_START = False

def write_to_splitted(fname,data):
    ofile = open(fname,'a')
    ofile.write(data)
    ofile.close()

def parser(finput):
    oname = 'output_%s.txt'
    count = 0
    output = finput.next()
    while not re.search(LINE_START,output):
        print output
        output = finput.next()
        
    output = finput.next()
    while output:
    
        if re.search(r'\] minta',output):
            print 'block %s ended' % str(count)
            count = count + 1
            print 'block %s started' % str(count)
            TEXT_START = True
            write_to_splitted(oname%str(count),output)
   
        elif re.match(r'^\s+([A-Z]\-*\s*)+$',output):
            print 'block %s ended' % str(count)
            TEXT_START = False
        
        elif re.match(r'^\s+$',output):
            #print 'blanks page: %s' % output
            
            pass
    
        elif re.match(r'^\s+\d+$',output):
            print 'page %s' % output
            pass
        
        elif re.match(r'^DR',output):
            print 'new page'
            pass
    
        else:
            if TEXT_START:
                print 'writing block %s' % str(count)
                write_to_splitted(oname%str(count),output)
            else:
                print 'block not started'
        output = finput.next()
            

def main(filename):
    f = open(filename)
    parser(f)
    
