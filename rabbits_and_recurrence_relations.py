#!/usr/bin/env python3

'''
The total number of rabbit pairs that will be present after n months, if we
begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

usage: python rabbits_and_recurrence_relations.py rosalind_fib.txt
'''

__author__ = 'George Carvalho'

import sys


def fib(n, k):
    ''' calculate the number of pairs after n moths, giving in consideration
    the number of pairs generate (k) '''
    if n < 0:
        raise ValueError('n must be a positive value')
    # f(0) have to be considered, eg.: n=5 result in f(0) -> f(4)
    if n < 3:
        return 1
    else:
        return fib(n-1, k) + k * fib(n-2, k)


if __name__ == "__main__":
    # n = 5
    # k = 3
    # out = 19
    # print(fibnum(n, k) == out)
    data = open(sys.argv[1]).readlines()[0].strip().split()
    n, k = int(data[0]), int(data[1])
    print(fib(n, k))
