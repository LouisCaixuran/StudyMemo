# encoding: utf-8
from collections import deque
class Graph(object):
    def __init__(self,start,fin,dic={}):
        self.start=start
        self.fin=fin
        self.graph=dic
        if self.start not in self.graph:
            self.graph[start]={}
        if self.fin not in self.graph:
            self.graph[fin]={}
        self.infinity=float("inf")
        self.costs={}
        self.parents={}
        self.processed=[]
        self.road=deque([fin])
        for i in self.graph.keys():
            self.costs[i]=self.infinity
            self.parents[i]=None
        for i in self.graph[self.start].keys():
            self.costs[i]=self.graph[self.start][i]
            self.parents[i]=self.start

    def add(self,a,b,n):
        if a not in self.graph:
            self.graph[a]={}
        if b not in self.graph:
            self.graph[b]={}
        self.graph[a][b]=n
        if a==self.start:
            self.costs[b]=n
            self.parents[b]=self.start
        else:
            self.costs[b]=self.infinity
            self.parents[b]=None

    def find_lowest_cost_node(self):
        lowest_cost = self.infinity
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def findroad(self):
        node = self.find_lowest_cost_node()
        while node is not None:
            cost = self.costs[node] 
            neighbors = self.graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.append(node)
            node = self.find_lowest_cost_node()
        n=self.fin
        while n !=self.start:
            n=self.parents[n]
            self.road.appendleft(n)

        return self.road

g={
    "start":{'a':5,'b':7,'c':11,'d':12},
    'a':{'c':5},
    'b': {'e': 5}, 
    'c':{'d':2,'f':5},
    'e': {'d': 3}, 
    'd': {'fin': 8, 'g': 6, 'f': 3}, 
    'g': {'fin': 8}, 
    'f': {'fin': 4, 'g': 7},
}


graph = Graph("start","fin",g)

'''
graph.add(graph.start,'a',5)
graph.add(graph.start,'b',7)
graph.add(graph.start,'c',11)
graph.add(graph.start,'d',9)
graph.add("a","c",5)
graph.add("b","e",5)
graph.add("c","d",2)
graph.add("c","f",5)
graph.add("d","f",3)
graph.add("d","g",6)
graph.add("d",graph.fin,8)
graph.add("e","d",3)
graph.add("f","g",7)
graph.add("f",graph.fin,4)
graph.add("g",graph.fin,8) 
print graph.graph
'''
print graph.findroad()

