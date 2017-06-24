#!/usr/bin/env python3

'''
The GC-content of a DNA string is given by the percentage of symbols in the
string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%

usage: python3 computing_gc_content.py rosalind_gc.txt
'''

__author__ = 'George Carvalho'

import sys
from datetime import datetime


def gc_content(fasta):
    ''' This one, expect a fasta file with sequence lines ending with \n '''
    sequence = ''
    seqs = dict()
    # organize the input in the format labelN:sequenceN
    for line in fasta:
        if line.startswith('>'):
            if len(sequence) > 0:
                sequence = ''
            label = line.strip().replace('>', '')
        else:
            sequence += line.strip()
            seqs[label] = sequence
    # create a dict with gc content by label labelN:gcContent
    gc_seq = dict()
    for lab, seq in seqs.items():
        gc_seq[lab] = (seq.count('G')+seq.count('C')) / len(seq)
    max_cont = max(gc_seq, key=gc_seq.get)
    return max_cont, gc_seq[max_cont]*100


if __name__ == "__main__":
    start = datetime.now()
    fasta = open(sys.argv[1])
    print('%s\n%.10f' % gc_content(fasta))
    end = datetime.now()
    print("time: {}".format(end - start))
