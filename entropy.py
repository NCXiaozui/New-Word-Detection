# -*- coding:utf-8 -*-
'''
left/right neighbors entropy for new word detection
Author: Xylander
Reference:
    https://github.com/Moonshile/ChineseWordSegmentation
    http://www.matrix67.com/blog/archives/5044
    https://zlc1994.com/2017/01/04/
'''

import math

def compute_entropy(_list):
    length = float(len(_list))
    frequence = {}
    if length == 0:
        return 0
    else:
        for i in _list:
            frequence[i] = frequence.get(i,0) + 1
        return sum(map(lambda x: - x/length * math.log(x/length) , frequence.values()))

