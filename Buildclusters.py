import sys
import numpy
#from collections import ChainMap
from collections import namedtuple

# Point = namedtuple('Point', 'coord opening chr_number factor')
#factor = open("input/input1.txt").readline().rstrip()

# Interval = namedtuple('Interval', 'n1 n2 chr_number factors')


def read_file(filename, points):
    with open(filename) as f:
        factor = f.readline().strip()
        for line in f:
            line = line.strip()
            chr, coords = line.split(':')
            chr_num = str_to_int(chr[3:])
            coords = coords.split('-')
            coord1, coord2 = [int(coord) for coord in coords]
            point = Point(coord1, True, chr_num, factor)
            points.append(point)
            point = Point(coord2, False, chr_num, factor)
            points.append(point)


class Point:
    def __init__(self, coord, opening, chr_num, factor):
        self.coord = coord
        self.opening = opening
        self.chr_num = chr_num
        self.factor = factor

    def __lt__(self, p):
        if self.chr_num != p.chr_num:
            return self.chr_num < p.chr_num
        if self.coord != p.coord:
            return self.coord < p.coord
        return self.opening and not p.opening

    def __str__(self):
        return 'Point({}, {}, {}, {})'.format(self.coord, self.opening, self.chr_num, self.factor)


class Interval:
    def __init__(self, n1, n2, chr_num, factors):
        self.n1 = n1
        self.n2 = n2
        self.chr_num = chr_num
        self.factors = factors

    def factors_count(self):
        count = 0
        factors = self.factors
        factor = 1
        while factor:
            if factors & factor:
                count = count + 1
            factor = factor << 1


def str_to_int(string):
    if string == "x" or string == "X":
        return 20
    if string == "y" or string == "Y":
        return 20
    return int(string)


def main():
    files_count = 0
    merge_gap = 200
    max_length = 500


if __name__ == '__main__':
    print('start')
    points = []
    fn = 'input5.txt'
    import time
    start = time.time()
    read_file(fn, points)
    end = time.time()
    print(end - start)
    print(len(points))

    pass
