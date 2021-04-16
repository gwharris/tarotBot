"""
bot.py
Written by Graham Harris. 
A simple twitter bot that reads out a daily tarot card.
"""

import tweepy
import random
import cards

# Keys needed to connect to Twitter API
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# Use Tweepy to tweet
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

try:
  # Verify connection to API
  api.verify_credentials()
  print("Authentication OK")

  # Randomize chance of major and minor arcana
  card_chosen = random.randint(0,77)
  # Hashtags to add
  hashtags = "\n#tarot #bot"

  # Find info about card chosen
  if (card_chosen <= 21):
    print("Major")
    card = "✨" + cards.major[card_chosen] + "✨"
    keywords = "\n\nKeywords: " + cards.major_desc[card_chosen]
  else: 
    print("Minor")
    # Randomize suit card
    num_pos = random.randint(0,13)
    suit_pos = random.randint(0,3)
    card = "✨" + cards.numbers[num_pos] + " of " + cards.suits[suit_pos] + "✨"
    keywords = "\n\nKeywords: " + cards.minor_desc[suit_pos][num_pos]
    
  # Tweet card info
  api.update_status(card + keywords + hashtags)

except:
  print("Error during program")
