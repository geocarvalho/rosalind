#!/usr/bin/activate python3

''' Given: Two DNA strings s and t
Return: All locations of t as a substring of s. '''

__author__ = 'George Carvalho'

import sys


def pattern_start(lst):
    ''' Hard way to search for the exact match starting point '''
    seq, pat = map(str, lst)
    match = []
    for i in range(len(seq) - len(pat) + 1):
        if seq[i:i+len(pat)] == pat:
            # add to every position match because python start count in 0
            match.append(str(i+1))
    return ' '.join(match)


if __name__ == '__main__':
    # lst = ['GATATATGCATATACTT', 'ATAT']
    # out = '2 4 10'
    # print(pattern_start(lst)==out)
    lst = [x.strip() for x in open(sys.argv[1]).readlines()]
    print(pattern_start(lst))
