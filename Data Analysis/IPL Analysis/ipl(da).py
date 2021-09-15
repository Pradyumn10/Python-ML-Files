# -*- coding: utf-8 -*-
"""IPL(DA).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s9AM3_lbIeplWHTn-geg47suXaLsDFxp
"""

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/Pradyumn10/Data-Science-Python/master/Data%20Analysis/IPL%20Analysis/ipl.csv"
ipl=pd.read_csv(url)

ipl

ipl.shape

type(ipl)

#getting details of mom
ipl['player_of_match'].value_counts()

#taking top 10 of the mom winners
mom=ipl['player_of_match'].value_counts()[0:5]

#making a bar plot for top 10 players
plt.figure(figsize=(5,5))
plt.bar(list(mom.keys()),list(mom))
plt.show()

ipl['result'].value_counts()

ipl['toss_winner'].value_counts()

#Extracting the details of team which won by batting first
batting_first = ipl[ipl["win_by_runs"]!=0]

batting_first

plt.figure(figsize=(7,7))
plt.hist(batting_first['win_by_runs'])
plt.show()

#finding out the count of teams winning after batting first
batting_first['winner'].value_counts()

#making a bar plot of top 3 teams which are winning by batting first
plt.figure(figsize=(7,7))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=["blue","yellow","orange"])
plt.show()

#Making a pie chart
plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()

#extracting the records of team which won by batting second
batting_second = ipl[ipl['win_by_wickets']!=0]

batting_second

#Making a histogram for frequency of wins w.r.t number of wickets
plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()

#Finding out the frequency of number of wins w.r.t each time after batting second
batting_second['winner'].value_counts()

#Making a bar plot for top-3 teams with most wins after batting second
plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=["black","blue","red"])
plt.show()

#Making a pie chart for distribution of most wins after batting second
plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()

#Looking at the number of matches played each season
ipl['season'].value_counts()

#Looking at the number of matches played in each city
ipl['city'].value_counts()

#Finding out how many times a team has won the match after winning the toss
np.sum(ipl['toss_winner']==ipl['winner'])

#finding the probability of toss winner=match winner
393/756
