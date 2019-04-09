#Ryan Anderson
#NLP assign 3 - Part 3

###USED POLITICAL CORPUS FROM USNA

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

kt = open("keyword-tweets.txt", "r")

data = []

#just receive tweet, not "POLIT/NOT"
for line in kt:
    data.append(line.split()[1:])

#print(data)

data_all = []

for i in data:
    data_all.append(" ".join(i))

#print(data_all)
    


tweet = []
vs_compound = []
vs_pos = []
vs_neu = []
vs_neg = []

analyzer = SentimentIntensityAnalyzer()

for i in range(0, len(data_all)):
     tweet.append(data_all[i])
     vs_compound.append(analyzer.polarity_scores(data_all[i])['compound'])
     vs_pos.append(analyzer.polarity_scores(data_all[i])['pos'])
     vs_neu.append(analyzer.polarity_scores(data_all[i])['neu'])
     vs_neg.append(analyzer.polarity_scores(data_all[i])['neg'])

import pandas 
from pandas import DataFrame

twitter_df = DataFrame({'Tweet': tweet,
     'Compound': vs_compound,
     'Positive': vs_pos,
     'Neutral': vs_neu,
     'Negative': vs_neg})
twitter_df = twitter_df[['Tweet',  'Compound',
     'Positive', 'Neutral', 'Negative']]


#part 3-1
twitter_df.head()

#part 3-2
import matplotlib.pyplot as plt
plt.hist(vs_compound, bins=20)

out = open("output.txt", "w")
out.write("I USED POLITCAL CORPUS FROM USNA.  WILL NOT INCLUDE FAVORITES COLUMN")
out.write("\n")
out.write(head)
out.write("\n")
out.write("\n screenshot of histogram will be named screenshot_hist.png in folder")
out.write("\n")

#part 3-3
sorted = twitter_df.sort_values(by=['Compound'], ascending = False)
sorted = sorted.head(10)
sorted

out.write("\n")
out.write("\n")
out.write(str(sorted))

out.write("\n")
out.write("\n")
out.write("NOTE: spyder does not format datafram correctly.  I have also put into the folder a python notebook to run if needed to see columns.")