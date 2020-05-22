from flask import Flask
import requests
import telebot
import time
import unshortenit
from unshortenit import UnshortenIt

app = Flask(__name__)
bot_token = '857617376:AAFX-IATq2rEKPsKcW7ylkhe_pA7jOZZeK0'
bot = telebot.TeleBot(token=bot_token)
@app.route('/')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome')
    
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'To use this bot, send it a bit.lu url!')
    
@bot.message_handler(func=lambda msg: msg.text is not None)
def send_answer(message):
    unshortener = UnshortenIt()
    message = unshortener.unshorten(msg.text)
    requests.get("https://api.telegram.org/bot857617376:AAFX-IATq2rEKPsKcW7ylkhe_pA7jOZZeK0/sendMessage?chat_id=478322885&text={}".format(message))
    
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)


#def main():
# unshortener = UnshortenIt() 
 
 #while True:
 # updates = requests.get("https://api.telegram.org/bot857617376:AAFX-IATq2rEKPsKcW7ylkhe_pA7jOZZeK0/getUpdates")
 # offset = updates[0]["update_id"]
  #for item in updates:
   
  # updates = requests.get("https://api.telegram.org/bot857617376:AAFX-IATq2rEKPsKcW7ylkhe_pA7jOZZeK0/getUpdates?offset={}".format(offset+1))
   #updates = json.loads(updates.content)
  # updates = updates["result"]                  
  # message = item["message"]["text"]
  # message = unshortener.unshorten(message)
#   requests.get("https://api.telegram.org/bot857617376:AAFX-IATq2rEKPsKcW7ylkhe_pA7jOZZeK0/sendMessage?chat_id=478322885&text={}".format(message))
   #return message
    

#def hello_world():
    #result = requests.get("https://www.npmjs.com/package/lodash")
   # src = result.content
    #soup = BeautifulSoup(src, 'html.parser')
    #license = soup.findAll('p' ,attrs={"class" :"f2874b88 fw6 mb3 mt2 truncate black-80 f4"})[1].text
    #send msg in the telegram bot
    #requests.get("https://api.telegram.org/bot857617376:AAF_rlduJrIP1iXfPDRj84ixm3JOzewjouw/sendMessage?chat_id=478322885&text={}".format(license))
    #return'the data was sent!'#
     
   #get the url from user
