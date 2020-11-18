

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


df1 = pd.read_csv('funny.csv')
df2 = pd.read_csv('askreddit.csv')
df3 = pd.read_csv('gaming.csv')
df4 = pd.read_csv('aww.csv')
df5 = pd.read_csv('pics.csv')
df6 = pd.read_csv('music.csv')
df7 = pd.read_csv('science.csv')
df8 = pd.read_csv('worldnews.csv')
df9 = pd.read_csv('videos.csv')
df10 = pd.read_csv('todayilearned.csv')
df11 = pd.read_csv('movies.csv')
df12 = pd.read_csv('news.csv')
df13 = pd.read_csv('showerthoughts.csv')
df14 = pd.read_csv('earthporn.csv')
df15 = pd.read_csv('gifs.csv')



total = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13,df14,df15]
dfsum = pd.concat(total)



#dfsum




fig1 = px.scatter(dfsum, x="Upvotes", y="Comments",
                  color= 'Subreddit', hover_name = 'Title',
                  template="plotly_dark",
                  title="Upvotes and Comments on the Top 15 Subreddits") #size='Awards'
fig1.show()
fig1.write_html("FigAA.html")



xx = []
for index, row in dfsum.iterrows():
    x = (index, row['Date'])
    x2 = x[1]
    x3 = (x2[:2])
    xx.append(x3)
dfsum.insert(11, "Month", xx, True)




#dfsum




#fig2 = px.bar(dfsum, x='Month', y='Upvotes', hover_name = 'Title',
   #           title="Upvotes over the months of 2020") #text = title color_discrete_sequence =['green']
#fig2.show()
#fig2.write_html("Fig5.html")



xy = []
for index, row in dfsum.iterrows():
    x = (index, row['Date'])
    x2 = x[1]
    x3 = (x2[11:14])
    xy.append(x3)
dfsum.insert(11, "Hour", xy, True)


#dfsum




#fig3 = px.bar(dfsum, x='Hour', y='Upvotes',
 #               title="Hour of the day and upvotes recieved") #text = title
#fig3.show()
#fig3.write_html("Fig10.html")



#dfsum.groupby(['Hour']).count()



#dfsum.describe()



figb = px.histogram(dfsum, x="Subreddit", y = "Upvotes", template="plotly_dark",
                    title="How Active are the 15 most Subscribed Subreddits?")
figb.show()
figb.write_html("FigAB.html")



#figb = px.histogram(dfsum, x="Subreddit", y = "Comments", title="How many comments do different top Subreddits get?")
#figb.show()



figc = px.histogram(dfsum, x="Month", y = "Awards", template="plotly_dark",
                    title="What impact did free Awards have? An analysis of Awards across 2020!")
figc.update_layout(
    #barmode="overlay",
    bargap=0.2)
figc.show()
figc.write_html("FigAC.html")


figd = px.histogram(dfsum, x="Month", template="plotly_dark",
                     y = "Upvotes", title="Upvotes on the Top 15 Subreddits across 2020")
figd.update_layout(
    #barmode="overlay",
    bargap=0.2)
figd.show()
figd.write_html("FigAD.html")



fige = px.histogram(dfsum, x="Hour", y = "Comments", template="plotly_dark",
                    title="What is the Best time to Post? Comments across Hour of Day")
fige.update_layout(
    #barmode="overlay",
    bargap=0.2)
fige.show()
fige.write_html("FigAE.html")


figf = px.histogram(dfsum, x="Hour", y = "Upvotes",
                    template="plotly_dark",  
                    title="What is the Best time to Post? Upvotes across Hour of Day"
                    )
figf.update_layout(
    #barmode="overlay",
    bargap=0.2)
figf.show()
figf.write_html("FigAF.html")




dfPC = dfsum



#dfPC = dfPC.drop('Unnamed',axis = 1)
dfPC = dfPC.drop('Title',axis = 1)
dfPC = dfPC.drop('Date',axis = 1)
dfPC = dfPC.drop('Subreddit',axis = 1)
dfPC = dfPC.drop('Unnamed: 0',axis = 1)
dfPC = dfPC.drop('Epoch Time',axis = 1)


#dfPC



#import plotly.express as px
#df = px.data.iris()
figg = px.parallel_coordinates(dfPC, template="plotly_dark",
                               title = "How do Top Posts do on Reddit? Trends of Different Data Points") #, color="Upvotes")
color_continuous_scale("=px.colors.diverging.Tealrose,")
                             #color_continuous_midpoint=2)
figg.show()
figg.write_html("FigAG.html")




