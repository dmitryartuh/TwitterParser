import tweepy
import pandas as pd
import datetime

# Twitter API credentials (replace with your own keys)
BEARER_TOKEN = "your_bearer_token"

# Authenticate with Twitter API
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_following(user_id):
    """Get a list of user IDs that the given user follows."""
    following = []
    for response in tweepy.Paginator(client.get_users_following, id=user_id, max_results=1000):
        following.extend(response.data)
    return [user.id for user in following if user]

def get_tweets_from_following(following_ids, start_time):
    """Fetch tweets from accounts followed by the user in the last 24 hours."""
    tweets_data = []
    for user_id in following_ids:
        try:
            tweets = client.get_users_tweets(id=user_id, start_time=start_time, tweet_fields=["created_at", "text"])
            if tweets.data:
                for tweet in tweets.data:
                    tweets_data.append([tweet.id, user_id, tweet.created_at, tweet.text])
        except Exception as e:
            print(f"Error fetching tweets for user {user_id}: {e}")
    return tweets_data

def main():
    # Get authenticated user ID
    user = client.get_me()
    user_id = user.data.id

    # Get accounts the user follows
    following_ids = get_following(user_id)

    # Get tweets from the last 24 hours
    start_time = (datetime.datetime.utcnow() - datetime.timedelta(days=1)).isoformat() + "Z"
    tweets_data = get_tweets_from_following(following_ids, start_time)

    # Save tweets to CSV
    df = pd.DataFrame(tweets_data, columns=["Tweet_ID", "User_ID", "Created_At", "Text"])
    df.to_csv("tweets_last_24h.csv", index=False)
    print("Tweets saved to tweets_last_24h.csv")

if __name__ == "__main__":
    main()
