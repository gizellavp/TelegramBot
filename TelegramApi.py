from telethon import TelegramClient

api_id = 6525343
api_hash = '079addf936300612e8b065bd8b7163da'
client = TelegramClient('anon', api_id, api_hash)

async def main():


    # You can send messages to yourself...
    await client.send_message('me', 'Hello, myself!')
   
    # ...or even to any username
    #await client.send_message('+6285334898142', 'Hallo Mbk Enno!')



with client:
    client.loop.run_until_complete(main())
