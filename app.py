from flask import Flask
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

result = requests.get("https://www.npmjs.com/package/lodash")

src = result.content
soup = BeautifulSoup(src, 'html.parser')
License = soup.findAll('p' ,attrs={"class" :"f2874b88 fw6 mb3 mt2 truncate black-80 f4"})[1].text

#send msg in the telegram bot
requests.get("https://api.telegram.org/bot857617376:AAFktPZYQfRG60voVoWvPyO7eFKWUahmEKE/sendMessage?chat_id=478322885&text={}".format(License))
