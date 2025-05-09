from bs4 import BeautifulSoup
import requests
import smtplib
TARGET_PRICE =100
SUBJECT ="Amazon Price Alert!"
MY_EMAIL = "shrestamallina.s@gmail.com"
PASSWORD = "ghsp vyag jywj zamc"
LANGUAGE = "en-IN,en;q=0.9,te-IN;q=0.8,te;q=0.7,en-GB;q=0.6,en-US;q=0.5"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
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
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="mallinamuralikrishna@gmail.com",
                        msg=f"subject:{SUBJECT}\n\n{subject} now ${prices}.{decimal_price}\n{LINK}.".encode(encoding="utf-8"))
