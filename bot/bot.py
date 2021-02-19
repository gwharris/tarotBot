import tweepy
import random
import cards

# Keys needed to connect to Twitter API
CONSUMER_KEY = '44X3mgoSsAinnLVA6IOTl4n3e'
CONSUMER_SECRET = 'V4F99ZGZibM5hd1qp5GsyjesVkLJzeYzyD3nuK7Tmads1iBd8q'
ACCESS_KEY = '1358837739098165249-n5rb14wYhHT30i8DXA80IqyMdJq2lh'
ACCESS_SECRET = 'P5MK3LjvCn00XpVeu1v0Y3tcyJG3tyqVL7qM56K8iyLiz'

# Use Tweepy to tweet
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Randomize the cards (if it's a suit card)
num_pos = random.randint(0,13)
suit_pos = random.randint(0,3)

try:
  # Verify connection to API
  api.verify_credentials()
  print("Authentication OK")
  # Randomize chance of major and minor arcana
  card_chosen = random.randint(0,77)
  if (card_chosen <= 21): # Major arcana
    api.update_status("✨\n" + cards.major[card_chosen] + "\n✨" + "\n\nKeywords: " + cards.major_desc[card_chosen])
  else: # Minor arcana
    api.update_status("✨\n" + cards.numbers[num_pos] + " of " + cards.suits[suit_pos] + "\n✨" + "\n\nKeywords: " + cards.minor_desc[suit_pos][num_pos])
except:
  print("Error during authentication")
