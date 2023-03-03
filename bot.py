import aiohttp
import telethon
import rpunct

import asyncio
import re
import logging

from config import API_HASH, API_ID, OPENAI_TOKEN, emotions, default_emotion, MESSAGES_COUNT

logging.basicConfig(level=logging.INFO)

rpunct = rpunct.RestorePuncts()


async def openai_emotion(text):
    query = 'What\'s the most likely sentiment emotion the writter of the following text felt when writing it?\n%s' % (
        rpunct.punctuate(text, lang='en'))
    url = 'https://api.openai.com/v1/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % OPENAI_TOKEN
    }
    payload = {
        'model': 'text-davinci-003',
        'prompt': query,
        'temperature': 0,
        'max_tokens': 256,
        'top_p': 0,
        'frequency_penalty': 2.0,
        'presence_penalty': 2.0
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, json=payload) as r:
            if r.status == 200:
                response = await r.json()
                text = response['choices'][0]['text'].split()[-1]
                return re.sub(r'[^a-zA-Z]+|\n', '', text).lower()

last_emotion_id = 0
messages_counter = 1
messages = ''

async def main():
    client = telethon.TelegramClient(
        "emotiogram", api_id=API_ID, api_hash=API_HASH)
    async with client:
        @client.on(telethon.events.NewMessage(outgoing=True, incoming=False))
        async def emotiogram(event):
            global last_emotion_id, messages_counter, messages
            if event.text and not event.text.startswith('.howami'):
                if messages_counter < MESSAGES_COUNT:
                    messages += '\n%s' + event.text
                    messages_counter += 1
                    return
                emotion = await openai_emotion(messages or event.text)
                logging.info('Text: %s' % event.text)
                logging.info('Emotion: %s' % emotion)
                if emotion in emotions.keys():
                    emotion_emoji_id = emotions[emotion]
                else:
                    emotion_emoji_id = default_emotion
                if last_emotion_id != emotion_emoji_id:
                    await client(telethon.tl.functions.account.UpdateEmojiStatusRequest(
                        emoji_status=telethon.tl.types.EmojiStatus(
                            document_id=emotion_emoji_id)
                    ))
                    last_emotion_id = emotion_emoji_id
                    messages_counter = 0
                    messages = ''

        @client.on(telethon.events.NewMessage(outgoing=True, incoming=False, pattern=r'^\.howami'))
        async def howami(event):
            feelings = []
            emoji = (await client.get_me()).emoji_status
            if not isinstance(emoji, telethon.tl.types.EmojiStatusEmpty):
                emoji_id = emoji.document_id
                for k, v in emotions.items():
                    if v == emoji_id:
                        feelings.append(k)
            if len(feelings) > 0:
                await event.edit('I have a feeling of %s' % (', '.join(feelings)))
            else:
                await event.edit('I have no idea how I\'m feeling')
        await client.run_until_disconnected()

asyncio.run(main())
