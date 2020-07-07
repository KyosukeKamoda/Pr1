# -*- coding: utf-8 -*-

f = open('wordcnt.py', 'r')
lines = f.readlines()
f.close()

lcnts = len(lines)
wcnts = 0
ccnts = 0

for l in lines:
    ccnts += len(l)
    words = l.split()
    wcnts += len(words)

print('lines: ', lcnts)
print('words: ', wcnts)
print('characters: ', ccnts)
