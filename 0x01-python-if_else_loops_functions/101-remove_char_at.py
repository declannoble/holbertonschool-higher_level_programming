#!/usr/bin/python3


def remove_char_at(str, n):

    nstring = str
    if n >= 0:
        nstring = nstring[:n] + nstring[n+1:]
    return nstring
