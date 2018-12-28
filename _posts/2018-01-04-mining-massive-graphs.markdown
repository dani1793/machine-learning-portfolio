---
layout: post
title:  "Social Network Analysis"
categories: jekyll update
img: social-network.png
categories: two
---

In this project several massive social network graphs are read and analyzed. Approximation methods are used to find the statistics for graphs which require unrealistic computation time 


## Project Description

Now a days the graphs for the real word networks are massive. Conventional exact computation techniques require unrealistic computation time and memory. 
To overcome this problem approximate computation techniques are used to find the statistics of graphs. 
In this project the statistics for the graphs were calculated and time complexity of exact and approximate methods was compared for different real world graphs. 
The exact computation method was parallelized to reduce the time complexity.
The networks used were from the Stanford Network Analysis Project [SNAP](http://snap.stanford.edu/data/index.html)
in particular, we worked with the following social networks, listed in increasing size

1. wiki-Vote : 7 115 nodes
2. soc-Epinions1 : 75 879 nodes
3. ego-Gplus : 107 614 nodes
4. soc-Pokec : 1 632 803 nodes

The code base for this project could be found [here](https://github.com/dani1793/Machine-Learning-Projects/tree/master/Mining%20Massive%20Graphs#abstract)