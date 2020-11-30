def select_text(tweets):
    ''' Assigns the main text to only one column depending
        on whether the tweet is a RT/quote or not'''
    
    tweets_list = []
    
    # Iterate through each tweet
    for tweet_obj in tweets:
        
        if 'retweeted_status-extended_tweet-full_text' in tweet_obj:
            tweet_obj['text'] = \
                        tweet_obj['retweeted_status-extended_tweet-full_text']
        
        elif 'retweeted_status-text' in tweet_obj:
            tweet_obj['text'] = tweet_obj['retweeted_status-text']
            
        elif 'extended_tweet-full_text' in tweet_obj:
                    tweet_obj['text'] = tweet_obj['extended_tweet-full_text']
                
        tweets_list.append(tweet_obj)
        
    return tweets_list