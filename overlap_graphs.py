#!/usr/bin/env python3
'''
Given a fasta file and a positive integer K, return the overlap edges in any
order
'''

__author__ = 'George Carvalho'

import sys


def read_fasta(fasta):
    ''' Read fasta and return a dictionary with label and sequence as key and
    value respectivelly '''
    seq = ''
    seqs = dict()
    for line in fasta:
        if line.startswith('>'):
            # if seq have a sequence restart it
            seq = ''
            label = line.strip().replace('>', '')
        else:
            seq = line.strip()
            seqs[label] = seq
    print(seqs)
    return seqs


def print_overlaps(seqs, num):
    ''' Search for overlaps in each sequence and print when the pattern
    match '''
    for lab1, seq1 in seqs.items():
        for lab2, seq2 in seqs.items():
            if seq1[-num:] == seq2[:num] and lab1 != lab2:
                print(lab1, lab2)
            else:
                continue


if __name__ == '__main__':
    fasta = open(sys.argv[1])
    seqs = read_fasta(fasta)
    print_overlaps(seqs, 3)
