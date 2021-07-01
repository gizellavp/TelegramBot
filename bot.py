from telethon import TelegramClient, events

bot = TelegramClient('bot', 6525343, '079addf936300612e8b065bd8b7163da').start(bot_token='1885975783:AAHnYYfwO3gkeu8QLH4gtdXi7qcoNWK8Z4M')

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('Hi! I am BOT! \n'
                        'gunakan /help untuk melihat command')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/help'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('ini halaman help! \n'
                        '/start - untuk memulai bot \n'
                        '/help - untuk bantuan command bot\n'
                        '/uploadImage - untuk upload gambar\n'
                        '/downloadPdf - untuk Download PDF \n')
    raise events.StopPropagation

@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message."""
    await event.respond(event.text)

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()

