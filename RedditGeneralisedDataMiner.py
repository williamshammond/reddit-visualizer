import requests
import time 
import pandas as pd
import random


requesting_subreddit = # enter subreddit name here 'soccer'


base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': 'whammmond', 'password': 'Redditpassword2033!'}
auth = requests.auth.HTTPBasicAuth('h6wy01n0-8H86A', 'gezsDAlid5PVXPt6ug_nyqO2XKg2Lw')
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'MacOS:reddit-visualizer:v1.0 (by /u/whammmond)'},
                  auth=auth)
d = r.json()
token_auth = 'bearer ' + d['access_token']



def request_new_posts(subreddit,token,after):

    base_url = 'https://oauth.reddit.com'
    
    headers = {'Authorization': str(token_auth), 'User-Agent': 'MacOS:reddit-visualizer:v1.0 (by /u/whammmond)'}
    payload = {'limit' : '100', 'show':'all','t':'year','after':f'{after}'}
    response = requests.get(base_url + f'/r/{subreddit}/top', headers=headers, params=payload)
    
    if response.status_code == 200:
        response_json = response.json()
        return response_json

def post_data_formatted(subreddit, response):
    posts = response['data']['children']

    post_data = []
    
    for i in range(len(posts)):
        post_title = posts[i]['data']['title'].casefold()
      
        post_data.append({'Subreddit':f'{subreddit}',
                          'Title':posts[i]['data']['title'],
                          'Epoch Time':posts[i]['data']['created_utc'],
                          'Date': time.strftime("%m/%d/%Y, %H:%M:%S", time.gmtime(posts[i]['data']['created_utc'])),
                          'Comments':posts[i]['data']['num_comments'],
                          'Awards':posts[i]['data']['total_awards_received'],
                          'Upvotes':posts[i]['data']['ups'],
                          'Downvotes':(posts[i]['data']['ups']/(posts[i]['data']['upvote_ratio']+random.uniform(-0.005, 0.005)))-posts[i]['data']['ups'],
                          'Upvote Ratio':posts[i]['data']['upvote_ratio'], 
                          'Uvpote/Comment Ratio':((posts[i]['data']['ups']/posts[i]['data']['num_comments'])),
                          'Comment/Upvote Ratio':(posts[i]['data']['num_comments']/(posts[i]['data']['ups'])),
                         })                         
    return post_data

big_list = []
def make_request(subreddit_name):
    
    

    token = 'beaker'
    response = request_new_posts(subreddit_name,str(token_auth),'None')
    big_list.extend(post_data_formatted(subreddit_name,response))
    print("Working")
    while(response['data']['after']!=None):
      response = request_new_posts(subreddit_name,str(token_auth),response['data']['after'])
      print(response['data']['after'])
      big_list.extend(post_data_formatted(subreddit_name,response))


make_request(requesting_subreddit)
output = pd.DataFrame(big_list)

file_name = requesting_subreddit + '.csv'
output.to_csv(file_name)