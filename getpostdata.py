#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:28:26 2020

@author: william
"""

import requests
import pandas as pd

def get_new_authentication():
    base_url = 'https://www.reddit.com/'
    data = {'grant_type': 'password', 'username': 'whammmond', 'password': 'Redditpassword2033!'}
    auth = requests.auth.HTTPBasicAuth('h6wy01n0-8H86A', 'gezsDAlid5PVXPt6ug_nyqO2XKg2Lw')
    r = requests.post(base_url + 'api/v1/access_token',
                      data=data,
                      headers={'user-agent': 'MacOS:reddit-visualizer:v1.0 (by /u/whammmond)'},
    		  auth=auth)
    d = r.json()
    token = 'bearer ' + d['access_token']
    print(token)
    return token
    
def request_new_posts(token,after):

    base_url = 'https://oauth.reddit.com'
    
    headers = {'Authorization': token, 'User-Agent': 'MacOS:reddit-visualizer:v1.0 (by /u/whammmond)'}
    subreddit = 'news'
    
    payload = {'limit' : '100', 'show':'all','t':'year','after':f'{after}'}
    response = requests.get(base_url + f'/r/{subreddit}/top', headers=headers, params=payload)
    
    if response.status_code == 200:
        response_json = response.json()
        return response_json

def add_post_data(response):
    posts = response['data']['children']

    post_data = []
    
    corona_keys = ['corona', 'covid', '-19', 'pandemic']
    trump_keys = ['trump', 'donald']
    biden_keys = ['biden', 'joseph r']
    racial_justice_keys = ['george floyd', 'black lives','blacklives','blm','racial justice','defund the police','police reform']
    economy_keys = ['the fed','stimulus','economy','unemployment','small business','federal reserve','economic']
    for i in range(len(posts)):
      post_title = posts[i]['data']['title'].casefold()
      if any(c in post_title for c in corona_keys):
        post_data.append({'Topic': 'COVID-19','Title':posts[i]['data']['title'],'Comments':posts[i]['data']['num_comments'],'Upvotes':posts[i]['data']['ups'],'Upvote Ratio':posts[i]['data']['upvote_ratio']})
      if any(c in post_title for c in trump_keys):
        post_data.append({'Topic': 'Donald Trump','Title':posts[i]['data']['title'],'Comments':posts[i]['data']['num_comments'],'Upvotes':posts[i]['data']['ups'],'Upvote Ratio':posts[i]['data']['upvote_ratio']})
      if any(c in post_title for c in biden_keys):
        post_data.append({'Topic': 'Joe Biden','Title':posts[i]['data']['title'],'Comments':posts[i]['data']['num_comments'],'Upvotes':posts[i]['data']['ups'],'Upvote Ratio':posts[i]['data']['upvote_ratio']})
      if any(c in post_title for c in racial_justice_keys):
        post_data.append({'Topic': 'Racial Justice Protests','Title':posts[i]['data']['title'],'Comments':posts[i]['data']['num_comments'],'Upvotes':posts[i]['data']['ups'],'Upvote Ratio':posts[i]['data']['upvote_ratio']})
      if any(c in post_title for c in economy_keys):
        post_data.append({'Topic': 'The Economy','Title':posts[i]['data']['title'],'Comments':posts[i]['data']['num_comments'],'Upvotes':posts[i]['data']['ups'],'Upvote Ratio':posts[i]['data']['upvote_ratio']})  
    return post_data


def get_four_posts_data(token):
    big_list = []
    response = request_new_posts(token,'None')
    big_list.extend(add_post_data(response))
    while(response['data']['after']!=None):
        response = request_new_posts(token,response['data']['after'])
        print(response['data']['after'])
        big_list.extend(add_post_data(response))
    return big_list

    
authentication = get_new_authentication()
#authentication = 'bearer 54885096-3WsI-NT6p3EoLCFU_kUjCMBukGv1Iw'
print(get_four_posts_data(authentication))

dataframe = pd.DataFrame()

    
