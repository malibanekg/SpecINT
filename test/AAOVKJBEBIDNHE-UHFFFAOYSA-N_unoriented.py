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

G.add_edge('0','1')
G.add_edge('0','3')
G.add_edge('0','5')
G.add_edge('0','6')
G.add_edge('0','8')
G.add_edge('0','9')
G.add_edge('0','22')
G.add_edge('0','23')
G.add_edge('0','26')
G.add_edge('0','28')
G.add_edge('0','30')
G.add_edge('0','31')
G.add_edge('1','3')
G.add_edge('1','5')
G.add_edge('1','6')
G.add_edge('1','8')
G.add_edge('1','9')
G.add_edge('1','22')
G.add_edge('1','23')
G.add_edge('1','26')
G.add_edge('1','28')
G.add_edge('1','30')
G.add_edge('1','31')
G.add_edge('3','33')
G.add_edge('3','5')
G.add_edge('3','6')
G.add_edge('3','32')
G.add_edge('3','8')
G.add_edge('3','9')
G.add_edge('3','54')
G.add_edge('3','40')
G.add_edge('3','41')
G.add_edge('3','22')
G.add_edge('3','23')
G.add_edge('3','57')
G.add_edge('3','26')
G.add_edge('3','38')
G.add_edge('3','28')
G.add_edge('3','37')
G.add_edge('3','30')
G.add_edge('3','31')
G.add_edge('5','6')
G.add_edge('5','8')
G.add_edge('5','9')
G.add_edge('5','22')
G.add_edge('5','23')
G.add_edge('5','26')
G.add_edge('5','28')
G.add_edge('5','30')
G.add_edge('5','31')
G.add_edge('6','8')
G.add_edge('6','9')
G.add_edge('6','22')
G.add_edge('6','23')
G.add_edge('6','26')
G.add_edge('6','28')
G.add_edge('6','30')
G.add_edge('6','31')
G.add_edge('8','9')
G.add_edge('8','22')
G.add_edge('8','23')
G.add_edge('8','26')
G.add_edge('8','28')
G.add_edge('8','30')
G.add_edge('8','31')
G.add_edge('9','22')
G.add_edge('9','23')
G.add_edge('9','26')
G.add_edge('9','28')
G.add_edge('9','30')
G.add_edge('9','31')
G.add_edge('22','23')
G.add_edge('22','26')
G.add_edge('22','28')
G.add_edge('22','30')
G.add_edge('22','31')
G.add_edge('23','26')
G.add_edge('23','28')
G.add_edge('23','30')
G.add_edge('23','31')
G.add_edge('26','28')
G.add_edge('26','30')
G.add_edge('26','31')
G.add_edge('28','30')
G.add_edge('28','31')
G.add_edge('30','31')
G.add_edge('32','33')
G.add_edge('32','37')
G.add_edge('32','38')
G.add_edge('32','40')
G.add_edge('32','41')
G.add_edge('32','54')
G.add_edge('32','57')
G.add_edge('33','37')
G.add_edge('33','38')
G.add_edge('33','40')
G.add_edge('33','41')
G.add_edge('33','54')
G.add_edge('33','57')
G.add_edge('37','38')
G.add_edge('37','40')
G.add_edge('37','41')
G.add_edge('37','54')
G.add_edge('37','57')
G.add_edge('38','40')
G.add_edge('38','41')
G.add_edge('38','54')
G.add_edge('38','57')
G.add_edge('40','41')
G.add_edge('40','54')
G.add_edge('40','57')
G.add_edge('41','54')
G.add_edge('41','57')
G.add_edge('54','57')

print G.nodes()
print nx.fiedler_vector(G,method='lobpcg')

pos=nx.circular_layout(G,dim=50, scale=100)
plt.clf()
nx.draw(G,with_labels=True)
plt.savefig('C:/Users/Branko/Desktop/AAOVKJBEBIDNHE-UHFFFAOYSA-N_unoriented.png')