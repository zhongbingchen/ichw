#currency.py: do currency change automatically
#__author__= "Zhong Bingchen"
#__pkuid__= "1700011738"
#__email__= "1700011738@pku.edu.cn"
#2017.12.4
"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""
from urllib.request import urlopen
def exchange(currency_from, currency_to, amount_from):
    url='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')  #get the strings
    x=jstr.split(':')
    y=x[2]   #get the part which contains the answer
    i=len(y)   
    n=''   #creat a new string which is to place the answer in
    global n
    for j in range(i):
        if ord(y[j])==46 or (ord(y[j])>47 and ord(y[j])<58):  #check numbers and radix point in the part
            n=n+y[j]  #transfer it into the new string one by one
    n=float(n)
    print(n)

def test_input(f, t, a):
    """test if the inputs are legal"""
    assert len(f)==3
    assert len(t)==3
    assert float(a)>0

def test_output():
    """test if the output is reasonable"""
    assert n>0
    assert type(n)==float

def main():
    f=input("from")
    t=input("to")
    a=input("amount")    #input three parameters
    test_input(f, t, a)
    exchange(f, t, a)
    test_output()

if __name__== '__main__':
    main()
