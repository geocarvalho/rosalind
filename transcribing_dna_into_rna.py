#!/usr/bin/env python

'''
Giving a DNA string D corresponding to a coding strand, its transcribed RNA
string R is formed by replacing all occurences of "T" in D with "U" in R.

usage: python3 transcribing_dna_into_rna.py rosalind_rna.txt
'''

import sys

__author__ = "George Carvalho"


def dna_into_rna(dna):
    ''' transform DNA strands in RNA strands '''
    return dna.upper().replace('T', 'U')


if __name__ == '__main__':
    # sequence = 'GATGGAACTTGACTACGTAAATT'
    # out = 'GAUGGAACUUGACUACGUAAAUU'
    # print(dna_into_rna(sequence) == out)
    sequence = open(sys.argv[1]).readlines()[0].upper()
    print(dna_into_rna(sequence))
