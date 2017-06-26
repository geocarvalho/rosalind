#!/usr/bin/env python3

'''Given: An RNA string S corresponding to a strand of mRNA.
Return: The protein string encoded by S '''

__author__ = 'George Carvalho'

import sys


def rna2ptn(rna):
    ''' Giving a RNA sequence match each 3 nucleotide with the translation in
    aminoacid '''
    ptn_dict = {
                'F': ['UUC', 'UUU'],
                'L': ['CUU', 'CUC', 'UUA', 'UUG', 'CUA', 'CUG'],
                'I': ['AUU', 'AUC', 'AUA'],
                'V': ['GUU', 'GUC', 'GUA', 'GUG'],
                'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
                'M': ['AUG'],
                'P': ['CCU', 'CCC', 'CCA', 'CCG'],
                'T': ['ACU', 'ACC', 'ACA', 'ACG'],
                'A': ['GCU', 'GCC', 'GCA', 'GCG'],
                'Y': ['UAU', 'UAC'],
                'H': ['CAU', 'CAC'],
                'N': ['AAU', 'AAC'],
                'D': ['GAU', 'GAC'],
                'Stop': ['UAA', 'UAG', 'UGA'],
                'Q': ['CAA', 'CAG'],
                'K': ['AAA', 'AAG'],
                'E': ['GAA', 'GAG'],
                'C': ['UGU', 'UGC'],
                'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'],
                'G': ['GGU', 'GGC', 'GGA', 'GGG'],
                'W': ['UGG']
    }
    ptn = ''
    for i in range(0, len(rna)-2, 3):
        for k, v in ptn_dict.items():
            if rna[i:i+3] in v:
                if k == 'Stop':
                    break
                ptn += k
    return ptn


if __name__ == '__main__':
    # rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    # out = 'MAMAPRTEINSTRING'
    # print(rna2ptn(rna) == out)
    rna = ''.join([x.strip() for x in open(sys.argv[1]).readlines()])
    print(rna2ptn(rna))
