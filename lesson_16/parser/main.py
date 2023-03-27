import time

from crypto_parser import CryptoParser

if __name__ == "__main__":
    parsers = [
        CryptoParser("bitcoin"),
        CryptoParser("ethereum"),
        CryptoParser("binance-coin"),
        CryptoParser("dogecoin"),
    ]

    counter = 0
    while True:
        counter += 1
        to_print = f"Crypto-Coin {counter:<4}: " + "\t\t".join(
            f"{parser()}" for parser in parsers
        )
        print("\r" + to_print, end="")
        time.sleep(2)
