# -*- coding: utf-8 -*-

f = open('fread2.py', 'r')

# 1行づつ読み込んで，行のリストを作ってくれる関数 readlines()
lines = f.readlines()
f.close()

print(lines)
