#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
from __future__ import print_function

import sqlite3
import sys
import argparse
import os
import csv

es = "978307200"
q = "SELECT "\
        "i.url as URL,"\
        "h.title,"\
        "datetime(h.visit_time + " + es + ", 'unixepoch', 'localtime') as 'visit time',"\
        "i.visit_count as 'visit count',"\
        "i2.url as 'visit from' "\
     "FROM "\
        "history_visits h inner join history_items i on h.history_item = i.id "\
        "inner join history_visits h2 on h.redirect_source = h2.id "\
        "inner join history_items i2 on h2.history_item = i2.id;"

if sys.version_info[0] != 3:
    print ( "this script is supporsed to be run on python 3.", file=sys.stderr )
    print ( "exitting.", file=sys.stderr )
    sys.exit(1)

def write_header(cursor, file):
    header = []
    for d in cursor.description:
        header.append( d[0] )

    out = open( file, "w" )
    writer = csv.writer( out, lineterminator="\n" )
    writer.writerow( header )
    out.close()

def write_records(cursor, file):
    out = open ( file, "a" )
    writer = csv.writer( out, lineterminator="\n" )
    for x in cursor.fetchall():
        row = []
        for c in x:
            row.append( c )
        writer.writerow( row )
    out.close()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument( "-i", "--input", default="History.db" )
    parser.add_argument( "-o", "--output", default="history.csv" )
    args = parser.parse_args()

    con = None
    if os.path.isfile(args.input):
        try:
            con = sqlite3.connect(args.input)
        except:
            print( "error", file=sys.stderr )
            sys.exit(1)
    else:
        print( "no such file {}".format(args.input), file=sys.stderr )
        print( "exitting.", file=sys.stderr )
        sys.exit(1)


    try:
        cursor = con.cursor()
        cursor.execute(q)
    except Exception as e:
        print ( e, file=sys.stderr )
        sys.exit(1)

    write_header( cursor, args.output )
    write_records( cursor, args.output )

    con.close()


if __name__ == '__main__':
    main()