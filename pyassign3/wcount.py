#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Zhong Bingchen"
__pkuid__  = "1700011738"
__email__  = "1700011738@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    words=lines.lower()
    words=words.replace('.', '')
    words=words.replace(',', ' ')
    words=words.replace('!', ' ')
    words=words.replace('?', ' ')
    words=words.replace(':', ' ')
    words=words.replace('_', ' ')
    words=words.replace('"', ' ')
    words=words.replace("'", ' ')
    words=words.replace('(', ' ')
    words=words.replace(')', ' ')
    words=words.replace('[', ' ')
    words=words.replace(']', ' ')
    words=words.replace('-', ' ')
    words=words.replace(';', ' ')
    words=words.replace('"', ' ')
    words=words.replace('*', ' ')
    lst=words.split(' ')
    lst2=list(set(lst))
    lst2.remove('')
    dic={}
    for i in lst2:
        dic[i]=lst.count(i)
    wds=list(dic.keys())
    numbers=list(dic.values())
    numbers2=sorted(numbers, reverse=True)
    for k in range(topn):
        m=numbers.index(numbers2[k])
        print("%-15s%-5d"%(wds[m],numbers2[k]))

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
