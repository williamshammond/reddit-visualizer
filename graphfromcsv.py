#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:11:05 2020

@author: william
"""

import pandas as pd
import plotly.express as px


df = pd.read_csv('/Users/william/Desktop/Python Website/output1.csv')

fig = px.scatter_ternary(df, a="Upvotes", b="Comments", c="Downvotes", hover_name="Title", opacity = 0.7, color="Topic", size="Upvotes", size_max=9, title = 'Post reception within news Subreddits by category (2020)', color_discrete_map = {"Donald Trump": "darkred", "Joe Biden": "blue", "Racial Justice Protests":"orange","COVID-19":"black","The Economy":"green"} )

fig.write_html("/Users/william/Desktop/Python Website/secondtry.html")
