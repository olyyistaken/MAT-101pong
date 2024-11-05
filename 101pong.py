#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## 101pong
## File description:
## files python for 101pong
##
import sys

def main():

    x0 = float(sys.argv[1])
    y0 = float(sys.argv[2])
    z0 = float(sys.argv[3])
    x1 = float(sys.argv[4])
    y1 = float(sys.argv[5])
    z1 = float(sys.argv[6])
    n = int(sys.argv[7])

    res = x1 - x0
    res2 = y1 - y0
    res3 = z1 - z0
    n1 = (res * n) + x1
    n2 = (res2 * n) + y1
    n3 = (res3 * n) + z1
    print("The velocity vector of the ball is:")
    print("({:.2f}, {:.2f}, {:.2f})".format(res, res2, res3))
    print("At time t + {:.0f}, ball coordinates will be: ".format(n))
    print("({:.2f}, {:.2f}, {:.2f})".format(n1, n2, n3))
    return 0

main()