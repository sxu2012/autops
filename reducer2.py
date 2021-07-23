!/usr/bin/env python

import sys
 
key = None
value = 0

# Get input from stdin
for line in sys.stdin:
    #Remove spaces from beginning and end of the line
    line = line.strip().split('\t')
    if key == None:
        key = line[0]
    if key == line[0]:
        value += 1
    else:
        print('%s\t%s' %(key, value))
        key = line[0]
        value = 1
#output the last
print('%s\t%s' %(key, value))

"""
Sample output from running on a local PC:

c:\study\sb\projects\autops>type data.csv | python mapper1.py | sort | reducer1.py | mapper2.py | sort | reducer2.py
Mercedes-2015   2
Mercedes-2016   1
Nissan-2003     1

c:\study\sb\projects\autops>
"""