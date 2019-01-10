# sin(x**2)+sqrt(x) 0 5 1000
# ((sin(x))**2)/(sqrt(x)) 1 10 1000
# log(x)+(x*sin(x)) 1 10 1000

#/usr/bin/python
import sys
import random
import numpy as np
from math import *
import csv


def generate_random_number(a, b):
    return np.random.uniform(a, b)


def generate_files(filename, data_list):
    filename = filename.replace('/', ':')
    print(filename)
    with open(filename + '.csv', 'w') as file:
        wr = csv.writer(file)
        wr.writerows(data_list)


def main():
    if len(sys.argv) < 5:
        print("Invalid number of parameters given.\nProper call: ./data_generator.py EXPRESSION a b SIZE")
        exit(1)

    expr = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    size = int(sys.argv[4])

    filename = expr + '_({},{})_{}'.format(a, b, size)

    data_list = []

    for i in range(size):
        x = generate_random_number(a, b)
        try:
            y = eval(expr)
            data_list.append((x, y))

        except ValueError:
            print(x)
            print("Invalid range (a, b) given!")
            exit(1)

    generate_files(filename, data_list)


if __name__ == "__main__":
    main()
