#!/usr/bin/python3

for n in range(0, 100):
    if n == 89:
        print(f"{n}")
    elif n % 10 > n / 10:
        print(f"{n:02d}, ", end="")
