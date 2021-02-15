import tweepy
import random
import cards


CONSUMER_KEY = '44X3mgoSsAinnLVA6IOTl4n3e'
CONSUMER_SECRET = 'V4F99ZGZibM5hd1qp5GsyjesVkLJzeYzyD3nuK7Tmads1iBd8q'
ACCESS_KEY = '1358837739098165249-n5rb14wYhHT30i8DXA80IqyMdJq2lh'
ACCESS_SECRET = 'P5MK3LjvCn00XpVeu1v0Y3tcyJG3tyqVL7qM56K8iyLiz'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Random variables
num_pos = random.randint(0,13)
suit_pos = random.randint(0,3)
major_pos = random.randint(0, 21)

try:
  # Verify connection to API
  api.verify_credentials()
  print("Authentication OK")
  # Randomize chance of major and minor arcana
  card_chosen = random.randint(0,77)
  if (card_chosen <= 21): # Major arcana
    api.update_status("✨\n" + cards.major[major_pos] + "\n✨" + "\n\nKeywords: " + cards.major_desc[major_pos])
  else: # Minor arcana
    api.update_status("✨\n" + cards.numbers[num_pos] + " of " + cards.suits[suit_pos] + "\n✨" + "\n\nKeywords: " + cards.minor_desc[suit_pos][num_pos])
except:
  print("Error during authentication")
