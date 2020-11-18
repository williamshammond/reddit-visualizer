

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import re

get_ipython().run_line_magic('matplotlib', 'inline')

import cufflinks as cf
import plotly.offline
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)

import plotly.express as px
long_df = px.data.medals_long()



df1 = pd.read_csv('askmen.csv')



df2 = pd.read_csv('askwomen.csv')




df3 = pd.read_csv('askreddit.csv')




#df1.describe()


#df2.describe()



#df3.describe()


#aa = 1



fig = px.scatter(df1, x="Upvotes", y="Comments", color= 'Upvote Ratio', 
                 size='Awards', hover_name = 'Title', 
                 title="Upvotes and Comments on Top 1000 Posts this year on r/AskMen")
fig.show()
fig.write_html("Fig1.html")




fig2 = px.scatter(df2, x="Upvotes", y="Comments", color= 'Upvote Ratio', 
                  size='Awards', hover_name = 'Title', 
                  title="Upvotes and Comments on Top 1000 Posts this year on r/AskWomen")
fig2.show()
fig2.write_html("Fig2.html")



fig3 = px.scatter(df3, x="Upvotes", y="Comments", color= 'Upvote Ratio',
                  size='Awards',
                  title="Upvotes and Comments on Top 1000 Posts this year on r/AskReddit")
fig3.show()
fig3.write_html("Fig3.html")

total = [df1, df2, df3]
dfsum = pd.concat(total)




#dfsum.head()



#fig = px.bar(dfsum, x='Subreddit', y='Upvotes', hover_name = 'Title', title="Total Upvotes Accross Different Subreddits") #text = title
#fig.show()




fig4 = px.scatter(dfsum, x="Upvotes", y="Comments",
                  color= 'Subreddit', hover_name = 'Title',
                  title="Upvote to Comment Ratio on Different Ask Reddits") #size='Awards'
fig4.show()
fig4.write_html("Fig4.html")


dftime = dfsum




#dftime.head()




xx = []
for index, row in dftime.iterrows():
    x = (index, row['Date'])
    x2 = x[1]
    x3 = (x2[:2])
    xx.append(x3)


#xx



dftime.insert(11, "Month", xx, True)



#dftime




figt = px.bar(dftime, x='Month', y='Upvotes', hover_name = 'Title',
              title="Upvotes over the months of 2020") #text = title
figt.show()
figt.write_html("Fig5.html")



figt = px.bar(dftime, x='Month', y='Comments', hover_name = 'Title',
              title="Comments over the months of 2020") #text = title
figt.show()
figt.write_html("Fig6.html")



figt = px.bar(dftime, x='Month', y='Awards', hover_name = 'Title'
              ,title="Awards over the months of 2020") #text = title
figt.show()




fig2222 = px.scatter(dftime, x="Upvotes", y="Comments", color= 'Month', 
                     size='Awards', hover_name = 'Title',
                     title="Upvote to Comment Ratio; Size of Circles indicates number of awards")
fig2222.show()
fig2222.write_html("Fig7.html")




#figt = px.bar(dftime, x='Month', y='Upvote Ratio',
             # hover_name = 'Title', title="Upvote Ratio of every month") #text = title
#figt.show()



fig4 = px.scatter(dftime, x="Month", y="Upvotes", 
                  color= 'Upvote Ratio', size='Comments', hover_name = "Title", 
                  title="Upvotes on r/Ask Subreddits across 2020, with Comments indicated by the Size of the Circles")
fig4.show()
fig4.write_html("Fig8.html")




fig5 = px.scatter(dftime, x="Month", y="Comments", 
                  color= 'Upvote Ratio', size='Upvotes', hover_name = "Title", 
                  title="Comments on r/Ask Subreddits across 2020, with Upvotes indicated by the Size of the Circles")
fig5.show()
fig5.write_html("Fig9.html")




dmhours = dfsum




xy = []
for index, row in dmhours.iterrows():
    x = (index, row['Date'])
    x2 = x[1]
    x3 = (x2[11:14])
    xy.append(x3)
    #print(x3)




dmhours.insert(11, "Hour", xy, True)



#dmhours



fighhr = px.bar(dmhours, x='Hour', y='Upvotes', hover_name = 'Title',
                title="Hour of the day and upvotes recieved") #text = title
fighhr.show()
fighhr.write_html("Fig10.html")



fighhr = px.bar(dmhours, x='Hour', y='Comments', hover_name = 'Title',
                title="Hour of the day and comments recieved") #text = title
fighhr.show()
fighhr.write_html("Fig11.html")




figthhh = px.scatter(dmhours, x="Hour", y="Comments", 
                  color= 'Hour', hover_name = "Title", 
                  title="Hour Posted vs Number of Comments")
figthhh.show()
figthhh.write_html("Fig12.html")



dmtrial = dmhours



dmtrial = dmtrial.sort_values('Hour', ascending=True)



#dmtrial






figthhhh = px.scatter(dmtrial, x="Hour", y="Comments", 
                  color= 'Hour', size='Upvotes', hover_name = "Title", 
                  title="Number of comments on r/Ask Subreddits with Time of Day, with Size of Dots indicating Upvotes")
figthhhh.show()
figthhhh.write_html("Fig13.html")




#fig321 = px.scatter(dmhours, x="Hour", y="Upvotes", color= 'Upvote Ratio', title="//")
#fig321.show()



figtt = px.scatter_ternary(dmhours, a = 'Downvotes', b = 'Comments', c = 'Upvotes', 
                           hover_name = 'Title', color = 'Upvote Ratio', 
                           title="Ternary Plot of Relative Upvotes, Downvotes, and Comments on r/Ask Subreddits")
figtt.show()
figtt.write_html("Fig14.html")



#figtta = px.scatter_ternary(dmhours, a = 'Upvotes', b = 'Comments', c = 'Comment/Upvote Ratio')
#figtta.show()


