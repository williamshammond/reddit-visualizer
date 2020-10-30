import praw
reddit = praw.Reddit(client_id="h6wy01n0-8H86A", client_secret="gezsDAlid5PVXPt6ug_nyqO2XKg2Lw",
                     password="Redditpassword2033!", user_agent="macOS:myRedditVisualizer:v1.0(by u/whammmond)",
                     username="whammmond")
# Output score for the first 256 items on the frontpage
# Output score for the first 256 items on the frontpage
for submission in reddit.front.hot(limit=256):
    print(submission.score)
