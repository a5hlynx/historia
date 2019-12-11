#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
from __future__ import print_function

import sqlite3
import sys
import os
import csv

def write_header(cursor, file):
    header = []
    for d in cursor.description:
        header.append(d[0])

    out = open(file, "w")
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(header)
    out.close()

def write_records(cursor, file):
    out = open (file, "a")
    writer = csv.writer(out, lineterminator="\n")
    for x in cursor.fetchall():
        row = []
        for c in x:
            row.append(c)
        writer.writerow(row)
    out.close()

def historia(input,output,q):
    con = None
    if os.path.isfile(input):
        try:
            con = sqlite3.connect(input)
        except:
            print("error", file=sys.stderr)
            sys.exit(1)
    else:
        print("no such file {}".format(input), file=sys.stderr)
        print("exitting.", file=sys.stderr)
        sys.exit(1)


    try:
        cursor = con.cursor()
        cursor.execute(q)
    except Exception as e:
        print (e, file=sys.stderr)
        sys.exit(1)

    write_header(cursor, output)
    write_records(cursor, output)

    con.close()