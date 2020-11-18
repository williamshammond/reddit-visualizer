#!/usr/bin/env python
# coding: utf-8

# In[9]:


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


# In[136]:


df = pd.read_csv('soccer.csv')


# In[4]:


df = df.drop(['Unnamed: 0', 'Epoch Time'],axis = 1)


# In[254]:


#df


# In[255]:


df.loc[df['Title'].str.contains('ronaldo|messi', flags = re.I, regex = True)] #.I ignores case 


# In[257]:


new_df = df.loc[df['Title'].str.contains('Messi|Ronaldo|Neymar|Haaland|Mbappé|Mbappe|Lewandowski|Suarez |Zlatan Ibrahimović|Zlatan|Ibrahimović|Ibrahimovic|Zlatan Ibrahimovic|Ramos|Agüero|Aguero|Virgil van Dijk|VVD|van Dijk|Bale |Sterling|Rashford |Kevin De Bruyne|Mohamed Salah|Salah|De Bruyne', flags = re.I, regex = True)] #.I ignores case 


# In[256]:


#new_df


# In[258]:


new_df = new_df.drop(['Subreddit',],axis = 1)


# In[259]:


#new_df


# In[260]:


new_df = new_df.reset_index()


# In[261]:


#new_df


# In[ ]:


#ss['test'] = ss['Comments'] + ss['Awards']


# In[262]:


trying = new_df 


# In[264]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Messi', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        #trying.iloc[index]['Player'] = 'Messi'
        trying.iloc[index,10] = 'Messi'
'''       


# In[265]:


#trying.iloc[0:4]


# In[266]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Neymar', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Neymar'
        
 '''       


# In[203]:


#trying.iloc[0:4]


# In[204]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Ronaldo', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Ronaldo'
        
 '''       


# In[205]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Haaland', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Haaland'
        
 '''       


# In[206]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Mbappé|Mbappe', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Mbappé'
        
 '''       


# In[207]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Lewandowski', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Lewandowski'
 '''       
        


# In[208]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Suarez', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Suarez'
        
 '''       


# In[209]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Zlatan Ibrahimović|Zlatan |Ibrahimović|Ibrahimovic|Zlatan Ibrahimovic', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Zlatan Ibrahimović'
'''      
        


# In[210]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Ramos', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Ramos'
'''       
        


# In[ ]:





# In[211]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Agüero|Aguero', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Agüero'
        
'''     


# In[212]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Virgil van Dijk|VVD|van Dijk', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Virgil van Dijk'
        
'''        


# In[213]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Bale', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Bale'
'''       
        


# In[ ]:





# In[214]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Sterling', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Sterling'
        
'''        


# In[215]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Rashford', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Rashford'
'''       
        


