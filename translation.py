import numpy as np

# select only not-null tweets not in English
mask1 = df_tweets['text'].notnull()
mask2 = df_tweets['language'] != 'English'
df_masked = df_tweets[(mask1) & (mask2)]

# split dataframe in x equal-size pieces
df_tweets_splitted = np.array_split(df_masked, 150)

def tweet_translation(df, idx):
    
    """ Translate tweets using googletrans """
    
    from googletrans import Translator
    
    translator = Translator()
    
    try:
        # translate raw tweet
        trans = df['text'].apply(translator.translate, dest='en')
        # create column extracting the translated text
        df['text_english'] = trans.apply(lambda x: x.text)
        # append to empty list
        translations.append(df)
        # save data in case error happens
        df.to_csv('Translations/translation_{}.csv'.format(idx))
   
    except Exception as e:  
        print(e, ' -- at index ', idx)
        
translations = []
for idx, df in enumerate(tqdm(df_tweets_splitted)):
    tqdm._instances.clear()
    tweet_translation(df, idx)
    
# concatenate the chunks into a single dataframe
df_translations = pd.concat(translations)
# join it with the old one
df_english = df_tweets.join(df_translations['text_english'])