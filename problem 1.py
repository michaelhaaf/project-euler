"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import argparse
import numpy as np
import operator
from itertools import combinations
from functools import reduce

__author__ = 'Michael Haaf'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", help="the number which caps the value of multiples", type=int, default=1000)
    parser.add_argument("--multiples", help="the numbers for which you wish to sum multiples of",
                        nargs='+', type=int, default=[3, 5])
    args = parser.parse_args()

    limit = args.limit
    multiples = args.multiples

    answer = 0
    for multiple in multiples:
        answer += sum(np.arange(start=0, stop=limit, step=multiple))
    for multiplePair in combinations(multiples, 2):
        commonMultiple = reduce(operator.mul, multiplePair, 1)
        answer -= sum(np.arange(start=0, stop=limit, step=commonMultiple))

    print("The sum of all the multiples of", multiples, "below", limit, "is", answer)