# In[216]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Kevin De Bruyne|De Bruyne', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Kevin De Bruyne'
'''       
        


# In[ ]:





# In[217]:


'''
for index, row in trying.iterrows():
    title = row[1]
    matched = re.match('Mohamed Salah|Salah', title, flags = re.I, )
    is_match = bool(matched)   
    if (is_match):
        trying.iloc[index,10] = 'Mohamed Salah'
 '''       
        


# In[267]:


#trying


# In[152]:


#trying.to_csv("error")


# In[230]:


#df_1 = df.loc[df['Title'].str.contains('Messi', flags = re.I, regex = True)] 


# In[241]:


#df2 = df.loc[df['Title'].str.contains('Ronaldo', flags = re.I, regex = True)] 


# In[268]:


#df2.reset_index()


# In[243]:


#This is sample code for extracting player name from title and making a new data frame 
#with that as a separate category 
#I did this separately, but this process can also be automated
df2 = df.loc[df['Title'].str.contains('Ronaldo', flags = re.I, regex = True)] 
random = []
for x in range(25):
    random.append("Ronaldo")

df2 = df2.assign(Player = random) 


# In[269]:


#df2


# In[ ]:





# In[247]:


frames = [df_1, df2]
result12 = pd.concat(frames)


# In[249]:


result12


# In[250]:


df2 = df.loc[df['Title'].str.contains('Haaland', flags = re.I, regex = True)] 
df2.reset_index()


# In[251]:


random = []
for x in range(10):
    random.append("Haaland")

df2 = df2.assign(Player = random) 


# In[270]:


#df2


# In[255]:


result12final = result12


# In[271]:


#result12final


# In[257]:


frames = [result12final, df2]
resultH = pd.concat(frames)


# In[272]:


#resultH


# In[273]:


#resultH.iloc[50:90]


# In[274]:


#result12


# In[262]:


tillHalland = resultH


# In[275]:


#tillHalland


# In[268]:


df33 = df.loc[df['Title'].str.contains('Mbappé|Mbappe', flags = re.I, regex = True)] 
df33.reset_index()



# In[269]:


random = []
for x in range(7):
    random.append("Mbappé")

df33 = df33.assign(Player = random) 


# In[276]:


#df33


# In[275]:


dfRL = df.loc[df['Title'].str.contains('Lewandowski', flags = re.I, regex = True)] 
dfRL.reset_index()


# In[276]:


random = []
for x in range(6):
    random.append("Lewandowski")

dfRL = dfRL.assign(Player = random) 


# In[277]:


#dfRL


# In[280]:


dfLS = df.loc[df['Title'].str.contains('Suarez', flags = re.I, regex = True)] 
dfLS.reset_index()



# In[281]:


random = []
for x in range(10):
    random.append("Suarez")

dfLS = dfLS.assign(Player = random) 


# In[278]:


#dfLS


# In[283]:


dfZ = df.loc[df['Title'].str.contains('Zlatan Ibrahimović|Zlatan |Ibrahimović|Ibrahimovic|Zlatan Ibrahimovic', flags = re.I, regex = True)] 
dfZ.reset_index()



# In[286]:


random = []
for x in range(15):
    random.append("Zlatan Ibrahimović")

dfZ = dfZ.assign(Player = random) 


# In[279]:


#dfZ


# In[288]:


dfra = df.loc[df['Title'].str.contains('Ramos', flags = re.I, regex = True)] 
dfra.reset_index()




# In[289]:


random = []
for x in range(6):
    random.append("Ramos")

dfra = dfra.assign(Player = random) 


# In[280]:


#dfra


# In[291]:


dfass = df.loc[df['Title'].str.contains('Agüero|Aguero', flags = re.I, regex = True)] 
dfass.reset_index()





# In[292]:


random = []
for x in range(3):
    random.append("Aguero")

dfass = dfass.assign(Player = random) 


# In[281]:


#dfass


# In[300]:


dfhate = df.loc[df['Title'].str.contains('Virgil|van Dijk|VVD', flags = re.I, regex = True)] 
dfhate.reset_index()






# In[301]:


random = []
for x in range(8):
    random.append("Virgil van Dijk")

dfhate = dfhate.assign(Player = random) 


# In[282]:


#dfhate


# In[ ]:





# In[303]:


dfLOLOL = df.loc[df['Title'].str.contains('Bale', flags = re.I, regex = True)] 
dfLOLOL.reset_index()






# In[304]:


random = []
for x in range(13):
    random.append("Bale")

dfLOLOL = dfLOLOL.assign(Player = random) 


# In[283]:


#dfLOLOL


# In[ ]:





# In[307]:


dfqqqq = df.loc[df['Title'].str.contains('Rashford', flags = re.I, regex = True)] 
dfqqqq.reset_index()






# In[309]:


random = []
for x in range(18):
    random.append("Rashford")

dfqqqq = dfqqqq.assign(Player = random) 


# In[284]:


#dfqqqq


# In[311]:


dfggg = df.loc[df['Title'].str.contains('Kevin De Bruyne|De Bruyne', flags = re.I, regex = True)] 
dfggg.reset_index()







# In[313]:


random = []
for x in range(9):
    random.append("Kevin De Bruyne")

dfggg = dfggg.assign(Player = random) 


# In[285]:


#dfggg


# In[315]:


dfmmd = df.loc[df['Title'].str.contains('Mohamed Salah|Salah', flags = re.I, regex = True)] 
dfmmd.reset_index()








# In[316]:


random = []
for x in range(8):
    random.append("Mohamed Salah")

dfmmd = dfmmd.assign(Player = random) 


# In[286]:


#dfmmd


# In[318]:


total = [dfmmd, dfggg, dfqqqq, dfLOLOL, dfhate, dfass, dfra, dfZ, dfLS, dfRL, df33, tillHalland]
plswork = pd.concat(total)

#This is compiling all the data sets we had created for indiviual players


# In[287]:


#plswork


# In[288]:


#plswork.reset_index()


# In[3]:


#plswork.to_csv('properdata') 
#This created a CSV file of the Data Frame, which can be used later 
#The advantage is you have a checkpoint in case original data frame is accidently modified


# In[5]:


dt = pd.read_csv('properdata')


# In[15]:


dt["Player"].iplot(kind="histogram", theme="white",
                title="Mentions in Top 1000 Most Upvoted Posts during 2020",xTitle='Player', yTitle='Frequency')


# In[16]:


'''Fig1.to_html(Fig1, config=None,
                  auto_play=True, include_plotlyjs=True, 
                  include_mathjax=False, post_script=None,
                  full_html=True, animation_opts=None, 
                  default_width='100%', default_height='100%', validate=True)
                  '''


# In[388]:


#dt["male_age"]=dt[dt["Sex"]=="male"]["Age"]
#dt["female_age"]=dt[dt["Sex"]=="female"]["Age"]
#dt[["male_age","female_age"]].iplot(kind="histogram", bins=20, theme="white", title="Passenger's Ages",
#         xTitle='Ages', yTitle='Count')
#dt["Player"]["Upvotes"]


# In[346]:


dt.corr().iplot(kind='heatmap',colorscale="Blues",title="Feature Correlation Matrix")


# In[355]:


#we will get help from pivot tables to get Fare values in different columns for each class.
df[['Upvote Ratio', 'Comments']].pivot(columns='Upvote Ratio', values='Comments').iplot(kind='box',
                                                                                        title="Upvote Ratio and Number of Comments",
                                                                                        xTitle='Upvote Ratio', yTitle='Comments')


# In[360]:


#we will get help from pivot tables to get Fare values in different columns for each class.
dt[['Player', 'Comments']].pivot(columns='Player', values='Comments').iplot(kind='box',
                                                                                        title="Players and Number of Comments",
                                                                                        xTitle='Players', yTitle='Comments')


# In[ ]:





# In[365]:


#we will get help from pivot tables to get Fare values in different columns for each class.
dt[['Player', 'Awards']].pivot(columns='Player', values='Awards').iplot(kind='box',
                                                                                        title="Player and Awards",
                                                                                        xTitle='Players', yTitle='Awards')


# In[366]:


#we will get help from pivot tables to get Fare values in different columns for each class.
dt[['Player', 'Upvote Ratio']].pivot(columns='Player', values='Upvote Ratio').iplot(kind='box',
                                                                                        title="Player and Upvote Ratio",
                                                                                        xTitle='Players', yTitle='Upvote Ratio')


# In[386]:


dt.iplot(kind="scatter", theme="white",x="Comments",y="Upvotes", categories = "Player", xTitle='Comments', yTitle='Upvotes')
            


# In[385]:


#converting Survived column to float64 to be able to use in plotly
dt.iplot(kind='bubble', x="Upvotes",y="Comments",categories="Player", size='Upvotes', text='Player', xTitle='Upvotes', yTitle='Comments')


# In[ ]:


#survived_sex = df[df['Survived']==1]['Sex'].value_counts()
#dead_sex = df[df['Survived']==0]['Sex'].value_counts()
#df1 = pd.DataFrame([survived_sex,dead_sex])
#df1.index = ['Survived','Dead']
#df1.iplot(kind='bar',barmode='stack', title='Survival by the Sex')


# In[7]:


dt


# In[ ]:


dt["Player"].iplot(kind="histogram", theme="white",
                title="Mentions in Top 1000 Most Upvoted Posts during 2020",xTitle='Player', yTitle='Frequency')


# In[242]:


figa = px.bar(dt, x='Player', y='Upvotes', hover_name = 'Title', template="plotly_dark",
              title="How many Upvotes has each player gotten this year?") #text = title
figa.show()
figa.write_html("FigA.html")


# In[175]:


#figa = px.bar(dt, x='Player', y='Downvotes', hover_name = 'Title',
 #             title="How many Downvotes has each player gotten this year?") #text = title
#figa.show()
#figt.write_html("Fig5.html")


# In[243]:


figb = px.histogram(dt, x="Player", template="plotly_dark", 
                    title="How many times has each player been mentioned in the Top 1000 posts this year?")
figb.show()
figb.write_html("FigB.html")


# In[253]:


figc = px.scatter(dt, x = "Upvotes", y = "Player", hover_name = "Title",
                  color = "Awards", template="plotly_dark", 
                  color_continuous_scale=["blue", "yellow", "purple", "red"],
                  title="Distribution of Upvotes on Posts about each Player")
figc.show()
figc.write_html("FigC.html")


# In[245]:


figd = px.scatter(dt, x = "Comments", y = "Player", hover_name = "Title", 
                  color = "Awards", template="plotly_dark",
                  color_continuous_scale=["blue", "yellow", "purple", "red"],
                 title="Distribution of Comments on Posts about each Player")
figd.show()
figd.write_html("FigD.html")


# In[173]:


#fige = px.scatter(dt, x = "Awards", y = "Player", hover_name = "Title", color = "Upvotes", template="plotly_dark",
 #                title="Distribution of Awards on different posts about each player")
#fige.show()
 #fig.write_html("Fig1.html")


# In[198]:


#fige = px.scatter(dt, x = "Downvotes", y = "Player", hover_name = "Title", color = "Upvotes", template="plotly_dark",
          #       title="Distribution of Awards on different posts about each player")
#fige.show()
#fig.write_html("Fig1.html")


# In[42]:


#figf = px.scatter(dt, x='Player', y='Upvote Ratio', hover_name = 'Title',
 #             title="How many Upvotes has each player gotten this year?") #text = title
#figf.show()
#figt.write_html("Fig5.html")


# In[68]:


#figf = px.scatter(dt, x="Upvotes", y="Comments", color = "Upvote Ratio",
 #3                 hover_name = 'Title',
  #                title="Upvote to Comment Ratio on Top 15 Subreddits") #size='Awards'
#figf.show()
#fig1.write_html("Fig1.html")


# In[246]:


figg = px.scatter(df, x="Upvotes", y="Comments", color = "Upvote Ratio", 
                  hover_name = 'Title', template="plotly_dark",
                  color_continuous_scale=["white", "purple", "red" ,"yellow"],
                  title="Upvotes and Comments on the Top 1000 Posts this year on r/soccer") #size='Awards'
figg.show()
figg.write_html("FigG.html")


# In[89]:


#figd.add_trace(fige)


# In[91]:


dfPC = df


# In[107]:


#dfPC.drop('Unnamed',axis = 1)
#dfPC = dfPC.drop('Title',axis = 1)
#dfPC = dfPC.drop('Date',axis = 1)
#dfPC = dfPC.drop('Subreddit',axis = 1)
#dfPC = dfPC.drop('Unnamed: 0',axis = 1)
dfPC = dfPC.drop('Epoch Time',axis = 1)


# In[147]:


#import plotly.express as px
#df = px.data.iris()
figh = px.parallel_coordinates(dfPC, title = "Trends of Different Data Points on r/soccer") #, color="Upvotes")
                             #color_continuous_scale=px.colors.diverging.Tealrose,
                             #color_continuous_midpoint=2)
figh.show()


# In[149]:


#fig = px.violin(df, x = "Comments", box=True, # draw box plot inside the violin
#                points='all', # can be 'outliers', or False
       #        )
#fig.show()


# In[144]:


#fig = px.bar_polar(df, r="Upvotes", theta="Comments",
 #                  color="Upvote Ratio", template="plotly_dark",
  #                 color_discrete_sequence= px.colors.sequential.Plasma_r)
#fig.show()


# In[151]:


xx = []
for index, row in df.iterrows():
    x = (index, row['Date'])
    x2 = x[1]
    x3 = (x2[:2])
    xx.append(x3)
df.insert(11, "Month", xx, True)


# In[152]:


xy = []
for index, row in df.iterrows():
    x = (index, row['Date'])
    x2 = x[1]
    x3 = (x2[11:14])
    xy.append(x3)
df.insert(11, "Hour", xy, True)


# In[155]:


#df


# In[248]:


figh = px.bar(df, x='Hour', y='Comments', hover_name = 'Title',
              template="plotly_dark",    
              title="Hour of the Day and Comments received on r/soccer Posts") #text = title
figh.show()
figh.write_html("FigH.html")


# In[250]:


figi = px.histogram(df, x='Month', y='Upvotes', hover_name = 'Title', template="plotly_dark",
              title="Upvotes on r/soccer over the Months of 2020") #text = title color_discrete_sequence =['green']
figi.update_layout(
    #barmode="overlay",
    bargap=0.2)
figi.show()
fig2.write_html("FigI.html")


# In[251]:


figj = px.histogram(df, x='Month', y='Comments', hover_name = 'Title', 
              template="plotly_dark",
              title="Comments r/soccer over the Months of 2020") #text = title color_discrete_sequence =['green']
figj.update_layout(
    #barmode="overlay",
    bargap=0.2)
figj.show()
figj.write_html("FigJ.html")


# In[ ]:





# In[ ]:





# In[ ]:




