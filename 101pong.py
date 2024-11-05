#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## 101pong
## File description:
## files python for 101pong
##
import sys
from math import *

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
    absolute = sqrt(res ** 2 + res2 ** 2 + res3 ** 2)
    res_angle = asin(abs(res3)/absolute)
    res_angle *= (180/pi)
    print("The velocity vector of the ball is:")
    print("({:.2f}, {:.2f}, {:.2f})".format(res, res2, res3))
    print("At time t + {:.0f}, ball coordinates will be: ".format(n))
    print("({:.2f}, {:.2f}, {:.2f})".format(n1, n2, n3))
    print("The incidence angle is:")
    print("{:.2f} degrees".format(res_angle))
    return 0

main()