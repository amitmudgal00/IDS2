#!/usr/bin/env python

import sys

# input comes from STDIN
for line in sys.stdin:
    # remove whitespace and split row into values
	line_split = line.strip().split("\t")
	case = line_split[0]
	service_time = line_split[4]

    # write the results to STDOUT;
    # key: case, value: service_time
	print('%s\t%s' % (case, service_time))