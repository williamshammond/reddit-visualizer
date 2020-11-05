import requests

headers = {
    'authority': 'www.reddit.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'reddaid=WWF4ZE75Z7G5SAIA; csv=1; edgebucket=WwM5Lz0BL4fMj6QQjD; __gads=ID=a779a8dbc16b17aa:T=1600274260:S=ALNI_MZtEqvgpBzx1HXfJZSKhlWMxcTl6Q; G_ENABLED_IDPS=google; pc=54; __aaxsc=2; g_state={"i_s":1,"i_l":0}; loid=0000000000000wodm0.2.1459041671000.Z0FBQUFBQmZtMXlTUzZFQm5ZTU0xZHpsajVhY1kxQmtoZmJKaE0zbmRxVFkzSy03Ujk1MnRJMk84QUx4QkJ2cS1kVEtjVlFIS1NZR1pDZ3JWeFlLbTNCV056RDRDaHAyV1dCV2JSbVlPNVRsUmZsMGZCc3pvYUtCQW84VTdEclllakt1R2lXckhqWi0; reddit_session=54885096%2C2020-10-30T16%3A47%3A57%2Cc6b29b72762f962929249e661c3d1737dcc8ddfa; whammmond_recentclicks2=t3_jkv294%2Ct3_jkw16s%2Ct3_jkzc17%2Ct3_jkwslm%2Ct3_jkzcms; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDQwOTAzMzYsInN1YiI6IjU0ODg1MDk2LTQ3M2JENDVjRkQ0eWlrOEc5aXBsNEZldXQ4cyIsImxvZ2dlZEluIjp0cnVlLCJzY29wZXMiOlsiKiIsImVtYWlsIl19.69AYauEYXdWXf7UaEchtiK69kVCPZOSDN1gLKf1O_6g; d2_token=3.bcb0ffe8fbc086dc8fdce2ddd07d0066b002437f2aefeb546c4c3672a7ad5937.eyJhY2Nlc3NUb2tlbiI6IjU0ODg1MDk2LVRoSm5KelJFU0tGSWpRMVhtTUpfMDRVUWd5QSIsImV4cGlyZXMiOiIyMDIwLTEwLTMwVDIwOjU0OjQ2LjAwMFoiLCJsb2dnZWRPdXQiOmZhbHNlLCJzY29wZXMiOlsiKiIsImVtYWlsIl19; recent_srs=t5_2qh3l%2Ct5_2qi58%2Ct5_2qqjc%2Ct5_2qh0y%2Ct5_2qhv6%2Ct5_2qj0l%2Ct5_2qig3%2Ct5_2qh23%2Ct5_2qhj4%2Ct5_2tk95; session=7d92179e8e75b4e6958e13a6510c295de99e67bcgASVSQAAAAAAAABKD3OcX0dB1+bPfY0Sa32UjAdfY3NyZnRflIwoOTY0Y2E2OWVhMDRjMzExNWIwZGMwNzk4N2I2Njg3ODU0Yjk0NWIyYpRzh5Qu; aasd=3%7C1604087751802; session_tracker=BZ8t0qxwmji6HBhPuZ.0.1604088731972.Z0FBQUFBQmZuSE9jVElGR01YSl9Mc2RSdUZxck0xaU5rNS1ENHlBVzhoVWo5VVVPcXJnOXVXd2pDQk1DdXBuOWVQaFVfam9kTElvSEw1c3pWdDlZd0hwRGZUYkhCWV9SUjlCb01KazBFVV9Semo0Ykd0dTVPTWZnUEMxUG5heEhYdFVsRTNWVzlYWVM',
}

def get_top_posts(subreddit):
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/top.json', headers=headers)
    response_json = response.json()
    top_posts = []
    for x in range(len(response_json['data']['children'])):
        post_link = response_json['data']['children'][x]['data']['permalink']
        top_posts.append(post_link)
    return top_posts
    
def get_comments(post_link):
    response = requests.get(f'https://www.reddit.com{post_link}.json', headers=headers)
    response_json = response.json()
    all_comments = response_json[1]['data']['children']
    all_text = []
    for i in range(len(all_comments)):
      comment_text = all_comments[i]['data']['body']
      all_text.append(comment_text)
    return all_text
    
def get_comments_with_thanks(post_link):
    response = requests.get(f'https://www.reddit.com/{post_link}.json', headers=headers)
    response_json = response.json()
    all_comments = response_json[1]['data']['children']
    all_text = []
    for i in range(len(all_comments)):
      comment_text = all_comments[i]['data']['body']
      if('thank' in comment_text.lower()):
          all_text.append(comment_text)
    return all_text



#get_comments('/r/Python/comments/jii8ex/i_teach_python_courses_heres_my_collection_of/')
top_post = get_top_posts('soccer')[0]
print(get_comments(top_post))
'''post_comments = get_comments(get_top_posts('soccer')[0])
print(post_comments)
print(len(post_comments))
print("---------------------------------------")
post_comments_thanks = get_comments_with_thanks(get_top_posts('soccer')[0])
print(post_comments_thanks)
print(len(post_comments_thanks))
'''
