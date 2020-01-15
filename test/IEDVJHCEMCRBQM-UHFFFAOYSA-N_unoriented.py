#!/usr/bin/env python
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('0')
G.add_node('1')
G.add_node('3')
G.add_node('4')
G.add_node('7')
G.add_node('12')
G.add_node('16')
G.add_node('20')
G.add_node('23')
G.add_node('25')
G.add_node('26')
G.add_node('27')
G.add_node('28')
G.add_node('29')
G.add_node('31')
G.add_node('32')
G.add_node('35')
G.add_node('47')
G.add_node('50')

G.add_edge('0','1')
G.add_edge('0','3')
G.add_edge('0','4')
G.add_edge('0','7')
G.add_edge('0','12')
G.add_edge('0','16')
G.add_edge('0','20')
G.add_edge('0','23')
G.add_edge('0','25')
G.add_edge('0','26')
G.add_edge('0','27')
G.add_edge('1','3')
G.add_edge('1','4')
G.add_edge('1','7')
G.add_edge('1','12')
G.add_edge('1','16')
G.add_edge('1','20')
G.add_edge('1','23')
G.add_edge('1','25')
G.add_edge('1','26')
G.add_edge('1','27')
G.add_edge('3','4')
G.add_edge('3','7')
G.add_edge('3','12')
G.add_edge('3','16')
G.add_edge('3','20')
G.add_edge('3','23')
G.add_edge('3','25')
G.add_edge('3','26')
G.add_edge('3','27')
G.add_edge('4','7')
G.add_edge('4','12')
G.add_edge('4','16')
G.add_edge('4','20')
G.add_edge('4','23')
G.add_edge('4','25')
G.add_edge('4','26')
G.add_edge('4','27')
G.add_edge('7','12')
G.add_edge('7','16')
G.add_edge('7','20')
G.add_edge('7','23')
G.add_edge('7','25')
G.add_edge('7','26')
G.add_edge('7','27')
G.add_edge('12','16')
G.add_edge('12','20')
G.add_edge('12','23')
G.add_edge('12','25')
G.add_edge('12','26')
G.add_edge('12','27')
G.add_edge('47','32')
G.add_edge('47','35')
G.add_edge('47','16')
G.add_edge('47','50')
G.add_edge('47','28')
G.add_edge('47','29')
G.add_edge('47','31')
G.add_edge('16','50')
G.add_edge('16','35')
G.add_edge('16','20')
G.add_edge('16','32')
G.add_edge('16','23')
G.add_edge('16','25')
G.add_edge('16','26')
G.add_edge('16','27')
G.add_edge('16','28')
G.add_edge('16','29')
G.add_edge('16','31')
G.add_edge('50','32')
G.add_edge('50','35')
G.add_edge('50','28')
G.add_edge('50','29')
G.add_edge('50','31')
G.add_edge('35','32')
G.add_edge('35','28')
G.add_edge('35','29')
G.add_edge('35','31')
G.add_edge('20','23')
G.add_edge('20','25')
G.add_edge('20','26')
G.add_edge('20','27')
G.add_edge('32','28')
G.add_edge('32','29')
G.add_edge('32','31')
G.add_edge('23','25')
G.add_edge('23','26')
G.add_edge('23','27')
G.add_edge('25','26')
G.add_edge('25','27')
G.add_edge('26','27')
G.add_edge('28','29')
G.add_edge('28','31')
G.add_edge('29','31')

 print G.nodes()
print nx.fiedler_vector(G,method='lobpcg')

pos=nx.circular_layout(G,dim=50, scale=100)
plt.clf()
nx.draw(G,with_labels=True)
plt.savefig('C:/Users/Branko/Desktop/IEDVJHCEMCRBQM-UHFFFAOYSA-N_unoriented.png')
