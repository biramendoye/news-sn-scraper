from datetime import date, timedelta
from requests import Session

from src.crawler import (
    extract_links_from_senego,
    send_request,
    extract_links_from_seneweb,
)
from src.cli import cli


def main():
    session = Session()

    args = cli()
    if args.name == "senego":
        BASE_URL = "https://senego.com/page/"
        for i in range(1, 13901):
            content = send_request(BASE_URL + i, session)
            post_urls = extract_links_from_senego(content)
            print(post_urls)
    elif args.name == "seneweb":
        urls = [
            "https://seneweb.com/news/politique/",
            "https://seneweb.com/news/videos/",
            "https://seneweb.com/news/societe/",
            "https://seneweb.com/news/religion/",
            "https://seneweb.com/news/sport/",
            "https://seneweb.com/news/afrique/",
            "https://seneweb.com/news/people/",
        ]
        for url in urls:
            content = send_request(url, session)
            post_urls = extract_links_from_seneweb(content)
        # for old links we start from the year 2010 to 2019
        start = date(2010, 1, 1)
        end = date(2019, 12, 31)
        BASE_URL = "https://seneweb.com/news/retronews/"
        delta = timedelta(days=1)
        while start <= end:
            post_date = start.strftime("%d-%m-%Y")
            start += delta
            content = send_request(BASE_URL + post_date, session)
            post_urls = extract_links_from_seneweb(content)
            for p in post_urls:
                print(p)
    else:
        print("Website not yet implemented!!")

    session.close()


if __name__ == "__main__":
    main()
