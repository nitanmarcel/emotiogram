# EMOTIOGRAM

Telegram UserBot to change user's status to exprime a possible emotion detected in the messages he sents.

Written with:
- `telethon` a python library to communicate with telegram)
- `aiohttp` async request library used in this case to communicate with OpenAI API to detect emotions. (Was best free solution available.)
- `rpunct` used to correct the punctuation of a message to make OpenAI responses more reliable.