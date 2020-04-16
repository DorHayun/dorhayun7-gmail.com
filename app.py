from flask import Flask
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    result = requests.get("https://www.npmjs.com/package/lodash")
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    license = soup.findAll('p' ,attrs={"class" :"f2874b88 fw6 mb3 mt2 truncate black-80 f4"})[1].text
    #send msg in the telegram bot
    requests.get("https://api.telegram.org/bot857617376:AAF_rlduJrIP1iXfPDRj84ixm3JOzewjouw/sendMessage?chat_id=478322885&text={}".format(license))
    print('the data was sent!')
    return
    
