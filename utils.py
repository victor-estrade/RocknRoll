#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals


def parse_passe_file(fname):
    with open(fname) as file:
        lines = file.readlines()
    d = {}
    passes = []
    for line in lines[2:]:  # skip header
        if line == '\n':  # empty lines separate moves
            if d:
                passes.append(d)
            d = {}
        else:
            k, v = line.split(sep=':')
            k = k.strip()  # remove leading and trailing spaces
            v = v.strip()  # remove leading and trailing spaces
            d[k] = v
    return passes

