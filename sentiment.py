from nltk.sentiment.vader import SentimentIntensityAnalyzer

df_sentiment = df_english.copy()

# instantiate new SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

sentiment_scores = df_sentiment['text_english'].progress_apply(
                                                            sid.polarity_scores)
sentiment = sentiment_scores.apply(lambda x: x['compound'])
df_sentiment['sentiment'] = sentiment