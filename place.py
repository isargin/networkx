import country_converter as coco

# change codes to iso3 
to_iso3_func = lambda x: coco.convert(names=x, to='iso3', not_found=None) \
                            if x is not None else x

df_tweets['place-country_code'] = \
                   df_tweets['place-country_code'].apply(to_iso3_func)

# change name to standard name
to_std_func = lambda x: coco.convert(names=x, to='name_short', not_found=None) \
                            if x is not None else x

df_tweets['place-country'] = \
                        df_tweets['place-country'].apply(to_std_func)