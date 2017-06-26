#!/usr/bin/env python3

'''
Given two strings S and T of equal length, the Hamming distance between S and T,
denoted dH(S,T), is the number of corresponding symbols that differ in S and T.

usage: python counting_point_mutations.py rosalind_hamm.txt
'''

__author__ = 'George Carvalho'

import sys


def hamming_distance(ref, seq):
    ''' Giving a reference sequence and a random sequence with the same lenght,
    return the number of differences between then '''
    diff = 0
    for i in range(len(ref)):
        if not ref[i] == seq[i]:
            diff += 1
    return diff


if __name__ == "__main__":
    # ref = 'GAGCCTACTAACGGGAT'
    # seq = 'CATCGTAATGACGGCCT'
    # out = 7
    # print(count_point_variants(ref, seq)==out)
    data = open(sys.argv[1]).readlines()
    ref = data[0].strip().upper()
    seq = data[1].strip().upper()
    print(hamming_distance(ref, seq))
