#!/usr/bin/env python3
'''
Having a string S of a DNA sequence return four integers counting the
respective number of times that ["A", "T", "G", "C"] occur in S.

usage: python3 counting_dna_nucleotides.py rosalind_dna.txt
'''

__author__ = "George Carvalho"

import sys
import collections
from datetime import datetime


def counterNucleotides(seq):
    ' Count the number of ACGT in a sequence DNA using counter '
    start = datetime.now()
    string = ""
    letters = collections.Counter(seq.replace(" ", ""))
    for k, v in letters.items():
        string += "%s " % v
    end = datetime.now()
    # print("time: {}".format(end - start))
    # time: 0:00:00.003728
    return string


def countNucleotides(seq):
    ' Count the frequency of ACGT in sequence DNA '
    start = datetime.now()
    # I could use "collections.defaultdict(0), but not"
    letters = dict()
    for letter in seq.replace(" ", ""):
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    # if the order has some importance
    string = "%s %s %s %s" % (
                                letters['A'],
                                letters['C'],
                                letters['G'],
                                letters['T']
    )
    # for k, v in letters.items():
    #    string += "%s " % v
    # end = datetime.now()
    # print("time: {}".format(end - start))
    # time: 0:00:00.003489
    return string


if __name__ == '__main__':
    # sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTG\
    # ATAGCAGC"
    # out = [20, 12, 17, 21]
    # print(countNucleotides(sequence) == out)
    sequence = open(sys.argv[1], "r").readlines()[0].strip().upper()
    print(countNucleotides(sequence))
    # print(counterNucleotides(sequence))
