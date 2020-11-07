from flask import Flask, redirect, render_template, request, url_for
from urllib.request import urlopen
from bs4 import BeautifulSoup


app = Flask(__name__, template_folder="newsapp_templates")

@app.route('/')
def index():
    url = 'https://news.google.com/news/rss'
    client = urlopen(url)
    xml_data = client.read()
    client.close()
    soup = BeautifulSoup(xml_data,'xml')
    print(soup.title)
    news_list = soup.find_all('item')

    return render_template('index.html',news_list=news_list)

if __name__ == "main":
    app.run(debug=True)
