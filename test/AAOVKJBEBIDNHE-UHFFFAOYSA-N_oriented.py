#!/usr/bin/env python
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node('0')
G.add_node('1')
G.add_node('3')
G.add_node('5')
G.add_node('6')
G.add_node('8')
G.add_node('9')
G.add_node('22')
G.add_node('23')
G.add_node('26')
G.add_node('28')
G.add_node('30')
G.add_node('31')
G.add_node('32')
G.add_node('33')
G.add_node('37')
G.add_node('38')
G.add_node('40')
G.add_node('41')
G.add_node('54')
G.add_node('57')
#fixed node 100
G.add_node('100')
G.add_edge('0','100')
G.add_edge('1','100')
G.add_edge('3','100')
G.add_edge('5','100')
G.add_edge('6','100')
G.add_edge('8','100')
G.add_edge('9','100')
G.add_edge('22','100')
G.add_edge('23','100')
G.add_edge('26','100')
G.add_edge('28','100')
G.add_edge('30','100')
G.add_edge('31','100')
G.add_edge('32','100')
G.add_edge('33','100')
G.add_edge('37','100')
G.add_edge('38','100')
G.add_edge('40','100')
G.add_edge('41','100')
G.add_edge('54','100')
G.add_edge('57','100')

G.add_edge('0','1')
G.add_edge('1','26')
G.add_edge('1','28')
G.add_edge('5','1')
G.add_edge('5','3')
G.add_edge('5','6')
G.add_edge('5','9')
G.add_edge('5','23')
G.add_edge('5','26')
G.add_edge('5','28')
G.add_edge('5','30')
G.add_edge('23','1')
G.add_edge('23','3')
G.add_edge('23','5')
G.add_edge('23','9')
G.add_edge('23','26')
G.add_edge('23','28')
G.add_edge('23','30')
G.add_edge('23','31')
G.add_edge('28','1')
G.add_edge('28','5')
G.add_edge('32','33')
G.add_edge('33','3')
G.add_edge('37','3')
G.add_edge('41','3')

print 'Degree: '
print G.degree(G.nodes())
print 'PG:'
print nx.pagerank(G)
pos=nx.circular_layout(G,dim=50, scale=100)
plt.clf()
nx.draw(G,with_labels=True)
plt.savefig('C:/Users/Branko/Desktop/AAOVKJBEBIDNHE-UHFFFAOYSA-N_oriented.png')
