import telegram
from telegram.ext import *
import gspread
import gspread_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import dataframe_image as dfi

bot = telegram.Bot('1859300275:AAH_RhUCS7hySa5Wu9_JArC7SrTu7xuMbTU', 6525343, '079addf936300612e8b065bd8b7163da')

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("testapi.json", scope)
gc = gspread.authorize(creds)
wk = gc.open('Data').sheet1
data = wk.get_all_records()
df = pd.DataFrame(data) 


def chart():
    df = pd.DataFrame(data) 
    x = df['Nama'].tolist()
    y = df['Usia'].tolist()
    plt.xlabel('Nama')
    plt.ylabel('Usia')
    plt.title('Laporan')
    #plt.legend()
    plt.plot(x,y, color='k', linestyle='--')
    plt.savefig('chart.png')
    
def chartImage(update, context):
    chart()
    context.bot.sendPhoto(update.effective_chat.id, photo=open('chart.png', 'rb'))

def dataFrame(update, context):
    df = pd.DataFrame(data)
    dfi.export(df,"table.png")
    context.bot.sendPhoto(update.effective_chat.id, photo=open('table.png', 'rb'))
    #chat_id = ''
    #context.bot.sendPhoto(chat_id = chat_id, photo=open('table.png', 'rb'))
    #klo pake chat_id hapus context ganti jadi bot

def start(update, context):
    print(update.message)
    update.message.reply_text('Hi! I am BOT!\n''gunakan /help untuk melihat command')

def help(update, context):
    update.message.reply_text('/start - untuk memulai bot\n'
                              '/help - untuk bantuan command bot\n'
                              '/uploadImage - untuk upload gambar\n'
                              '/downloadPdf - untuk Download PDF \n'
                              '/linkGForm - untuk mengisi Google Form \n'
                              '/dataFrame - untuk melihat table DataFrame \n'
                              '/chartImage - untuk melihat data dalam bentuk Chart')

def downloadPdf(update, context):
    update.message.reply_text('The file is Downloading')
    context.bot.sendDocument(update.effective_chat.id, document=open('pdfTest.pdf','rb'))


def image(update, context):
     update.message.reply_text('Silahkan Upload Gambarnya')

def linkGForm(update, context):
     update.message.reply_text('link untuk mengisi Google Form \n'
                               'https://forms.gle/roJXMKXQrp7TogVM6')
     
def uploadImage(update, context):
    #print(update.message)
   
    filename = "test.jpg"
    file_id = update.message.photo[-1].file_id
    newFile = context.bot.get_file(file_id)
    print(update.message.photo)
    newFile.download('test.jpg')

    update.message.reply_text('Saya Dapat Gambarnya!')

def echo(update, context):
    query = update.message.text
    update.message.reply_text(query)

def main():
    updater = Updater('1859300275:AAH_RhUCS7hySa5Wu9_JArC7SrTu7xuMbTU', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("uploadImage", image))
    dp.add_handler(CommandHandler("linkGForm", linkGForm))
    dp.add_handler(CommandHandler("downloadPdf", downloadPdf))
    dp.add_handler(CommandHandler("chartImage", chartImage))
    dp.add_handler(CommandHandler("dataFrame", dataFrame))
    
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.photo, uploadImage))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
