import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mat = pd.read_csv("matches.csv")

#How many matches we’ve got in the dataset?
print(mat['id'].max())

#How many seasons we’ve got in the dataset?
print(len(mat["season"].unique()))

#Which Team had won by maximum runs?
r = mat.iloc[mat["win_by_runs"].idxmax()]["winner"]
print(r)

#Which Team had won by maximum wicket?
g = mat.loc[mat['win_by_wickets'] == mat ['win_by_wickets'].max()]['winner']
print(g)

#Which Team had won by closest Margin (minimum runs)?
w = mat.loc[mat['win_by_runs'] == mat ['win_by_runs'].min()]['winner']
print(w)

#Which Team had won by minimum wicket?
d = mat.loc[mat['win_by_wickets'] == mat ['win_by_wickets'].min()]['winner']
print(d)

#Which Season had most number of matches?
ad = mat['season']
pat = ad.value_counts()
print(pat)
pat.plot(kind = 'bar')
plt.show()

#Which IPL Team is more successful?
sad = mat['winner']
lat = sad.value_counts()
print(lat)

#Has Toss-winning helped in winning matches?
tos = mat['toss_winner'] == mat['winner']
ask = tos.groupby(tos).size()
print(ask)