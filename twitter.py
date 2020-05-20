# frequently used libraries
import tweepy
import json
import mysql.connector
from mysql.connector import Error


def connect(username, time, tweet, retweets, place, location):
    """
    connect to MySQL database and insert twitter data
    """
    try:
        con = mysql.connector.connect(host='localhost', username='twitter', password='root')

        if con.is_connected():
            cursor = con.cursor()
            query = 'insert into (username, time, tweet, retweets, place, location) values (%s, %s, %s, %s, %s, %s)'
            cursor.execute(query, (username, time, tweet, retweets, place, location))
            con.commit()

    except Error as e:
        print(e)

    cursor.close()
    con.close()

    return


class stream_listner(tweepy.StreamListener):
    """
    python class to access twitter API
    """    
    
    def on_connect(self):
        """
        show connection status
        """  
        print('You are connected to the Twitter API')

    def on_error(self):
        """
        throw error if status code is not 200
        """
        if status_code != 200:
            print('error found')
            return False


    def on_data(self, data):
        """
        read tweets from twitter API and insert into MySQL database
        """
        try:
            # read JSON data from twitter API
            raw_data = json.loads(data)

            # extract desired information from JSON data
            if 'text' in raw_data:
				username = raw_data['user']['screen_name']
				created_at = parser.parse(raw_data['created_at'])
				tweet = raw_data['text']
				retweet_count = raw_data['retweet_count']

				if raw_data['place'] is not None:
					place = raw_data['place']['country']
					print(place)
				else:
					place = None
				

				location = raw_data['user']['location']

                # insert information into MySQL database
                connect(username, time, tweet, retweets, place, location)
                print('Tweet collected at: {}'.format(str(created_at)))


        except Error as e:
            print(e)


if __name__=='__main__':
    
    # twitter authentication for accessing tweets 
    consumer_key = 'Z7P7gYSpzvnibvhLV56FQqhPa'
    consumer_secret = 'PLEi9WvcAi3P58ZSV2odeZrlz9JmLrhYOZuYD6t8N5x2Xhkq6X'
    access_token = '1003553168557510656-N1dSDC1oYmu3n9vwnLGMCuFy5sNu4V'
    token_secret = 'of5o0HeV4R9GnUTEpCuSFeeATrWhGWsoYL5paOADZlt6B'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # twitter stream with desired word filter
    listner = stream_listner(api=api)
    stream = tweepy.Stream(auth, listener=listener)
    track = ['gold', 'masters', 'reed', 'mcilroy', 'woods']
    stream.filter(track=track, languages='en')


