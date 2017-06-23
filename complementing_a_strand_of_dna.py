#!/usr/bin/env python

'''
The reverse complement of a DNA string S is RC formed by reversing the symbols
of S, then taking the complement of each symbol (eg.: S="GTCA" -> RC="TGAC")

usage: python3 complementing_a_strand_of_dna.py rosalind_revc.txt
'''

__author__ = 'George Carvalho'

import sys


def reverseComplement(seq):
    ' Returns a reverse complement DNA string from a giving sequence '
    complements = {
                    "A": "T",
                    "T": "A",
                    "G": "C",
                    "C": "G"
    }
    rComp = ""
    for n in seq:
        rComp = complements[n] + rComp
    return rComp


if __name__ == '__main__':
    # sequence = 'AAAACCCGGT'
    # out = 'ACCGGGTTTT'
    # print(reverseComplement(sequence) == out)
    sequence = open(sys.argv[1]).readlines()[0].strip().upper()
    print(reverseComplement(sequence))
