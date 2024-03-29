#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
from __future__ import print_function

import util
import sys
import argparse

es = "978307200"
q = "SELECT "\
        "i.url AS URL,"\
        "h.title,"\
        "datetime(h.visit_time + " + es + ", 'unixepoch', 'localtime') AS 'visit time',"\
        "i.visit_count AS 'visit count',"\
        "i2.url AS 'visit from' "\
     "FROM "\
        "history_visits AS h "\
        "INNER JOIN history_items AS i ON h.history_item = i.id "\
        "LEFT JOIN history_visits AS h2 ON h.redirect_source = h2.id "\
        "LEFT JOIN history_items AS i2 ON h2.history_item = i2.id;"

if sys.version_info[0] != 3:
    print ("this script is supporsed to be run on python 3.", file=sys.stderr)
    print ("exitting.", file=sys.stderr)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default="History.db")
    parser.add_argument("-o", "--output", default="history.csv")
    args = parser.parse_args()

    util.historia(args.input, args.output, q)

if __name__ == '__main__':
    main()