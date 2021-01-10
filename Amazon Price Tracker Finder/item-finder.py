#Created by bajra-manandhar17
#Read description before executing

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from win10toast import ToastNotifier
import requests
import time


toast = ToastNotifier()
print('Made by github.com/bajra-manandhar17')

product = input("Enter Product Name: ")
list = {}
product_list = product.split()

amazon_link = "https://amazon.in"
url = amazon_link + "/s?k=" + "+".join(product_list) + "&ref=nb_sb_noss"

# function
def finder(random_header):
    url_open = requests.get(url, headers=random_header)
    soup = BeautifulSoup(url_open.content, "html.parser")
    name = soup("span", {"class": "a-size-medium a-color-base a-text-normal"})
    price = soup("span", {"class": "a-price-whole"})

    for i, j in zip(name, price):
        if product.lower() in (i.text).lower():
            print("{} || price: Rs {}".format(i.text, j.text))
            list[str(i.text)] = j.text

            for a, b in list.items():
                if str(i.text) == a:
                    if j.text < b:
                        toast.show_toast("Deal",i.text + " Rs ||" + j.text)


while True:
    user = UserAgent()
    randomHeader = {"User-Agent": str(user.random)}
    print("Tracking Request...........", time.asctime(time.localtime(time.time())))
    finder(randomHeader)
    time.sleep(60 * 5)
