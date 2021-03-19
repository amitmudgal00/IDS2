#!/usr/bin/env python

from operator import itemgetter
import sys

current_case = None
current_service_time = 0
case = None

# input comes from STDIN
for kv_pair in sys.stdin:
    # remove whitespace
    kv_pair = kv_pair.strip()
    # parse the input (case,service_time) we got from mapper.py
    case, service_time = kv_pair.split('\t', 1)
    # convert service_time (currently a string) to float
    service_time = float(service_time)
    # shuflling is done by Hadoop
    if current_case!=case:
        if current_case:
            # write result to STDOUT
            print('%s\t%s' % (current_case, current_service_time))
        current_case = case
        current_service_time = service_time
    else:
        current_service_time += service_time

# output the last case
if current_case == case:
    print('%s\t%s' % (current_case, current_service_time))