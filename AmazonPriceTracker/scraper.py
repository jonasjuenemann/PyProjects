import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/-/en/AMD-Ryzen-5800X-Box-Processor/dp/B0815XFSGK/ref=sr_1_3?crid=3S1E28014H5GT&dchild=1&keywords=amd+ryzen+5800x&qid=1620403955&sprefix=AMD+ryzen+5800%2Caps%2C316&sr=8-3'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}

priceTrue = True


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('jonas.juenemann95@gmail.com', 'Leondias95')
    subject = 'Hey Price fell down'
    body = 'Check the Amazon link ' + URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'jonas.juenemann95@gmail.com',
        'jonas.juenemann@gmx.de',
        msg
    )
    print('Email has been sent')
    server.quit()


def check_price(URL):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify()) super viel, super unnötig

    title = soup.find(id='productTitle').get_text()

    # print(title.strip())

    price = soup.find(id='priceblock_ourprice').get_text()
    price = float(price.strip()[1:-3])

    # print(price)

    if price <= 350:
        send_mail()
        global priceTrue
        priceTrue = False


while priceTrue:
    check_price(URL)
    time.sleep(60 * 60 * 12)  # Alle zwölf Stunden

