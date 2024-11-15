#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## 101pong
## File description:
## files python for 101pong
##

import sys
from math import *

def usage():
    print("USAGE")
    print("    ./101pong x0 y0 z0 x1 y1 z1 n")
    print("")
    print("DESCRIPTION")
    print("    x0  ball abscissa at time t - 1")
    print("    y0  ball ordinate at time t - 1")
    print("    z0  ball altitude at time t - 1")
    print("    x1  ball abscissa at time t")
    print("    y1  ball ordinate at time t")
    print("    z1  ball altitude at time t")
    print("    n   time shift (greater than or equal to zero, integer)")

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        usage()
        exit(0)
    if len(sys.argv) == 1:
        sys.stderr.write("no argument\n")
        exit(84)
    if len(sys.argv) < 8:
        sys.stderr.write("too few argument\n")
        exit(84)
    if len(sys.argv) > 8:
        sys.stderr.write("too many argument\n")
        exit(84)
    try:
        x0 = float(sys.argv[1])
        y0 = float(sys.argv[2])
        z0 = float(sys.argv[3])
        x1 = float(sys.argv[4])
        y1 = float(sys.argv[5])
        z1 = float(sys.argv[6])
        n = int(sys.argv[7])
    except ValueError:
        sys.stderr.write("all argument must be numbers\n")
        exit(84)
    if n < 0:
        sys.stderr.write("n must be a positive integer\n")
        exit(84)

    vx = x1 - x0
    vy = y1 - y0
    vz = z1 - z0

    nx = vx * n + x1
    ny = vy * n + y1
    nz = vz * n + z1

    speed = sqrt(vx**2 + vy**2 + vz**2)
    if speed == 0:
        sys.stderr.write("Velocity vector is zero\n")
        exit(84)

    print("The velocity vector of the ball is:")
    print("({:.2f}, {:.2f}, {:.2f})".format(vx, vy, vz))
    print("At time t + {:.0f}, ball coordinates will be:".format(n))
    print("({:.2f}, {:.2f}, {:.2f})".format(nx, ny, nz))

    if vz == 0 or vz * z1 > 0:
        print("The ball won't reach the paddle.")
    else:
        angle = asin(abs(vz) / speed) * (180 / pi)
        print("The incidence angle is:")
        print("{:.2f} degrees".format(angle))

main()
