#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
from __future__ import print_function

import util
import sys
import argparse

es = "11644473600"
q = "SELECT "\
        "u.url AS URL,"\
        "u.title AS title,"\
        "datetime(v.visit_time/1000000 - " + es + ", 'unixepoch', 'localtime' ) AS 'visit time',"\
        "u.visit_count AS 'visit count',"\
        "u2.url AS 'visit from' "\
     "FROM "\
        "visits AS v "\
        "INNER JOIN urls AS u ON v.url = u.id "\
        "LEFT JOIN visits AS v2 ON v.from_visit = v2.id "\
        "LEFT JOIN urls AS u2 ON v2.url = u2.id;"

if sys.version_info[0] != 3:
    print ("this script is supporsed to be run on python 3.", file=sys.stderr)
    print ("exitting.", file=sys.stderr)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default="History")
    parser.add_argument("-o", "--output", default="history.csv")
    args = parser.parse_args()

    util.historia(args.input, args.output, q)

if __name__ == '__main__':
    main()