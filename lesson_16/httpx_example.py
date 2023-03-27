import httpx

if __name__ == "__main__":
    print("Get page")
    # https://weather.com/weather/tenday/l/Kyiv+Ukraine?canonicalCityId=0b66fcc8c4490e8b96bcf6af087a80df429e7ce442645cf1a27546703dbd551a
    r = httpx.get(
        "https://weather.com/weather/tenday/l/Kyiv+Ukraine",
        params={
            "canonicalCityId": "0b66fcc8c4490e8b96bcf6af087a80df429e7ce442645cf1a27546703dbd551a"
        },
    )
    print(r)
    print(r.status_code)
    print(r.headers["content-type"])
    print(r.text[:100])
    #
    print("Get api response")
    r3 = httpx.get(
        "https://httpbin.org/get",
        params={
            "q": "50.4539606,30.5480298",
            "lang": "ua",
        },
    )
    print(r3)
    print(r3.status_code)
    print(r3.headers["content-type"])
    print(r3.text)
    print(r3.json())
    #
    # r4 = httpx.get("https://www.kyivpost.com/uk")
    # print(r4)
    # print(r4.status_code)
    # print(r4.headers["content-type"])
    # print(r4.text)
