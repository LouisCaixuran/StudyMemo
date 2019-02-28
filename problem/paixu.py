import numpy as np
import os
from collections import deque

class Paixu(object):
    def __init__(self,lists):
        self.lists=lists
        self.deq=deque(self.lists)
        self.deq.appendleft(0)
    
    def merge(self,a, b):
        c = []
        h = j = 0
        while j < len(a) and h < len(b):
            if a[j] < b[h]:
                c.append(a[j])
                j += 1
            else:
                c.append(b[h])
                h += 1

        if j == len(a):
            for i in b[h:]:
                c.append(i)
        else:
            for i in a[j:]:
                c.append(i)

        return c


    def merge_sort(self):
        if len(self.lists) <= 1:
            return self.lists
        middle = len(self.lists)/2
        l=Paixu(self.lists[:middle])
        left = l.merge_sort()
        r=Paixu(self.lists[middle:])
        right = r.merge_sort()
        return self.merge(left, right)

    def RadixSort(self):
        i = 0
        n = 1
        max = np.max(self.lists)
        while max/(10**n) > 0:
            n += 1
        while i < n:
            bucket = {}
        for x in range(0,10):
            bucket.setdefault(x, [])
        for x in self.lists:
            radix =(x / (10**i)) % 10
            bucket[radix].append(x)
        j = 0
        for k in xrange(0, 10):
            if len(bucket[k]) != 0:
                for y in bucket[k]:
                    self.lists[j] = y
                    j += 1
        i += 1
        return self.lists

    def QuickSort(self,start,end):
        if start < end:
            i,j = start,end
            base = self.lists[i]

            while i < j:
                while (i < j) and (self.lists[j] >= base):
                    j = j - 1

                self.lists[i] = self.lists[j]

                while (i < j) and (self.lists[i] <= base):
                    i = i + 1
                self.lists[j] = self.lists[i]
            self.lists[i] = base

            self.QuickSort( start, i - 1)
            self.QuickSort(j + 1, end)
        return self.lists




    def heap_adjust(self, start, end):
        temp = self.deq[start]

        i = start
        j = 2 * i

        while j <= end:
            if (j < end) and (self.deq[j] < self.deq[j + 1]):
                j += 1
            if temp < self.deq[j]:
                self.deq[i] = self.deq[j]
                i = j
                j = 2 * i
            else:
                break
        self.deq[i] = temp

    def heap_sort(self):
        length = len(self.deq) - 1

        first_sort_count = length / 2
        for i in range(first_sort_count):
            self.heap_adjust(first_sort_count - i, length)

        for i in range(length - 1):
            self.deq[1],self.deq[length-i]=self.deq[length-i],self.deq[1]
            self.heap_adjust( 1, length - i - 1)

        return [self.deq[i] for i in range(1, length+1)]
   

def fileop(filepath):
    try:
        lists=open(filepath)
    except Exception as e:
        print(e)
        return[0]
    else:
        lists1=lists.read().split(',')
        lists.close()
        lists2=[]
        for i in range(len(lists1)):
            if lists1[i].isdigit():
                lists2.append(int(lists1[i]))
            else:
                print("error,please type in numbers")
                return [0]
        return lists2




