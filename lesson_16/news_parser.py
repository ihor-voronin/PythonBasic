import json
from pprint import pprint

import bs4
import httpx

if __name__ == "__main__":
    url = "https://www.kyivpost.com/uk"
    request = httpx.get(url)
    print(request.status_code)
    # print(request.text[:100])

    html_parser = bs4.BeautifulSoup(request.text, "html.parser")

    new_blocks = html_parser.findAll(
        "div", class_=lambda value: value and value.startswith("post-regular")
    )
    # print(new_blocks[1])

    list_news = []
    for new_block in new_blocks:
        title_element = new_block.find("div", class_="title")
        if not title_element:
            continue

        link_element = title_element.find("a")
        link_news = ""
        if link_element:
            link_news = link_element["href"]

        label_element = new_block.find(
            "span", class_=lambda value: value and value.startswith("label-boxed")
        )
        label = ""
        if label_element:
            label = label_element.text

        author_element = new_block.find("div", class_="author")
        author = ""
        if author_element:
            author = author_element.text

        list_news.append(
            {
                "label": label,
                "title": title_element.text,
                "link": link_news,
                "author": author,
            }
        )

        # print(label, end="\t")
        # print(title_element.text)

    # pprint(list_news)
    print(json.dumps(list_news, indent=4))
