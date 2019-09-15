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
Our purpose is to categorize different kind of web developers and find out which are complementary technologies with different web frameworks. We use clustering techniques for this purpose. The most famous of clustering techniques is K-Mean clustering. However, this technique does not work for categorical data. We use another variant of K-Means known as K-Mode. There are two major differences between K-Means and K-Mode. Firstly, the distance means is changed to hamming distance, and secondly, means of cluster is changed by modes; hence giving algorithm its name. An easy to integrate python [library](https://pypi.org/project/kmodes/) was used to cluster the users into different groups. 

Furthermore, To find ideal number of clusters elbow method is used. In elbow method we use inter cluster distances to find optimal cluster size. A grid search was conducted over number of clusters to find the elbow cluster. The Figure below shows result of gird search

![ ]({{site.baseurl}}/images/k-modes-elbow.png)

Cluster number of 16 was selected as the ideal number. Next we used inter cluster density to find top 3 most dense clusters for further evaluation. The statistics from top 3 groups vary in counts
                                               
```
('Windows', 6521.0), ('jQuery', 5901.0), ('Linux', 4527.0), ('Android', 2297.0), ('Spring', 1769.0), ('Other(s):', 1746.0), ('Raspberry Pi', 1711.0), ('Django', 1611.0), ('ASP.NET', 1587.0), ('WordPress', 1547.0), ('Angular/Angular.js', 1364.0), ('Docker', 1324.0), ('AWS', 1321.0), ('MacOS', 1248.0), ('Laravel', 1242.0), ('Vue.js', 1185.0), ('Arduino', 1114.0), ('iOS', 1101.0), ('React.js', 1032.0), ('Slack', 941.0), ('Google Cloud Platform', 934.0), ('Flask', 802.0), ('Ruby on Rails', 689.0), ('Microsoft Azure', 601.0), ('Kubernetes', 587.0), ('Heroku', 581.0), ('Drupal', 364.0), ('Express', 287.0), ('IBM Cloud or Watson', 183.0)
```

![ ]({{site.baseurl}}/images/developer-survay-pie-data1.png)

- The first cluster is more inclined towards platform instead of web technologies                                                                                                     

```
('React.js', 6140.0), ('Angular/Angular.js', 5054.0), ('jQuery', 5018.0), ('Express', 4042.0), ('Android', 2422.0), ('Vue.js', 2312.0), ('Linux', 2040.0), ('AWS', 1578.0), ('WordPress', 1562.0), ('iOS', 1549.0), ('Docker', 1364.0), ('Windows', 1356.0), ('Spring', 1302.0), ('Django', 1261.0), ('MacOS', 1246.0), ('Heroku', 1217.0), ('Google Cloud Platform', 1188.0), ('Laravel', 1165.0), ('Slack', 993.0), ('Raspberry Pi', 931.0), ('Other(s):', 854.0), ('Ruby on Rails', 821.0), ('Kubernetes', 749.0), ('Flask', 637.0), ('Arduino', 634.0), ('ASP.NET', 609.0), ('Drupal', 335.0), ('Microsoft Azure', 312.0), ('IBM Cloud or Watson', 204.0)
```
 
![ ]({{site.baseurl}}/images/developer-survay-pie-data2.png)

- Looking at the number of counts it could be deduced that the second cluster represents Web Developers as there is large count for web technologies and technologies like **jQuery** **Vue.js** **React.js** are on the top.
  

```
('ASP.NET', 6497.0), ('Windows', 6337.0), ('Angular/Angular.js', 5912.0), ('Microsoft Azure', 5522.0), ('Docker', 5014.0), ('React.js', 4668.0), ('jQuery', 3130.0), ('Linux', 2878.0), ('AWS', 2510.0), ('Kubernetes', 2453.0), ('Android', 1963.0), ('Slack', 1647.0), ('Vue.js', 1544.0), ('Raspberry Pi', 1523.0), ('Google Cloud Platform', 1366.0), ('iOS', 1271.0), ('MacOS', 1122.0), ('Express', 1115.0), ('Spring', 1063.0), ('WordPress', 928.0), ('Arduino', 761.0), ('Django', 711.0), ('Heroku', 617.0), ('Other(s):', 602.0), ('Flask', 478.0), ('Ruby on Rails', 410.0), ('Laravel', 370.0), ('IBM Cloud or Watson', 285.0), ('Drupal', 153.0)
```

![ ]({{site.baseurl}}/images/developer-survay-pie-data3.png)
 
- Last cluster is more inclined towards dev ops as it has more counts for technologies like Docker AWS Linux and Azure.

It could be seen that the most used web technologies are **ReactJS**, **Angular** and **jQuery**, followed by **Vue.js**
