import pip
pip install snscrape
pip install streamlit
import snscrape
import streamlit as st
import pandas as pd
import numpy as np
import json

#Creating Title for the GUI
st.title('Twitter Scraping')

import snscrape.modules.twitter as sntwitter


def scraping(Search,Limit):
    # Creating list to append tweet data 
    tweetlist = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(Search).get_items()): #declare a username 
        if i>Limit: #number of tweets you want to scrape
            break
        tweetlist.append([tweet.date, tweet.id, tweet.url,tweet.user.username, tweet.content, tweet.replyCount, 
                        tweet.retweetCount, tweet.likeCount, tweet.lang, tweet.user.location, tweet.sourceLabel]) #declare the attributes to be returned
    # Creating a dataframe from the tweets list above 
    df_scrape= pd.DataFrame(tweetlist, columns=['Datetime', 'Tweet Id', 'Url', 'Username','Text','Num Of Reply', 
                                                'Num Of Retweet','Num Of Like' ,'Language','Location', 'Source'])
   
    

    return df_scrape

# IMPORTANT: Cache the conversion to prevent computation on every rerun
@st.cache
#Converting file to json
def json_records(df):
    return df.to_json(orient ='records')
#Converting file to csv
def convert_df(df):
    
    return df.to_csv().encode('utf-8')


    
#Creating a form for the GUI to input data to search
with st.form(key='Twitter_Form'):
	search_term=st.text_input('Enter keyword/hastag to search')
	limit= st.slider('How mant tweets do you want to get?',0,1000,step=10)
	sfile_name=st.text_input('Name your CSV file:',max_chars=10)
	submitted=st.form_submit_button("Submit")
	
	
	
	if submitted:
		scraping(search_term,limit)

#Used to show data scraped
st.table(scraping(search_term,limit))

#Assingning converted file to their assign variable
csv = convert_df(scraping(search_term,limit))
jSon = json_records(scraping(search_term,limit))		

#Adding download button to GUI
st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name=sfile_name,
        mime='text/csv',
    )		

st.download_button(
    "Download as jsonl",
    data=jSon,
    file_name="output.json",
    mime="application/jsonl",
)
