"""Module for computing power sets."""

from typing import Any

def power(x: list[Any]) -> list[list[Any]]:
    """
    Compute the power-set of x.

    Returns the power-set of x as a list of lists.
    """
    powerset = []
    for i in range(0, 2**len(x)):
        bit_representation = format(i, "b").zfill(len(x))
        idx = 0
        subset = []
        for j in bit_representation[::-1]:
            if j == "0":
                idx += 1
                continue
            elif j == "1":
                subset.append(x[idx])
                idx += 1
        powerset.append(subset)

    return sorted(powerset, key = len)
