from geopy.geocoders import Nominatim
from tqdm import tqdm

tqdm.pandas()

def geo_locator(user_location):
    
    # initialize geolocator
    geolocator = Nominatim(user_agent='Tweet_locator')

    if user_location is not None:
        try :
            # get location
            location = geolocator.geocode(user_location, language='en')
            # get coordinates
            location_exact = geolocator.reverse(
                        [location.latitude, location.longitude], language='en')
            # get country codes
            c_code = location_exact.raw['address']['country_code']

            return c_code

        except:
            return None

    else : 
        return None

# apply geo locator to user-location
loc = df_tweets['user-location'].progress_apply(geo_locator)
df_tweets['user-country_code'] = loc

# change codes to iso3 
df_tweets['user-country_code'] = \
                    df_tweets['user-country_code'].apply(to_iso3_func)

# create user-country column
df_tweets['user-country'] = \
                    df_tweets['user-country_code'].apply(to_std_func)

# drop old column
df_tweets.drop(['user-location'], axis=1, inplace=True)