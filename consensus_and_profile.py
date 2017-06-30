#!/usr/bin/env python3

''' Given: A collection of at most 10 DNA strings of equal length in FASTA
format.
Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)

usage: python consensus_and_profile.py rosalind_cons.txt'''

__author__ = 'George Carvalho'

import sys


def profile_matrix(lst):
    ''' Using all reads calculate the distribution of nucleotides '''
    # create a dict with the len of the sequences
    nuc_dict = {
                'A': [0]*len(lst[0]),
                'C': [0]*len(lst[0]),
                'G': [0]*len(lst[0]),
                'T': [0]*len(lst[0])
    }
    # loop through the list of sequences to put the nucleotide frequencies by
    # position in the nucleotide list made in the dict
    for seq in lst:
        for i in range(len(seq)):
            nuc_dict[seq[i]][i] += 1
    return nuc_dict


if __name__ == '__main__':
    # remove white spaces from the lines
    lines = [x.strip() for x in open(sys.argv[1]).readlines()]
    fasta = {}
    for line in lines:
        if not line:
            continue
        # create the sequence name in the dict and a variable
        if line.startswith('>'):
            sname = line
            if line not in fasta:
                fasta[line] = ''
            continue
        # add the sequence to the last sequence name variable
        fasta[sname] += line
    # just to facilitate the input for my function
    lst = list(fasta.values())
    matrix = profile_matrix(lst)
    fseq = ''
    for i in range(len(lst[0])):
        val = 0
        seq = ''
        # loop through the matrix to see the frequencies by position and add
        # the nucleotide to the final sequence
        for k, v in matrix.items():
            if v[i] > val:
                val = v[i]
                seq = k
        fseq += seq
    # print the final sequence and matrix how they want
    print(fseq)
    for k in matrix.keys():
        print('%s: %s' % (k, ' '.join([str(x) for x in matrix[k]])))
