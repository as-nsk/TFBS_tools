import sys
import numpy
#from collections import ChainMap
from collections import namedtuple

# Point = namedtuple('Point', 'coord opening chr_number factor')
#factor = open("input/input1.txt").readline().rstrip()

# Interval = namedtuple('Interval', 'n1 n2 chr_number factors')


def add_interval(interval, intervals, max_length):
    while interval.n2 - interval.n1 > max_length:
        n2 = interval.n2
        interval.n2 = interval.n1 + max_length
        intervals.append(interval)
        interval.n2 = n2
        interval.n1 = interval.n1 + max_length
    intervals.append(interval)


def make_intervals(points, intervals, merge_gap, max_length):
    counter = 0
    inside = False
    interval = Interval()
    for i in range(len(points) - 1):
        pass
        if points[i].opening:
            counter = counter + 1
            if not inside:
                interval.n1 = points[i].coord
                interval.chr_num = points[i].chr_num
                inside = True
            interval.factors.add(points[i])
        else:
            pass
            counter = counter - 1
            distance = points[i+1].coord - points[i].coord
            last_point = i == len(points) - 1
            if counter == 0 and (last_point or distance > merge_gap):
                pass
                interval.n2 = points[i].coord
                add_interval(interval, intervals, max_length)
                inside = False


def read_file(filename, points):
    with open(filename) as f:
        factor = f.readline().strip()
        for line in f:
            line = line.strip()
            if not line:
                continue
            chr, coords = line.split(':')
            chr_num = str_to_int(chr[3:])
            coords = coords.split('-')
            coord1, coord2 = [int(coord) for coord in coords]
            point = Point(coord1, True, chr_num, factor)
            points.append(point)
            point = Point(coord2, False, chr_num, factor)
            points.append(point)


def write_file(filename, intervals):
    with open(filename) as f:
        for interval in intervals:
            args = (interval.chr_num, interval.n1, interval.n2, interval.factors_count())
            f.write('chr{}:{}-{} TF: {}'.format(*args))
            for factor in interval.factors:
                f.write(' ')
                f.write(factor)
            f.write(os.linesep)


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
    def __init__(self, n1=None, n2=None, chr_num=None, factors=None):
        self.n1 = n1
        self.n2 = n2
        self.chr_num = chr_num
        self.factors = factors if factors else set([])

    def factors_count(self):
        return len(self.factors)


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
    import os
    import time
    files = os.listdir('input')
    files = [os.path.join('input', file) for file in files]
    times = []
    for file in files:
        points = []
        print('reading {}'.format(file))
        start = time.time()
        read_file(file, points)
        end = time.time()
        print(end - start)

    pass
