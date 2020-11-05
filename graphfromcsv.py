#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:11:05 2020

@author: william
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import statsmodels.api as sm


df = pd.read_csv('/Users/william/Desktop/Python Website/output4.csv')

fig = px.scatter_ternary(df, a="Relative Upvotes", b="Relative Comments", c="Relative Downvotes", hover_name="Title", opacity = 0.7, color="Topic", size="Upvotes", size_max=9, title = 'Post reception within news Subreddits by category (2020) — Normalized Upvotes, Comments, and Downvotes', color_discrete_map = {"Donald Trump": "darkred", "Joe Biden": "blue", "Racial Justice Protests":"orange","COVID-19":"black","The Economy":"green"} )


'''trace_a = go.Scatterternary({
    'mode': 'markers',
    'name': 'Donald Trump',
    'a': df.loc[df['Topic'] == 'Donald Trump']['Relative Upvotes'],
    'b': df.loc[df['Topic'] == 'Donald Trump']['Relative Comments'],
    'c': df.loc[df['Topic'] == 'Donald Trump']['Relative Downvotes'],
    'text': df['Title'],
    'hoverinfo': ['name','a'],
    'marker': {
        'color': 'red',
        'size': 14,
        'line': { 'width': 2 }
    }} )

trace_b = go.Scatterternary({
    'mode':'markers',
    'name': 'Joe Biden',
    'marker.size': df['Upvotes'],
    'marker.sizeref':0.0001,
    'a': df.loc[df['Topic'] == 'Joe Biden']['Relative Upvotes'],
    'b': df.loc[df['Topic'] == 'Joe Biden']['Relative Comments'],
    'c': df.loc[df['Topic'] == 'Joe Biden']['Relative Downvotes'],
    'text': df['Title'],
    'hoverinfo': ['name','a'],
    'marker': {
        'color': 'blue',
        'size': 14,
        'line': { 'width': 2 }
    }} )

trace_c = go.Scatterternary({
    'mode': 'markers',
    'name': 'Racial Justice Protests',
    'a': df.loc[df['Topic'] == 'Racial Justice Protests']['Relative Upvotes'],
    'b': df.loc[df['Topic'] == 'Racial Justice Protests']['Relative Comments'],
    'c': df.loc[df['Topic'] == 'Racial Justice Protests']['Relative Downvotes'],
    'text': df['Title'],
    'hoverinfo': ['name','a'],
    'marker': {
        'color': 'yellow',
        'size': 14,
        'line': { 'width': 2 }
    }} )

trace_d = go.Scatterternary({
    'mode': 'markers',
    'name': 'COVID-19',
    'a': df.loc[df['Topic'] == 'COVID-19']['Relative Upvotes'],
    'b': df.loc[df['Topic'] == 'COVID-19']['Relative Comments'],
    'c': df.loc[df['Topic'] == 'COVID-19']['Relative Downvotes'],
    'text': df['Title'],
    'hoverinfo': ['name','a'],
    'marker': {
        'color': 'black',
        'size': 14,
        'line': { 'width': 2 }
    }} )

trace_e = go.Scatterternary({
    'mode': 'markers',
    'name': 'The Economy',
    'a': df.loc[df['Topic'] == 'The Economy']['Relative Upvotes'],
    'b': df.loc[df['Topic'] == 'The Economy']['Relative Comments'],
    'c': df.loc[df['Topic'] == 'The Economy']['Relative Downvotes'],
    'text': df['Title'],
    'hoverinfo': ['name','a'],
    'marker': {
        'color': 'green',
        'size': 14,
        'line': { 'width': 2 }
    }} )

fig = go.Figure([trace_a,trace_b,trace_c,trace_d,trace_e])

def makeAxis(title, tickangle):
    return {
      'title': title,
      'titlefont': { 'size': 20 },
      'tickangle': tickangle,
      'tickfont': { 'size': 15 },
      'tickcolor': 'rgba(0,0,0,0)',
      'ticklen': 5,
      'showline': True,
      'showgrid': True
    }

fig.update_layout({
    'ternary': {
        'sum': 100,
        'aaxis': makeAxis('Upvotes', 0),
        'baxis': makeAxis('Comments', 45),
        'caxis': makeAxis('Downvotes', -45)
    },
    'annotations': [{
      'showarrow': False,
      'text': 'Plot',
        'x': 0.5,
        'y': 1.3,
        'font': { 'size': 15 }
    }]
})

scatterplot = px.scatter(
    data_frame = df,
    x = 'Downvotes',
    y= 'Comments',
    size = 'Upvotes',
    facet_col='Subreddit',
    marginal_x = 'violin',
    size_max = 10,
    color = 'Topic',
    color_discrete_map = {'Donald Trump':'red','Joe Biden':'blue','Racial Justice Protests':'yellow',
                          'The Economy':'green','COVID-19':'black'},
    hover_name = 'Title',
    hover_data = ['Upvotes','Comments','Downvotes'],
    labels={"Topic":"Post Topic"},
    title='Comment Interaction and Downvotes on Posts in r/news and r/politics',
    template='ggplot2', 
    )
   ''' 

fig.write_html("/Users/william/Desktop/Python Website/ternarythree.html")




