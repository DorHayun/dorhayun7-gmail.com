
# YouTube Link:

# Ensure that you have both beautifulsoup and requests installed:
#   pip install beautifulsoup4
#   pip install requests

import requests
from bs4 import BeautifulSoup


result = requests.get("https://www.npmjs.com/package/lodash")

src = result.content
soup = BeautifulSoup(src, 'html.parser')
License = soup.findAll('p' ,attrs={"class" :"f2874b88 fw6 mb3 mt2 truncate black-80 f4"})[1].text

#send msg in the telegram bot
requests.get("https://api.telegram.org/bot857617376:AAFktPZYQfRG60voVoWvPyO7eFKWUahmEKE/sendMessage?chat_id=478322885&text={}".format(License))

# License = soup.select(".f2874b88 fw6 mb3 mt2 truncate black-80 f4")[
# print(license.get_text())
# print("\n")



# Perhaps we just want to extract the link that has contains the text
# "About" on the page instead of every link. We can use the built-in
# "text" function to access the text content between the <a> </a>
# tags.
# for link in links:
#  if "About" in link.text:
#     print(link)
#    print(link.attrs['href'])


# for License in Licenses:
# if "About" in link.text:
#   print(License)
#   print(link.attrs['href'])



