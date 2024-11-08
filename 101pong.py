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

    if int(len(sys.argv)) == 1:
        print("no argument")
        exit (84)
    if int(len(sys.argv)) < 8:
        print("too few argument")
        exit (84)
    if int(len(sys.argv)) > 8:
        print("too many argument")
        exit (84)
    try:
        x0 = float(sys.argv[1])
        y0 = float(sys.argv[2])
        z0 = float(sys.argv[3])
        x1 = float(sys.argv[4])
        y1 = float(sys.argv[5])
        z1 = float(sys.argv[6])
        n = int(sys.argv[7])
    except ValueError:
        print("all argument must be numbers")
        exit (84)
    if n <= 0:
        print ("n must be a postive int")
        exit (84)

    res = x1 - x0
    res2 = y1 - y0
    res3 = z1 - z0
    n1 = (res * n) + x1
    n2 = (res2 * n) + y1
    n3 = (res3 * n) + z1

    absolute = sqrt(res ** 2 + res2 ** 2 + res3 ** 2)
    if (absolute == 0):
        print("Velocity vector is zero, can't be calculate incidence angle")
        exit (84)

    res_angle = asin(abs(res3)/absolute)
    res_angle *= (180/pi)
    print("The velocity vector of the ball is:")
    print("({:.2f}, {:.2f}, {:.2f})".format(res, res2, res3))
    print("At time t + {:.0f}, ball coordinates will be: ".format(n))
    print("({:.2f}, {:.2f}, {:.2f})".format(n1, n2, n3))

    if (res3 == 0):
        print("The ball can't be bounce")
        #print("The ball won't reach the paddle") -> à revoir
    else:
        print("The incidence angle is:")
        print("{:.2f} degrees".format(res_angle))
    return 0

main()