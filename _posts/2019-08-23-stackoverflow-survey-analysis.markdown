---
layout: post
title:  "Categorization of Web Developers"
date:   2019-08-23
categories: jekyll update
img: data-science.jpeg
categories: [one, two]
---

A categorical analysis of stack overflow questions is performed to learn about trends in web technologies. Different categorical clustering techniques are used to extract non obvious trends and help decision making

Stack Overflow is one of the most active forum used worldwide by developers to find solutions to the problem they face in everyday tasks. In recent years Stack Overflow has started conducting surveys to get to know thoughts of developers about recent technologies and future technologies. More details and the dataset could be found [here](https://insights.stackoverflow.com/survey). 

For the purpose of this project we choose subset of features namely **WebFrameWorkedWith**, **WebFrameDesireNextYear**, **PlatformWorkedWith** and **PlatformDesireNextYear**. The data for these features looks like this

![ ]({{site.baseurl}}/images/raw-features.png)

The features are comma separated list of features which cannot be used directly for analysis. For the purpose of analysis we convert this data into categorical data. There are 29 unique feature extracted and each feature can take binary value for each user. The below shows exhaustive list of features

```
'React.js', 'Ruby on Rails', 'jQuery', 'Android', 'Arduino', 'Microsoft Azure', 'Angular/Angular.js', 'IBM Cloud or Watson', 'MacOS', 'Docker', 'Express', 'Raspberry Pi', 'Flask', 'iOS', 'WordPress', 'Windows', 'Other(s):', 'Spring', 'Laravel', 'Heroku', 'Kubernetes', 'Google Cloud Platform', 'Django', 'ASP.NET', 'Linux', 'Drupal', 'Slack', 'Vue.js', 'AWS'
```

Our purpose is to categorize different kind of web developers and find out which are complementary technologies with different web frameworks. We use clustering techniques for this purpose. The most famous of clustering techniques is K-Mean clustering. However, this technique does not work for categorical data. We use another variant of K-Means known as K-Mode. There are two major differences between K-Means and K-Mode. Firstly, the distance means is changed to hamming distance, and secondly, means of cluster is changed by modes; hence giving algorithm its name. An easy to integrate python [library](https://pypi.org/project/kmodes/) which was used to cluster the users into different groups. 

Furthermore, To find ideal number of clusters elbow method is used. In elbow method we use inter cluster distances to find optimal cluster size. A grid search was conducted over number of clusters to find the elbow cluster. The Figure below shows result of gird search

![ ]({{site.baseurl}}/images/k-modes-elbow.png)

Cluster number of 16 was selected as the ideal number. Next we used inter cluster density to find top 3 most dense clusters for further evaluation. The statistics from top 3 groups vary in counts
                                               
![ ]({{site.baseurl}}/images/k-modes-all-1-cluster.png)
                                                                                                     
- Looking at the number of counts it could be deduced that the first cluster represents Web Developers as there is large count for web technologies and technologies like **jQuery** **Vue.js** **React.js** are on the top.

![ ]({{site.baseurl}}/images/k-modes-all-2-cluster.png)
 
- The second cluster is more inclined towards dev ops as it has more counts for technologies like  **Docker** **AWS** **Linux** and **Azure**.

![ ]({{site.baseurl}}/images/k-modes-all-3-cluster.png)
 
- Last but not the least the third cluster has minimal counts showing that its a mixed hybrid group with no dominance

As our objective is to look for web developer we would take a closer look at the second cluster as it has greater number of statistics for web technologies. We can now find the technology stack that being used for each web framework by filtering out users that uses the specific technology. For the sake of project we choose Angular.

![ ]({{site.baseurl}}/images/k-modes-all-angular.png)

It can be deduced from the statistics that the big counts are for **Angular**, **Vue.js** and **React.js**. After them comes **jQuery** followed by **Express** and **Docker**
