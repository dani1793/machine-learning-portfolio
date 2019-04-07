---
layout: post
title:  "Email Marketing"
date:   2019-03-01
categories: jekyll update
img: data-science.jpeg
categories: [one, two]
---

## Introduction

This project uses Reinforcement Learning to predict optimal time for sending multiple category emails to different type of users

For email campaign, the traditional problem is to personalize email to clients. The problem could be divided into several sub problems including but not limiting to finding most effective time period to send the email, personalize the content of the email depending on feature extracted from client. One way to approach this problem is to observe the patterns of interactions people have with emails and try to depict their behavior. A stream of interactions occurs between the company and each customer, including actions from the company (such as emails) and actions by the customer (such as registering to advertised campaign). Understanding user decisions is a problem gaining increased interest in today’s research. Mining behavior patterns has been used to discover users that share similar habits\cite{inproceedings} and using sequential patterns to learn models of human behavior has been employed in lifestyle assistants to increase the life quality of elderly people\cite{nt:models-human}. Research has been done to automate different aspects of campaigning problem using Reinforcement Learning, \cite{cost-sensitive} have used reinforcement learning to address the issue of sequential decision making when interactions can occur among decision outcomes. They have used function approximation with batch reinforcement learning along with data mining to learn scalable model for marketing targeted audience. \cite{cross-channel} discusses method to find link between marketing actions taken in one channel and customer response obtained in another, specifically they discussed maximization of profit/ revenue obtained in store channel by optimizing direct mail catalogue mailings for multiple campaigns. They have used batch Q learning with advantage updating to tackle the problem. \cite{DBLP:journals/eswa/Gomez-PerezMSBPC09} uses RL to optimize discount rates for customers to help companies retain loyal customers, the paper suggests use of Self Organizing Maps (SOPs) to model state space and neural network was used as predictor of q-values for state space. 

In this report we simulate the user behaviour to email campaigns and try to build a Reinforcement Learning agent that would optimize email campaigns by analysing category of email and time at which email was sent. The agent performs well on simulated data, it is able to find times when it is optimal to send email to users, it also categorize the users into campaigns that they respond to positively.