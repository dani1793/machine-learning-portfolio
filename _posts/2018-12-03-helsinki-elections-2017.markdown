---
layout: post
title:  "Helsinki 2017 elections"
date:   2018-04-02
categories: jekyll update
img: data-science.jpeg
categories: [one, two]
---
In this post we analyze questioners for Helsinki 2017 municipal elections using different embeddings

Figure below shows the embedding for Helsinki Data. The quick look on the MDS plot shows that there is huge difference between the Espoo and Helsinki data. There are no clusters in the Helsinki data whereas there are some clusters present in Espoo data. The difference could be real, or it could be some noise added to the data. As MDS takes euclidian distance into account directly, the shape of the graph could be effected by the addition of noise. We therefore have to observe the other two plots created; namely PCA and ISOMAP.

PCA is one of the projection pursuit methods, which finds the axis with maximum variance and hence addition of noise does not affect directly to the projection. In the PCA plot we can observe that the clusters are the same as that of Espoo dataset.

Furthermore, to support our observation we look into the ISOMAP plot. This embedding technique finds the nearest neighbors of a point, and constructs a tree. It than finds the distance between the points using that tree and feed it to MDS stress function. In ISOMAP plot of the Helsinki data it could be seen that the clusters are preserved in the data.

Looking at all the three plots we can conclude that the difference between data is not real but noise artifact. The noise changed the plot for the MDS; which is directly taking into account the euclidean distance; but it does not affect the PCA or the ISOMAP plot which project the data using different technique. Hence, it could be concluded that the response of candidates for Helsinki and Esppo are almost the same.

![ ]({{site.baseurl}}/images/election-1.png)

#### Projection Description

PCA is one of the projection pursuit methods, which finds the axis with maximum variance. The data matrix is decomposed into SVD and the axis with highest variance is selected to represent the data. In this example of candidate elections dataset we choose 2 principle axis with the highest vairance. The plot of PCA in Figure above shows that the clusters of data are still preserved in the embedded dimension. PCA embedded data keeps the distance between close points close and distant points distant. The behavior could be seen in the figure as well.

ISOMAP embedding technique is a variation of traditional MDS embedding. We first create a graph of the nearest neighbor of data points and than find the distance between the points using that graph. Those geodestic distances are than fed into linear MDS. The technique represents small distances much better than the classical MDS. In Figure above it could be observed that the clusters are maintained as in the original data even after the addition of noise artifact.

MDS uses euclidean distance or in non-metric case a monotonic transformation of embedded space euclidean distance to compare with original space. It than uses regression to find the local minima. MDS is tries to preserve the large distances at the expense of small ones, hence, it can
“collapse” some small distances on the expense of preserving large distances. However, as raw euclidean distances are used, small noise in the data collection or noise could change the embedding. This effect could be seen in the non-metric MDS Figure above.

The implementation could be found [here](https://github.com/dani1793/Machine-Learning-Projects/blob/master/Information%20Visualization/helsinki-elections-2017.ipynb)