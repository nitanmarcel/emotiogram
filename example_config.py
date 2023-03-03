# Make a copy to config.py before editing. (Do not edit this example_config.py)

# OpenAI api key from https://platform.openai.com/account/api-keys
OPENAI_TOKEN = ''

# Telegram api id and hash
API_ID = 0
API_HASH = ''

# after how many messages the bot will try to detect the emotion.
MESSAGES_COUNT = 1

# dict of known emotions and specific telegram animated emoji document id
emotions = {'anger': 5237765359670404869,
            'anxiety': 5199628386544132862,
            'compassion': 5240158644296753897,
            'confusion': 5230982773086365287,
            'contentment': 5267071038222509469,
            'disappointment': 5204036010832307295,
            'disgust': 5424632746699924204,
            'embarrassment': 5231010832107708935,
            'envy': 5409129508194229502,
            'excitement': 5267071038222509469,
            'fear': 5434111653622850347,
            'frustration': 5231115466100975063,
            'guilt': 5197506689879778001,
            'happiness': 5431388747436400105,
            'hope': 5445103656049322797,
            'humiliation': 5231010832107708935,
            'hurt': 5193030028287287905,
            'jealousy': 5434111653622850347,
            'joy': 5431388747436400105,
            'loneliness': 5195463707081056014,
            'love': 5445335816211538344,
            'nostalgia': 5193030028287287905,
            'regret': 5258483856704544199,
            'sadness': 5195463707081056014,
            'shame': 5274108127388640086,
            'surprise': 5434111653622850347}

# default emotion to use when the posible emotion given by the message can't be identified
default_emotion = 5409131999275262353
