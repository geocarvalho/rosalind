#!/usr/bin/env python3

''' Given: Three positive integers k, m, and n, representing a population
containing k+m+n organisms: k individuals are homozygous dominant for a factor,
m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will
produce an individual possessing a dominant allele (and thus displaying the
dominant phenotype). Assume that any two organisms can mate. '''

__author__ = 'George Carvalho'

import sys


def mendelian_inheritance(lst):
    ''' Givin a list with the number of individuos per per haplotype return the
    probability of take two random dominant alleles '''
    # lst = ['2', '2', '2']
    k, m, n = map(float, lst)
    t = sum(map(float, lst))
    # organize a list with allele one * allele two (possibles) * dominant prob
    # multiplications by on were ignored
    # remember to substract the haplotype from the total when they're the same
    couples = [
                k*(k-1),  # AA x AA
                k*m,  # AA x Aa
                k*n,  # AA x aa
                m*k,  # Aa x AA
                m*(m-1)*0.75,  # Aa x Aa
                m*n*0.5,  # Aa x aa
                n*k,  # aa x AA
                n*m*0.5,  # aa x Aa
                n*(n-1)*0  # aa x aa
    ]
    # (t-1) indicate that the first haplotype was selected
    return round(sum(couples)/t/(t-1), 5)


if __name__ == "__main__":
    # lst = [2, 2, 2]
    # out = 0.78333
    # print(mendelian_inheritance(lst) == out)
    lst = open(sys.argv[1]).readlines()[0].strip().split()
    print(mendelian_inheritance(lst))
