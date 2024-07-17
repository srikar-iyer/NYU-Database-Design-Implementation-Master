import pandas as pd

df = pd.DataFrame(pd.read_csv("data/listings.csv"))
df_clean = df.drop(columns=['neighbourhood', 'source', 'bathrooms', 'host_about', 'host_location', 'neighbourhood_cleansed', 'listing_url', 'host_response_rate', 'host_acceptance_rate', 'scrape_id', 'last_scraped', 'description', 'neighborhood_overview', 'picture_url', 'host_url', 'host_since', 'host_response_time', 'host_thumbnail_url', 'host_picture_url', 'host_verifications', 'host_has_profile_pic', 'host_identity_verified', 'latitude', 'longitude'])
df_clean = df_clean.drop(columns=['property_type', 'host_neighbourhood', 'room_type', 'accommodates', 'bathrooms_text', 'bedrooms', 'amenities', 'minimum_nights', 'maximum_nights'])
df_clean = df_clean.drop(columns=['maximum_minimum_nights','minimum_minimum_nights','minimum_maximum_nights','maximum_maximum_nights','minimum_nights_avg_ntm','maximum_nights_avg_ntm','calendar_updated','has_availability','availability_30','availability_60','availability_90','availability_365','calendar_last_scraped','number_of_reviews','number_of_reviews_ltm','number_of_reviews_l30d','host_total_listings_count','first_review','last_review','review_scores_accuracy','review_scores_cleanliness','review_scores_checkin','review_scores_communication','review_scores_location','review_scores_value','license','instant_bookable','calculated_host_listings_count','calculated_host_listings_count_entire_homes','calculated_host_listings_count_private_rooms','calculated_host_listings_count_shared_rooms','reviews_per_month'])
df_clean['review_scores_rating']=df_clean['review_scores_rating'].fillna(0)
df_clean['beds']=df_clean['beds'].fillna(0)
df_clean.to_csv("data/listings_clean.csv")

