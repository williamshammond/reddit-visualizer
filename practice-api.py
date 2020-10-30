import requests
import time
import pandas as pd

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
    'cookie': 'reddaid=WWF4ZE75Z7G5SAIA; csv=1; edgebucket=WwM5Lz0BL4fMj6QQjD; __gads=ID=a779a8dbc16b17aa:T=1600274260:S=ALNI_MZtEqvgpBzx1HXfJZSKhlWMxcTl6Q; G_ENABLED_IDPS=google; pc=54; __aaxsc=2; g_state={"i_s":1,"i_l":0}; loid=0000000000000wodm0.2.1459041671000.Z0FBQUFBQmZtMXlTUzZFQm5ZTU0xZHpsajVhY1kxQmtoZmJKaE0zbmRxVFkzSy03Ujk1MnRJMk84QUx4QkJ2cS1kVEtjVlFIS1NZR1pDZ3JWeFlLbTNCV056RDRDaHAyV1dCV2JSbVlPNVRsUmZsMGZCc3pvYUtCQW84VTdEclllakt1R2lXckhqWi0; reddit_session=54885096%2C2020-10-30T16%3A47%3A57%2Cc6b29b72762f962929249e661c3d1737dcc8ddfa; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDQwODAxNTcsInN1YiI6IjU0ODg1MDk2LXYxVzI0czQ5dmRDaWZFZFI5QUdrNUxKZExKTSIsImxvZ2dlZEluIjp0cnVlLCJzY29wZXMiOlsiKiIsImVtYWlsIl19.sQvKycNu_ybO_-9EBwu9Stu1daFCiknqBks1T0r2Zfo; whammmond_recentclicks2=t3_jkmd7k%2Ct3_jkv112%2Ct3_jkv294%2Ct3_jkw16s%2Ct3_jkzc17; d2_token=3.761b2f1ab78e2080fcb13d1c7b65f98bea0c02e9807d92b08dfb36fb4bdabc84.eyJhY2Nlc3NUb2tlbiI6IjU0ODg1MDk2LWo5THRSbW1TWVpUbDlPeUtnMGN2TVh3WFJkdyIsImV4cGlyZXMiOiIyMDIwLTEwLTMwVDE4OjAyOjMwLjAwMFoiLCJsb2dnZWRPdXQiOmZhbHNlLCJzY29wZXMiOlsiKiIsImVtYWlsIl19; recent_srs=t5_2qh0y%2Ct5_2qhv6%2Ct5_2qj0l%2Ct5_2qig3%2Ct5_2qh23%2Ct5_2qhj4%2Ct5_2tk95%2Ct5_2qizd%2Ct5_2sptq%2Ct5_318ly; session=137c0a5e67a982ea74160ce4de52a8959838eb59gASVSQAAAAAAAABKYEecX0dB1+bPfY0Sa32UjAdfY3NyZnRflIwoZmZmODkzYWEzOTQ0OWNhZTM5OGZlMjRiYmQyMmYyYWZiMDU2YTlhOJRzh5Qu; aasd=2%7C1604077389991; session_tracker=BPFVYIolns9VbsxGIc.0.1604077438360.Z0FBQUFBQmZuRWQtN01HT1ZnaWJWUDhjUHMtX18yY2R3WnRiUUQ1VW5WTzFiMkU1TTJHUFhCREZ1SVhTQl9OcE9qbGQ5X0ZaQ3lJQ0VuVV96VnhwSEdHVlN6a3pJT25LRktQb1oyVUJ0MUM3QVhqRTBFcjVmaEtuUUlzekUtd05fUVhqaEJobWxHelc',
}
def get_mods(subreddit):
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about/moderators.json', headers=headers)
    json_response = response.json()
    mods = [{'subreddit':subreddit,'mod':item['name']} for item in json_response['data']['children'] if item['name']!='AutoModerator']
    return(mods)
    

def get_comments(user):
    after = None
    all_user_activity = []
    for _ in range(4):
        print("I am running")
        if after==None:
            url = f'https://www.reddit.com/user/{user}.json'
        else:
            url = f'https://www.reddit.com/user/{user}.json?after={after}'
        response = requests.get(url, headers=headers)
        after = response.json()['data']['after']
        #user_activity = [{'user':user,'activity_utc':int(item['data']['created_utc'])} for item in response.json()['data']['children']]
        for item in response.json()['data']['children']:
            utc_time = int(item['data']['created_utc'])
            
            user_activity = {'user': user,
                             'activity_utc': utc_time,
                             'activity_date': time.strftime("%Y-%m-%d",time.gmtime(utc_time)),
                             'activity_hour': time.strftime("%H",time.gmtime(utc_time))}
            all_user_activity.append(user_activity)
    return all_user_activity
    #print(len(all_user_activity))
    
#print(get_mods('learnprogramming'))

def get_comments_from_mods(subreddit):
    mods = get_mods(subreddit)
    all_activity = []
    for mod in mods:
        try:
            one_mod_activity = get_comments(mod['mod'])
            all_activity.extend(one_mod_activity)
        except:
            continue
    return all_activity    

df = pd.DataFrame(get_comments_from_mods('Python'))
df.to_csv('output1.csv', index=0)
        
