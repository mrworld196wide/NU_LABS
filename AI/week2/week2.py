#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:59:37 2023

@author: niit
"""

def go_back(r,c,t,ch):
    t = t + r+c
    ch = ch - (r+c)
    r = 0
    c = 0
    ch = x
    return (r,c,t,ch)

def forward(s,t,ch):
    s = s + 1
    t = t + 1
    ch = ch - 1
    return (s,t,ch)

def backward(s,t,ch):
    s = s - 1
    t = t + 1
    ch = ch - 1
    return (s,t,ch)

n = int(input("Enter N : "))
x = int(input("Enter number of rooms bot can enter with full charge : "))
gi = int(input("Enter gold position (row) : "))
gj = int(input("Enter gold position (column) : "))

rooms = [[0 for col in range(n)] for row in range(n)]
rooms[gi][gj] = 1

i = 0
j = 0
t = 0
ch = x
ch_consumed = 0
li = 0 
hi = n-1
lj = 0
hj = n-1

while(li <= hi and lj <= hj):
    if(ch == i+j):
        print("Recharge")
        prev_i = i
        prev_j = j
        i,j,t,ch = go_back(i,j,t,ch)
        i = prev_i 
        j = prev_j
        ch = ch - (prev_i + prev_j)
        ch_consumed = ch_consumed + 2*(prev_i + prev_j)
        
    elif(rooms[i][j]):
        out_charge_consumed = ch_consumed+i+j
        out_posi = i
        out_posj = j
        i,j,t,ch = go_back(i,j,t,ch)
        ch_consumed = ch_consumed + out_posi + out_posj
        out_time = t
        break

    elif(j==lj and i<hi): 
        i,t,ch = forward(i,t,ch)
        if(i == hi): lj = lj + 1
        ch_consumed = ch_consumed + 1
        print(i,j)
    elif(i==hi and j<hj): 
        j,t,ch = forward(j,t,ch)
        if(j == hj): hi = hi - 1
        ch_consumed = ch_consumed + 1
        print(i,j)
    elif(j==hj and i>li): 
        i,t,ch = backward(i,t,ch)
        if(i == li): hj = hj - 1
        ch_consumed = ch_consumed + 1
        print(i,j)
    elif(i==li and j>lj): 
        j,t,ch = backward(j,t,ch)
        if(j == lj): li = li + 1
        ch_consumed = ch_consumed + 1
        print(i,j)

print("Position of Gold : (",out_posi,",",out_posj,")")
print("Time taken to fetch gold : ",out_time)
print("Charge consumed : ",out_charge_consumed)