#uncomment the following line for using Hadoop
!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # [derive mapper output key values]
    line = line.strip()
    incident_id, incident_type, vin_number, make, model, year, incident_date, description= line.split(",")

     #results = [vin_number, incident_type, make, year]
     #print("\t".join(results))

    print('%s\t%s\t%s\t%s' %(vin_number,incident_type,make,year))


"""
sample program execution on my local Windows 10 machine:

c:\study\sb\projects\autops>type data.csv | python mapper1.py
VXIO456XLBB630221       I       Nissan  2003
INU45KIOOPA343980       I       Mercedes        2015
VXIO456XLBB630221       A
VXIO456XLBB630221       R
VOME254OOXW344325       I       Mercedes        2015
VOME254OOXW344325       R
VXIO456XLBB630221       R
EXOA00341AB123456       I       Mercedes        2016
VOME254OOXW344325       A
VOME254OOXW344325       R
EXOA00341AB123456       R
EXOA00341AB123456       A
VOME254OOXW344325       R
UXIA769ABCC447906       I       Toyota  2017
UXIA769ABCC447906       R
INU45KIOOPA343980       A

c:\study\sb\projects\autops>
"""
