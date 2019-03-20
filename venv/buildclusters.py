import sys
import numpy
#from collections import ChainMap
from collections import namedtuple

Point = namedtuple('Point', 'coord opening chr_number factor')
#factor = open("input/input1.txt").readline().rstrip()

Interval = namedtuple('Interval', 'n1 n2 chr_number factors')


def read_file(filename):
    arrname = []
    with open(filename) as f:
        #f.next()
        for line in f:
            line = line.strip()
            if line != "NA":
                line = float(line)
                arrname.append(float(line))
    f.close()
    return arrname

print(sys.path)
fname_pattern = 'input/input%s.txt'


def count_lines(fname):
    proc = sp.Popen(['wc', '-l', fname], stdout=sp.PIPE)
    (out, _) = proc.communicate()
    # status = proc.wait()
    out = str(out).decode()
    pos = out.find(' ')
    lc = int(out[:pos])
    return lc


for i in ['1', '2', '3']:
        fname = fname_pattern % i
        #number_of_lines = count_lines(fname)
        #number_of_lines
        #number_of_all_lines.append(number_of_lines)
        my_list = read_file(fname)
        my_lists.append(my_list)

