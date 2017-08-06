#!/usr/bin/env python3
'''
Given a fasta file and a positive integer K, return the overlap edges in any
order
usage: python overlap_graphs.py rosalind_grph.txt > overlaps.txt
'''

__author__ = 'George Carvalho'

import sys


def read_fasta(fasta):
    ''' Read fasta and return a dictionary with label and sequence as key and
    value respectivelly '''
    fasta_dict = {}
    for line in fasta:
        if not line:
            continue
        if line.startswith('>'):
            sname = line.replace('>', '')
            if sname not in fasta_dict:
                fasta_dict[sname] = ''
        else:
            fasta_dict[sname] += line
    return fasta_dict

def print_overlaps(fasta, k):
    ''' Search for overlaps in each sequence and print when the pattern
    match '''
    for sn1, s1 in fasta.items():
        for sn2, s2 in fasta.items():
            if sn1 != sn2 and s1[-k:] == s2[:k]:
                print(sn1, sn2)


if __name__ == '__main__':
    fasta = [line.strip() for line in open(sys.argv[1])]
    r_fasta = read_fasta(fasta)
    print_overlaps(r_fasta, 3)
