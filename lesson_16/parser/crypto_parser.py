from decimal import Decimal
from typing import Tuple

import colors
import httpx
from bs4 import BeautifulSoup


class ParserException(Exception):
    pass


CURRENCY_TYPE = str


class CryptoParser:
    base_url = "https://www.coindesk.com/price/{currency}/"

    def __init__(self, crypto_coin: str):
        self.crypto_coin = crypto_coin

    def _get_html_request(self) -> str:
        url = self.base_url.format(currency=self.crypto_coin)
        request = httpx.get(url)
        if not request.is_success:
            raise ParserException(
                f"Service {url} response with code {request.status_code}"
            )

        content_type = request.headers["content-type"]
        if "text/html" not in content_type:
            raise ParserException(
                f"Service {url} response with {content_type} - incorrect content type"
            )

        return request.text

    def _parse_html(self, html) -> Tuple[CURRENCY_TYPE, Decimal]:
        soup = BeautifulSoup(html, "html.parser")
        currency_details = soup.findAll(
            "span",
            class_=lambda value: value and value.startswith("currency-pricestyles__"),
        )
        # print(currency_details)
        if len(currency_details) != 2:
            raise ParserException(f"Cannot parse html with currency details")

        return currency_details[0].text, Decimal(
            currency_details[1].text.replace(",", "")
        )

    def __call__(self, *args, **kwargs):
        currency, value = self._parse_html(self._get_html_request())
        return f"{colors.RED}{self.crypto_coin} {colors.GREEN}{currency} {colors.BOLD}{value:,}{colors.RESET}"


if __name__ == "__main__":
    cp = CryptoParser("bitcoin")
    # print(cp._parse_html(cp._get_html_request()))
    print(cp())

    cp2 = CryptoParser("ethereum")
    # print(cp2._parse_html(cp2._get_html_request()))
    print(cp2())
