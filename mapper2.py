#uncomment the following line for using Hadoop
!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    if line:
        # parse the input we got from reducer1.py
        line = line.split('\t')
        make=line[0]
        year=line[1]

        #output key, value pair, the key is make_year, value is 1
        print('%s-%s\t%d' %(make,year,1))

"""
Sample result running on local PC:
c:\study\sb\projects\autops>type data.csv | python mapper1.py | sort | reducer1.py | mapper2.py
Mercedes-2016   1
Mercedes-2015   1
Mercedes-2015   1
Nissan-2003     1

c:\study\sb\projects\autops>
"""