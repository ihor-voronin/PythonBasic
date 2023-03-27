import time

import bs4
import httpx

if __name__ == "__main__":
    while True:
        crypto_currencies = ["ethereum", "bitcoin"]
        for crypto_currency in crypto_currencies:
            request = httpx.get(f"https://www.coindesk.com/price/{crypto_currency}/")
            # print(request.status_code)
            # print(request.text[:200])
            # print("currency-pricestyles___Symbol-sc-1rux8hj-1 eBoMRj" in request.text)
            # print(request.text.split("currency-pricestyles___Symbol-sc-1rux8hj-1 eBoMRj")[1][2:3])

            soup = bs4.BeautifulSoup(request.text, "html.parser")
            currency = soup.find(
                "span",
                class_=lambda value: value
                and value.startswith("currency-pricestyles___Symbol"),
            ).text
            amount = soup.find(
                "span",
                class_=lambda value: value
                and value.startswith("currency-pricestyles__Price"),
            ).text
            print(crypto_currency, currency, amount)
            print()

        time.sleep(2.0)
