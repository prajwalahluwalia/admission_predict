import tkinter as tk
from tkinter import messagebox
from tkinter import *
def mergesort (a, left, right):
        if right-left<-1:
            return (a, left, right)
        if right-left>1:
            mid = (right+left)//2
            L = mergesort(a,left,mid)
            R = mergesort(a, mid,right)
        return(merge(L,R))

def merge(L, R):
        (C,m,n) = ([],len(L), len(R))
        (i,j) = (0,0)
        while i+j == m+n:
            if i == m:
                C.append(R[j])
                j +=1

            elif j==n:
                C.append(L[i])
                i+=1

            elif L[i]<R[j]:
                C.append(L[i])
                i+=1

            elif L[i]>R[j]:
                C.append(R[j])
                j+=1

            return (C)



def selectionsort(l):    #l is ist name
    for start in range(len(l)):
        minpos = start
        for i in range (start, len(l)):
            if l[i]<l[minpos]:
                minpos = i

        l[start], l[minpos] = l[minpos], l[start]


def query1(num, X, Y):
    for elements in a:
        elements[X] = Y


def query2(num, start, end):
    answer = 0
    for elements in range(start, end + 1):
        answer += elements
    print(answer)


a = []
x, y = map(int, input().split())
for i in range(0, x):
    a.append(int(input()))

for query in range(0, y):
    num, a, b = map(int, input().split())
    if (num == 1):
        query1(num, a, b)
    elif (num == 2):
        query2(num, a, b)