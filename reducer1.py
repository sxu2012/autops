#uncomment the following line for using Hadoop
!/usr/bin/env python

import sys

#Define group level master information
current_vin =  None
make = None
year = None
accidents = 0 

#Run for end of every group
def flush():
    #Write the output
    if (accidents > 0):    
        print('%s\t%s\n' %(make,year) * accidents)

for line in sys.stdin:
    line = line.strip()

    line= line.split("\t")
    vin = line[0]
    incident_type= line[1]
    #parse the input we got from mapper1 and update the master info
    #the input is sorted by the key (vin)
    if incident_type == 'I' and current_vin == vin:
        make= line[2]
        year= line[3]    
        
    #detect key changes, new vin
    if current_vin != vin:
        if current_vin != None:
            #write current_vin to STDOUT
            flush()
        #reset for a new group of lines with the same vin
        current_vin =  None
        make = None
        year = None
        accidents = 0 

   # [update more master info after the key change handling]
    if incident_type == 'I':
        make= line[2]
        year= line[3]  
    elif incident_type == 'A':
        accidents += 1

    current_vin = vin
# do not forget to output the last group if needed!
flush()

"""
Sample execution of mapper1.py and reducer1.py on local machine:

c:\study\sb\projects\autops>type data.csv | python mapper1.py | sort | reducer1.py
Mercedes        2016

Mercedes        2015

Mercedes        2015

Nissan  2003


c:\study\sb\projects\autops>
"""
