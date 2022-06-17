from datetime import date, timedelta
from requests import Session

from src.crawler import extract_links_from_senego, send_request, extract_links_from_seneweb


def main():
    session = Session()

    # if senego
    # BASE_URL = "https://senego.com/page/1"
    # for i in range(10):
    #     content = send_request(BASE_URL, session)
    #     post_urls = extract_links_from_senego(content)
    #     print(post_urls)

    # if seneweb
    start = date(2010,1,1)
    end = date(2019,12,31)
    BASE_URL = "https://seneweb.com/news/retronews/"
    delta = timedelta(days=1)
    while start <= end:
        post_date = start.strftime("%d-%m-%Y")
        start += delta
        content = send_request(BASE_URL+ post_date, session)
        post_urls = extract_links_from_seneweb(content)
        for p in post_urls:
            print(p)
        break

    session.close()


if __name__ == '__main__':
    main()