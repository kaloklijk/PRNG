import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import networkx as nx

def power(a, b):
  ''' 
  function for quick powering a by b, where a and b are integers
  '''
  if b == 1:
    return a
  if b%2 == 0:
    return power(a, b/2) * power(a, b/2)
  return power(a, b//2) * power(a, b//2 + 1)

class prng:
  def __init__(self, start, randomseq = nx.Graph(), num = 1):
    '''
    Create a starting number as a parameter for the prng algorithm
    '''
    self.start = start
    self.randomseq = randomseq
    self.num = num
    
  def middle_square(self):
    '''
    The middle square algorithm for constructing 
    sequence of random number from an input
    '''
    s = str(power(self.start))
    l = len(s)
    tmp = s[l//4:]
    ans = int(tmp(:len(self.start))
    self.randomseq.add_node(ans)
    self.randomseq.add_edge(self.start, ans)
    self.start = ans
    print(ans)
              
  def Lehmer_rng(self):
    '''
    Use Lehmer algorithm to generate random numbers
    '''
    a = 16807
    m = 65537
    ans = (a*self.start)%m
    self.randomseq.add_node(ans)
    self.randomseq.add_edge(self.start, ans)
    self.start = ans
    print(ans)
              
    def LCG_rng(self, c = 0):
    '''
    Use LCG algorithm to generate random numbers
    '''
    a = 16807
    m = 65537
    ans = (a*self.start+c)%m
    self.randomseq.add_node(ans)
    self.randomseq.add_edge(self.start, ans)
    self.start = ans
    print(ans)
    
              
  def printseq(self):
    '''
    print the sequence that come out from prng using graph
    '''
    graph = self.randomseq
    pos = nx.circular_layout(graph)
    plt.figure(f"random sequence {self.num}")
    self.num = self.num+1
    nx.draw(graph, pos, with_labels = True, node_size = 600, node_color = "lightblue", edge_color = "red")
    plt.show()

 def multiuse(self, alg, n):
    '''
    use a specific algorithm to generate random number n times
    '''
    if alg = "LCG_rng":
       for i in range(0, n):
          LCG_rng()
    if alg = "Lehmer_rng":
       for i in range(0, n):
          Lehmer_rng()
    if alg = "middle_square":
       for i in range(0, n):
          middle_square()
    printseq()
              
