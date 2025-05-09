from bs4 import BeautifulSoup
import requests
import smtplib
TARGET_PRICE =100
SUBJECT ="Amazon Price Alert!"
MY_EMAIL = "your mail"
PASSWORD = "ghsp vyag jywj zamc"
LANGUAGE = "HTTP header"
USER_AGENT = "Http Header"
LINK = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response = requests.get(url=LINK,headers={"Accept-Language":LANGUAGE,
                                          "User-Agent":USER_AGENT})
pot_w_page = response.text
soup = BeautifulSoup(pot_w_page,"html.parser")
pot_price = soup.find(name="span",class_="a-price-whole")
price = pot_price.text
prices = int(price.split(".")[0])

subject = ("Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker,"
           " Rice Cooker, Steamer, Sauté, Yogurt Maker,"
           " Warmer & Sterilizer, Includes App With Over 800 Recipes, "
           "Stainless Steel, 3 Quart")

decimal = soup.find(name="span",class_="a-price-fraction")
decimal_price = decimal.text
if prices < TARGET_PRICE:
    connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="12345@gmail.com",
                        msg=f"subject:{SUBJECT}\n\n{subject} now ${prices}.{decimal_price}\n{LINK}.".encode(encoding="utf-8"))
