#!/usrt/bin/env python3

''' Given the number of months to analyze (n) and the survival time (m)
calculate the amount of rabbits alive in the last month '''

__author__ = 'George Carvalho'


import sys


def main(n, m):
    # the first two months we just have a couple (newborn -> mature)
    rab = [1, 1]
    months = 2
    while months < n:
        # They are to young to die
        if months < m:
            rab.append(rab[-2]+rab[-1])
        # Die the oldest
        elif months == m:
            rab.append(rab[-2]+rab[-1]-1)
        # Die the one that aws born m weeks ago
        else:
            rab.append(rab[-2]+rab[-1]-rab[-(m+1)])
        months += 1
    return rab[-1]

if __name__ == '__main__':
    #n, m = 6, 3
    #out = 4
    data = [x.strip() for x in open(sys.argv[1]).readlines()[0].split(' ')]
    n, m = map(int, data)
    print(main(n, m))
