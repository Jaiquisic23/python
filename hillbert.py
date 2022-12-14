# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:35:54 2022

@author: Usuario
"""
import turtle

def d2xy(n,d):
    t=d
    x=y=0
    s=1
    while s<n:
        rx=1&(t/2)
        ry=1&(t^rx)
        s,x,y,rx,ry=rot(s,x,y,rx,ry)
        x+=s*rx
        y+=s*ry
        t/=4
        s*=2
    return x,y

def rot(n,x,y,rx,ry):
    if ry==0:
        if rx==1:
            x=n-1-x
            y=n-1-y
        x,y=y,x

    return n,x,y,rx,ry